from ursina import *
from lib.uger.editor.pnl import *
class EditorUI(Entity):
    def __init__(self, app : application):
        super().__init__(self)
        self.leftp = UGERPanel(position = app.left)
        self.rightp = UGERPanel(position = app.right)
    def update(self):
        self.leftp.enabled = self.enabled
        self.rightp.enabled = self.enabled