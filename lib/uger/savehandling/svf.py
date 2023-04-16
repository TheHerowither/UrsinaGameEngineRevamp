import os
from ursina import *
from lib.uger.cla import *
def StrToTuple(string):
    t = string.split()
    tup = []
    for i in t:
        i = i.replace("(", "")
        i = i.replace(")", "")
        i = i.replace(",", "")
        tup.append(float(i))
    return tuple(tup)

class UGERSaveHandler:
    def __init__(self, root_folder):
        self.root = root_folder
    def init(self, name):
        self.name = name
        #Checking if projects folder exists, and if not make it
        if not os.path.exists(self.root+"\\projects"):
            os.mkdir(self.root+"\\projects")
        #Checking if the folder for the project {name} exists, and if not make it
        if not os.path.exists(self.root+f"\\projects\\{self.name}"):
            os.mkdir(self.root+f"\\projects\\{self.name}")
    def save(self, in_scene_entities):
        ent = []
        for i in in_scene_entities:
            if type(i) == UGEREntity: ent.append(f"Entity;{tuple(i.position)};{tuple(i.rotation)};{tuple(i.scale)};{i.strmodel};{tuple(i.color)};lit_with_shadows_shader")
            elif type(i) == DirectionalLight: ent.append(f"DirectionalLight;{tuple(i.position)};{i.shadows};{tuple(i.scale)};{tuple(i.rotation)})")
            elif type(i) == Sky: ent.append("Sky;")
        with open(self.root+f"\\projects\\{self.name}\\entities.ugersf", "w") as f:
            for i in ent:
                f.write(i+"\n")
        print(f"[{__name__}]: Saved!")
    def load_entities(self) -> tuple:
        ents = []
        gizmos = []
        with open(self.root+f"\\projects\\{self.name}\\entities.ugersf") as f:
            content = f.read()
            lines = content.split("\n")
            for line in lines:
                params = line.split(";")
                if params[0] == "Entity": 
                    e = UGEREntity(position = StrToTuple(params[1]), rotation = StrToTuple(params[2]), scale = StrToTuple(params[3]), model = params[4], color = StrToTuple(params[5]), shader = params[6])
                    ents.append(e)
                    gizmos.append(GizmoForObject(e))
                if params[0] == "DirectionalLight": ents.append(DirectionalLight(position = StrToTuple(params[1]), shadows = params[2], scale = StrToTuple(params[3]), rotation = StrToTuple(params[4])))
                if params[0] == "Sky": ents.append(Sky())
        print(f"[{__name__}] Loaded savefile {self.name}")
        return ents, gizmos