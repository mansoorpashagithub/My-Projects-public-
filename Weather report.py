from tkinter import *
import requests,json
from PIL import Image, ImageTk



root=Tk()
root.geometry("600x600")
root.minsize(500,450)
root.wm_iconbitmap("1.ico")
bgcolor="limegreen"
root.title("Weather Report")
root.config(bg=bgcolor)
f=Frame(root,bg=bgcolor)
f.pack()
head=Label(f,text="WEATHER NOW",font="cambria 30 bold",bg="green")
head.pack(pady=5,ipadx=10,ipady=5)
image=Image.open(".img\\weather_logo.jpg")
image=image.resize((350,60))
photo=ImageTk.PhotoImage(image)
Label(root,image=photo).pack()


city=StringVar()
temp=StringVar()
pres=StringVar()
humid=StringVar()
report=StringVar()
cityname=StringVar()

def enter(event):
    api_key="ac7c75b9937a495021393024d0a90c44"#"2e3fa4b03bce7e733337b1b5705856e"
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    city_name=city.get().lower()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response=requests.get(complete_url)
    x=response.json()
    print(x)

    if x["cod"]!="404":
        y=x["main"]
        cityname.set(x["name"]+", "+x["sys"]["country"])
        temp.set(str(round(y["temp"]-273.15,4)))
        pres.set(y["pressure"])
        humid.set(str(y["humidity"])+"%")
        z=x["weather"]
        report.set(z[0]["description"])
        city.set("")
    else:
        cityname.set("")
        temp.set("Error!!")
        pres.set("Error!!")
        humid.set("Error!!")
        report.set("Error!!")
        city.set("")
    with open("weather.txt", "a") as f:
        f.write(f"city:{cityname.get()},  temp:{temp.get()},  presure:{pres.get()},  humidity:{humid.get()},  description:{report.get()}\n\n")


def submit():
    api_key="ac7c75b9937a495021393024d0a90c44"#"2e3fa4b03bce7e733337b1b5705856e"
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    city_name=city.get().lower()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response=requests.get(complete_url)
    x=response.json()

    if x["cod"]!="404":
        y=x["main"]
        cityname.set(x["name"]+", "+x["sys"]["country"])
        temp.set(str(round(y["temp"]-273.15,4)))
        pres.set(y["pressure"])
        humid.set(str(y["humidity"])+"%")
        z=x["weather"]
        report.set(z[0]["description"])
        city.set("")
    else:
        cityname.set("")
        temp.set("Error!!")
        pres.set("Error!!")
        humid.set("Error!!")
        report.set("Error!!")
        city.set("")
    with open("weather.txt", "a") as f:
        f.write(f"city:{cityname.get()},  temp:{temp.get()},  presure:{pres.get()},  humidity:{humid.get()},  description:{report.get()}\n\n")






f=Frame(root,bg=bgcolor)
f.pack()
Label(f,text="Enter the city name: ",font="cambria 15 bold",bg="green").pack(padx=30,pady=15,ipadx=20,side=LEFT)
citye=Entry(f,textvar=city,font="cambria 15 bold",borderwidth=5,relief=RIDGE)
citye.pack(side=LEFT,padx=30)
citye.bind('<Return>',enter)


b=Button(root,text="SUBMIT",bg="red",font="cambria 15 bold",command=submit)
b.pack(pady=25,side=TOP)

# __________________________________________________________________
f=Frame(root,bg=bgcolor,width=500)
Label(f,text="          City",font="cambria 15 bold",bg=bgcolor).pack(padx=114,pady=5,side=LEFT)
citye=Entry(f,textvar=cityname,font="cambria 15 bold",borderwidth=5,relief=RIDGE,state=DISABLED)
citye.pack(padx=25,pady=5,side=TOP)
f.pack(side=TOP)

# _____________________________________________________________________
f1=Frame(root,bg=bgcolor,width=500)
Label(f1,text="Current Temprature (in °C) : ",font="cambria 15 bold",bg=bgcolor).pack(padx=20,pady=5,side=LEFT)
tempe=Entry(f1,textvar=temp,font="cambria 15 bold",borderwidth=5,relief=RIDGE,state=DISABLED)
tempe.pack(padx=25,pady=5,side=TOP)
f1.pack(side=TOP)
# ____________________________________________________________________________

f2=Frame(root,bg=bgcolor,width=500)
Label(f2,text="Current Pressure (in hPa): ",font="cambria 15 bold",bg=bgcolor).pack(padx=30,side=LEFT,pady=5)
prese=Entry(f2,textvar=pres,font="cambria 15 bold",borderwidth=5,relief=RIDGE,state=DISABLED)
prese.pack(padx=25,pady=5,side=RIGHT)
f2.pack(side=TOP)
# _____________________________________________________________________________

f3=Frame(root,bg=bgcolor)
Label(f3,text="Current Humidity (in %): ",font="cambria 15 bold",bg=bgcolor).pack(padx=35,side=LEFT,pady=5)
humide=Entry(f3,textvar=humid,font="cambria 15 bold",borderwidth=5,relief=RIDGE,state=DISABLED)
humide.pack(padx=25,pady=5,side=TOP)
f3.pack(side=TOP)
# _____________________________________________________________________________
f4=Frame(root,bg=bgcolor)
Label(f4,text="Weather Report : ",font="cambria 15 bold",bg=bgcolor).pack(padx=70,side=LEFT,pady=12)
reporte=Entry(f4,textvar=report,font="cambria 15 bold",borderwidth=5,relief=RIDGE,state=DISABLED)
reporte.pack(padx=25,pady=12)
f4.pack(side=TOP)
# _____________________________________________________________________________


root.mainloop()
