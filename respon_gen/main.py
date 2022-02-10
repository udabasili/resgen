import argparse
import os
import sys
from . import initialize
from .bulk_resizer import save_image


def main():
    parser = argparse.ArgumentParser(prog="responsive-images-gen",
                                     description="Generate multiple responsive images that can used for your web "
                                                 "application "
                                     )
    parser.add_argument(
        '-i',
        '--input_folder',
        dest='input_folder',
        help='The name of the input folder where the image(s) are located ')
    parser.add_argument(
        '-o',
        '--output_folder',
        dest='output_folder',
        help='The name of the output folder you want to place the saved images')
    args = parser.parse_args()

    if not args.input_folder:
        print('You must put in the input folder name')
        return
    if not args.output_folder:
        print('You must put in the output folder name')
        return
    current_directory = os.getcwd()
    try:
        [output_folder, input_folder] = args
        input_directory = os.path.join(current_directory, input_folder)
        output_directory = os.path.join(current_directory, output_folder)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        initialize(input_directory, output_directory)
    except OSError as e:
        print(e.message)
    except KeyboardInterrupt:
        print('[-] Detected CTRL +C. Exiting....')
        sys.exit()
