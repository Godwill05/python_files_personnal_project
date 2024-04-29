from customtkinter import*
from tkinter import messagebox, ttk
from tkcalendar import*
from tkinter import*
import pymysql
import time

# Creer un seul objet  utilisable par tout les utilisateurs
class user:
    def __init__(self,app):
        self.app = app
        self.app.title("Inscriptions")
        self.app.geometry("1366x768+0+0")
        self.app.config(bg="white")
        frame1 = CTkFrame(self.app, bg_color="cyan", fg_color="cyan", width=800, height=600, border_color="green", border_width=6)
        frame1.place(x=300, y=50)

        #prenom et nom
        #nom
        affich_nom = CTkLabel(frame1, text="Nom : ", fg_color="cyan", text_color="black", font=("Elephant", 16, "bold")).place(x=50, y=50)
        
        self.ecri_nom = CTkEntry(frame1, fg_color="white", text_color="black", font=("Microsoft YaHei UI Light", 13), width=300)
        self.ecri_nom.place(x=60, y=85)
        
        #nom
        affich_prenom = CTkLabel(frame1, text="Prenom : ", fg_color="cyan", text_color="black", font=("Elephant", 16, "bold")).place(x=400, y=50)
        self.ecri_prenom = CTkEntry(frame1, fg_color="white", text_color="black", font=("Microsoft YaHei UI Light", 13), width=300)
        self.ecri_prenom.place(x=410, y=85)
        
        #adresse et mail
                #mail
        affich_mail = CTkLabel(frame1, text="Mail : ", fg_color="cyan", text_color="black", font=("Elephant", 16, "bold")).place(x=50, y=150)
        self.ecri_mail = CTkEntry(frame1, fg_color="white", text_color="black", font=("Microsoft YaHei UI Light", 13), width=300)
        self.ecri_mail.place(x=60, y=185)
        
                #adresse
        affich_adresse = CTkLabel(frame1, text="Adresse : ", fg_color="cyan", text_color="black", font=("Elephant", 16, "bold")).place(x=400, y=150)
        self.ecri_adresse = CTkEntry(frame1, fg_color="white", text_color="black", font=("Microsoft YaHei UI Light", 13), width=300)
        self.ecri_adresse.place(x=410, y=185)
        
        #sexe et date de naissance
                #sexe
        affich_sexe = CTkLabel(frame1, text="Sexe : ", fg_color="cyan", text_color="black", font=("Elephant", 16, "bold")).place(x=50, y=250)
        self.ecri_sexe = CTkComboBox(frame1, fg_color="white", text_color="black", font=("Microsoft YaHei UI Light", 13), width=300, state="readonly", values=["Homme", "Femme","Personnalisé"])
        self.ecri_sexe.set("Veuillez Sélectionné")
        self.ecri_sexe.place(x=60, y=285)
        
        
                # date de naissance
        affich_date = CTkLabel(frame1, text="Date d'inscriptions : ", fg_color="cyan", text_color="black", font=("Elephant", 16, "bold")).place(x=400, y=250)
        self.ecri_date = DateEntry(frame1, fg_color="white", text_color="black", font=("Microsoft YaHei UI Light", 13), width=27, state="readonly")
        self.ecri_date.place(x=400, y=285)
        
        #passe et confirmation
        
        affich_pass = CTkLabel(frame1, text="Mots de Passe : ", fg_color="cyan", text_color="black", font=("Elephant", 16, "bold")).place(x=50, y=350)
        self.ecri_pass = CTkEntry(frame1, fg_color="white", text_color="black", font=("Microsoft YaHei UI Light", 13), width=300, show="*")
        self.ecri_pass.place(x=60, y=385)
        
        affich_confirm_pass = CTkLabel(frame1, text="Confirmer le Passe : ", fg_color="cyan", text_color="black", font=("Elephant", 16, "bold")).place(x=400, y=350)
        self.ecri_confirm_pass = CTkEntry(frame1, fg_color="white", text_color="black", font=("Microsoft YaHei UI Light", 13), width=300, show="*")
        self.ecri_confirm_pass.place(x=400, y=385)
        
        self.condition = CTkCheckBox(frame1, text="J'accepte les termes, contracts et licences", offvalue=0, onvalue=1, text_color="red")
        self.condition.place(x=250, y=450)
        
        # botton qui permet d'envoyer
        
        btn = CTkButton(frame1, text="Créer un compte", font=("algerian",16,"bold"), text_color="black", command=self.creercompte, fg_color="gold", border_color="gray", border_width=3)
        btn.place(x=250, y=500)
        
    def creercompte(self):
        if self.ecri_date.get()=="" or self.ecri_adresse.get()=="" or self.ecri_mail.get()=="" or self.ecri_nom.get()=="" or self.ecri_prenom.get()=="":
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs", parent=self.app)
            
        elif self.ecri_pass.get()!=self.ecri_confirm_pass.get():
            messagebox.showerror("Fatale", "Les mots de passe ne sont pas identiques", parent=self.app)
        elif len(self.ecri_pass.get())!=6 or len(self.ecri_confirm_pass.get())!=6:
            messagebox.showwarning("Erreur",
                                   "Le mot doit contenir aux moins 6 caractère",
                                   parent=self.app
                                   )
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", database="monapp")
                cur=con.cursor()
                cur.execute("select * from infocli where mail=%s",self.ecri_mail.get())
                row = cur.fetchone()
                if row != None:
                        messagebox.showerror("Invalide", "Ce mail existe déja", parent=self.app)
                elif self.condition.get()==0:
                    messagebox.showerror("Erreur", "Accepter les termes et contrats")
            
                else:
                    cur.execute("insert into infocli (nom, prenom, datenaiss, sexe, mail, adresse, password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.ecri_nom.get(),
                                    self.ecri_prenom.get(),
                                    self.ecri_date.get(),
                                    self.ecri_sexe.get(),
                                    self.ecri_mail.get(),
                                    self.ecri_adresse.get(),
                                    self.ecri_pass.get()   
                                ))
                    messagebox.showinfo("Succés", "Vous avez enregistrer avec succès\n Connecté vous maintenant", parent=self.app) 
                    con.commit()
                    
                    con.close()
                    self.efface()
                    
            except Exception as es:
                    messagebox.showerror("Erreur", f"Pas de connexion a la base de doonées{str(es)}", parent=self.app)
    def efface(self):
        self.ecri_adresse.delete(0, END)
        self.ecri_confirm_pass.delete(0, END)
        self.ecri_date.delete(0, END)
        self.ecri_pass.delete(0, END)
        self.ecri_nom.delete(0, END)
        self.ecri_prenom.delete(0, END)
        self.ecri_mail.delete(0, END)
        messagebox.showinfo("Patientez", "CHARGEMENT", parent=self.app)
        time.sleep(2)
        app.destroy()
        import connexion            

# creer un seul objet

app = CTk()
objet = user(app)
app.mainloop()