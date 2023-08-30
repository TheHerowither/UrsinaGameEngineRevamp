#STH - Settings handler
from configparser import ConfigParser

class Settings:
    def __init__(self, file : str):
        self.file = file
        self.__parser__ = ConfigParser()

        print(f"[{__name__}] Initialized settings")
        self.__parser__.read(self.file)
    def get(self, section : str, section_key : str, type = None):
        if type == None:
            print(f"[{__name__}] Loaded variable {section_key} from {self.file}. Variable of type {type}")
            return self.__parser__.get(section, section_key)
        if type == float:
            print(f"[{__name__}] Loaded variable {section_key} from {self.file}. Variable of type {type}")
            return self.__parser__.getfloat(section, section_key)
        if type == int:
            print(f"[{__name__}] Loaded variable {section_key} from {self.file}. Variable of type {type}")
            return self.__parser__.getint(section, section_key)
        if type == bool:
            print(f"[{__name__}] Loaded variable {section_key} from {self.file}. Variable of type {type}")
            return self.__parser__.getboolean(section, section_key)
    def set(self, section : str, section_key : str, value, is_new_section : bool = True):
        if is_new_section:
            self.__parser__.add_section(section)
            print(f"[{__name__}] Added new section to {self.file}, {section}")
        self.__parser__.set(section, section_key, value)
        print(f"[{__name__}] Added section_key {section_key} to {section}. Value = {value}")
    def end(self):
        with open(self.file, "w") as config:
            config.write(self.__parser__)