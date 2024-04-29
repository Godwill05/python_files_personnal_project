class maclasse ():
    def fontion():
        global recup
        recup = no.get()
        print(recup) 
        button.destroy()
        nom.destroy()
        no.destroy()
        if(recup!="#"):
            def fontion1():
                global recup2, prix_entrer
                recup2= int(saisie.get())
                print(recup2)
                qte.destroy()
                saisie.destroy()
                boutton_saisie.destroy()
                prix = tk.Label(app, text="Prix Unitaire : ",font=("Calibri 14"), bg="white")
                prix.pack() 
                prix_entrer = tk.Entry(app, width=20)
                prix_entrer.pack()
                prix_boutton = tk.Button(app, text="Valider", command=fontion2)
                prix_boutton.pack()
            def fontion2():
                global recup3
                recup3 = int(prix_entrer.get())
                calcule = recup2*recup3
                print(calcule)
         
        qte = tk.Label(app, text="Quantité du produit  : ", font=("Calibri 14"), bg="white")
        qte.pack()
        saisie = tk.Entry(app, width=20)
        saisie.pack()
        boutton_saisie = tk.Button(app, text="Valider", command=fontion1)
        boutton_saisie.pack()