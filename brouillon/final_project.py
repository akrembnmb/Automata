# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:09:06 2022

@author: akrembnmb
"""

from tkinter import *
from tkinter import ttk
import tkinter.font as font
from automata.fa.dfa import DFA
import ast
from PIL import ImageTk,Image
import graphviz
from automata.fa.nfa import NFA
import automata.base.exceptions as exceptions

root = Tk()
root.geometry("650x550")
root.title('automate generator')
Frame_Menu=ttk.Frame(root, padding=5)
Frame_Menu.grid()  
global img
global bg
img = Image.open("assets/pic.png")
bg = ImageTk.PhotoImage(img)

lbl = Label(Frame_Menu, image=bg)
lbl.place(x=0, y=0)
#Label_Welcome_vocab=ttk.Label(Frame_Menu,text='start by defining the number of elements of your automate" s vocabulary' ,font=('Arial',15)).grid(column=0,row=11)

mainloop() 