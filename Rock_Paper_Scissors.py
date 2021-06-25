from tkinter import*
import random
import tkinter.simpledialog as tsd
from PIL import Image, ImageTk
# ______________________________________________________________________
name=""
root=Tk()
root.geometry("600x400")
root.resizable(0,0)
root.minsize(500,450)
root.wm_iconbitmap("1.ico")
bgcolor="peachpuff"
root.title("Rock Paper Scissor Game")
root.config(bg=bgcolor)
name=tsd.askstring("Rock Paper Scissor Game","What is your name?")
# _____________________________________________________________________________________
player=StringVar()
computer_btn=StringVar()
count=0
def rock():
    global count,draw,lost,won
    player.set("ROCK")
    computer_btn = random.choice(["ROCK","PAPER","SCISSOR","ROCK","PAPER","SCISSOR","ROCK","PAPER","SCISSOR"])
    computerlabel.config(text=f"CPU :-  {computer_btn}")
    if player.get()==computer_btn:
        a.config(text="DRAW!")
        a.update()
    elif computer_btn=="PAPER":
        a.config(text="YOU LOST!")
        a.update()
        count-=1
    elif computer_btn=="SCISSOR":
        a.config(text="YOU WON!")
        a.update()
        count+=1

def paper():
    global count,draw,lost,won
    player.set("PAPER")
    computer_btn = random.choice(["ROCK","PAPER","SCISSOR","ROCK","PAPER","SCISSOR","ROCK","PAPER","SCISSOR"])
    computerlabel.config(text=f"CPU :-  {computer_btn}")
    if player.get()==computer_btn:
        a.config(text="DRAW!")
        a.update()
    elif computer_btn=="ROCK":
        a.config(text="YOU WON!")
        a.update()
        count+=1
    elif computer_btn=="SCISSOR":
        a.config(text="YOU LOST!")
        a.update()
        count-=1

def scissor():
    global count,draw,lost,won
    player.set("SCISSOR")
    computer_btn = random.choice(["ROCK","PAPER","SCISSOR","ROCK","PAPER","SCISSOR","ROCK","PAPER","SCISSOR"])
    computerlabel.config(text=f"CPU :-  {computer_btn}")
    if player.get()==computer_btn:
        a.config(text="DRAW!")
        a.update()
    elif computer_btn=="PAPER":
        a.config(text="YOU WON!")
        a.update()
        count+=1
    elif computer_btn=="ROCK":
        a.config(text="YOU LOST!")
        a.update()
        count-=1

# ____________________________________________________________________________________
Label(root,text="ROCK, PAPER & SCISSOR  GAME",font="algerian 20 bold",fg="midnightblue",bg=bgcolor).pack(pady=15)
f=Frame(root,bg=bgcolor)
# _________________________________________________________________________





# ____________________________________________________________________________
rimage=Image.open("rock.png")
rimage=rimage.resize((100,100))
rphoto=ImageTk.PhotoImage(rimage)

Button(f,image=rphoto,command=rock,relief=RIDGE,bd=4).pack(side=LEFT,padx=40,pady=50)
Label(f,text="ROCK",font="lucida 16 bold",bg=bgcolor).place(x=57,y=160)
f.pack()
# _____________________________________________________________________________

pimage=Image.open("paper.png")
pimage=pimage.resize((100,100))
pphoto=ImageTk.PhotoImage(pimage)

Button(f,image=pphoto,command=paper,relief=RIDGE,bd=4).pack(side=LEFT,padx=40,pady=50)
Label(f,text="PAPER",font="lucida 16 bold",bg=bgcolor).place(x=240,y=160)
f.pack()
# __________________________________________________________________________

simage=Image.open("scissor.png")
simage=simage.resize((100,100))
sphoto=ImageTk.PhotoImage(simage)

Button(f,image=sphoto,command=scissor,relief=RIDGE,bd=4).pack(side=LEFT,padx=40,pady=50)
Label(f,text="SCISSOR",font="lucida 16 bold",bg=bgcolor).place(x=414,y=160)
f.pack()

a=Label(root,text="",font="lucida 15 bold",bg=bgcolor)
a.pack(pady=10)

computerlabel=Label(root,text=f"CPU :-{computer_btn.get()}",bg=bgcolor,font="lucida 16 bold")
computerlabel.pack(pady=10)

root.mainloop()
with open("rock_paper_scissor.txt", "a") as f:
    f.write(f"{name} : {count}\n")
