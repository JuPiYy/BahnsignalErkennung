from ultralytics import YOLO

# 1. Modell laden
model = YOLO("yolov8m.pt")

# 2. Training starten
results = model.train(
    data="/content/dataset/gerald.yaml",  # Pfad auf der schnellen Colab-SSD
    epochs=100,
    imgsz=640,
    batch=32,
    workers=8,
    project="/content/drive/MyDrive/YOLO_Runs",  # Speicherziel im Google Drive
    name="yolov8m_colab_run",
    save_period=5,  # Speichert alle 5 Epochen einen Sicherheits-Checkpoint
)