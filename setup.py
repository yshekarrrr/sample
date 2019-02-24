import sys
from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = r'C:\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python35\tcl\tk8.6'
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
executables = [
    Executable('example2.py', base='Console')
]
setup(name="example2",
      version='version',
      description='desc',
      executables=executables
      )