import nltk

import tkinter as tk
from nltk.corpus import words

class AutoCompleteEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        tk.Entry.__init__(self, *args, **kwargs)
        self.words = set(words.words())
        self.suggestion_list = []
        self.bind('<KeyRelease>', self.show_suggestions)

    def show_suggestions(self, event):
        self.suggestion_list = []
        current_text = self.get()
        if current_text:
            for word in self.words:
                if word.startswith(current_text):
                    self.suggestion_list.append(word)
        self.autocomplete()

    def autocomplete(self):
        self.delete(0, tk.END)
        if self.suggestion_list:
            self.insert(tk.END, self.suggestion_list[0])

root = tk.Tk()

label = tk.Label(root, text="Saisissez du texte :")
label.pack()

entry = AutoCompleteEntry(root)
entry.pack()

root.mainloop()
