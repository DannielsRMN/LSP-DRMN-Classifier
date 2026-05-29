# 🤟 LSP-DRMN-Classifier (Reconocimiento de Lengua de Señas Peruana)

![Python](https://img.shields.io/badge/Python-3.12.9-blue.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Vision-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-MLPClassifier-orange.svg)

Módulo enfocado en el reconocimiento de 4 letras estáticas (**D, R, M, N**) de la Lengua de Señas Peruana (LSP). El sistema utiliza la librería MediaPipe para la extracción geométrica de los 21 puntos clave (landmarks) de la mano y un clasificador de red neuronal perceptrón multicapa (`MLPClassifier`) para la categorización en tiempo real.

---

## ⚠️ Estado del Proyecto y Optimización de Patrones
El sistema se encuentra en una fase de desarrollo y calibración, con foco en resolver dos desafíos principales de variabilidad morfológica:

* **Falsos Positivos:** Optimización del modelo mediante una clase neutra (`None`/Fondo) para evitar predicciones forzadas cuando la mano se encuentra abierta o en reposo.
* **Similitud Estructural:** Ajuste de umbrales y filtrado geométrico para mitigar las fluctuaciones de predicción entre caracteres con morfologías de landmarks similares (como la transición entre la **M** y la **N**).

---

## 📸 Señas Implementadas

A continuación se presentan las configuraciones manuales capturadas para el entrenamiento del dataset local:

| 1. Letra "D" | 2. Letra "R" |
| :---: | :---: |
| <img src="Lenguaje_Peruano/D.jpeg" width="260" alt="Letra_D"> | <img src="Lenguaje_Peruano/R.jpeg" width="260" alt="Letra_R"> |
| **3. Letra "M"** | **4. Letra "N"** |
| <img src="Lenguaje_Peruano/M.jpeg" width="260" alt="Letra_M"> | <img src="Lenguaje_Peruano/N.jpeg" width="260" alt="Letra_N"> |

---

## 🛠️ Instalación de Dependencias

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener tu entorno virtual activo e instala las dependencias requeridas generadas en el proyecto:
   ```bash
   pip install -r requirements.txt

---

## * 📺 **Video de Referencia:** [Alfabeto LSP en YouTube](https://youtu.be/xEsI4vFBLSQ?si=E8ErLnCdFNTGjW5d)