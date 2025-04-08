from tkinter import *
pw=123
def password():
    print("asd")


def submit():
    username=entry.get()
    print (username)
    entry.config(state=DISABLED)


window=Tk()
window.geometry("640x480")
window.title("Login")


button=Button(window,
              text="Login",
              font="Consolas",
              activeforeground="blue",
              activebackground="white",
              state=ACTIVE,
              compound=BOTTOM
              )


entry=Entry(window,
            font=("Consolas",25),
            fg="black",
            bg="white",
            )


entry2=Entry(window,
            font=("Consolas",25),
            fg="black",
            bg="white",
            show="*"
            )
entry.grid(row=0,column=0,padx=10,pady=10)
entry2.pack()
button.pack()

window.mainloop()