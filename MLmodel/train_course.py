# Training model based only on skills, field, and years_of_experience

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the dataset
df = pd.read_csv("legit_course_recommendation_dataset.csv")

# Separate features and target
X = df[['skills', 'field', 'years_of_experience']]
y = df['recommended_course']

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('skills_field', OneHotEncoder(handle_unknown='ignore'), ['skills', 'field']),
        ('experience', StandardScaler(), ['years_of_experience'])
    ]
)

# Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Hyperparameter grid
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [10, 20, None],
    'classifier__min_samples_split': [2, 5],
    'classifier__min_samples_leaf': [1, 2]
}

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Grid search
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

# Predict and evaluate
y_pred = grid_search.predict(X_test)

print("\nBest Parameters Found:\n", grid_search.best_params_)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Save the best model
joblib.dump(grid_search.best_estimator_, "course_recommendation_model.pkl")
print("\n✅ Model saved as 'course_recommendation_model.pkl'")