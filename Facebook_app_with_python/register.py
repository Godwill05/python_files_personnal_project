from customtkinter import *
from tkinter import *
import messagebox
from PIL import Image, ImageTk

import time
import sqlite3
import pymysql
class Register :
    def __init__(self, app):
        self.app = app
        #réglages de la fenetres
        app.minsize(600, 500)
        app.resizable(False, False)
       
        
        image = Image.open("bg.jpg")
        
        image.resize((600, 400))
        photo = ImageTk.PhotoImage(image)
        
        bac = CTkLabel(app, image=photo)
        p = CTkLabel(app, image=photo)
        p.pack()
    
app = CTk()
ins = Register(app)
app.mainloop()