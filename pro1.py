import Tkinter
from Tkinter import *
import tkMessageBox
import Tkinter
import random

top=Tk()
frame=Frame(top,bg='goldenrod1')
frame.grid(row=0,column=0)

bframe=Frame(top)
bframe.grid(row=1,column=0)

frameb=Frame(top)
frameb.grid(row=3,column=0,pady=5)

Var1=IntVar()
Var1.set(3)
mvar=StringVar()
maxno=0
global picflag

def randompics():
    global picflag
    Apic=picflag
    hang(Apic)

def msg(event=None):
     mainset()
     randompics()

#functions of button
def f1f():
     a=mvar.get()
     mvar.set(a+'1')
def f2f():
     a=mvar.get()
     mvar.set(a+'2')
def f3f():
     a=mvar.get()
     mvar.set(a+'3')
def f4f():
     a=mvar.get()
     mvar.set(a+'4')
def f5f():
     a=mvar.get()
     mvar.set(a+'5')
def f6f():
     a=mvar.get()
     mvar.set(a+'6')
def f7f():
     a=mvar.get()
     mvar.set(a+'7')
def f8f():
     a=mvar.get()
     mvar.set(a+'8')
def f9f():
     a=mvar.get()
     mvar.set(a+'9')
def f0f():
     a=mvar.get()
     mvar.set(a+'0')

     
def af():
     a=mvar.get()
     mvar.set(a+'A')
def bf():
     a=mvar.get()
     mvar.set(a+'B')
def cf():
     a=mvar.get()
     mvar.set(a+'C')
def df():
     a=mvar.get()
     mvar.set(a+'D')
def ef():
     a=mvar.get()
     mvar.set(a+'E')
def ff():
     a=mvar.get()
     mvar.set(a+'F')
def gf():
     a=mvar.get()
     mvar.set(a+'G')
def hf():
     a=mvar.get()
     mvar.set(a+'H')
def iif():
     a=mvar.get()
     mvar.set(a+'I')
def jf():
     a=mvar.get()
     mvar.set(a+'J')
def kf():
     a=mvar.get()
     mvar.set(a+'K')
def lf():
     a=mvar.get()
     mvar.set(a+'L')
def mf():
     a=mvar.get()
     mvar.set(a+'M')
def nf():
     a=mvar.get()
     mvar.set(a+'N')
def of():
     a=mvar.get()
     mvar.set(a+'O')
def pf():
     a=mvar.get()
     mvar.set(a+'P')
def qf():
     a=mvar.get()
     mvar.set(a+'Q')
def rf():
     a=mvar.get()
     mvar.set(a+'R')
def sf():
     a=mvar.get()
     mvar.set(a+'S')
def tf():
     a=mvar.get()
     mvar.set(a+'T')
def uf():
     a=mvar.get()
     mvar.set(a+'U')
def vf():
     a=mvar.get()
     mvar.set(a+'V')
def wf():
     a=mvar.get()
     mvar.set(a+'W')
def xf():
     a=mvar.get()
     mvar.set(a+'X')
def yf():
     a=mvar.get()
     mvar.set(a+'Y')
def zf():
     a=mvar.get()
     mvar.set(a+'Z')
def space():
     a=mvar.get()
     mvar.set(a+' ')
    
def submit():
     var=mvar.get()
     if var==picflag[1]:
          tkMessageBox.showinfo("Event Triggered","Congratulations")
          mvar.set('')
          msg()
     else:
          tkMessageBox.showinfo("Sorry","Worng Guess")
          mvar.set('')
          num=Var1.get()
          if num==3:
              hang2(B1)
              Var1.set(num-1)
          elif num==2:
              hang2(B2)
              Var1.set(num-1)
          elif num==1:
              hang2(B3)
              Var1.set(num-1)
          if num==1:
               tkMessageBox.askretrycancel("Game Over","Game Over")
               Var1.set(3)
               hang2(B4)
    
def play():
    Var1.set(3)
    msg()
    hang2(B4)
    
def mainset():
    global picflag
    direct=[[A0,"LEMON"],[A1,"GRAPES"],[A2,"TIGER"],[A3,"PIZZA"],[A4,"ROSE"],[A5,"APPLE"],[A6,"DOG"],[A7,"IRONMAN"],[A8,"AUDI"],[A9,"MESSI"]]
    picflag=random.choice(direct)
    
#photos in database
A0=PhotoImage(file="lemon.gif")
A1=PhotoImage(file="grape.gif")
A2=PhotoImage(file="tiger.gif")    
A3=PhotoImage(file="pizza.gif")
A4=PhotoImage(file="rose.gif")
A5=PhotoImage(file="apple.gif")
A6=PhotoImage(file="dog.gif")
A7=PhotoImage(file="ironman.gif")
A8=PhotoImage(file="audi.gif")
A9=PhotoImage(file="messi.gif")

B1=PhotoImage(file="1.gif")
B2=PhotoImage(file="2.gif")
B3=PhotoImage(file="3.gif")
B4=PhotoImage(file="4.gif")

canvas = Canvas(frame,width = 315, height = 160, bg = 'DarkOrange1')
gif1 = PhotoImage(file ='amri.gif')
canvas.create_image(0, 0, image = gif1, anchor = NW)
canvas.grid(row=0,column=0,padx=350,pady=30)

qu=Button(frame,text='QUIT', relief=RAISED,width=15 ,command=top.destroy, height=1 ,activeforeground='blue', bd=4,bg='DarkOrange1')
qu.grid(row=0,column=2,padx=0)


def hang(Apic):
    But1=Button(bframe,image=Apic[0],height=180,width=180,bd=0)
    But1.grid(row=2,column=0,rowspan=2,pady=5)   

label0 = Tkinter.Label(bframe,text="Guess the word from Image",font='Helvetica -13 bold',bg='DarkOrange1')
label0.grid(row=2,column=1)

E1=Entry(bframe,bd=7,width=35,textvariable=mvar)
E1.grid(row=2,column=2)

submit=Button(bframe,text='Submit', relief=RAISED,width=15 ,height=5 ,activeforeground='blue', bd=4 ,bg='DarkOrange1',command=submit)
submit.grid(row=2,column=4)

label0 = Tkinter.Label(bframe,text=E1.get(),font='Helvetica -13 bold')
label0.grid(row=2,column=3)

Var1=IntVar()
Var1.set(3)

label2 = Tkinter.Label(bframe, text='Remaining number of choice = ',font='Helvetica -13 bold')
label2.grid(row=3,column=2,columnspan=2)

en=Label(bframe,textvariable=Var1,width=4,bd=4,font="Times 15 bold italic")
en.grid(row=3,column=3,rowspan=1)

play=Button(bframe,text='PLAY', relief=RAISED,width=15 ,height=5 ,activeforeground='blue', bd=4 ,bg='DarkOrange1',command=play)
play.grid(row=2,column=5,pady=3)

nextp=Button(bframe,text='NEXT IMAGE', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,bg='DarkOrange1',command=msg)
nextp.grid(row=4,column=0,pady=20)


a1=Button(frameb,text='1', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f1f,bg='#fdfd67')
a1.grid(row=1,column=3)
a2=Button(frameb,text='2', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f2f,bg='#fdfd67')
a2.grid(row=1,column=4)
a3=Button(frameb,text='3', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f3f ,bg='#fdfd67')
a3.grid(row=1,column=5)
a4=Button(frameb,text='4', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f4f,bg='#fdfd67')
a4.grid(row=1,column=6)
a5=Button(frameb,text='5', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f5f,bg='#fdfd67')
a5.grid(row=1,column=7)
a6=Button(frameb,text='6', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f6f,bg='#fdfd67')
a6.grid(row=1,column=8)
a7=Button(frameb,text='7', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f7f,bg='#fdfd67')
a7.grid(row=1,column=9)
a8=Button(frameb,text='8', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f8f,bg='#fdfd67')
a8.grid(row=1,column=10)
a9=Button(frameb,text='9', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f9f,bg='#fdfd67')
a9.grid(row=1,column=11)
a0=Button(frameb,text='0', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f0f,bg='#fdfd67')
a0.grid(row=1,column=12)

def hang2(Apic2):
    But2=Button(frameb,image=Apic2,height=180,width=180,bd=0)
    But2.grid(row=0,column=13,rowspan=10,padx=20,pady=10 ,columnspan=3)

q=Button(frameb,text='Q', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=3 ,command=qf,bg='#fdfd67')
q.grid(row=2,column=3)
w=Button(frameb,text='W', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=3,command=wf,bg='#fdfd67')
w.grid(row=2,column=4)
e=Button(frameb,text='E', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=ef ,bg='#fdfd67')
e.grid(row=2,column=5)
r=Button(frameb,text='R', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=rf ,bg='#fdfd67')
r.grid(row=2,column=6)
t=Button(frameb,text='T', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=tf,bg='#fdfd67')
t.grid(row=2,column=7)
y=Button(frameb,text='Y', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=yf,bg='#fdfd67')
y.grid(row=2,column=8)
u=Button(frameb,text='U', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=uf,bg='#fdfd67')
u.grid(row=2,column=9)
i=Button(frameb,text='I', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=iif,bg='#fdfd67')
i.grid(row=2,column=10)
o=Button(frameb,text='O', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=of,bg='#fdfd67')
o.grid(row=2,column=11)
p=Button(frameb,text='P', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=pf,bg='#fdfd67')
p.grid(row=2,column=12)

a=Button(frameb,text='A', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=af,bg='#fdfd67')
a.grid(row=3,column=3,columnspan=2)
s=Button(frameb,text='S', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=sf,bg='#fdfd67')
s.grid(row=3,column=4,columnspan=2)
d=Button(frameb,text='D', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=df,bg='#fdfd67')
d.grid(row=3,column=5,columnspan=2)
f=Button(frameb,text='F', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=ff,bg='#fdfd67')
f.grid(row=3,column=6,columnspan=2)
g=Button(frameb,text='G', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=gf,bg='#fdfd67')
g.grid(row=3,column=7,columnspan=2)
h=Button(frameb,text='H', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=hf,bg='#fdfd67')
h.grid(row=3,column=8,columnspan=2)
j=Button(frameb,text='J', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=jf,bg='#fdfd67')
j.grid(row=3,column=9,columnspan=2)
k=Button(frameb,text='K', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=kf,bg='#fdfd67')
k.grid(row=3,column=10,columnspan=2)
l=Button(frameb,text='L', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=lf,bg='#fdfd67')
l.grid(row=3,column=11,columnspan=2)

z=Button(frameb,text='Z', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=zf,bg='#fdfd67')
z.grid(row=4,column=4,columnspan=2)
x=Button(frameb,text='X', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=xf,bg='#fdfd67')
x.grid(row=4,column=5,columnspan=2)
c=Button(frameb,text='C', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=cf,bg='#fdfd67')
c.grid(row=4,column=6,columnspan=2)
v=Button(frameb,text='V', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=vf,bg='#fdfd67')
v.grid(row=4,column=7,columnspan=2)
b=Button(frameb,text='B', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=bf,bg='#fdfd67')
b.grid(row=4,column=8,columnspan=2)
n=Button(frameb,text='N', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=nf,bg='#fdfd67')
n.grid(row=4,column=9,columnspan=2)
m=Button(frameb,text='M', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=mf,bg='#fdfd67')
m.grid(row=4,column=10,columnspan=2)

space=Button(frameb,text='SPACE', relief=RAISED,width=40 ,height=1 ,activeforeground='blue', bd=4,command=space,bg='#fdfd67')
space.grid(row=5,column=5,columnspan=4)

top.mainloop()
