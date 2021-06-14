from tkinter import*
root=Tk()
root.geometry("450x550")
root.title("Covid-19 Data country wise")
root.config(bg="khaki")
def showdata():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid
    covid=Covid()
    cases=[]
    confirmed=[]
    active=[]
    deaths=[]
    recovered=[]
    try:
        root.update()
        countries=data.get()
        country_names=countries.strip()
        country_names=countries.replace(" ",",")
        country_names=countries.split(",")

        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
            print(cases)
        for y in cases:
            confirmed.append(y["confirmed"])
            active.append(y["active"])
            deaths.append(y["deaths"])
            recovered.append(y["recovered"])
            confirmedvar.set(y["confirmed"])
            activevar.set(y["active"])
            deathsvar.set(y["deaths"])
            recoveredvar.set(y["recovered"])
        confirmed_patches=mpatches.Patch(color="orange",label='Confirmed')
        recovered_patch=mpatches.Patch(color="green",label="Recovered")
        active_patch=mpatches.Patch(color="red",label="Active")
        deaths_patch=mpatches.Patch(color="grey",label="Deaths")
        plt.legend(handles=[confirmed_patches,recovered_patch,active_patch,deaths_patch])

        for x in range(len(country_names)):
            plt.bar(country_names[x],confirmed[x],color="orange")
            if recovered[x]>active[x]:
                plt.bar(country_names[x],recovered[x],color="green")
                plt.bar(country_names[x],active[x],color="red")
            else:
                plt.bar(country_names[x], active[x], color="red")
                plt.bar(country_names[x], recovered[x], color="green")
            plt.bar(country_names[x],deaths[x],color="grey")

        plt.title("Current Covid Cases")
        plt.xlabel("Country name")
        plt.ylabel("Cases in millions")
        plt.show()
    except Exception as e:
        print("Enter correct details")
        print(e)





Label(root,text="Enter country name for\n whome you want to get\nCovid-19 data",font="comicsansms 15 bold",fg="blue3",pady=10,bg="khaki").pack()
Label(root,text="Enter the country name:",font="lucida 14 bold",pady=10,bg="khaki").pack()
#######################################################
data=StringVar()
data.set("")
entry=Entry(root,textvariable=data,width=40,relief=GROOVE,font="lucida 13 bold").pack(pady=10)
Button(root,text="Get Data",command=showdata,width=30,font="lucida 13 bold",bg="green").pack()
confirmedvar=IntVar()
confirmedvar.set(0)
recoveredvar=IntVar()
recoveredvar.set(0)
activevar=IntVar()
activevar.set(0)
deathsvar=IntVar()
deathsvar.set(0)
f1=Frame(root,bg="khaki")
f1.pack(pady=10)
Label(f1,text="Confirmed",font="lucida 13 bold",pady=10,bg="khaki").pack(side=LEFT,fill=X,padx=20)
Entry(f1,textvariable=confirmedvar,font="lucida 12 bold",relief=GROOVE).pack(side=LEFT,fill=X,padx=20)


f2=Frame(root,bg="khaki")
f2.pack(pady=10)
Label(f2,text="Recovered",font="lucida 13 bold",pady=10,bg="khaki").pack(side=LEFT,fill=X,padx=17)
Entry(f2,textvariable=recoveredvar,font="lucida 12 bold",relief=GROOVE).pack(side=LEFT,fill=X,padx=20)


f3=Frame(root,bg="khaki")
f3.pack(pady=10)
Label(f3,text="Active",font="lucida 13 bold",pady=10,bg="khaki").pack(side=LEFT,fill=X,padx=35)
Entry(f3,textvariable=activevar,font="lucida 12 bold",relief=GROOVE).pack(side=LEFT,fill=X,padx=35)


f4=Frame(root,bg="khaki")
f4.pack(pady=10)
Label(f4,text="Deaths",font="lucida 13 bold",pady=10,bg="khaki").pack(side=LEFT,fill=X,padx=32)
Entry(f4,textvariable=deathsvar,font="lucida 12 bold",relief=GROOVE).pack(side=LEFT,fill=X,padx=30)
root.mainloop()