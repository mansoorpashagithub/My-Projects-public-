from tkinter import*
from tkinter import filedialog
from pytube import YouTube
from tkinter import ttk
root=Tk()
root.geometry("800x600")
root.title("YouTube Video Downloader")
bgcolor="khaki"
folder_name=""

def Location():
    global folder_name
    folder_name=filedialog.askdirectory()
    if(len(folder_name)>1):
        location_error.config(text=folder_name,fg="green2")
    else:
        location_error.config(text="Please choose Folder")


def download():
    choice=stream.get()
    url=e.get()
    # Label(root,text=f"Title of the video is:\n\n{str(my_video.title)}",bg=bgcolor,font="lucida 12 bold").pack(pady=10)
    if(len(url)>1):
        my_video = YouTube(url)
        if choice==choices[0]:
            select=my_video.streams.filter(progressive=True).first()
        elif choice==choices[1]:
            select = my_video.streams.filter(progressive=True,file_extension='mp4').last()
        elif choice==choices[2]:
            select=my_video.streams.filter(only_audio=True).first()
        else:
            linkError.config(text="Paste Link again!!",fg="red2")
    select.download(folder_name)
    linkError.config(text="Download Completed",fg="green2")





url=StringVar()
url.set("https://www.youtube.com/watch?v=jNQXAC9IVRw")
root.config(bg=bgcolor)
Label(root,text="YouTube Video Downloader",font="Jost 18 bold",fg="red2",bg=bgcolor).pack(pady=25)



f1=Frame(root,bg=bgcolor)
f1.pack(pady=10,padx=5,side=TOP,anchor="w")
Label(f1,text="Enter URL of YouTube Video here: ",font="Lucida 16 bold",bg=bgcolor).pack(side=LEFT)
e=Entry(f1,textvariable=url,font="lucida 12 ",width=50,relief=RIDGE,border=4)
e.pack(side=LEFT)
linkError=Label(root,text=" ",bg=bgcolor,fg="red4",font=("jost",10))
linkError.pack()


f2=Frame(root,bg=bgcolor).pack(pady=10)
Label(f2,text="Save the Video file",font="Lucida 16 bold",bg=bgcolor).pack(pady=7)
b1=Button(f2,text="Choose path ",font="lucuida 16 bold",bg="red3",command=Location).pack(padx=8)
location_error=Label(root,text=" ",bg=bgcolor,fg="red4",font=("jost",10))
location_error.pack()

choices=["720p","144p","Only Audio"]
f3=Frame(root,bg=bgcolor).pack(pady=15)
Label(f3,text="Select quality",font="Lucida 16 bold",bg=bgcolor).pack(pady=5)
stream=ttk.Combobox(f3,values=choices,font="lucida 12")
stream.pack(pady=4)

b2=Button(root,text="Download ⬇ ",font="lucuida 16 bold",bg="red3",width=20,command=download).pack(pady=30)

Label(root,text="      Made by -\n\tMansoor Pasha",bg=bgcolor,font="System 12 bold").pack(side=RIGHT,padx=10)
root.mainloop()