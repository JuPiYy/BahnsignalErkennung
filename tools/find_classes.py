import os
import xml.etree.ElementTree as ET

annotations_folder = 'dataset/Annotations'
all_classes = set()

for xml_file in os.listdir(annotations_folder):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(annotations_folder, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        for obj in root.iter('object'):
            cls_name = obj.find('name').text
            all_classes.add(cls_name)

# Exakte Liste für dein Konvertierungsskript:
CLASSES = sorted(list(all_classes))

print("Gefundene Klassen:", CLASSES)