from ursina import *
from lib.uger.cla import *
from lib.uger.ats import *
from lib.uger.dofef import *
from lib.uger.editor.eui import *




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
sl = UGERSelectionMenu(["cube", "sphere", "plane"], in_scene_entities, in_scene_entities_gizmo)

#Input loop
def input(key):
    sl.input(key)
    #print(key)
    if key == "left mouse down":
        for i in in_scene_entities_gizmo:
            if i.object.hovered:
                i.toggle()
            if (not i.object.hovered and not i.get_hovered()):
                i.disable()
    if key == "f1 up":
        eui.enabled = not eui.enabled

#Update loop
def update():
    eui.update()
cam = EditorCamera()
app.run()