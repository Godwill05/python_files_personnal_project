from customtkinter import *

class Calculator :
    def __init__(self, app):
        self.app = app
        #reglage de la fenetre
        self.app.minsize(400, 300)
        self.app.resizable(FALSE, FALSE)
        #les variables 
        self.sept = StringVar()
        
        #creation des boutons et de la zone de texte
        self.btn1 = CTkEntry(app, font=("times new roman", 12), width=270, textvariable=self.sept)
        self.btn1.place(x=90, y=10)
        #creation des boutons
        
        #premier niveau
        self.btn2 = CTkButton(app, text="C", fg_color="black", width=60, command=self.clear)
        self.btn2.place(x=90, y=40)
        
        self.btn3 = CTkButton(app, text="7", fg_color="black", width=60, command=self.chage_7)
        self.btn3.place(x=160, y=40)
        
        self.btn4 = CTkButton(app, text="8", fg_color="black", width=60, command=self.chage_8)
        self.btn4.place(x=230, y=40)
        
        self.btn5 = CTkButton(app, text="9", fg_color="black", width=60, command=self.chage_9)
        self.btn5.place(x=300, y=40)
        
        #deuxieme niveau
        self.btn6 = CTkButton(app, text="*", fg_color="black", width=60, command=self.multi)
        self.btn6.place(x=90, y=70)
        
        self.btn7 = CTkButton(app, text="6", fg_color="black", width=60, command=self.chage_6)
        self.btn7.place(x=160, y=70)
        
        self.btn8 = CTkButton(app, text="5", fg_color="black", width=60, command=self.chage_5)
        self.btn8.place(x=230, y=70)
        
        self.btn9 = CTkButton(app, text="4", fg_color="black", width=60, command=self.chage_4)
        self.btn9.place(x=300, y=70)
        
        #troisieme niveau
        self.btn10 = CTkButton(app, text="/", fg_color="black", width=60, command=self.division)
        self.btn10.place(x=90, y=100)
        
        self.btn11 = CTkButton(app, text="3", fg_color="black", width=60, command=self.chage_3)
        self.btn11.place(x=160, y=100)
        
        self.btn12 = CTkButton(app, text="2", fg_color="black", width=60, command=self.chage_2)
        self.btn12.place(x=230, y=100)
        
        self.btn13 = CTkButton(app, text="1", fg_color="black", width=60, command=self.chage_1)
        self.btn13.place(x=300, y=100)
        
        #quatrieme niveau
        self.btn14 = CTkButton(app, text="+", fg_color="black", width=60, command=self.plus)
        self.btn14.place(x=90, y=130)
        
        self.btn15 = CTkButton(app, text="-", fg_color="black", width=60, command=self.moins)
        self.btn15.place(x=160, y=130)
        
        self.btn16 = CTkButton(app, text="0", fg_color="black", width=60, command=self.chage_0)
        self.btn16.place(x=230, y=130)
        
        self.btn17 = CTkButton(app, text="=", fg_color="black", width=60, command=self.resultat)
        self.btn17.place(x=300, y=130)
        
    def chage_0(self):
        self.btn1.insert(END, "0")
    def chage_1(self):
        self.btn1.insert(END, "1")
    def chage_2(self):
        self.btn1.insert(END, "2")
    def chage_3(self):
        self.btn1.insert(END, "3")
    def chage_4(self):
        self.btn1.insert(END, "4")
    def chage_5(self):
        self.btn1.insert(END, "5")
    def chage_6(self):
        self.btn1.insert(END, "6")
    def chage_7(self):
        self.btn1.insert(END, "7")
    def chage_8(self):
        self.btn1.insert(END, "8")
    def chage_9(self):
        self.btn1.insert(END, "9")
    
    def plus(self):
       self.btn1.insert(END, "+")
    def moins(self):
        self.btn1.insert(END, "-")
    def division(self):
        self.btn1.insert(END, "/")
    def multi(self):
        self.btn1.insert(END, "*")
    def plus(self):
        self.btn1.insert(END, "+")
    def clear(self):
       self.btn1.delete(0, END)

    def resultat(self):
        v = eval(self.btn1.get())
        self.btn1.delete(0, END)
        self.btn1.insert(END, v)
        v= IntVar()
    
app = CTk()
Calculator(app)
app.mainloop()