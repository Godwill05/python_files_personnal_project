from customtkinter import*
def autre():
    
    app.destroy()
    app2=CTk()
    app2.title("Une autre fenetre")
    ca=CTkSlider(app2)
    ca.pack()
    app2.mainloop()
app = CTk()
la = CTkLabel(app, text="ceci est un label", font=("algerian",19))
la.pack()
s=CTkTextbox(app, text_color="red")
s.pack()
b=CTkButton(app, text="boutton", command=autre)
b.pack()
app.mainloop()
