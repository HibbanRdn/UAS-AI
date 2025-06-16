import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("/Users/muhamadhibbanramadhan/Documents/UAS AI/Kredit.csv")
data.dropna(inplace=True)

# Pisahkan fitur dan label
X = data.drop('Kelayakan', axis=1)
y = data['Kelayakan']

# Encode fitur kategorikal (one-hot encoding)
X = pd.get_dummies(X)

# Encode label target (layak / tidak layak)
le = LabelEncoder()
y_encoded = le.fit_transform(y)  # 'layak' = 1, 'tidak layak' = 0

# Split data training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# Inisialisasi dan latih Decision Tree (menggunakan entropy → ID3)
clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
clf.fit(X_train, y_train)

# Prediksi
y_pred = clf.predict(X_test)

# === Evaluasi ===
print("            === Classification Report ===")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()
