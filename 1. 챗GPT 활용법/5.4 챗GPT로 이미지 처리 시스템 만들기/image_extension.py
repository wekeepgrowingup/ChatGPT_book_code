import os
import zipfile
from PIL import Image

try:
    # Create the 'result' folder if it doesn't exist
    if not os.path.exists('result'):
        os.makedirs('result')

    # Loop through all files in the 'original' folder
    for filename in os.listdir('original'):
        # Get the file extension
        ext = os.path.splitext(filename)[1].lower()

        # If the file extension is not 'png', convert it to 'png'
        if ext != '.png':
            # Open the image using PIL
            with Image.open(os.path.join('original', filename)) as img:
                # Convert the image to 'RGBA' mode if it's not already
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')

                # Create a new filename with the '.png' extension
                new_filename = os.path.splitext(filename)[0] + '.png'
                # Save the image in the 'result' folder with the new filename
                img.save(os.path.join('result', new_filename), format='PNG')
        else:
            # If the file extension is 'png', just copy the file to the 'result' folder
            os.replace(os.path.join('original', filename), os.path.join('result', filename))

    # Create a zip file of the 'result' folder
    with zipfile.ZipFile('result.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('result'):
            for file in files:
                zipf.write(os.path.join(root, file))

    print('모두 완성!')
except Exception as e:
    print('오류 발생:', e)
