from customtkinter import *
import sqlite3
class User:
    def __init__(self, app):
        self.app = app
        self.app.minsize(700, 500)
        self.app.resizable(FALSE, FALSE)
        self.nom = CTkLabel(app, text="Nom")
        self.nom.place(x=50, y=10)
        
        self.ecri_nom = CTkEntry(app)
        self.ecri_nom.place(x=100, y=10)
        
        self.prenom = CTkLabel(app, text="Prénom")
        self.prenom.place(x=50, y=60)
        
        self.ecri_prenom = CTkEntry(app)
        self.ecri_prenom.place(x=100, y=60)
        
        self.mail= CTkLabel(app, text="mail")
        self.mail.place(x=50, y=110)
        
        self.ecri_mail = CTkEntry(app)
        self.ecri_mail.place(x=100, y=110)
        
        self.age = CTkLabel(app, text="age")
        self.age.place(x=50, y=160)
        
        self.ecri_sexe = CTkEntry(app)
        self.ecri_sexe.place(x=100, y=160)
        
        butto = CTkButton(app, text="Enregistrement", command=self.conect)
        butto.place(x=200, y=300)
        
    def conect (self):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user(nom, prenom, mail, age) VALUES (?, ?, ?, ?)', (
            self.ecri_nom.get(),
            self.ecri_prenom.get(),
            self.ecri_mail.get(),
            self.ecri_sexe.get()
        ))
        connection.commit()
        connection.close()
app = CTk()
user_use = User(app)
app.mainloop()