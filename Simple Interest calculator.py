from tkinter import*
def si():
    a=P.get()
    b=T.get()
    c=R.get()
    d=(a*b*c)/100
    e=a*(1+c/100)**b-a
    C.set(e)
    S.set(d)
    f=d+a
    SA.set(f)
    g=e+a
    CA.set(g)




root=Tk()

root.title("Simple Interest Calculator")
root.geometry("655x333")
root.minsize(450,300)
Label(root,text="Interest Calculator",font="arial 16 bold").pack(fill=X,side=TOP)
Label(root,text=" Principal",font="arial 12 bold").place(x=0,y=30)
Label(root,text=" Time (in years)",font="arial 12 bold").place(x=0,y=60)
Label(root,text=" Rate of interest ( % )",font="arial 12 bold").place(y=90)



# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

P=DoubleVar()
T=DoubleVar()
R=DoubleVar()
S=IntVar()
C=IntVar()
SA=IntVar()
CA=IntVar()

PE=Entry(root,textvariable=P,font="arial 12 bold",justify="right")
TE=Entry(root,textvariable=T,font="arial 12 bold",justify="right")
RE=Entry(root,textvariable=R,font="arial 12 bold",justify="right")
PE.place(x=170,y=30)
TE.place(x=170,y=60)
RE.place(x=170,y=90)
b1=Button(root,text="Calculate",font="arial 12 bold",command=si,).place(x=170,y=120,width=185)
Label(root,text=" Simple Interest",font="arial 12 bold").place(x=0,y=170)
Label(root,text=" Compound Interest",font="arial 12 bold").place(x=0,y=200)
Label(root,text=" Amount",font="arial 12 bold").place(x=400,y=125)
SE=Entry(root,textvariable=S,font="arial 12 bold",justify="right").place(x=170,y=170)
CE=Entry(root,textvariable=C,font="arial 12 bold",justify="right").place(x=170,y=200)
SAE=Entry(root,textvariable=SA,font="arial 12 bold",justify="right").place(x=380,y=170)
CAE=Entry(root,textvariable=CA,font="arial 12 bold",justify="right").place(x=380,y=200)




root.mainloop()