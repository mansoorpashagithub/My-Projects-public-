from tkinter import *
import random
import time
import tkinter.messagebox as tmsg
import tkinter.simpledialog as tsd

root=Tk()
root.geometry("700x600")
root.minsize(700,450)
root.wm_iconbitmap("1.ico")
bgcolor="darkkhaki"
root.title("Color Game")
root.config(bg=bgcolor)


wordlist=["Red","Blue","Green","Yellow","Purple","Pink","Brown","Black","White","Orange","Grey","Cyan"]
colorlist=["red","blue","green","yellow","purple","pink","brown","black","orange","grey","cyan"]
color=f"{random.choice(colorlist)}"
name=""
startgame=int(0)
counteron=int(0)
count=int(0)
wrong=int(0)
timeofgame=60 #in seconds
# __________________________________________________________________________
def start(event):
    global startgame,counteron,name
    name=tsd.askstring("Color Game","What is your name?")
    startgame=1
    counteron=1
    for i in range(timeofgame,0,-1):
        if counteron==1:
            t.config(text=f"Time left :{i}s")
            t.update()
            time.sleep(1)
        else:
            counteron=0
    if wrong==0:
        t.config(text="Time up!!!")
        t.update()
        time.sleep(2)
        t.config(text=f"Your final score is {count}")
    startgame=0
# ____________________________________________________________________________
# def valid(event):
#     global startgame,counteron,wrong,count,color
#     if startgame==1 and inpval.get()==color:
#         a.config(text=f"Your Score is : {count + 1}")
#         count += 1
#         inpval.set("")
#         color = f"{random.choice(colorlist)}"
#         b.config(text=f"{random.choice(wordlist)}",fg=color)
#         b.update()
#     elif startgame==0:
#         t.config(text="First Start the game")
#     else:
#             t.config(text=f"Wrong!! Your final score is {count}")
#             t.update()
#             with open("game.txt", "a") as f:
#                 f.write(f"{name}:{count}\n")
#             startgame=0
#             counteron=0
#             wrong=1
#             time.sleep(2)


# _______________________________________________________________________________
def reset():
    global count,startgame
    res=tmsg.askquestion("Color Game","Do you want to reset this game")
    if res=="yes":
        count=0
        startgame=0
        a.config(text=f"Your Score is : {count}")
        inpval.set("")
# ________________________________________________________________________________
Label(root,text="Colour Game by Mansoor Pasha",font="broadway 25 bold",bg="slategray3",pady=7).pack(fill=X,ipady=10)
Label(root,text="Game Description: Enter the color of the word display below\nand keep in mind NOT to enter the word",font="aharoni 15 bold",bg="slategray",justify=LEFT,pady=7).pack(fill=X)


# Your score
a=Label(root,text=f"Your Score is : 0",font="lucida 15 bold",bg=bgcolor)

# Word
b=Label(root,text=f"{random.choice(wordlist)}",font="lucida 40 ",fg=color,bg=bgcolor)
b.pack(pady=25,padx=5)
a.pack(fill=X)

# Time
t=Label(root,text=f"Time left :-",bg=bgcolor,font="lucida 15 bold")
t.pack(padx=5,pady=25)

inpval=StringVar()
e=Entry(root,textvar=inpval,borderwidth=4,relief=SUNKEN,font="lucida 20 bold")
e.pack()
e.bind('<Return>',start)


f=Frame(root,bg=bgcolor)
f.pack()
b1=Button(f,text="Start",bg="green3",font="lucida 15 bold",width=15,command=start).pack(side=LEFT,padx=20,pady=60)
b2=Button(f,text="Reset",bg="red3",font="lucida 15 bold",width=15,command=reset).pack(side=LEFT,padx=20,pady=60)



root.mainloop()
