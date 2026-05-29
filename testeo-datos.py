import cv2
import mediapipe as mp
import joblib
import pandas as pd

print("...Cargando modelo...")
pipeline = joblib.load('modelo_drmn.pkl')
print("...Iniciando...")

cap = cv2.VideoCapture(0)
mp_mano = mp.solutions.hands
mp_dibujo = mp.solutions.drawing_utils

columnas = []
for i in range(21):
    columnas += [f"x{i}",f"y{i}",f"z{i}"]

with mp_mano.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as manos:
    while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame,1)
            rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            resultado = manos.process(rgb)
            
            if resultado.multi_hand_landmarks:
                
                
                descriptores_mano = resultado.multi_hand_landmarks[0]
                mp_dibujo.draw_landmarks(frame,descriptores_mano,mp_mano.HAND_CONNECTIONS)
                
                base_x = descriptores_mano.landmark[0].x
                base_y = descriptores_mano.landmark[0].y
                base_z = descriptores_mano.landmark[0].z
                
                fila = []
                for lm in descriptores_mano.landmark:
                    fila.extend([lm.x - base_x,lm.y - base_y,lm.z - base_z])
                
                datos_entrada = pd.DataFrame([fila], columns=columnas)
                prediccion = pipeline.predict(datos_entrada)[0]
                
                probabilidad = pipeline.predict_proba(datos_entrada)[0]
                procentaje = max(probabilidad) * 100
                
                if procentaje > 90 and prediccion != 'NONE':
                    resultado = f"La letra es: {prediccion} ({procentaje:.2f}%)"
                    cv2.putText(frame, resultado, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                
            cv2.imshow('Prueba de Datos', frame)
            
            tecla = cv2.waitKey(1) & 0xFF
            if tecla == 27:
                break   

cap.release()
cv2.destroyAllWindows()