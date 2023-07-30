# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:50:55 2022

@author: akrembnmb
"""

from tkinter import *
from tkinter import ttk
import tkinter.font as font

import ast
from PIL import ImageTk,Image
import graphviz


Letters_List=[]
Number_V=0
Number_S=0
Transitions_Dict = dict()
States=[]
Initial_state=[]
final_states=[]
transitions=""
Number_F_S=0
test=FALSE
list_S=list()

root = Tk()
root.geometry("650x550")
root.title('automata')
root.iconbitmap('assets/hypnose.ico')
img2=Image.open("assets/menu.png")
Automat_View_Path=ImageTk.PhotoImage(img2)
Label_img=ttk.Label(root,image=Automat_View_Path)
Label_img.place(x=0, y=0)

def menu():
    def vocab_page():
        
        but1.destroy()
        but2.destroy()
        global Automat_View_Path
        Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/2.png"))
        Label_img=ttk.Label(root,image=Automat_View_Path)
        Label_img.place(x=0, y=0)

        Vocab_Sum = IntVar()
        global Number_Input
        Number_Input=Entry(root,textvariable=Vocab_Sum,highlightthickness=2)
        Number_Input.place(x=20,y=250)
        def next():
            def vocab_letters():
                def save3():
                    print("im here")
                    Letters_List.append(Letter.get())
                    print(Letters_List)
                def cases_page():
                    Label_Vocab_1.destroy()
                    Letters_Input.destroy()
                    Button_Submit.destroy()
                    Button_Next2.destroy()
                    global Automat_View_Path
                    Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/4.png"))
                    Label_img=ttk.Label(root,image=Automat_View_Path)
                    Label_img.place(x=0, y=0)
                    
                    States_Sum = IntVar()
                    def Save4():
                        print("im here")
                        global Number_S
                        Number_S=States_Sum.get()
                        for i1 in range (Number_S):
                            States.append('q'+str(i1))
                        print(Number_S)
                        print(States)
                    def Matrice_Page():
                        
                        def Save5():
                            print("hey")
                            global transitions
                            transitions=T_diction.get()
                            print("transtions as string =", transitions)
                            global Transitions_Dict
                            Transitions_Dict = ast.literal_eval(transitions)
                            print(type(Transitions_Dict))
                            print(Transitions_Dict)
                            
                        def Page_Intial():
                            def Save6():
                                global Initial_state
                                Initial_state.append(State_In.get())
                                print(Initial_state)
                            def Save7():
                                global Number_F_S
                                Number_F_S=Num_S.get()
                                print(Number_F_S)
                            def Final_States_Page():
                                def Save8():
                                    print("ty")
                                    final_states.append(State_String.get())
                                    print(final_states)
                                def Automat_Welcome_Page():
                                    print("hey")
                                    
                                
                                Label_2.destroy()
                                I_Input.destroy()
                                Button_Submit33.destroy()
                                Label_3.destroy()
                                F_Sum_Input.destroy()
                                Button_Submit31.destroy()
                                Button_Next00.destroy()
                                global Automat_View_Path
                                Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/0.png"))
                                Label_img=ttk.Label(root,image=Automat_View_Path)
                                Label_img.place(x=0, y=0)
                                Label_Add2=Label(root,bg="#ffffff").grid(column=0,row=0)
                                Label_Add2=Label(root,bg="#ffffff").grid(column=0,row=1)
                                Label_Add2=Label(root,bg="#ffffff").grid(column=3,row=2)
                                Label_Add2=Label(root,bg="#ffffff").grid(column=3,row=3)
                                Label_Add2=Label(root,bg="#ffffff").grid(column=3,row=4)
                                Label_Add2=Label(root,bg="#ffffff").grid(column=0,row=5)
                                Label_Add2=Label(root,bg="#ffffff").grid(column=0,row=6)
                                
                                c=7
                                a=0
                                sf=Number_F_S 
                                State_String = StringVar()
                                while  sf!=0:
                                    global Label_f
                                    Label_f=Label(root,text='final state n°'+str(a) ,font=('french script mt',10))
                                    Label_f.grid(column=0,row=c) 
                                    global I_Input0
                                    I_Input0=Entry(root,textvariable=State_String)
                                    I_Input0.grid(row=c,column=1)
                                    global Button_Submit00
                                    Button_Submit00=Button(root,text='Submit',command=Save8)
                                    Button_Submit00.grid(column=2,row=c)
                                    c=c+1
                                    a=a+1
                                    sf=sf-1
                                global  Button_Sub
                                Button_Sub=Button(root,text='Visualize your automate',command=Automat_Welcome_Page)
                                Button_Sub.grid(column=2,row=c+1)
                                
                                
                            print("im tired")
                            T_Input.destroy()
                            Button_Next4.destroy()
                            Button_Submit3.destroy()
                            global Automat_View_Path
                            Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/0.png"))
                            Label_img=ttk.Label(root,image=Automat_View_Path)
                            Label_img.place(x=0, y=0)
                            
                            global Label_2
                            Label_2=Label(root,text='type the initial state' ,font=('french script mt',15))
                            Label_2.place(x=50,y=250)
                            State_In = StringVar()
                            global I_Input
                            I_Input=Entry(root,textvariable=State_In)
                            I_Input.place(x=350,y=250)
                            global Button_Submit33
                            Button_Submit33=Button(root,text='Submit',command=Save6)
                            Button_Submit33.place(x=500,y=250)
                            global Label_3
                            Label_3=Label(root,text='type the number of the final states' ,font=('Arial',10))
                            Label_3.place(x=50,y=350)
                            Num_S = IntVar() 
                            global F_Sum_Input
                            F_Sum_Input=Entry(root,textvariable=Num_S)
                            F_Sum_Input.place(x=350,y=350)
                            global Button_Submit31
                            Button_Submit31=Button(root,text='Submit',command=Save7)
                            Button_Submit31.place(x=500,y=350)
                            global Button_Next00
                            Button_Next00=Button(root,text='Next',command=Final_States_Page)
                            Button_Next00.place(x=500,y=500)
                            
                        States_Sum_Input.destroy()
                        Button_Submit2.destroy()
                        Button_Next3.destroy()
                        global Automat_View_Path
                        Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/5.png"))
                        Label_img=ttk.Label(root,image=Automat_View_Path)
                        Label_img.place(x=0, y=0)
                        T_diction = StringVar()
                        global T_Input
                        T_Input=Entry(root,textvariable=T_diction,highlightthickness=2)
                        T_Input.place(x=100,y=200)
                        global Button_Submit3
                        Button_Submit3=Button(root,text='Submit',command=Save5)
                        Button_Submit3.place(x=200,y=200)
                        global Button_Next4
                        Button_Next4=Button(root,text='Next',command=Page_Intial)
                        Button_Next4.place(x=300,y=300)
                        print("hey")
                    myFont3 = font.Font(family='french script mt',size=15)
                    global States_Sum_Input
                    States_Sum_Input=Entry(root,textvariable=States_Sum,highlightthickness=2)
                    States_Sum_Input.place(x=10,y=200)
                    global Button_Submit2
                    Button_Submit2=Button(root,text='Submit1',font=myFont3,command=Save4)
                    Button_Submit2.place(x=250,y=190)
                    global Button_Next3
                    Button_Next3=Button(root,text='Next',width=6,font=myFont3,command=Matrice_Page)
                    Button_Next3.place(x=250,y=300)
                    print("i ll be back")
                Letter=StringVar()
                print(Number_V)
                global Letters_List
                j=Number_V
                i=9 
                n=0
                Label_Add=Label(root,bg="#ffffff").grid(column=1,row=0)
                Label_Add=Label(root,bg="#ffffff").grid(column=2,row=1)
                Label_Add=Label(root,bg="#ffffff").grid(column=3,row=2)
                Label_Add=Label(root,bg="#ffffff").grid(column=4,row=3)
                Label_Add=Label(root,bg="#ffffff").grid(column=1,row=4)
                Label_Add=Label(root,bg="#ffffff").grid(column=1,row=5)
                Label_Add=Label(root,bg="#ffffff").grid(column=3,row=6)
                Label_Add=Label(root,bg="#ffffff").grid(column=3,row=7)
                Label_Add=Label(root,bg="#ffffff").grid(column=9,row=8)
                while j != 0 :
                    global Label_Vocab_1
                    Label_Vocab_1=Label(root,text='element number'+' '+str(n),bg="#ffffff" ,font=('french script mt',20))
                    Label_Vocab_1.grid(column=0,row=i)
                    global Letters_Input 
                    Letters_Input=Entry(root,textvariable=Letter,highlightthickness=2)
                    Letters_Input.grid(column=1,row=i)
                    global Button_Submit
                    myFont3 = font.Font(family='french script mt',size=15)
                    Button_Submit=Button(root,text='Submit',bg="#ffffff",command=save3,height=0,width=0,font=myFont3)
                    Button_Submit.grid(column=2,row=i)
                    n=n+1
                    j=j-1
                    i=i+1
                global Button_Next2
                Label_Add=Label(root,bg="#ffffff").grid(column=9,row=i)
                Button_Next2=Button(root,text='Next',bg="#ffffff",command=cases_page,height=0,width=6,font=myFont3)
                Button_Next2.grid(column=2,row=i+2)
            def save1():
                global Number_V 
                Number_V=Vocab_Sum.get()
                print(Number_V)
            save1()
            Button_Next.destroy()
            Number_Input.destroy()
            global Automat_View_Path
            Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/3.png"))
            Label_img=ttk.Label(root,image=Automat_View_Path)
            Label_img.place(x=0, y=0)
            vocab_letters()
            
            
        myFont2 = font.Font(family='french script mt',size=15)
        global Button_Next
        Button_Next=Button(root,text='next',font=myFont2,width=5,command=next)
        Button_Next.place(x=290,y=340)
    
    myFont = font.Font(family='french script mt',size=22)
    myFont2 = font.Font(family='french script mt',size=15,weight="bold")
    global but1
    but1= Button(root,text='Start',command=vocab_page,height=1,width=9,font=myFont,bg="#c0deef")
    but1.place(x=429, y=274)
    global but2
    but2= Button(root,text='?',command=vocab_page,height=0,width=13,font=myFont2,bg="#f2f2f2",fg='#c3c3c3')
    but2.place(x=427, y=351)
  
  
   
    
    
menu()
root.mainloop()