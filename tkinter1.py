from tkinter import *
#from tkinter import ttk
#root = Tk()
#a=Label(root, text= "Hello World!",font=("Consolas",100))
#a.pack(padx=100,pady=100)

#root.mainloop()

window=Tk()
window.geometry("640x480")
window.title("Floppy")

icon= PhotoImage(file="floppy_disk.png")
window.iconphoto(True, icon)
window.config(background="black")

window.mainloop()