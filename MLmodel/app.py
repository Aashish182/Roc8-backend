# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import joblib
# import numpy as np
# import pickle
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# # # ------------------ Load Salary Prediction Model ------------------ #
# # try:
# #     salary_model = joblib.load("salary_model.pkl")
# #     scaler = joblib.load("scaler.pkl")
# #     print("✅ Salary model and scaler loaded successfully!")
# # except Exception as e:
# #     print(f"❌ Error loading salary model or scaler: {e}")
# #     salary_model = None
# #     scaler = None

# # ------------------ Load Course Recommendation Model ------------------ #
# try:
#     course_recommendation_model = joblib.load("course_recommendation_model.pkl")
#     print("✅ Course recommendation model loaded successfully!")
# except Exception as e:
#     print(f"❌ Error loading course recommendation model: {e}")
#     course_recommendation_model = None

# # ------------------ COURSE RECOMMENDATION ROUTE ------------------ #
# @app.route("/recommend_course", methods=["POST"])
# def recommend_course():
#     if not course_recommendation_model:
#         return jsonify({"error": "Model not loaded"}), 500

#     try:
#         data = request.json
#         print("📥 Incoming Course Recommendation Data:", data)

#         required_fields = ["skills", "years_of_experience", "field"]
#         missing_fields = [field for field in required_fields if field not in data]
#         if missing_fields:
#             return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

#         # Combine skills list into a single string (if it's a list)
#         if isinstance(data["skills"], list):
#             skills = ', '.join([skill.strip().lower() for skill in data["skills"]])
#         else:
#             skills = data["skills"].strip().lower()

#         input_dict = {
#             "skills": skills,
#             "years_of_experience": float(data["years_of_experience"]),
#             "field": data["field"].strip()
#         }

#         input_df = pd.DataFrame([input_dict])
#         print("📊 Input DataFrame:\n", input_df)

#         prediction = course_recommendation_model.predict(input_df)[0]
#         print("🎯 Predicted Course:", prediction)

#         return jsonify({
#             "recommended_course": prediction
#         })

#     except Exception as e:
#         print(f"❌ Error in course recommendation: {e}")
#         return jsonify({"error": "Invalid input data"}), 400

# # ------------------ SALARY PREDICTION ROUTE ------------------ #
# model = pickle.load(open('salary_model.pkl', 'rb'))
# edu_encoder = pickle.load(open('edu_encoder.pkl', 'rb'))
# job_encoder = pickle.load(open('job_encoder.pkl', 'rb'))
# loc_encoder = pickle.load(open('loc_encoder.pkl', 'rb'))
# mlb = pickle.load(open('skill_encoder.pkl', 'rb'))

# skill_weight = {
#     'Python': 1.6,
#     'Java': 1.5,
#     'JavaScript': 1.4,
#     'CSS': 1.0,
#     'HTML': 1.0,
#     'C++': 1.3,
#     'Ruby': 1.2,
#     'SQL': 1.3,
#     'R': 1.4,
#     'PHP': 1.1,
#     'Swift': 1.3,
#     'Go': 1.3,
#     'Kotlin': 1.3,
#     'TypeScript': 1.3,
#     'Dart': 1.2,
# }

# def apply_skill_bonus(base_salary, skill_list):
#     bonus = 0
#     if len(skill_list) > 3:
#         bonus += 40000
#     if 'Python' in skill_list:
#         bonus += 25000
#     if 'Java' in skill_list:
#         bonus += 20000
#     return base_salary + bonus

# @app.route('/predict_salary', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()
#         experience = float(data.get('experience', 0))
#         education = data.get('education', '').strip()
#         location = data.get('location', '').strip()
#         job_title = data.get('job_title', '').strip()
#         skills_raw = data.get('skills', '')

#         print(f"Experience: {experience}, Education: {education}, Location: {location}, Job Title: {job_title}, Skills: {skills_raw}")

#         skills = [skill.strip() for skill in skills_raw.split(',') if skill.strip()]

#         encoded_education = edu_encoder.transform([[education]])
#         encoded_location = loc_encoder.transform([[location]])
#         encoded_job_title = job_encoder.transform([[job_title]])
#         encoded_skills = mlb.transform([skills])
#         encoded_skills_weighted = encoded_skills * [skill_weight.get(skill, 1.0) for skill in mlb.classes_]

#         features = np.hstack([
#             [experience], 
#             encoded_education.flatten(), 
#             encoded_location.flatten(), 
#             encoded_job_title.flatten(), 
#             encoded_skills_weighted.flatten()
#         ])

#         base_salary = model.predict([features])[0]

#         final_salary = apply_skill_bonus(base_salary, skills)

#         return jsonify({'predicted_salary': round(final_salary, 2)})

#     except Exception as e:
#         error_message = f"Error during prediction: {str(e)}"
#         print(error_message)
#         return jsonify({'error': error_message}), 500
# # ------------------ ROOT ROUTE ------------------ #
# @app.route("/", methods=["GET"])
# def home():
#     return jsonify({"message": "Welcome to the Salary Prediction & Course Recommendation API!"})

# # ------------------ MAIN ENTRY POINT ------------------ #
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)



from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib, pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# ------------------ LOAD MODELS SAFELY ------------------ #
try:
    course_recommendation_model = joblib.load("course_recommendation_model.pkl")
    print("✅ Course recommendation model loaded")
except:
    course_recommendation_model = None
    print("❌ Course model failed to load")

try:
    model = pickle.load(open('salary_model.pkl', 'rb'))
    edu_encoder = pickle.load(open('edu_encoder.pkl', 'rb'))
    job_encoder = pickle.load(open('job_encoder.pkl', 'rb'))
    loc_encoder = pickle.load(open('loc_encoder.pkl', 'rb'))
    mlb = pickle.load(open('skill_encoder.pkl', 'rb'))
    print("✅ Salary model & encoders loaded")
except:
    model = None
    print("❌ Salary model failed to load")

# ------------------ COURSE RECOMMENDATION ------------------ #
@app.route("/recommend_course", methods=["POST"])
def recommend_course():
    if not course_recommendation_model:
        return jsonify({"error": "Model not loaded"}), 500
    
    data = request.json
    skills = data.get("skills", "")
    years = float(data.get("years_of_experience", 0))
    field = data.get("field", "")

    if isinstance(skills, list):
        skills = ", ".join(skills)

    df = pd.DataFrame([{
        "skills": skills.lower(),
        "years_of_experience": years,
        "field": field
    }])

    prediction = course_recommendation_model.predict(df)[0]
    return jsonify({"recommended_course": prediction})

# ------------------ SALARY PREDICTION ------------------ #
skill_weight = {
    'Python': 1.6, 'Java': 1.5, 'JavaScript': 1.4, 'CSS': 1.0, 'HTML': 1.0,
    'C++': 1.3, 'Ruby': 1.2, 'SQL': 1.3, 'R': 1.4, 'PHP': 1.1,
}

def apply_skill_bonus(base_salary, skill_list):
    bonus = 0
    if len(skill_list) > 3: bonus += 40000
    if 'Python' in skill_list: bonus += 25000
    if 'Java' in skill_list: bonus += 20000
    return base_salary + bonus

@app.route('/predict', methods=['POST'])
def predict_salary():
    if not model:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.json
    skills = [s.strip() for s in data.get('skills','').split(',')]

    features = np.hstack([[float(data.get('experience',0))],
        edu_encoder.transform([[data.get('education')]]).flatten(),
        loc_encoder.transform([[data.get('location')]]).flatten(),
        job_encoder.transform([[data.get('job_title')]]).flatten(),
        mlb.transform([skills]).flatten()
    ])

    base_salary = model.predict([features])[0]
    final_salary = apply_skill_bonus(base_salary, skills)

    return jsonify({'predicted_salary': round(final_salary,2)})

@app.route("/")
def home():
    return jsonify({"message": "ROC8 ML API Running ✅"})

# ------------------ RENDER ENTRY POINT ------------------ #
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
