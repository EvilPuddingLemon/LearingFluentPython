import tkinter
from PythonTest.S12.s12_2 import print_mro

print_mro(tkinter.Toplevel)

print_mro(tkinter.Widget)

print_mro(tkinter.Button)

print_mro(tkinter.Entry)

print_mro(tkinter.Text)

print(dir(tkinter.Button))