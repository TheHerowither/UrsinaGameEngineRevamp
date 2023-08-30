#Pre import
import sys, os
if not os.path.exists("logs/"): os.mkdir("logs")
origstd = sys.stdout
origerr = sys.stderr
__name__ = "UGER.__main__"
sys.stdout = open(f"logs/{__name__}.log", "w")
sys.stderr = open(f"logs/{__name__}.err.log", "w")
#Imports
from ursina import *

#Import internal librarys
from dofef import *
from lib.uger.cla import *
from lib.uger.ats import *
from lib.uger.sth import *
from lib.uger.coder.ced import *
from lib.uger.editor.eui import *
from lib.uger.savehandling.svf import *


#Pre init
Clean(os.getcwd())

#Initialization
app = Ursina()
window.borderless = False




#Define variables
in_scene_entities = []
in_scene_entities_gizmo = []

#Define lighting
pivot = Entity()
sun = DirectionalLight(parent=pivot, y=10, z=10, shadows=True, scale = 10)
sun.look_at((0,0,0))
in_scene_entities.append(sun)


settings = Settings("settings.ini")

eui = EditorUI(window)
sl = UGERSelectionMenu(["cube", "sphere", "plane", "sky"], in_scene_entities, in_scene_entities_gizmo)
code_editor = UGERCodeEditor()
save_handler = UGERSaveHandler(os.getcwd())
save_field = UGERInputWindow("Enter name", "Save", save_handler.save, [in_scene_entities, ], save_handler)
build_input = UGERInputWindow("Build as", "Build", Build, [in_scene_entities, "returnval",])
load_input = UGERInputWindow("Load", "Load!", save_handler.load_entities, ["returnval",])

#Input loop
def input(key):
    if key == "left mouse down":
        for i in in_scene_entities_gizmo:
            if i.object.hovered:
                i.toggle()
            if (not i.object.hovered and not i.get_hovered()):
                i.disable()
    
    
save_field.panel.enable()
#Update loop
def update():
    global in_scene_entities, in_scene_entities_gizmo
    eui.update()
    if (held_keys["control"] and held_keys["b"]):
        build_input.panel.enable()
    if (held_keys["control"] and held_keys["l"]):
        load_input.panel.enable()
    
    if load_input.has_been_called:
        if load_input.returned != None:
            [destroy(i) for i in in_scene_entities]
            [destroy(j) for j in in_scene_entities_gizmo]
            in_scene_entities, in_scene_entities_gizmo = load_input.returned
            load_input.has_been_called = False
cam = EditorCamera()
app.run()