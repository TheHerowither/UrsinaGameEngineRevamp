from dofef import *
from ursina import *
from lib.qol import *
from lib.uger.cla import *
from lib.uger.ats import *
from lib.uger.coder.ced import *
from lib.uger.editor.eui import *
from lib.uger.savehandling.svf import *





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



eui = EditorUI(window)
sl = UGERSelectionMenu(["cube", "sphere", "plane", "sky"], in_scene_entities, in_scene_entities_gizmo)
code_editor = UGERCodeEditor()
save_handler = UGERSaveHandler(os.getcwd())
save_field = UGERInputWIndow("Save as", "Save", save_handler.save, [in_scene_entities, ], save_handler)
save_handler.init("test")

#code_editor.enable()

#Input loop
def input(key):
    global in_scene_entities, in_scene_entities_gizmo
    if key == "left mouse down":
        for i in in_scene_entities_gizmo:
            if i.object.hovered:
                i.toggle()
            if (not i.object.hovered and not i.get_hovered()):
                i.disable()
    #if key == "b":
    #    Build(in_scene_entities)
    if key == "s":
        save_field.panel.enable()
    #if key == "l":
    #    in_scene_entities, in_scene_entities_gizmo = save_handler.load_entities()

#Update loop
def update():
    eui.update()
cam = EditorCamera()
app.run()