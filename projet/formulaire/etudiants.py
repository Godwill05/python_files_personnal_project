from tkinter import*
from tkinter import ttk, messagebox
import pymysql
from pymysql import cursors

#creation de la classe
class Etudiant:
    def __init__(self, root):
        self.root = root
        self.root.title("Inscription")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="gray")
        #generation du formulaire
        gestion_frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        gestion_frame.place(x=50, y=50, width=600, height=650)
        
        self.id = StringVar()
        self.nom = StringVar()
        self.mail = StringVar()
        self.sexe = StringVar()
        self.contact = StringVar()
        self.dat = StringVar()
        
        
        self.recherch_bar = StringVar()
        self.recherc = StringVar()
        gestion_titre = Label(gestion_frame, text="Information de l'étudiant", font=("times new roman", 30, "bold"), bg="cyan")
        gestion_titre.place(x=50, y=50)
        
        #id Etudiant
        idetudiant = Label(gestion_frame,text="ID de l'Etudiant :", font=("times new roman", 20), bg="cyan")
        idetudiant.place(x=50, y=150)
        
        id_text = Entry(gestion_frame,textvariable=self.id  ,font=("times new roman", 20), bg="lightgray")
        id_text.place(x=220, y=150)

        #nom complet
        idnomcomplet = Label(gestion_frame, text="Nom complet  :", font=("times new roman", 20), bg="cyan")
        idnomcomplet.place(x=50, y=210)
        
        nom_text = Entry(gestion_frame,textvariable=self.nom, font=("times new roman", 20), bg="lightgray")
        nom_text.place(x=220, y=210)
        
        #mail Etudiant
        idemail = Label(gestion_frame, text="E-mail : ", font=("times new roman", 20), bg="cyan")
        idemail.place(x=50, y=250)
        
        email_text = Entry(gestion_frame,textvariable=self.mail, font=("times new roman", 20), bg="lightgray")
        email_text.place(x=220, y=250)
        
        #sexe Etudiant
        sexe = Label(gestion_frame, text="Sexe : ", font=("times new roman", 20), bg="cyan")
        sexe.place(x=50, y=310)
        
        sexe_text = ttk.Combobox(gestion_frame,textvariable=self.sexe, font=("times new roman", 20), state="readonly")
        sexe_text["value"]=("Homme", "Femme")
        sexe_text.place(x=220, y=310,width=285)
        sexe_text.current(0)
        
        # contact
        contact = Label(gestion_frame, text="Contact : ", font=("times new roman", 20), bg="cyan")
        contact.place(x=50, y=360)
        
        contact_text = Entry(gestion_frame,textvariable=self.contact, font=("times new roman", 20), bg="lightgray")
        contact_text.place(x=220, y=360)
        
        #date de naisance Etudiant
        date = Label(gestion_frame, text="Date naissance : ", font=("times new roman", 20), bg="cyan")
        date.place(x=50, y=410)
        
        date_text = Entry(gestion_frame,textvariable=self.dat, font=("times new roman", 20), bg="lightgray")
        date_text.place(x=220, y=410)
        
         #adresse Etudiant
        adresse = Label(gestion_frame, text="Adresse : ", font=("times new roman", 20), bg="cyan")
        adresse.place(x=50, y=460)
        
        self.adresse_text = Text(gestion_frame, font=("times new roman", 15))
        self.adresse_text.place(x=220, y=460, height=60, width=285)
        
        #les bouttons 
            #boutton ajouer
        btn_ajouter = Button(gestion_frame, text="Ajouter", font=("times new roman", 15), bd=10, relief=GROOVE, bg="green", command=self.ajout_etudiants)
        btn_ajouter.place(x=10, y=560, width=120)
        
            #le bouttons modifier 
        btn_modifier = Button(gestion_frame, text="Modifier", font=("times new roman", 15), bd=10, relief=GROOVE, bg="yellow", command=self.modifier)
        btn_modifier.place(x=150, y=560, width=120)
        
            #boutton pour supprimer
        btn_supprimer = Button(gestion_frame, text="Supprimer", font=("times new roman", 15), bd=10, relief=GROOVE, bg="red", command=self.supprimer)
        btn_supprimer.place(x=300, y=560, width=120)
        
            #boutton pour rénitialiser
        btn_renitialiser = Button(gestion_frame, text="Rénitialiser", command=self.reniti(), font=("times new roman", 15), bd=10, relief=GROOVE, bg="blue")
        btn_renitialiser.place(x=450, y=560, width=120)
        
        #recherche 
        
        details_frame = Frame(self.root,bd=5, relief=GROOVE, bg="cyan")
        details_frame.place(x=700, y=50, width=650, height=650)
        
        affiche_resultats = Label(details_frame, text="Rechercher par : ", font=("times new roman", 30, "bold"), bg="cyan")
        affiche_resultats.place(x=5, y=50)
        
        
        rech = ttk.Combobox(details_frame,textvariable=self.recherch_bar, font=("times new roman", 20), state="readonly")
        rech["values"]=("id", "nom", "contact")
        rech.place(x=300, y=60, width=100, height=40)
        rech.current(0)
        
        rech_txt = Entry(details_frame,textvariable=self.recherc, font=("times new roman", 20), bd=5, relief=GROOVE)
        rech_txt.place(x=410, y=60, width=100, height=40)
        
        btn_rech = Button(details_frame, text="Rechercher",font=("times new roman", 20), bd=10, bg="purple", relief=GROOVE, command=self.rechercherd_info)
        btn_rech.place(x=520, y=60, width=120, height=40)
        
        btn_aff = Button(details_frame, text="Afficher",font=("times new roman", 20), bd=10, bg="#FFD700", relief=GROOVE, command=self.afficherresultat)
        btn_aff.place(x=520, y=0, width=120, height=40)

        # affichage
        
        result_frame = Frame(details_frame,bd=5 ,relief=GROOVE, bg="white")
        result_frame.place(x=10, y=110, height=520, width=620)

        scroll_x = Scrollbar(result_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(result_frame, orient=VERTICAL)
        self.tabl_resul = ttk.Treeview(result_frame, columns=("id", "nom", "mail", "sexe", "contact", "date", "adresse"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.tabl_resul.heading("id", text="ID Etudiant")
        self.tabl_resul.heading("nom", text="Nom Complet")
        self.tabl_resul.heading("mail", text="E-mail")
        self.tabl_resul.heading("sexe", text="Sexe")
        self.tabl_resul.heading("contact", text="Contact")
        self.tabl_resul.heading("date", text="Date naissance")
        self.tabl_resul.heading("adresse", text="Adresse")
        
        self.tabl_resul["show"] = "headings"
        
        self.tabl_resul.column("id", width=100)
        self.tabl_resul.column("nom", width=120)
        self.tabl_resul.column("mail", width=50)
        self.tabl_resul.column("sexe", width=50)
        self.tabl_resul.column("contact", width=60)
        self.tabl_resul.column("date", width=120)
        self.tabl_resul.column("adresse", width=80)
        
        self.tabl_resul.pack()
        
        self.tabl_resul.bind("<ButtonRelease-1>", self.informations)
        self.afficherresultat()

    def ajout_etudiants(self):
        if self.id.get()==""or self.nom.get()=="" or self.mail.get() =="":
            messagebox.showerror("Erreur", "Remplir les champs obligatoires", parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", database="creer")
            cur = con.cursor()
            cur.execute("insert into inscris value(%s, %s, %s,%s,%s,%s,%s)", (self.id.get(), self.nom.get(), self.mail.get(), self.sexe.get(), self.contact.get(), self.dat.get(), self.adresse_text.get("1.0", END)))
            con.commit()
            self.afficherresultat()
            self.reniti()
            con.close()
            messagebox.showinfo("Succés", "Enregistrement effectué")
    
    def afficherresultat(self):
        con = pymysql.connect(host="localhost", user="root", database="creer")
        cur = con.cursor()  
        cur.execute("select *from inscris")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:self.tabl_resul.insert("", END, values=row)
        con.commit()
        con.close()  

    def reniti(self):
        self.id.set("")
        self.nom.set("")
        self.mail.set("")
        self.sexe.set("")
        self.contact.set("")
        self.dat.set("")
        self.adresse_text.delete("1.0")
        
    def informations (self, ev):
        cursors_row = self.tabl_resul.focus()
        contents = self.tabl_resul.item(cursors_row)
        row = contents ["values"]
        self.id.set(row[0]),
        self.nom.set(row[1]),
        self.mail.set(row[2]),
        self.sexe.set(row[3]),
        self.contact.set(row[4]),
        self.dat.set(row[5]),
        self.adresse_text.delete("1.0", END)
        self.adresse_text.insert(END, row[6])
        
    def modifier(self):
        con = pymysql.connect(host="localhost", user="root", database="creer")
        cur = con.cursor()
        cur.execute("update inscris set nom=%s, mail=%s, sexe=%s, contact=%s, date=%s, adresse=%s, where id='%s'", (self.nom.get(), self.mail.get(), self.sexe.get(), self.contact.get(), self.dat.get(), self.adresse_text.get("1.0", END), self.id.get()))
        con.commit()
        self.afficherresultat()
        self.reniti()
        con.close()
        messagebox.showinfo("Succès", "Modification prise en charge")
    
    def supprimer(self):
        con = pymysql.connect(host="localhost", user="root", database="creer")
        cur = con.cursor()
        cur.execute("delete from inscris where id = %s", self.id.get())
        con.commit()
        self.afficherresultat()
        self.reniti()
        con.close()
        self.reniti()
        messagebox("Succes", "Supprimer avec succes")
        
    def rechercherd_info(self):
        con = pymysql.connect(host="localhost", user="root", database="creer")
        cur = con.cursor()
        cur.execute("select * inscris where"+str(self.recherch_bar.get())+"LIKE'%"+str(self.recherc.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows :
                self.tabl_resul.insert('', END, values=row)
        con.commit()
        con.close 
root = Tk()
obj=Etudiant(root)
root.mainloop()