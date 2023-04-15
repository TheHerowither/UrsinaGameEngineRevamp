import os, shutil
import PyInstaller.__main__ as pyi
from ursina import *
from threading import Thread
from lib.uger.cla import UGEREntity

def write_file(list):
    ent = ["from ursina import *", "from ursina.shaders import lit_with_shadows_shader", "app = Ursina()"]
    for i in list:
        if type(i) == UGEREntity:
            ent.append(f"Entity(position = {i.position}, scale = {i.scale}, model = '{i.strmodel}', color = {i.color}, shader = lit_with_shadows_shader, rotation = {i.rotation})")
        elif type(i) == DirectionalLight:
            ent.append(f"DirectionalLight(position = {i.position}, shadows = {i.shadows}, scale = {i.scale}, rotation = {i.rotation})")
        elif type(i) == Sky:
            ent.append("Sky()")
    string = "\n".join(ent)+"\napp.run()"
    with open("lib\\build\\b.py", "w") as f:
        
        f.write(string)
def _del_folder(folder_path):
    
    folder = folder_path
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            os.rmdir(folder)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    

def _build(in_scene_entities, name : str):
    start_time = time.time()
    write_file(in_scene_entities)
    alwaysinclude = os.getcwd() + "\\lib\\build\\alwaysinclude\\"
    paths = os.listdir(alwaysinclude + "\\Lib\\site-packages")
    data = []
    for i in paths:
        data.append(f'--add-data=lib\\build\\alwaysinclude\\Lib\\site-packages\\{i};{i}')
    #print(data)
    pyi.run([
        "--console",
        "--onefile",
        "--clean",
        "--log-level=CRITICAL",
        f"-name={name}"
        *data,
        "lib\\build\\b.py",
        
    ])
    print("[DOFEF Build system]: Build complete, cleaning up")
    _del_folder(f"{os.getcwd()}\\build")
    os.system("del b.spec")
    print("[DOFEF Build system]: Completed building program in:", time.time()-start_time, "seconds")
def Build(in_scene_entities : list):
    th = Thread(target = _build, args = [in_scene_entities,])
    print("[DOFEF Build system]: Initialized build thread", th)
    th.start()
    print("[DOFEF Build system]: Begining to build program on thread", th)
    print("[DOFEF Build system]: Disabling pyinstaller output")