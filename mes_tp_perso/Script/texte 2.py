import pyglet
from pyglet.window import key

# Créer une fenêtre
fenetre = pyglet.window.Window(800, 600, "Exemple de jeu avec Pyglet")

# Charger une image
image = pyglet.image.load("./img.png")
sprite = pyglet.sprite.Sprite(image)

@fenetre.event
def on_draw():
    fenetre.clear()
    sprite.draw()

@fenetre.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        sprite.x -= 10
    elif symbol == key.RIGHT:
        sprite.x += 10
    elif symbol == key.UP:
        sprite.y += 10
    elif symbol == key.DOWN:
        sprite.y -= 10

pyglet.app.run()