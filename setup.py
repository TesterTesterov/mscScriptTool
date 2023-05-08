import cx_Freeze
import sys
import os
import struct

base = None 

if sys.platform=='win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("main.py")]    

cx_Freeze.setup(
        name = "mscScriptTool 1.1",
        options = {"build_exe":{"packages":[]}},
        version="1.1",
        executables=executables) 