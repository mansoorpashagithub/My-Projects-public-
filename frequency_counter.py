import matplotlib.pyplot as plt
from tkinter import *

def hello(event):
    msg=msg_.get()
    msg=msg.upper()
    msg=[char for char in msg]
    all_count=[]
    my_labels=[]
    for i in msg:
        if i in my_labels:
            continue
        count=msg.count(i)
        all_count.append(count)
        my_labels.append(i)
    plt.pie(all_count,labels=my_labels,autopct='%1.2f%%')
    plt.title("FREQUENCY COUNTER\n                         -by  MANSOOR PASHA")
    plt.show()


root = Tk()
root.geometry("500x150")
root.title("Python Project")
msg_=StringVar()
f=Frame(root)
f.pack()
Label(f, text="Enter your name here : ", font="lucida 15 bold", fg="black").pack(side=LEFT,pady=30,padx=10)
t=Entry(f,textvariable=msg_,relief=GROOVE,borderwidth=2,font="lucida 15 bold")
t.pack(side=LEFT,pady=30,padx=10)
t.bind('<Return>',hello)
f1=Frame(root,bg="red")
Button(f1,text="NEXT",font="lucida 12 bold",bg="red3",command=hello).pack()
f1.pack()
root.mainloop()















