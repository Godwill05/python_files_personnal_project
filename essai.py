from tkinter import*
app = Tk()
app.minsize(500, 600)
app.resizable(False, False)

label = Label(app, text="Kali Linux")
label.pack()
boutton = Button(app, text="Un boutton")
boutton.pack()
app.mainloop()
