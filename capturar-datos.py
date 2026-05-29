import cv2
import mediapipe as mp
import os
import csv
from datetime import datetime

#py -3.12 -m venv env
#pip install "mediapipe==0.10.14" opencv_python

LETRA = input('INGRESE LA LETRA A CAPTURAR: ').upper()
ARCHIVO_CSV = 'DataSet.csv'
CARPETA_IMAGENES = 'capturas'

os.makedirs(CARPETA_IMAGENES, exist_ok=True)
existe_csv = os.path.exists(ARCHIVO_CSV)
contador = 0

#Capturamos el video, el índice 0 puede cambiar si se tiene muchas cámaras web.
#Registro mi dispositivo de captura (0 = índice de la cámara web)
cap = cv2.VideoCapture(0)

#Detector de mano
mp_mano = mp.solutions.hands
mp_dibujo = mp.solutions.drawing_utils

with open(ARCHIVO_CSV,mode='a',newline="") as f:
    writer = csv.writer(f)
    if not existe_csv:
        #Para los encabezados
        columnas = []
        for i in range(21):
            columnas += [f"x{i}",f"y{i}",f"z{i}"]
        columnas.append("letra")
        writer.writerow(columnas)
    #Configurar el detector
    with mp_mano.Hands(
            max_num_hands = 1,
            min_detection_confidence = 0.7,
            min_tracking_confidence = 0.7
    ) as manos:
        
        #Bucle infinito
        while True:
            #CV(Computer Vision) - Se realizaran capturas (imagen) de lo que ve en la cámara web.
            ret, frame = cap.read()
            #Si no captura nada se detiene
            if not ret:
                break
            #Para rotar la imagen (Ya no es espejo)
            frame = cv2.flip(frame,1)
            frame_original = frame.copy()
            rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            resultado = manos.process(rgb)
            if resultado.multi_hand_landmarks:
                descriptores_mano = resultado.multi_hand_landmarks[0]
                mp_dibujo.draw_landmarks(frame,descriptores_mano,mp_mano.HAND_CONNECTIONS)
                cv2.putText(frame, f"Letra:{LETRA} | Precione S para guardar",(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
                cv2.putText(frame, f"Captura:{contador}",(20,80),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

            cv2.imshow('Captura de Datos', frame)
            #Si precionamos el ESC se para el video
            tecla = cv2.waitKey(1) & 0xFF
            if tecla == 27:
                break
            if tecla == ord("s") and resultado.multi_hand_landmarks:
                contador +=1
                nombre_imagen = f"{LETRA}_{datetime.now().strftime('%y%m%d_%H%M%S_%f')}.jpg"
                ruta_imagen = os.path.join(CARPETA_IMAGENES,nombre_imagen)
                cv2.imwrite(ruta_imagen, frame_original)
                base_x = descriptores_mano.landmark[0].x
                base_y = descriptores_mano.landmark[0].y
                base_z = descriptores_mano.landmark[0].z
                fila = []
                for lm in descriptores_mano.landmark:
                    fila.extend([lm.x - base_x,lm.y - base_y,lm.z - base_z])
                fila.append(LETRA)
                writer.writerow(fila)
                print(f"Guardado: {LETRA} - {ruta_imagen}")
cap.release()
cv2.destroyAllWindows()