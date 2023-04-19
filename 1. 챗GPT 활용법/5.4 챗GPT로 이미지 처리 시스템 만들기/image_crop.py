import os
from PIL import Image
import shutil

try:
    # create result folder
    os.mkdir('result')
    
    # loop through original folder and crop images
    for filename in os.listdir('original'):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            with Image.open(os.path.join('original', filename)) as img:
                width, height = img.size
                crop_size = min(width, height)
                left = (width - crop_size) // 2
                top = (height - crop_size) // 2
                right = (width + crop_size) // 2
                bottom = (height + crop_size) // 2
                img_cropped = img.crop((left, top, right, bottom))
                img_cropped.save(os.path.join('result', filename))
    
    # create zip file of result folder
    shutil.make_archive('result', 'zip', 'result')

    print("모두 완성!")
    
except Exception as e:
    print("오류 코드: ", e)

