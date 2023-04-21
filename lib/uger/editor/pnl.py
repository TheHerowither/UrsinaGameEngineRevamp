from ursina import *
from lib.uger.cla import UGEREntity
class UGERPanel(Panel):
    def __init__(self, position):
        super().__init__()
        self.position = position

class UGERInspector(UGERPanel):
    def __init__(self, position):
        super().__init__(self)
        self.position = position
        self.active = None
        self.pos_txt = Text()
    def do_inspect(self, object_to_inspect):
        self.active = object_to_inspect
        self.pos_txt.enable()
    def update(self):
        if (self.active != None):
            if (self.active.toggled):
                ac = self.active.object
                self.pos_txt.text = (
                    f"Position  X:{round(ac.x, 2)}  Y:{round(ac.y, 2)}  Z:{round(ac.z, 2)}"
                    )
        else:
            self.pos_txt.disable()
    def reset(self):
        self.active = None
        self.disable()