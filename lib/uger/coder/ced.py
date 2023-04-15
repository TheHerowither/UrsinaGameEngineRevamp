import tkinter as tk
from tkinter.scrolledtext import ScrolledText
class UGERCodeEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        self.text_field = ScrolledText(self, width = 500, height = 100)
        self.text_field.pack()
    def enable(self):
        self.mainloop()