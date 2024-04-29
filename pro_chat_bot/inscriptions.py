from customtkinter import *
import pymysql
from tkinter import messagebox
from tkinter import *
from tkinter import ttk,  messagebox
from tkcalendar import*
class Inscriptions:
    def __init__(self, app):
        self.app = app
        #reglages de la fenêtre
        app.title("Chat bot sign up")
        self.app.config(bg="black")
        app.minsize(500, 500)
        app.resizable(FALSE, FALSE)
        
        wel = CTkLabel(app, text="Inscriptions..", font=("corbel", 40), bg_color="black", text_color="white")
        wel.place(x=150, y=10)
        
        #nom et prenom
        ecri_nom = CTkLabel(app, text="Nom", font=("candara light", 30), bg_color="black", text_color="white").place(x=10, y=50)
        ecri_prenom = CTkLabel(app, text="Prénom", font=("candara light", 30), bg_color="black", text_color="white").place(x=300, y=50)
        
        self.nom = CTkEntry(app, font=("candara light", 20),  bg_color="black", width=230, placeholder_text="Nom")
        self.nom.place(x=10, y=90)
        self.prenom = CTkEntry(app, font=("candara light", 20),  bg_color="black", width=230, placeholder_text="Prenom")
        self.prenom.place(x=250, y=90)
        
        #mail et age 
        ecri_mail = CTkLabel(app, text="Mail", font=("candara light", 30), bg_color="black", text_color="white").place(x=10, y=130)
        self.mail = CTkEntry(app, font=("candara light", 20),  bg_color="black", width=230, placeholder_text="Mail")
        self.mail.place(x=10, y=170)
        
        #Date
        ecri_age = CTkLabel(app, text="Age", font=("candara light", 30), bg_color="black", text_color="white").place(x=300, y=130)
        self.age = DateEntry(app, font=("candara light", 20),  bg_color="black", placeholder_text="Age", state="readonly", width=14, height=2)
        self.age.place(x=250, y=165)
        
        question = CTkLabel(app, text="Question de sécurité", font=("candara light", 30), bg_color="black", text_color="white").place(x=125, y=220)
        li = ["Selectionez", "Ton surnom ? ", "Lieu de naissance ? ", "Meilleur ami ? ", "Film Préféré ? ", "Nom de votre animal préféré ? "]
        self.ecri = CTkComboBox(app, font=("microsoft yahei ui light", 19), state="readonly", values=li, width=230, bg_color="black")
        self.ecri.place(x=10, y=270)
        self.reponse = CTkEntry(app, font=("candara light", 20),  bg_color="black", width=230, placeholder_text="Repondre ici")
        self.reponse.place(x=250, y=270)
        
        ecri_password = CTkLabel(app, text="Mot de passe", font=("candara light", 30), bg_color="black", text_color="white").place(x=155, y=330)
        self.password = CTkEntry(app, font=("candara light", 20),  bg_color="black", width=230, placeholder_text="password", show="*")
        self.password.place(x=10, y=380)
        self.confirm_pass = CTkEntry(app, font=("candara light", 20),  bg_color="black", width=230, placeholder_text="confirm password", show="*")
        self.confirm_pass.place(x=250, y=380)
        
        self.contrat = CTkCheckBox(app, onvalue=1, offvalue=0, font=("candara light", 20),  bg_color="black")
        self.contrat.place(x=100, y=420)
        license = CTkLabel(app, text="Approbation du contrat termes et licenses",  font=("candara light", 20),  bg_color="black", text_color="green").place(x=130, y=415)
        
        #bouton d'inscriptions 
        inscri = CTkButton(app, text="Inscriptions", font=("candara light", 20),  bg_color="black", fg_color="green", command=self.inscriptions)
        inscri.place(x=130, y=450)
        
        labe = CTkLabel(app, text="ou", font=("candara light", 20),  bg_color="black", text_color="white").place(x=280, y=450)
        conu = CTkButton(app, text="Connexion", command=self.connexion, font=("candara light", 20),  bg_color="black", text_color="red", fg_color="black")
        conu.place(x=320, y=445)
        
        #reglage du boutton connexion
    def connexion (self):
        self.app.destroy()
        import register_or_connect
        
    # reglage du bouton inscriptions
    def inscriptions(self):
        if self.nom.get() == '' or self.prenom.get() == '' or self.mail.get() == '' or self.reponse.get() == '' or self.password.get() == '' or self.confirm_pass.get() == '' or self.ecri.get() =='' or self.ecri.get() =="Selectionez":
            messagebox.showerror("Erreur","Remplir les champs", parent=self.app)
        elif self.contrat.get() == 0 :
            messagebox.showerror("Erreur","Acceptez les termes contrats et licenses", parent=self.app)
        elif self.password.get()!=self.confirm_pass.get():
            messagebox.showerror("Erreur", "Les mots de passe ne sont pas identiques", parent=self.app)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", database="chat_bot")
                cur = con.cursor()
                cur.execute("select * from inscriptions where mail=%s", self.mail.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Erreur", "Ce mail existe deja", parent=self.app)
                else : 
                    cur.execute("insert into inscriptions(nom, prenom, mail, date, question, reponse, password) values(%s, %s, %s, %s,%s, %s, %s)", (
                        self.nom.get(),
                        self.prenom.get(),
                        self.mail.get(),
                        self.age.get(),
                        self.ecri.get(),
                        self.reponse.get(),
                        self.password.get()
                    ))
                    messagebox.showinfo("Succes", "Votre compte a été bien créé", parent=self.app)
                con.commit()
                self.renitialiser()
                con.close()
                import register_or_connect
            except EXCEPTION as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self.root)
    
    def renitialiser(self):
        self.nom.delete(0, END),
        self.prenom.delete(0, END),
        self.mail.delete(0, END),
        self.age.delete(0, END),
        self.ecri.delete(0, END),
        self.reponse.delete(0, END),
        self.password.delete(0, END)
app = CTk()
instance0 = Inscriptions(app)
app.mainloop()