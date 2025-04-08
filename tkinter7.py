from tkinter import *

puffers=[1,2,3]

def send():
    if x.get()==0:
        print("Puffy 1")
    elif x.get()==1:
        print("Puffy 2")
    else:
        print("Puffy 3")

window=Tk()

puffy_1=PhotoImage(file="amogus.png")
puffy_2=PhotoImage(file="trollface.png")
puffy_3=PhotoImage(file="spiderman.png")
puffy_pics=[puffy_1,puffy_2,puffy_3]
x=IntVar()
for puffy in range(len(puffers)):
    radiobutton=Radiobutton(window,
                            text=puffers[puffy],
                            variable=x,
                            value=puffy,
                            padx=100,
                            pady=100,
                            font="Consolas",
                            image=puffy_pics[puffy],
                            compound=RIGHT,
                            indicatoron=0,
                            width=1000,
                            height=160,
                            command=send
                            )
    radiobutton.pack()

window.mainloop()