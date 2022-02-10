# Responsive generator
Responsive images generator is a command line python package that would convert all the images in your folder to responsive ones
in their own designated folder. The main goal of this package is to help developers quickly generate
responsive images in bulk.

###Image Sizes 
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
pip install respon_gen
```

## Usage
You need to run the command in the folder where your image folder would be
For example, in the tree below,  if your image folder is  images, you run the command in root

```bash
├── root
│   ├── images

````

Features:
* functions.listChunker  --> generator that chunks and interable in evenly sized chunks 
* functions.weirdCase    --> converts a string to a totally unreadable format
* functions.report      --> prints to the console with a timestamp
* decorators.singleton  --> used for decoratint your class to make it a singleton

#### Demo:

```bash
 respon_gen --input_folder input_folder --output_folder output_folder
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
