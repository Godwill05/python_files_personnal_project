from toga import*
def build(app):
    main_window = MainWindow(title="fenetre avec toga")
    label = Label(text="Hello Toga")
    main_window.content = label
    return main_window

app = App("Mon app", "org.example.monapp", startup=build)
app.main_loop()