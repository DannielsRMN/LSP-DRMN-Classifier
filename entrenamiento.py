import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

dataset = pd.read_csv('DataSet.csv')

X = dataset.drop(['letra'], axis=1)
y = dataset['letra']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = MLPClassifier(
    hidden_layer_sizes=(128, 64, 32),
    activation='relu',
    solver='adam',
    max_iter=3000,
    random_state=12
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('modelo', modelo)
])

print("...Entrenando...")
pipeline.fit(X_train, y_train)

predicciones = pipeline.predict(X_test)
precision = accuracy_score(y_test, predicciones)

print(f"Precisión: {precision:.2f}")
print("Reporte de Clasificación:")
print(classification_report(y_test, predicciones))

print("...Guardando el modelo entrenado...")
joblib.dump(pipeline, 'modelo_drmn.pkl')