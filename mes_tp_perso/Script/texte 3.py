from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3

class MonJeu(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Charger un modèle 3D
        self.environ = self.loader.loadModel("chemin/vers/modele.egg")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.2)
        self.environ.setPos(Point3(0, 0, 0))

        # Ajouter des contrôles de caméra
        self.disableMouse()
        self.camera.setPos(Point3(0, -10, 5))
        self.camera.lookAt(self.environ)

app = MonJeu()
app.run()