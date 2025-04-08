from tkinter import *

def display():
    if tick.get() is 1:
        print("Agree")
    else:
        print("Don't agree")

window=Tk()

tick=IntVar()
pic=PhotoImage(file="floppy_disk.png")

check_button=Checkbutton(window,
                         text="elfogadom",
                         variable=tick,
                         onvalue=1,
                         offvalue=0,
                         command=display,
                         font="Consolas",
                         foreground="white",
                         background="black",
                         activeforeground="white",
                         activebackground="black",
                         padx=10,
                         pady=10,
                         image=pic,
                         compound="left"
                         )
check_button.pack()

window.mainloop()