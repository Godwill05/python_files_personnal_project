from tkinter import*
import time
# definir la fenetre
app = Tk()
# definir les liste qui vont stocker les valeurs entrer
produits_nom = []
produit_qte = []
produit_prix = []
final = []

def submit():
    global recup0, recup1, recup2, total
    recup0 = str(entrer_nom.get())
    recup1 = int(qte_nom.get())
    recup2 = int(prix_nom.get())
    produits_nom.append(recup0)
    produit_qte.append(recup1)
    produit_prix.append(recup2)
    somme = int()
    for r,n in zip(produit_qte, produit_prix):
        somme = r*n
        print(somme)
    
    final.append(somme)
    total = sum(final)
    entrer_nom.delete(0, END)
    qte_nom.delete(0, END)
    prix_nom.delete(0, END)
    print(total)


#Nom et parametre de la fenetre
app.title("FACTURATION")
app.minsize(500, 600)
app.resizable(False, False)
app.config(bg="white")

# definir les paramètres de la fenêtre
name = Label(app, text="Facturation", font=("Impact 29"), bg="white")
name.pack()

nom_prod = Label(app, text="Nom du produit : ", fg="green" , font=("Calibri 16"), bg="white")
nom_prod.pack()
entrer_nom = Entry(app, width=20, font=("bold 14"))
entrer_nom.pack()

qte_prod = Label(app, text="Quanrité du produit : ", fg="yellow" , font=("Calibri 16"),bg="white")
qte_prod.pack()
qte_nom = Entry(app, width=20, font=("bold 14"))
qte_nom.pack()

prix_prod = Label(app, text="Prix Unitaire : ", fg="red" , font=("Calibri 16"), bg="white")
prix_prod.pack()
prix_nom = Entry(app, width=20, font=("bold 14"))
prix_nom.pack()
def quitter():
    app.destroy()
    root = Tk()
    #Nom et parametre de la fenetre
    root.title("*****FACTURE*****")
    root.minsize(500, 600)
    root.resizable(False, False)
    root.config(bg="white")
    entete = Label(root, text="LISTE DES PRODUITS ET PRIX : ", font=("Impact  19"))
    entete.pack()
    detail = Label(root, text="Produits\tQuantité\tPrix", font=("Calibri 18"))
    detail.pack()
    for chose, valeur, choses in zip(produits_nom, produit_qte, produit_prix):
        prod = Label(root, text=f" {chose}\t{valeur}\t{choses}", font=("Calibri 18"))
        prod.pack()
    facture = Label(root, text=f"Vous devez payé {total}", font=("algerian"), fg="blue")
    facture.pack()
    root.mainloop()

# le boutton principale
boutton = Button(app, text="VALIDER ...", font=("bold 16"), bg="white", fg="#124578", command=submit)
boutton.pack()
quitter = Button(app, text="GENERER LA FACTURE...", font=("bold 10"), bg="white", command=quitter)
quitter.pack()

#maintenir la boucle ouverte
app.mainloop()