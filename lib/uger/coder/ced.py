import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
class UGERCodeEditor(object):
    #def __init__(self):
        #super().__init__(self)
    def mainloop(self):
        master = tk.Tk()
        master.geometry("1080x720")
        self.text_field = ScrolledText(master, width = 500, height = 100)
        self.text_field.pack()
        master.mainloop()
    def enable(self):
        th = Thread(target = self.mainloop)
        th.start()