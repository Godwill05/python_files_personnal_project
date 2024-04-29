#import random
#e = ["jnfv", "hd", "o,", "dfv"]
#print(random.choices(e))
from customtkinter import *
from tkinter import *
import pymysql
from tkinter import messagebox
class Mot_de_passe_oublié :
    def __init__(self, root):
        self.root = root
        root.title("Reset password")
        root.minsize(400, 500)
        root.resizable(False, False)
        pa = CTkLabel(root, text="Mot de passe oublié", fg_color="lightgreen", font=("candara", 30, "bold"), text_color="black")
        pa.place(x=80, y=10)
        #les widgets
        m = CTkLabel(root, text="Mail", fg_color="lightgreen", font=("candara light", 20, ))
        m.place(x=190, y=50)
        self.mail = CTkEntry(root, font=("candara", 20), width=380, bg_color="lightgreen", placeholder_text="Renseigner encore le mail")
        self.mail.place(x=10, y=90)
        question = CTkLabel(root, text="Question de sécurité", font=("candara light", 20), fg_color="lightgreen").place(x=100, y=130)
        li = ["Selectionez", "Ton surnom ? ", "Lieu de naissance ? ", "Meilleur ami ? ", "Film Préféré ? ", "Nom de votre animal préféré ? "]
        self.ecri = CTkComboBox(root, font=("microsoft yahei ui light", 19), state="readonly", values=li, width=185, bg_color="lightgreen")
        self.ecri.place(x=10, y=170)
        self.reponse = CTkEntry(root, font=("candara light", 20),  bg_color="lightgreen", width=185, placeholder_text="Repondre ici")
        self.reponse.place(x=200, y=170)
        
        #
        nou = CTkLabel(root, text="Nouveau mot de passe", fg_color="lightgreen", font=("candara light", 20))
        nou.place(x=100, y=210)
        
        #zone des motde passes
        self.password = CTkEntry(root, font=("candara light", 20),  bg_color="lightgreen", width=185, show="*", placeholder_text="Nouveau mot de passe")
        self.password.place(x=10, y=240)
        self.conf_password = CTkEntry(root, font=("candara light", 20),  bg_color="lightgreen", width=185, show="*", placeholder_text="Confirmer le nouveau mot de passe")
        self.conf_password.place(x=210, y=240)
        
        #bouton de changement 
        rese = CTkButton(root, corner_radius=100, text="Confirmer le changement", command=self.reni, font=("candara light", 20, "bold"), fg_color="gold", text_color="black")
        rese.place(x=80, y=300)
        
        con = CTkButton(root, text="Se connecter maintenant", text_color="black", fg_color="lightgreen", font=("microsoft yahei ui light", 20, "bold"), command=self.connection)
        con.place(x=80, y=360)
        
        #reglages du bouton connection
    def connection(self):
        self.root.destroy()
        import register_or_connect
        
    #reglages du bouton renitialiser 
    def reni(self):
        if self.mail.get() == '' :
            messagebox.showerror("Innvalide", "Remplir le mail")
        elif self.password.get() =='' or self.conf_password.get() =='':
            messagebox.showerror("Erreur", "Les mot de passe sont vide")
        elif self.password.get() !=self.conf_password.get():
            messagebox.showerror("Erreur", "Les mots de passe ne sont pas identiques")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", database="chat_bot")
                cur = con.cursor()
                cur.execute("select * from inscriptions where mail=%s and question=%s and reponse=%s", (
                    self.mail.get(),
                    self.ecri.get(),
                    self.reponse.get()
                ))
                row = cur.fetchone()
                if row == NONE :
                    messagebox.showwarning("Erreur", "Mail ou questions et reponse mal renseigné")
                else:
                    cur.execute("update inscriptions set password=%s where mail=%s and question=%s and reponse=%s", (
                       self.password.get(),
                       self.mail.get(),
                       self.ecri.get(),
                       self.reponse.get()
                    ))
                    ro = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Erreur", "Vous avez mal répondu a une question")
                    else:
                        messagebox.showinfo("Succès", "Mot de passe Modifié avec succès", parent=self.root)
                    self.clean()
                    con.commit()
                    con.close()
            except :
                messagebox.showwarning("Erreur", f"Pas de connexion a la base de donnée erreur")    
        
    def clean(self):
        self.mail.delete(0, END),
        self.ecri.delete(0, END),
        self.reponse.delete(0, END),
        self.password.delete(0,END),
        self.conf_password.delete(0, END)
            
root = CTk(fg_color="lightgreen")
instance2 = Mot_de_passe_oublié(root)
root.mainloop()