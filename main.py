import os
import cv2
from paddleocr import PPStructure, save_structure_res

# table recognition
table_engine = PPStructure(layout=False, show_log=True, use_gpu=False)

save_folder = './output'
img_path = 'ppstructure/docs/table/table.jpg'
img = cv2.imread(img_path)
result = table_engine(img)
save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

for line in result:
    line.pop('img')
    print(line)
