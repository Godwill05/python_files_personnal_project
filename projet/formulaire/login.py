from tkinter import*
from tkinter import ttk,  messagebox
import pymysql
import os

class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+230+250")
        self.root.config(bg="white")
        self.root.focus_force()
        login_frame = Frame(self.root, bg="cyan")
        login_frame.place(x=500, y=130, width=500, height=500)
        title = Label(login_frame, text="Connexion", font=("algerian", 40, "bold"), bg="cyan", fg="black")
        title.pack(side=TOP, fill=X)

        lbl_email = Label(login_frame, text="Email : ", font=("times new roman", 30, "bold"), bg="cyan").place(x=150, y=100, width=200)
        lbl_password = Label(login_frame, text="Password : ", font=("times new roman", 30, "bold"), bg="cyan").place(x=150, y=200, width=200)
        
        #box pour recevoir les entrees au clavier
        self.txt_email = Entry(login_frame, font=("times new roman", 20), bg="lightgray")
        self.txt_email.place(x=100, y=160, width=320)
        
        self.txt_password = Entry(login_frame,show=".", font=("times new roman", 20), bg="lightgray")
        self.txt_password.place(x=100, y=270, width=320)
        
        #boutton 
        creer_btn = Button(login_frame, text="Créer un nouveau compte", cursor="hand2", font=("times new roman", 15), bd=0, bg="cyan", fg="green", command=self.fenetre_formulaire).place(x=30, y=320)
        
        oublie_btn = Button(login_frame, text="Mot de passe oublié", cursor="hand2", font=("times new roman", 15), bd=0, bg="cyan", fg="red", command=self.oublie).place(x=300, y=320)
        
        connect_btn = Button(login_frame, text="Connexion", cursor="hand2", font=("times new roman", 15), bd=0, bg="lightgray", fg="green", command=self.connection).place(x=190, y=370)
    
    def connection(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Erreur", "Veuillez saisir l'Email et le mot de passe correctement", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root", database="creer")
                cur = con.cursor()
                cur.execute("select * from compte where email=%s and password=%s", (self.txt_email.get(), self.txt_password.get()))
                row = cur.fetchone()
                if row == None :
                    messagebox.showerror("Erreur", "Invalide maill et password", parent=self.root)
                else:
                    messagebox.showinfo("Succès", "Bienvenu")
                    self.root.destroy()
                    import etudiants
                    con.close()
            except Exception as ex :
                messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}", parent=self.root)
    
    def oublie(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Erreur", "Veuillez donnez un mail valide", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="creer")
                cur = con.cursor()
                cur.execute("select * from compte where email=%s", self.txt_email.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", "Veuillez entrer un mail valide",parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Mot de passe oublié")
                    self.root2.config(bg="white")
                    self.root2.geometry("400x400+800+500")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    title = Label(self.root2, text="Mot de passe oublié", font=("algerian", 20, "bold"), bg="red", fg="black")
                    title.pack(side=TOP, fill=X)
                    
                    #question
                    aff_question = Label(self.root2, text="Sélectionez une Question : ", font=("Lines new roman", 15, 'bold'), bg="white",fg="black").place(x=70, y=50)
                    self.ecri_question = ttk.Combobox(self.root2, font=("times new roman",15, "bold"), state="readonly")
                    self.ecri_question["value"]=("Selectionez", "Ton surnom ? ", "Lieu de naissance ? ", "Meilleur ami ? ", "Film Préféré ? ", "Nom de votre animal préféré ? ")
                    self.ecri_question.place(x=70, y=100, width=250)
                    self.ecri_question.current(0)
                    
                    #reponse
                    aff_reponse = Label(self.root2, text="Repondre ici : ", font=("Lines new roman", 15, "bold"), bg="white",fg="black").place(x=70, y=150)
                    self.ecri_reponse = Entry(self.root2, font=("times new roman",), bg="lightgrey")
                    self.ecri_reponse.place(x=70, y=200, width=250)
                    
                    #changer le mot de passe
                    aff_nouvpass = Label(self.root2, text="Nouveau Mot de Passe: ", font=("Lines new roman", 15, "bold"), bg="white",fg="black").place(x=70, y=250)
                    self.ecri_nouvpass= Entry(self.root2, font=("times new roman",), bg="lightgrey")
                    self.ecri_nouvpass.place(x=70, y=300, width=250)
                                                                                                                                 
                    #boutton pour changer le mot de passe
                    
                    change_btn = Button(self.root2, text="Modifier", font=("times new roman", 15, "bold"), bg="lightgray", fg="green", command=self.passwor_oublier).place(x=160, y=350)
                    
                    
            except Exception as ex :
                messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}", parent=self.root)
    def effacer(self):
        self.ecri_question.current(0)
        self.ecri_reponse.delete(0, END)
        self.ecri_nouvpass.delete(0, END)              
    def passwor_oublier(self):
        if self.ecri_question.get()=="" or self.ecri_reponse.get()=="" or self.ecri_nouvpass.get()=="" :
            messagebox.showerror("Erreur", "Remplir tous les champs", parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", database="creer")
                cur = con.cursor()
                cur.execute("select * from compte where email=%s and question=%s and reponse=%s", (self.txt_email.get(), self.ecri_question.get(), self.ecri_reponse.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", "Vous n'avez pas bien répondu à la question sélectionnée", parent=self.root2)
                else:
                    cur.execute("update compte set password=%s where email=%s", (self.ecri_nouvpass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Succès", "Mot de passe Modifié avec succès", parent=self.root2)
                    self.effacer()
                    self.root2.destroy()
            except Exception as es :
                messagebox.showerror("Erreur", f"Erreur de connexion{str(es)}", parent=self.root2)
    def fenetre_formulaire(self):
        self.root.destroy()
        import formulaire
root =Tk()
obj = login(root)
root.mainloop()