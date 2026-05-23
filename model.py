import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# Step 1: Create Dataset
# -------------------------------
data = {
    "Age": [25, 40, 35, 50, 28, 60, 45, 33, 55, 38],
    "BMI": [22, 30, 27, 35, 24, 32, 29, 26, 34, 28],
    "BP": ["No","Yes","No","Yes","No","Yes","Yes","No","Yes","No"],
    "GULCOSE": ["High","Low","Medium","Low","High","Low","Medium","High","Low","Medium"],
    "ACTIVITY": ["Low","High","Medium","High","Low","High","Medium","Low","High","Medium"]
}

df = pd.DataFrame(data)


le_bp = LabelEncoder()
le_gulcose = LabelEncoder()
le_activity = LabelEncoder()

df['BP'] = le_bp.fit_transform(df['BP'])
df['GULCOSE'] = le_gulcose.fit_transform(df['GULCOSE'])
df['ACTIVITY'] = le_activity.fit_transform(df['ACTIVITY'])

# -------------------------------
# Step 3: Features & Target
# -------------------------------
X = df[['Age', 'BMI', 'BP', 'GULCOSE']]
y = df['ACTIVITY']

# -------------------------------
# Step 4: Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# -------------------------------
# Step 5: Model Training
# -------------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# -------------------------------
# Step 6: Evaluation
# -------------------------------
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred))

# -------------------------------
# Step 7: Save Model
# -------------------------------
pickle.dump((model, le_bp, le_gulcose, le_activity), open('health_model.pkl', 'wb'))

print("✅ Health Model Saved Successfully!")