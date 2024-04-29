from tkinter import*
from tkinter import ttk,  messagebox
from tkcalendar import*
import os
import pymysql
class Formulaire:
    def __init__(self, root):
        self.root  = root
        self.root.title("Formulaire")
        self.root.geometry("1920x1080+0+0")
        frame1 = Frame(self.root, bg="grey")
        frame1.place(x=500, y=200, width=700, height=500)
        title = Label(frame1, text="Créér un compte", font=("algerian", 20, "bold"), fg="orange").place(x=50, y=30)
        # prénom et nom
        
        aff_prenom = Label(frame1, text="Prénom : ", font=("Lines new roman", 15, "bold"), bg="grey",fg="black").place(x=50, y=100)
        self.ecri_prenom = Entry(frame1, font=("times new roman",), bg="lightgrey")
        self.ecri_prenom.place(x=50, y=130, width=250)
        
        aff_nom = Label(frame1, text="Nom : ", font=("Lines new roman", 15, "bold"), bg="grey",fg="black").place(x=370, y=100)
        self.ecri_nom = Entry(frame1, font=("times new roman",), bg="lightgrey")
        self.ecri_nom.place(x=370, y=130, width=250)

        # téléphone et email  
        
        aff_tel = Label(frame1, text="Téléphone : ", font=("Lines new roman", 15, "bold"), bg="grey",fg="black").place(x=50, y=160)
        self.ecri_tel = Entry(frame1, font=("times new roman",), bg="lightgrey")
        self.ecri_tel.place(x=50, y=190, width=250)
        
        aff_mail = Label(frame1, text="Email : ", font=("Lines new roman", 15, "bold"), bg="grey",fg="black").place(x=370, y=160)
        self.ecri_mail = Entry(frame1, font=("times new roman",), bg="lightgrey")
        self.ecri_mail.place(x=370, y=190, width=250)
        
        # Question et réponse 
        aff_question = Label(frame1, text="Sélectionez une Question : ", font=("Lines new roman", 15, 'bold'), bg="grey",fg="black").place(x=50, y=220)
        self.ecri_question = ttk.Combobox(frame1, font=("times new roman",15, "bold"), state="readonly")
        self.ecri_question["value"]=("Selectionez", "Ton surnom ? ", "Lieu de naissance ? ", "Meilleur ami ? ", "Film Préféré ? ", "Nom de votre animal préféré ? ")
        self.ecri_question.place(x=50, y=250, width=250)
        self.ecri_question.current(0)
                        #reponse
        aff_reponse = Label(frame1, text="Repondre ici : ", font=("Lines new roman", 15, "bold"), bg="grey",fg="black").place(x=370, y=220)
        self.ecri_reponse = Entry(frame1, font=("times new roman",), bg="lightgrey")
        self.ecri_reponse.place(x=370, y=250, width=250)
        
        #password and confirm
        
        # téléphone et email  
        
        aff_pass = Label(frame1, text="Password : ", font=("arial", 15, "bold"), bg="grey",fg="black").place(x=50, y=280)
        self.ecri_pass = Entry(frame1, font=("times new roman",15, "bold"), bg="lightgrey", show=".")
        self.ecri_pass.place(x=50, y=310, width=250)
        
        aff_conf_pass = Label(frame1, text="Confirmer le password : ", font=("Lines new roman", 15, "bold"), bg="grey",fg="black").place(x=370, y=280)
        self.ecri_conf_pass = Entry(frame1, show=".", font=("times new roman",18, "bold"), bg="lightgrey")
        self.ecri_conf_pass.place(x=370, y=310, width=250)
        
        #accepter les termes contrats et licenses
        self.var_check = IntVar()
        chk = Checkbutton(frame1, variable=self.var_check,onvalue=1, offvalue=0, cursor="hand2" ,text="J'accepte les conditions et les termes ", font=("times new roman", 12), bg="lightgrey").place(x=50, y=370)
        
        #les bouttons de validation
        btn = Button(frame1, text="Créer un compte", cursor="hand2", font=("times new man",15, "bold"), bg="cyan", fg="black", command=self.creer).place(x=250, y=430, width=250)
        btn1 = Button(frame1, text="Connexion", cursor="hand2", font=("times new man",15, "bold"), bg="cyan", fg="black", command=self.fenetre_login).place(x=550, y=50, width=150)
        
    def creer(self):
        if self.ecri_prenom.get() == "" or self.ecri_mail.get() =="" or self.ecri_question.get() =="" or self.ecri_reponse.get() =="" or self.ecri_pass.get() == "":
            messagebox.showerror("Erreur","Remplir les champs", parent=self.root)
        elif self.ecri_pass.get()!=self.ecri_conf_pass.get():
            messagebox.showerror("Erreur", "Les mot de passes ne sont pas conforme", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Erreur", "Veuillez accepter les termes et conditions", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root", database="creer")
                cur=con.cursor()
                cur.execute("select * from compte where email=%s", self.ecri_mail.get())
                row = cur.fetchone()
                
                if row != None:
                    messagebox.showerror("Erreur", "Ce mail existe deja", parent=self.root)
                else:
                    cur.execute("insert into compte(prenom, nom, telephone, email, question, reponse, password) values(%s, %s, %s,%s, %s, %s,%s)",
                    (
                        self.ecri_prenom.get(),
                        self.ecri_nom.get(),
                        self.ecri_tel.get(),
                        self.ecri_mail.get(),
                        self.ecri_question.get(),
                        self.ecri_reponse.get(),
                        self.ecri_pass.get(),
                    ))
                    messagebox.showinfo("Succes", "Votre compte a été bien créé", parent=self.root)
                con.commit()
                self.reni()
                con.close()
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self.root)
    
    #fonction pour renitialiser les cases remplir
    def reni(self):
        self.ecri_prenom.delete(0, END)
        self.ecri_nom.delete(0, END)
        self.ecri_tel.delete(0, END)
        self.ecri_mail.delete(0, END)
        self.ecri_question.delete(0, END)
        self.ecri_question.delete(0, END)
        self.ecri_pass.delete(0, END)
        self.ecri_conf_pass.delete(0, END)
        
    def fenetre_login(self):
        self.root.destroy()
        import login
        

 
root = Tk()
obj = Formulaire(root)
root.mainloop()        