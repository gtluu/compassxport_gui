# CompassXport GUI Wrapper

A simple GUI wrapper for Bruker's CompassXport batch file conversion tool

## Easy Setup
Download the files [here](https://github.com/gtluu/compassxport_gui/raw/master/exe/compassxport_gui.zip) and unzip.

## Advanced Setup
1. Download the files in this repo and unzip.
2. By default, the CompassXport executable is looked for in the default file path: ```C:\Program Files (x86)\Bruker Daltonik\CompassXport\compassXport.exe```
  - If CompassXport is installed somewhere else, change the file path in ```config.ini``` using a text editor or go to ```Options > Change CompassXport.exe Location```.
3. If Python 2 is not set to PATH, do so.
  - Follow the instructions [here](https://gtluu.github.io/blanka/documentation/installation/index.html) to check if Python 2 is added to PATH and add it if it is not.
  - Note that ```pythonw.exe``` should also be added to PATH.

## Usage
1. Run ```run_compassxport_gui.bat``` or ```compassxport_gui.exe``` to start the program.
2. Select ```.d``` format files or a folder containing one or more ```.d``` format file(s).
3. Select the desired output folder.
4. Select the desired file format to convert to and whether or not peaks should be centroided.
5. Click ```Run``` to begin conversion.

## To Do
* Add menu option to choose CompassXport executable path and write to config file.
