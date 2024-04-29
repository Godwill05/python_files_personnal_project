import tkinter as tk
from customtkinter import*

class MyInterface:
    def __init__(self, root):
        self.root = root

        self.label = CTkLabel(root, text="Entrez un texte:")
        self.label.pack()

        self.entry = CTkEntry(root)
        self.entry.pack()

        self.button = CTkButton(root, text="Afficher", command=self.display_text)
        self.button.pack()

    def display_text(self):
        text = self.entry.get()
        print("Texte entré :", text, self.entry.get())

root = CTk()
my_interface = MyInterface(root)
root.mainloop()
