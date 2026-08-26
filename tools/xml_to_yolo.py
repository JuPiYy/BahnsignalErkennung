import os
import xml.etree.ElementTree as ET

# Liste aller Klassen genau in der Reihenfolge, wie sie in den XMLs stehen!
CLASSES = ['El_6', 'Hectometer_Sign', 'Hp_0_HV', 'Hp_0_Ks', 'Hp_0_Sh', 'Hp_1', 'Hp_2', 'ICE', 'Ks_1', 'Ks_2', 'LZB', 'Lf_2', 'Lf_3', 'Lf_6', 'Lf_7', 'Mast_Sign_WRW', 'Mast_Sign_WYWYW', 'Mast_Sign_Y_Triangle', 'Ne_1', 'Ne_2', 'Ne_3_1', 'Ne_3_2', 'Ne_3_3', 'Ne_3_4', 'Ne_3_5', 'Ne_4', 'Ne_5', 'Ne_6', 'Ne_7a', 'Ne_7b', 'Platform_Display', 'Platform_Text_Sign', 'Platform_Track_Sign', 'Platform_Warn_Sign', 'Ra_10', 'Ride_Indicator_1', 'Ride_Indicator_Off', 'Sh_0', 'Sh_1', 'Sh_2', 'Sign_Back', 'Signal_Back', 'Signal_Identifier_Sign', 'Signal_Invalid', 'Signal_Off', 'So_20_Left', 'So_20_Right', 'Traffic_Light', 'Traffic_Sign', 'Vr_0', 'Vr_1', 'Vr_2', 'Wn_1', 'Wn_2', 'Zs_2', 'Zs_2v', 'Zs_3', 'Zs_3v', 'Zs_6', 'Zs_Off']

def convert_box(size, box):
    # Wandelt (xmin, xmax, ymin, ymax) in normierte YOLO-Koordinaten um
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0 - 1.0
    y = (box[2] + box[3]) / 2.0 - 1.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)

def convert_xml_to_yolo(xml_folder, output_txt_folder):
    os.makedirs(output_txt_folder, exist_ok=True)
    
    for xml_file in os.listdir(xml_folder):
        if not xml_file.endswith('.xml'):
            continue
            
        xml_path = os.path.join(xml_folder, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        txt_name = os.path.splitext(xml_file)[0] + '.txt'
        txt_path = os.path.join(output_txt_folder, txt_name)
        
        with open(txt_path, 'w') as out_file:
            for obj in root.iter('object'):
                cls_name = obj.find('name').text
                if cls_name not in CLASSES:
                    continue
                cls_id = CLASSES.index(cls_name)
                
                xml_box = obj.find('bndbox')
                b = (
                    float(xml_box.find('xmin').text),
                    float(xml_box.find('xmax').text),
                    float(xml_box.find('ymin').text),
                    float(xml_box.find('ymax').text)
                )
                bb = convert_box((w, h), b)
                out_file.write(f"{cls_id} {' '.join([f'{a:.6f}' for a in bb])}\n")

if __name__ == '__main__':
    # Pfade anpassen:
    convert_xml_to_yolo('dataset/Annotations', 'dataset/XMLAnnotations')
    print("Konvertierung abgeschlossen!")