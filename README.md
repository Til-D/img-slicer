# Img Slicer

A wee script slicing images along detected contours.

## Execution
The executable (MacOS) app can be found [here](blob/master/dist/ImageSlicer.zip).

To directly call from the command line, use the following modules:

### [crop.py](blob/master/crop.py)
```
Optional arguments:
  -h, --help  show this help message and exit
  -d FOLDER   output folder

Required arguments:
  -s FILE     input image file
```

### [gui.py](blob/master/gui.py)
Fires up a simple tkinter GUI

## Author
- [Tilman Dingler](https://github.com/Til-D/)

## Used libraries and utilities
- [openCV](https://pypi.org/project/opencv-python/) ([MIT license](https://github.com/jquery/jquery/blob/master/MIT-LICENSE.txt))

## License
All scripts are published under the [MIT license](http://www.opensource.org/licenses/mit-license) and [GPL v3](http://opensource.org/licenses/GPL-3.0).