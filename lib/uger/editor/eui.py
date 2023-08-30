#EUI - Editor UI
from ursina import *
from lib.uger.editor.pnl import *
from lib.uger.savehandling.svf import *
class EditorUI(Entity):
    def __init__(self, app : application):
        super().__init__(self)
        #self.leftp = UGERPanel(position = app.left)
        self.rightp = UGERInspector(position = app.right)
    def update(self):
        #self.leftp.enabled = self.enabled
        self.rightp.enabled = self.enabled
        self.rightp.update()
    def ins(self, obj):
        if obj != None:
            self.rightp.do_inspect(obj)
        else:
            self.rightp.reset()

class UGERInputWindow:
    def __init__(self, title, button_text, on_submit, params, save_handler = None):
        
        self.title = title
        self.popup = True
        self.params = params
        self.save_handler = save_handler
        self.enabled = False
        self.on_submit = on_submit
        self.input = InputField(parent = self)
        self.returned = None
        self.has_been_called = False
        self.panel = WindowPanel(popup = self.popup, title = self.title, enabled = self.enabled, content = (
            Space(),
            self.input,
            Button(text = button_text, on_click = self.returnval, parent = self)
        ))
    def returnval(self):
        self.has_been_called = False
        self.panel.disable()
        if "returnval" in self.params:
           self.params[self.params.index("returnval")] = self.input.text
        if self.save_handler != None:
            self.save_handler.init(self.input.text)
        self.returned = self.on_submit(*self.params)
        self.has_been_called = True