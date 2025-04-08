from tkinter import *

window=Tk()
logo=PhotoImage(file="floppy_disk.png")

label=Label(
    window,
    text="Floppy!",
    font=("Consolas", 40, "bold"),
    foreground="pink",
    background="black",
    relief=RAISED,
    border=10,
    padx=10,
    pady=20,
    image=logo,
    compound=BOTTOM

)

label.pack(side="right",padx=10,ipadx=10)

window.mainloop()