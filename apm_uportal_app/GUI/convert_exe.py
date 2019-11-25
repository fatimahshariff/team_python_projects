import cx_Freeze
import sys
import os 
from tkinter import *
from tkinter import filedialog

base = None 

if sys.platform=='win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("GUI.py")]    

cx_Freeze.setup(
        name = "Name",
        options = {"build_exe":{"packages":["tkinter"]}},
        version="0.01",
        executables=executables) 