from tkinter import *
def submit(value):
    print(value)

window=Tk()
logo=PhotoImage(file="floppy_disk.png")

scale=Scale(window,
            from_=10,
            to=1,
            length=1000,
            orient=VERTICAL,
            font="Consolas",
            tickinterval=1,
            showvalue=0,
            resolution=1,
            troughcolor="white",
            foreground="yellow",
            background="black",
            command=submit)
scale.set(1)
scale.pack(side=LEFT)

puffy_1=PhotoImage(file="amogus.png")
puffy_label=Label(image=puffy_1)
puffy_label.config(width=1000)
puffy_label.pack(side=RIGHT)

window.mainloop()