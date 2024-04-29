import time
from customtkinter import *
from tkinter import *
class Chatbot:
    def __init__(self, app):
        
        self.valeur = "normal"
        self.app = app
        app.title("Chat bot")
        self.app.config(bg="black")
        app.minsize(500, 600)
        app.resizable(FALSE, FALSE)
        # entrer pour l'utilisateur
        self.user_entry = CTkTextbox(app, font=("microsoft yahei ui light", 13), width=330,height=12, bg_color="black")
        self.user_entry.place(x=10, y=550)
        #bouton pour soumettre la question
        self.send_button = CTkButton(app, text="Envoyer", font=("corbel", 16), height=35, bg_color="black", fg_color="green", command=self.envoyer)
        self.send_button.place(x=350, y=550)
        
        #Zone de reponse pour le robot
        self.chat_response = CTkTextbox(app, font=("times new roman", 16), bg_color="black", width=475, height=450, state=self.valeur)
        self.chat_response.place(x=10, y=50)
        
        #les listes a prendres en compte
        self.salutations = ["hello", "comment tu vas", "Comment tu vas", "Comment sa va", "comment sa va"]
        self.salu = ["oui"]
    def envoyer(self):
        if self.user_entry.get("1.0", "end-1c") =="Bonjour" or self.user_entry.get("1.0", "end-1c") =="bonjour"  or self.user_entry.get("1.0", "end-1c") =="salut" or self.user_entry.get("1.0", "end-1c") =="Salut" :
            time.sleep(1)
            self.chat_response.insert("1.0", "Bonjour comment puis-je vous aidez aujourd'hui ???\n")
            self.valeur = "disabled"
        for mot in self.salutations:
            if mot in self.user_entry.get("1.0", "end-1c"):
                self.chat_response.insert("1.0",
                                          "Je me porte a merveile\n comment puis-je vous aidez aujourd'hui ???\n")
        
            
app = CTk()
Chatbot(app)
app.mainloop()