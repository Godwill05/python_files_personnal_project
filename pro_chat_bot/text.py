from customtkinter import *

class Text :
    def __init__(self, app):
        self.app = app
        self.taille = 14
        self.fontu = ("Microsof Yahei ui light", self.taille)
        app.minsize(700, 600)
        self.text = CTkTextbox(app, height=360, width=400, font=self.fontu)
        self.text.place(x=250, y=50)
        
        #les box
        self.font1 = CTkButton(app, text="Microsof Yahei ui light", font=("Microsoft yahei ui light", 12))
        self.font1.place(x=10, y=10)
    def se(self):
        fontu=("microsoft yahei ui light", self.taille)
        
        
app = CTk()
instance1 = Text(app)
app.mainloop()
