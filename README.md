# PamphletMaker
A small python tool to automatically organize pdf-pages into small hand-bindable pamphlets

## Installation

First download the repository from github. Maker sure you have python 3.8 or newer installed.
Now open the terminal, navigate to the repository and run `pip install requirements.txt`

Alternatively you can install pypdf2 and tkinter seperately:

```
$ pip install pypdf2
$ pip install tkinter
```

## Usage

You can either use the pamphlet_maker in the console or as a desktop app. Please note that the pamphlet maker can only take pdfs with a multiple of 4 pages.

### Terinal
To open it as a console-app open the terminal and run `pamphlet_maker.py` with python3:

```
$ python3 pamphlet_maker.py
File: ~/Desktop/FILENAME.pdf
Document has 4 pages
Output: ~/Desktop/Output.pdf
```

The paths here are in the Linux format.

### Graphical User Interface

To open the program with a gui open the terminal and run `gui.py` with python3:

```
$ python3 gui.py
```

You will be confronted with a GUI with a file-select button and a make-button. First select a valid pdf, then press "Make".

> There are currently no security checks in place and if you select an invalid pdf things may go wrong. The system is currently untested

After the rearangement a save-dialog will open and after you have saved the new pdf the program will close.

The page-selector section is currently disabled, as these are planned features.
