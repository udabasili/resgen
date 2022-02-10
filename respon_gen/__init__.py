import imghdr
import os
from .main import save_image
from PIL import Image


def initialize(input_directory, output_directory):
    counter = 1
    folder_name = f'image_{counter}'
    try:
        print('[+] Creating responsive images.... ')
        for file in os.listdir(input_directory):
            f_image = os.path.join(input_directory, file)
            img = Image.open(f_image)
            save_image(img, folder_name, output_directory)
            folder_name = f'image_{counter + 1}'
        print(f'[+] Responsive Images created. Saved in {output_directory}')
    except OSError as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)



