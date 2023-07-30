# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:29:54 2022

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
Frame_Menu=ttk.Frame(root, padding=5)
Frame_Menu.grid()
# NFA which matches strings beginning with 'a', ending with 'a', and containing
# no consecutive 'b's
nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1'}},
        # Use '' as the key name for empty string (lambda/epsilon) transitions
        'q1': {'a': {'q1'}, '': {'q2'}},
        'q2': {'b': {'q0'}}
    },
    initial_state='q0',
    final_states={'q1'}
)

final_states={'q1'}
transitions={
    'q0': {'a': {'q1'}},
    # Use '' as the key name for empty string (lambda/epsilon) transitions
    'q1': {'a': {'q1'}, '': {'q2'}},
    'q2': {'b': {'q0'}}
}
if nfa.accepts_input("aa"):
    print('accepted')
else:
    print('rejected')
Transitions={"q0": {"a": "q1"}, "q1": {"a": "q1", "b": "q2"},"q2": {"b": "q0"}}


l=list(nfa.read_input_stepwise('aaaa'))
print(l)
ch="aa"
def draw():
    f.attr('node', shape='doublecircle')
    for F_state in final_states:
        f.node(F_state)
    f.attr('node', shape='circle')
    for start,Dic_State in Transitions.items():
        for k,v in Dic_State.items():
            f.edge(start, v, label=k)
        
                
    
    
def afficher():
    k=0
    for i in range ( len(ch)):
        while (k<=len(l)):
            f = graphviz.Digraph('finite_state_machine', filename='part'+str(i),format="png")
            f.attr(rankdir='LR', size='8,5')
            f.attr('node', shape='circle')
            
            f.view()
            k=k+1
            
        
        
    
                



Button_Submit00=ttk.Button(Frame_Menu,text='Submit',command=afficher).grid(column=2,row=4)
root.mainloop()
                
