import cv2

from ultralytics import YOLO

from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

# 1. Trainiertes Modell laden
# Ersetze 'best.pt' durch den Pfad zu deiner gespeicherten Modelldatei
model = YOLO("best.pt")

# 2. Input-Video öffnen (Ersetze den Pfad durch dein Testvideo oder nutze 0 für die Webcam)
video_path = "fuehrerstandsmitfahrt.mp4"

cap = cv2.VideoCapture(video_path)

# Video-Eigenschaften für den Export auslesen
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# 3. VideoWriter einrichten (speichert das fertige Video ab)
output_path = "bahn_erkennung_output.mp4"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Start- und Endzeit in Sekunden festlegen
start_sekunde = 90  # Minute 1:30
end_sekunde = 240  # Minute 4:00

# Frame-Positionen berechnen und anspringen
start_frame = int(start_sekunde * fps)
end_frame = int(end_sekunde * fps)

cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
current_frame = start_frame

print("Inferenz gestartet. Drücke 'q' im Fenster, um abzubrechen.")

# 4. Frame-für-Frame-Verarbeitung
while cap.isOpened() and current_frame <= end_frame:
    cv2.namedWindow("YOLOv8 Bahnsignal-Erkennung Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("YOLOv8 Bahnsignal-Erkennung Live", 1280, 720)
    
    ret, frame = cap.read()
    if not ret:
        break  # Ende des Videos erreicht

    # Erkennung durchführen
    # conf=0.4 filtert Unsicherheiten unter 40% Wahrscheinlichkeit heraus
    results = model(frame, conf=0.4)

    # Bounding Boxen und Klassennamen auf das Bild zeichnen
    annotated_frame = results[0].plot(
        line_width = 2,
        font_size = 1.5,
        labels = True,
        conf = True,
        boxes = True
    )

    # Live-Ergebnis in einem Fenster anzeigen
    cv2.imshow("YOLOv8 Bahnsignal-Erkennung Live", annotated_frame)

    # Frame in das Output-Video schreiben
    out.write(annotated_frame)

    current_frame += 1

    # Mit der Taste 'q' kann die Wiedergabe jederzeit manuell beendet werden
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Ressourcen freigeben
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Fertig! Das verarbeitete Video wurde unter '{output_path}' gespeichert.")