from ursina import *
from ursina.shaders import *
class UGEREntity(Button):
    def __init__(self, model):
        super().__init__(self)
        self.shader = lit_with_shadows_shader
        self.model = model
        self.color = color.random_color()
        self.position = (0,0,0)
        self.parent = scene
        self.highlight_color = self.color + Vec4(.1, .1, .1, .1)
class GizmoForObject(Entity):
    def __init__(self, object : UGEREntity):
        super().__init__()
        self.object = object
        self.x_slider = Draggable(position = self.object.position, parent = scene, lock = (0,1,1), plane_direction = (1,1,1), model = "cube", scale_z = .1, scale_y = .1,
                                   enabled = False)
        self.x_slider.x += 1
        self.y_slider = Draggable(position = self.object.position, parent = scene, lock = (1,0,1), plane_direction = (1,1,1), model = "cube", scale_z = .1, scale_x = .1,
                                   enabled = False)
        self.y_slider.y += 1
        self.z_slider = Draggable(position = self.object.position, parent = scene, lock = (1,1,0), plane_direction = (1,1,1), model = "cube", scale_y = .1, scale_x = .1,
                                   enabled = False)
        self.z_slider.z += 1

        self.toggled = False
    def get_hovered(self):
        e = [self.x_slider.hovered, self.y_slider.hovered, self.z_slider.hovered]
        return True in e
        
    def toggle(self):
        self.x_slider.enabled = not self.x_slider.enabled
        self.y_slider.enabled = not self.y_slider.enabled
        self.z_slider.enabled = not self.z_slider.enabled
        self.toggled = self.x_slider.enabled
    def disable(self):
        self.x_slider.enabled = False
        self.y_slider.enabled = False
        self.z_slider.enabled = False
    def update(self):
        obj = self.object
        
        self.object.x = self.x_slider.x-1
        self.object.y = self.y_slider.y-1
        self.object.z = self.z_slider.z-1
        self.x_slider.position = (obj.x + 1, obj.y, obj.z)
        self.y_slider.position = (obj.x, obj.y + 1, obj.z)
        self.z_slider.position = (obj.x, obj.y, obj.z + 1)