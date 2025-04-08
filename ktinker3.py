from tkinter import *

count=0

def click():
    global count
    count+=1
    print(count)
    print("click")

window= Tk()
logo=PhotoImage(file="floppy_disk.png")

button=Button(window,
              text="Click Me",
              command=click,
              font="Consolas",
              fg="blue",
              bg="black",
              activeforeground="green",
              activebackground="white",
              state=ACTIVE,
              image=logo,
              compound="bottom"
              )
button.pack()

window.mainloop()