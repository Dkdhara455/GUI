#model calculator
import tkinter as tk
#----create window-----
w=tk.Tk()
w.geometry("420x250+300+300")
w.title("modern_calculator")

#create global variable
s=0
total=0
op=[]
#start functions
def one():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+1))
    s=10*s+1
def two():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+2))
    s=10*s+2
def three():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+3))
    s=10*s+3
def four():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+4))
    s=10*s+4
def five():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+5))
    s=10*s+5
def six():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+6))
    s=10*s+6
def seven():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+7))
    s=10*s+7
def eight():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+8))
    s=10*s+8
def nine():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+9))
    s=10*s+9
def zero():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(10*s+0))
    s=10*s+0
def dublezero():
    global s
    e1.delete(0,tk.END)
    e1.insert(0,str(100*s))
    s=100*s
def divi():
    global s,op
    global total
    e1.delete(0,tk.END)
    total+=s
    op.append("/")
    s=0
def mul():
    global s,op
    global total
    e1.delete(0,tk.END)
    total=total+s
    op.append("*")
    s=0
def minu():
    global s,op
    global total
    e1.delete(0,tk.END)
    total+=s
    op.append("-")
    s=0
def plush():
    global s,op
    global total
    e1.delete(0,tk.END)
    total+=s
    op.append("+")
    s=0
def eql():
    global s,total,op
    if op!=[]:
        if op[-1]=="+":
            total=total+s
            e1.delete(0,tk.END)
            e1.insert(0,str(total))
            s=0
            
        elif op[-1]=="-":
            total=total-s
            e1.delete(0,tk.END)
            e1.insert(0,str(total))
            s=0
            
        elif op[-1]=="*":
            total=total*s
            e1.delete(0,tk.END)
            e1.insert(0,str(total))
            s=0
        elif op[-1]=="/":
            total=total/s
            e1.delete(0,tk.END)
            e1.insert(0,str(total))
            s=0
    else:
        e1.delete(0,tk.END)
        e1.insert(0,str(s))
        s=0
        total=0
        
        
    op.clear()
def cancle():
    global s,total
    e1.delete(0,tk.END)
    s=0
    total=0
def cross():
    global s,total
    if s!=0:
        s=s//10
        e1.delete(0,tk.END)
        e1.insert(0,str(s))
    else:
        e1.delete(0,tk.END)
        e1.insert(0,str(s))
        total=0
#create buttons
e1=tk.Entry(w,width=8,font=("arial",14),border=5)
b1=tk.Button(w,text="1",width=8,font=("arial",14),border=5,command=one)
b2=tk.Button(w,text="2",width=8,font=("arial",14),border=5,command=two)
b3=tk.Button(w,text="3",width=8,font=("arial",14),border=5,command=three)
b4=tk.Button(w,text="4",width=8,font=("arial",14),border=5,command=four)
b5=tk.Button(w,text="5",width=8,font=("arial",14),border=5,command=five)
b6=tk.Button(w,text="6",width=8,font=("arial",14),border=5,command=six)
b7=tk.Button(w,text="7",width=8,font=("arial",14),border=5,command=seven)
b8=tk.Button(w,text="8",width=8,font=("arial",14),border=5,command=eight)
b9=tk.Button(w,text="9",width=8,font=("arial",14),border=5,command=nine)
b10=tk.Button(w,text="0",width=8,font=("arial",14),border=5,command=zero)
div=tk.Button(w,text="/",width=8,font=("arial",14),border=5,command=divi)
multi=tk.Button(w,text="x",width=8,font=("arial",14),border=5,command=mul)
minus=tk.Button(w,text="-",width=8,font=("arial",14),border=5,command=minu)
plus=tk.Button(w,text="+",width=8,font=("arial",14),border=5,command=plush)
b0=tk.Button(w,text="00",width=8,font=("arial",14),border=5,command=dublezero)
equl=tk.Button(w,text="=",width=8,font=("arial",14),border=5,command=eql)
canc=tk.Button(w,text="C",width=8,font=("arial",14),border=5,command=cancle)
cro=tk.Button(w,text="<-",width=8,font=("arial",14),border=5,command=cross)

cro.grid(row=1,column=3)
canc.grid(row=1,column=4)
e1.grid(row=1,columnspan=2)
b7.grid(row=2,column=1)
b8.grid(row=2,column=2)
b9.grid(row=2,column=3)
div.grid(row=2,column=4)
b4.grid(row=3,column=1)
b5.grid(row=3,column=2)
b6.grid(row=3,column=3)
multi.grid(row=3,column=4)
b1.grid(row=4,column=1)
b2.grid(row=4,column=2)
b3.grid(row=4,column=3)
minus.grid(row=4,column=4)
b0.grid(row=5,column=1)
b10.grid(row=5,column=2)
equl.grid(row=5,column=3)
plus.grid(row=5,column=4)
