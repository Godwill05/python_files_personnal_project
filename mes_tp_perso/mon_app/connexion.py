from customtkinter import*
from tkinter import messagebox, ttk

from tkinter import*
import pymysql
import time

class connexion :
    def __init__(self, app):
        #parametre de la fenetre
        self.app = app
        self.app.title("Connexion")
        self.app.config(bg="white")
        self.app.geometry("1366x768+0+0")
        #frame
        frame2 = CTkFrame(self.app, fg_color="#efacbd", width=400, height=450, border_color="blue", border_width=6)
        frame2.place(x=500, y=150)
        #titre des contenu du frame
        titre = CTkLabel(frame2, text="Connexion", font=("Impact", 50), text_color="green", fg_color="#efacdb").place(x=55, y=10)
        #mail et mot de passe
                #mail
        affich_mail = CTkLabel(frame2, text="E-mail:", font=("times new roman", 26), text_color="black", fg_color="#efacdb").place(x=20, y=100)
        self.ecri_mail = CTkEntry(frame2, fg_color="white", font=("Microsoft YaHei UI Light",20), text_color="black", width=275)
        self.ecri_mail.place(x=100, y=100)
                #passe
        affich_pass = CTkLabel(frame2, text="Mot de passe:", font=("times new roman", 26), text_color="black", fg_color="#efacdb").place(x=20, y=150)
        self.ecri_pass = CTkEntry(frame2, fg_color="white", font=("Microsoft YaHei UI Light",20), text_color="black", width=205)
        self.ecri_pass.place(x=170, y=150)
        
        #gestions des boutton de la fenetre
        #boutton de connexions
        btn1 = CTkButton(frame2, text="Se connecter", font=("algerian", 30), text_color="black", cursor="hand2", command=self.connexion)
        btn1.place(x=100, y=200)
        
        phrase = CTkLabel(frame2, text="OU", font=("Elephant", 25), fg_color="#efacdb", text_color="black")
        phrase.place(x=190, y=250)
        btn2 = CTkButton(frame2, text="Mot de passe oublié", font=("algerian", 30), text_color="black", cursor="hand2", fg_color="red", command=self.modifier)
        btn2.place(x=50, y=300)
        
    def connexion(self):
        if self.ecri_mail.get()=="" or self.ecri_pass.get()=="":
            messagebox.showerror("Erreur", "Certains Champs sont vides", parent=self.app)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", database="monapp")
                cur=con.cursor()
                cur.execute("select * from infocli where mail=%s and password=%s",
                            (
                                self.ecri_mail.get(),
                                self.ecri_pass.get()
                            ))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Erreur",  "Mail ou Mots de passe incorrecte", parent=self.app)
                else:
                    messagebox.showinfo("Succes", "Connexion réussite\nvous ête a présents connecté")
                    con.close()
            except Exception as es:
                    messagebox.showerror("Connexion", f"Erreur de connexion {str(es)}avec la base de donnée")
    def modifier(self):
        if self.ecri_mail=="":
                messagebox.showerror("Erreur", "Veuillez au moins renseigner le mail")
        else:
            try:
                
                con=pymysql.connect(host="localhost", user="root", database="monapp")
                cur=con.cursor()
                cur.execute("select * from infocli where mail=%s", (self.ecri_mail.get()))
                row=cur.fetchone()
                cur.close()
                if row==None:
                    self.app2=CTkToplevel()
                    self.app2.title("Mot de passe oublié")
                    self.app2.config(bg="white")
                    self.app2.geometry("400x400+400+200")
                    self.app2.mainloop()
                    messagebox.showwarning("Erreur", "Mail introuvable ou mal renseigné")
                else:
                    self.app2=app2
                    app2=CTk()
                    rap = CTkLabel(self.app2, text="Date d'inscriptions", font=("algerian", 18))
                    rap.pack()
                    app2.mainloop()
            except Exception as x:
                    messagebox.showerror("Erreur", f"Pas de connexion a la base de donnée{str(x)}")
app=CTk()
obj = connexion(app)
app.mainloop()    