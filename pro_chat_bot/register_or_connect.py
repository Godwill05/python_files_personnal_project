from customtkinter import *
import random
import pymysql
from tkinter import messagebox
from tkinter import *
from tkinter import ttk,  messagebox
from tkcalendar import*
class Register:
    def __init__(self, app):
        self.app = app
        #reglages de la fenêtre
        app.title("Chat bot connect")
        self.app.config(bg="#dddfda")
        app.minsize(500, 500)
        app.resizable(FALSE, FALSE)
        
        #body windows
        wel = CTkLabel(app, text="Connexion..", font=("corbel", 40), fg_color="#dddfda")
        wel.place(x=150, y=10)
        
        #input zone
        aff_mail = CTkLabel(app, text="Mail : ", font=("calibri", 30), fg_color="#dddfda")
        aff_mail.place(x=20, y=70)
        aff_pass = CTkLabel(app, text="Password : ", font=("calibri", 30), fg_color="#dddfda")
        aff_pass.place(x=20, y=120)
        
        #input
        self.mail = CTkEntry(app, font=("microsoft yahei ui light", 19), width=360, placeholder_text="mail")
        self.mail.place(x=90, y=70)
        self.password = CTkEntry(app, font=("microsoft yahei ui light", 19, "bold"), width=300, show="*", placeholder_text="mot de passe")
        self.password.place(x=160, y=120)
        
        #question
        li = ["Selectionez", "Ton surnom ? ", "Lieu de naissance ? ", "Meilleur ami ? ", "Film Préféré ? ", "Nom de votre animal préféré ? "]
        question = CTkLabel(app, text="Question : ",font=("calibri", 30), fg_color="#dddfda").place(x=20, y=170)
        self.ecri = CTkComboBox(app, font=("microsoft yahei ui light", 19), state="readonly", values=li, width=300)

        self.ecri.place(x=150, y=170)
        
        #reponse
        self.reponse = CTkLabel(app, text="Reponse : ", font=("calibri", 30), bg_color="#dddfda")
        self.reponse.place(x=20, y=230)
        self.ecri_reponse = CTkEntry(app,font=("microsoft yahei ui light", 19), width=300, placeholder_text="Répondre ici")
        self.ecri_reponse.place(x=150, y=230)
        
        #bouton se connecter
        
        connexion = CTkButton(app, text="Connexion...", font=("candara", 30), fg_color="green", bg_color="#dddfda", command=self.connexion)
        connexion.place(x=150, y=300)
        
        pas_decompte = CTkLabel(app, text="Pas de compte??->", font=("times new roman", 19), fg_color="#dddfda")
        pas_decompte.place(x=100, y=350)
        
        inscription = CTkButton(app, text="Inscriptions", font=("microsoft yahei ui light", 19), text_color="green", fg_color="#dddfda", bg_color="#dddfda", command=self.inscriptions)
        inscription.place(x=250, y=345)
        
        ou = CTkButton(app, text="Renitialiser le mot de passe", font=("microsoft yahei ui light", 19), text_color="green", fg_color="#dddfda", bg_color="#dddfda", command=self.renitialiser)
        ou.place(x=100, y=400)
        
    #reglage du bouton renitialsier
    def renitialiser (self):
        if self.mail.get() == '':
            messagebox.showwarning("Erreur", "Renseigner le mail")
        else:
            self.app.destroy()
            import ran
    #reglage du boutons inscriptions
    def inscriptions(self):
        self.app.destroy()
        import inscriptions
    def connexion (self):
        if self.mail.get() =='' or self.password.get() == '' or self.ecri.get() =='' or self.ecri.get() =="Selectionez" or self.ecri_reponse.get() =='':
            messagebox.showerror("Erreur", "Touts les champs ne sonrt pas remplir", parent=self.app)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", database="chat_bot")
                cur = con.cursor()
                cur.execute("select * from inscriptions where mail=%s and question=%s and reponse=%s and password=%s", (
                    self.mail.get(),
                    self.ecri.get(),
                    self.ecri_reponse.get(),
                    self.password.get()
                ))
                row = cur.fetchone()
                if row == None :
                    messagebox.showerror("Erreur", "Invalide mail et mot de passe\n ou revoir les questions reponses", parent=self.app)
                else:
                    messagebox.showinfo("Succès", "Bienvenu")
                    self.app.destroy()
                    import main
                    con.close()
            except EXCEPTION as es :
                messagebox.showerror("Erreur", f"Erreur de connexion{str(es)}", parent=self.app)
app = CTk()
instance1 = Register(app)
app.mainloop()