# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:10:44 2022

@author: akrembnmb
"""

from tkinter import *
from tkinter import ttk
import tkinter.font as font
from automata.fa.dfa import DFA
import json
from PIL import ImageTk,Image
import graphviz
from automata.fa.nfa import NFA



root = Tk()
root.minsize(height=550,width=650)
root.title('automate generator')



img2=Image.open("assets/pic.png")

Automat_View=ImageTk.PhotoImage(img2)
Label_img=ttk.Label(root,image=Automat_View)
Label_img.place(x=0, y=0)
#Label_text=ttk.Label(Frame_Menu,text="hey im testing this").grid(column=0,row=1)
root.mainloop()

