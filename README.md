# Ursina Game Engine Revamp (UGER)
Another rewrite of my ursina game engine

## Plans for the future
I have been planning on making this engine for a long time, and this is the third rewrite of it.
My plans are to add usability for coding objects, more editing options for objects and much, much more.

## Running the source code:
If you want to have an early look at the game engine you will need to obviusly download the source code first.
The you need to install the Ursina library and Pyinstaller, all other librarys are standard librarys from python.
```bash
pip install Ursina & pip install pyinstaller
```
After that, just run the engine and the engine will start.
### Controls:
##### Right click:
Open AddToScene menu, this will let you add objects to the scene
##### Left click:
Selection, you can select objects and/or move the around with this
##### B:
Build, This is subject to change, but this will let you build the scene that you have build

# Building:
A build is created using the DOFEF Build system, developed by me, that is included in the dofef.py file.
What it will do, is take the librarys saved in "alwaysinclude" and append them to a list that is used with the "--add-data" parameter of pyinstaller to add them to the build.
```python
import os
import PyInstaller.__main__ as pyi
alwaysinclude = os.getcwd() + "\\lib\\build\\alwaysinclude\\"
paths = os.listdir(alwaysinclude + "\\Lib\\site-packages")
data = []
for i in paths:
    data.append(f'--add-data=lib\\build\\alwaysinclude\\Lib\\site-packages\\{i};{i}')
pyi.run([
    "--console",
    "--onefile",
    "--clean",
    "--log-level=CRITICAL",
    f"-name={name}"
    *data,
    "lib\\build\\b.py",
        
])
```
This will create an executable named "b.exe" in the dist folder, which has the scene you built in it, just that you yet cannot move the camera in the build.


# Notes:
Please note that this is an early prototype, and a lot of it is subject to change.
I most of all hope that i manage to make the coding system waaaay better that in the originale UGER.

Build will probably be released on my itch.io page.