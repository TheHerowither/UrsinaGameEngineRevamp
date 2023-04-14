import os
import PyInstaller.__main__ as pi


def Build(in_scene_entities : list):
    alwaysinclude = os.getcwd() + "\\lib\\build\\alwaysinclude\\"
    paths = os.listfir(alwaysinclude + "\\Lib\\site-packages")
    data = []
    for i in paths:
        data.append("--add_data="+i)
    pi.run(
        "b.py",
        "--console",
        *data
    )