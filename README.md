# Responsive generator
Responsive images generator is a command line python package that would convert all the images in your folder to responsive ones
in their own designated folder. The main goal of this package is to help developers quickly generate
responsive images in bulk.

### Image Sizes that would be generated
The Image sizes that would be generated would be based on the recommendations of this [article](https://medium.com/hceverything/applying-srcset-choosing-the-right-sizes-for-responsive-images-at-different-breakpoints-a0433450a4a3)
- 1920px (For FullHD Screens and up)
- 1600px (For desktops anf tables in portrait mode
- 1366px (Desktop)
- 1024px (1024X768 screens)
- 768px (Useful for 2x 375px mobile screens as well as any device)
- 640px (for smartphones)


## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Res like below. 
Rerun this command to check for and install  updates .

```bash
pip install resgen
```

## Usage

**Make use you have python installed and Python script has been added to [Windows Path](https://datatofish.com/add-python-to-windows-path/), [Mac's Path](https://www.educative.io/edpresso/how-to-add-python-to-the-path-variable-in-mac) or Linux Path**

You need to run the command in the folder where your image folder would be
For example, in the tree below,  if your image folder is  images, you run the command in root

```bash
├── root
│   ├── images

````
While inside the folder, set the output folder and input folder

```bash
resgen  --input_folder  [input_folder] --output_folder [output_folder] 
```
or (if you havent added Python/Script to path)
```bash
python -m resgen  --input_folder  [input_folder] --output_folder [output_folder] 
```


- input_folder: The name of the input folder where the images are. Don't use ./input_folder . Just the name only
- output_folder: The name of the input folder where you want to save the files

**For Windows: To use this command without adding Python -m as the beginning, Make sure Python Script
is added to your PATH. [Refer Here](https://datatofish.com/add-python-to-windows-path/)**




The command would create folders in the output folder depending on the number of the images you have.

```bash
├── output_folder
│   ├── image_1
        ├── image_1_640_.jpeg
        ├── image_1_760_.jpeg
        
````
image_1_760_.jpeg represent the image with 760px for instance



#### Demo:

```bash
 resgen --input_folder input_folder --output_folder output_folder
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
