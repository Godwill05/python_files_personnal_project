from customtkinter import *
class user :
    def __init__(self, app):
        self.app = app

        app.config()
        frame = CTkFrame(app, fg_color="cyan", width=220, height=400)
        frame.pack()

        label = CTkLabel(app, text="Ceci est un label", font=("times new roman", 19, "bold"))
        label.pack()
        self.texte = CTkEntry(app)
        self.texte.pack()
        boot = CTkButton(app, text="Un jolie Bouton", command=comand)
        boot.pack()

def comand(self):
    if self.texte.get()=="":
        print("Champs laissée vide")
    else:
        print("ok")
        print(self.texte.get())
app = CTk()
obf = user(app)
app.mainloop()