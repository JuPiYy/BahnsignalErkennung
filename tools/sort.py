import os
import random
import shutil

# Pfade anpassen
IMAGE_DIR = r"C:\Users\Josef\source\repos\BahnsignalErkennung\GERALD\dataset\JPEGImages"
LABEL_DIR = r"C:\Users\Josef\source\repos\BahnsignalErkennung\GERALD\dataset\yololabels"
OUTPUT_DIR = r"C:\Users\Josef\source\repos\BahnsignalErkennung\GERALD\dataset\dataset"

# Zielordner erstellen
for split in ['train', 'val']:
    os.makedirs(os.path.join(OUTPUT_DIR, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'labels', split), exist_ok=True)

# Alle Bilddateien auflisten
images = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Mischen für zufällige Aufteilung
random.seed(42)  # Für Reproduzierbarkeit
random.shuffle(images)

# 80% Training, 20% Validation
split_idx = int(len(images) * 0.8)
train_images = images[:split_idx]
val_images = images[split_idx:]

def move_files(file_list, split):
    for img_name in file_list:
        base_name = os.path.splitext(img_name)[0]
        txt_name = base_name + ".txt"

        img_src = os.path.join(IMAGE_DIR, img_name)
        txt_src = os.path.join(LABEL_DIR, txt_name)

        img_dst = os.path.join(OUTPUT_DIR, 'images', split, img_name)
        txt_dst = os.path.join(OUTPUT_DIR, 'labels', split, txt_name)

        # Bild kopieren
        if os.path.exists(img_src):
            shutil.copy(img_src, img_dst)

        # Zuordnungs-TXT kopieren (falls vorhanden)
        if os.path.exists(txt_src):
            shutil.copy(txt_src, txt_dst)

# Dateiverschiebung ausführen
move_files(train_images, 'train')
move_files(val_images, 'val')

print(f"Fertig! {len(train_images)} Bilder in 'train' und {len(val_images)} Bilder in 'val' einsortiert.")