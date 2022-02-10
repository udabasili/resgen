import os

sizes = [
    1920,
    1600,
    1366,
    1024,
    768,
    640
]


def save_image(image, name, output_directory):
    try:
        for size in sizes:
            resized_image = image.resize((size, size))
            if not os.path.exists(os.path.join(output_directory, name)):
                os.mkdir(os.path.join(output_directory, name))
            current_file_name = os.path.join(output_directory, name, f'{name}_{size}_.jpeg')
            print(current_file_name)
            resized_image.save(current_file_name)
    except Exception as e:
        raise Exception(e)




