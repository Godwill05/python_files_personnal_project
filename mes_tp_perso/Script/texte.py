import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ExampleApp(toga.App):
    def startup(self):
        # Crée les widgets
        self.name_input = toga.TextInput(placeholder='Nom', style=Pack(flex=1))
        self.firstname_input = toga.TextInput(placeholder='Prénom', style=Pack(flex=1))
        self.age_input = toga.TextInput(placeholder='Âge', style=Pack(flex=1))
        self.sex_input = toga.TextInput(placeholder='Sexe', style=Pack(flex=1))
        self.dob_input = toga.DatePicker(style=Pack(flex=1))
        self.button = toga.Button('Envoyer', on_press=self.display_data)

        # Crée la boîte de dialogue
        box = toga.Box(
            children=[
                toga.Label('Nom:'),
                self.name_input,
                toga.Label('Prénom:'),
                self.firstname_input,
                toga.Label('Âge:'),
                self.age_input,
                toga.Label('Sexe:'),
                self.sex_input,
                toga.Label('Date de naissance:'),
                self.dob_input,
                self.button
            ],
            style=Pack(direction=COLUMN, padding=10)
        )

        # Crée la fenêtre principale
        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(box)

        # Définit la fenêtre principale de l'application
        self.main_window = toga.MainWindow(title=self.name, size=(400, 300))
        self.main_window.content = main_box
        self.main_window.show()

    def display_data(self, widget):
        # Récupère les données saisies
        name = self.name_input.value
        firstname = self.firstname_input.value
        age = self.age_input.value
        sex = self.sex_input.value
        dob = self.dob_input.value

        # Affiche les données dans une boîte de dialogue
        self.main_window.info_dialog(
            'Données saisies',
            f'Nom: {name}\nPrénom: {firstname}\nÂge: {age}\nSexe: {sex}\nDate de naissance: {dob}'
        )


def main():
    return ExampleApp('Interface graphique avec Toga', 'org.example.interface')


if __name__ == '__main__':
    main().main_loop()
