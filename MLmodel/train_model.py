import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
import pickle
from sklearn.preprocessing import MultiLabelBinarizer

data = pd.read_csv('salary_data.csv')
data['Skills'] = data['Skills'].apply(lambda x: x.split('|'))
skill_weight = {
    'Python': 1.5,
    'Java': 1.5,
    'JavaScript': 1.2,
    'CSS': 1.0,
    'HTML': 1.0,
    'C++': 1.4,
    'Ruby': 1.2,
    'SQL': 1.3,
    'R': 1.4,
    'PHP': 1.1,
    'Swift': 1.3,
    'Go': 1.3,
    'Kotlin': 1.3,
    'TypeScript': 1.2,
    'Dart': 1.2,
}

def adjust_salary(row):
    skill_list = row['Skills']
    bonus = 0

    if len(skill_list) > 3:
        bonus += 40000
    if 'Python' in skill_list:
        bonus += 25000
    if 'Java' in skill_list:
        bonus += 20000

    return row['Salary'] + bonus

data['Salary'] = data.apply(adjust_salary, axis=1)
X = data[['Experience', 'Education', 'Location', 'Job_Title', 'Skills']]
y = data['Salary']
edu_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
job_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
loc_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

X_edu = edu_encoder.fit_transform(X[['Education']])
X_job = job_encoder.fit_transform(X[['Job_Title']])
X_loc = loc_encoder.fit_transform(X[['Location']])
mlb = MultiLabelBinarizer()
X_skills = mlb.fit_transform(X['Skills'])

X_skills_weighted = X_skills * [skill_weight.get(skill, 1.5) for skill in mlb.classes_]

X_exp = X[['Experience']].reset_index(drop=True)
X_final = pd.concat([
    X_exp,
    pd.DataFrame(X_edu, columns=edu_encoder.get_feature_names_out(['Education'])).reset_index(drop=True),
    pd.DataFrame(X_job, columns=job_encoder.get_feature_names_out(['Job_Title'])).reset_index(drop=True),
    pd.DataFrame(X_loc, columns=loc_encoder.get_feature_names_out(['Location'])).reset_index(drop=True),
    pd.DataFrame(X_skills_weighted, columns=mlb.classes_).reset_index(drop=True)
], axis=1)

model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_final, y)

with open('salary_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('edu_encoder.pkl', 'wb') as f:
    pickle.dump(edu_encoder, f)

with open('job_encoder.pkl', 'wb') as f:
    pickle.dump(job_encoder, f)

with open('loc_encoder.pkl', 'wb') as f:
    pickle.dump(loc_encoder, f)

with open('skill_encoder.pkl', 'wb') as f:
    pickle.dump(mlb, f)

print("✅ Model and encoders saved successfully.")
