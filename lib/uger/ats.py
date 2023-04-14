from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
import lib.uger.cla as cla
class UGERSelectionMenu:
    def __init__(self, models : list, in_scene_entities : list, in_scene_gizmos : list):
        self.in_scene_entities = in_scene_entities
        self.in_scene_gizmos = in_scene_gizmos
        btns = []
        for i in models:
            if type(i) == str:
                btns.append(
                    DropdownMenuButton(text = i,
                                        on_click = Func(self.add_to_scene, i))
                )
            else:
                raise TypeError(f"Input {i} at index {models.index(i)} is not a string")
        self.drop = DropdownMenu("Add to Scene", buttons = tuple(btns), enabled = False)
    def add_to_scene(self, model):
        if model != "sky":
            ent = cla.UGEREntity(model = model)
            self.in_scene_entities.append(ent)
            self.in_scene_gizmos.append(cla.GizmoForObject(ent))
        else:
            self.in_scene_entities.append(Sky())
    def input(self, key):
        if key == "right mouse up":
            self.drop.position = mouse.position
            self.drop.y += .01
            self.drop.enabled = True
        if key == "right mouse down":
            g = [self.drop.hovered]
            for i in self.drop.buttons:
                g.append(i.hovered)
            if not True in g:
                self.drop.disable()
        if key == "left mouse down":
            g = [self.drop.hovered]
            for i in self.drop.buttons:
                g.append(i.hovered)
            if not True in g:
                self.drop.disable()