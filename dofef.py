import os
import PyInstaller.__main__ as pi


def write_file(list):
    ent = ["from ursina import *", "app = Ursina()"]
    for i in list:
        ent.append(f"Entity(position = {i.position}, model = '{i.strmodel}', color = {i.color})")
    string = "\n".join(ent)+"\napp.run()"
    with open("lib\\build\\b.py", "w") as f:
        
        f.write(string)

def Build(in_scene_entities : list):
    write_file(in_scene_entities)
    alwaysinclude = os.getcwd() + "\\lib\\build\\alwaysinclude\\"
    paths = os.listdir(alwaysinclude + "\\Lib\\site-packages")
    data = []
    for i in paths:
        data.append(f'--add-data=lib\\build\\alwaysinclude\\Lib\\site-packages\\{i};{i}')
    print(data)
    pi.run([
        "--console",
        "--onefile",
        *data,
        "lib\\build\\b.py",
        
    ])