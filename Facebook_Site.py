from tkinter import*
from tkinter import messagebox
import cgi
import webbrowser


class Application:
    def __init__(self):
        self.site = Tk()
        self.site.geometry("400x600")
        self.site.title("Gestion Restaurant")
        
        # self.site.resizable(False, False)
        self.site.config(bg="#fff")

        # self.numero = number
        # self.password = password

        self.numberEnter()
        self.passwordEnter()
        # self.passwordLeave()

        Label(self.site, text="Connexion FaceBook",
              bg="silver", fg="teal",
              font=("Elephant", 20, "bold")).place(x=30, y=50)
        Button(self.site, text=" Facebook ", pady=7, width=39, fg="white",
               bg="#57a1f8", border=0,
               command=None).place(x=35, y=309)

        Button(self.site, text="Help", fg="blue",
               bg="white", font=("Microsoft YaHei UI Light", 8), bd=2,
               command=None).place(x=350, y=315)

    def numberEnter(self):
        
        self.number = Entry(self.site, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
        self.number.place(x=30, y=150)
        self.number.insert(0, "username")
        self.number.bind("<FocusIn>", self.numberEnter)
        self.number.delete(0, "end")

        name = self.number.get()
        if name == "":
            self.number.insert(0, "Numero de Téléphone")

        # creation de la barre noir,  c'est un frame cette barre

        Frame(self.site, width=295, height=2, bg="black").place(x=30, y=177)

    def passwordEnter(self):

        password = Entry(self.site, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
        password.place(x=30, y=240)
        password.insert(0, "Mot de passe")
        password.bind("<FocusIn>", self.passwordEnter)
        # password.bind("<FocusOut>", self.passwordLeave(password))
        password.delete(0, "end")

        name = password.get()
        if name == "":
            password.insert(0, "password")

        Frame(self.site, width=295, height=2, bg="black").place(x=35, y=265)


app = Application()
app.site.mainloop()
