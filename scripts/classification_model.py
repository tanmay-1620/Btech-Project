import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Directory where processed data files are stored
processed_dir = 'D:/BTP/Data/processed/crisislex26/'

# List all processed files
file_paths = [
    os.path.join(processed_dir, f'crisis_text_cleaned_disaster{i}.csv.txt') for i in range(1, 26)
]


# Load and concatenate all processed CSV files
dataframes = [pd.read_csv(file) for file in file_paths]
df = pd.concat(dataframes, ignore_index=True)

# Verify that the 'cleaned_text' column exists
if 'cleaned_text' not in df.columns:
    raise ValueError("Error: 'cleaned_text' column missing in the data.")

# Step 1: Feature Extraction with TF-IDF
# Initialize TF-IDF Vectorizer with a maximum of 1000 features
tfidf = TfidfVectorizer(max_features=1000)

# Fit and transform the cleaned text data
X_text = tfidf.fit_transform(df['cleaned_text']).toarray()  # Convert to array format

# Check the shape of the TF-IDF output to ensure it’s processed correctly
print("Shape of TF-IDF output:", X_text.shape)

# Step 2: Label Encoding for Target Variable
# Assuming 'informativeness_encoded' is the target variable for classification
y = df['informativeness_encoded']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_text, y, test_size=0.2, random_state=42)

# Step 3: Train a Logistic Regression Model
# Initialize the model
model = LogisticRegression(max_iter=200)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Step 4: Evaluate the Model
# Print accuracy and classification report
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 5: Save the Model
# Save the trained model and TF-IDF vectorizer for later use
joblib.dump(model, os.path.join(processed_dir, 'crisis_classification_model.pkl'))
joblib.dump(tfidf, os.path.join(processed_dir, 'tfidf_vectorizer.pkl'))

print("Model and vectorizer saved successfully.")
