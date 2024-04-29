import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
largeur = 800
hauteur = 600

# Créer la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Exemple de jeu avec Pygame")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Position et taille du joueur
joueur_x = largeur // 2
joueur_y = hauteur // 2
joueur_largeur = 50
joueur_hauteur = 50

# Boucle principale du jeu
en_cours = True
while en_cours:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Déplacement du joueur avec les touches directionnelles
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        joueur_x -= 5
    if touches[pygame.K_RIGHT]:
        joueur_x += 5
    if touches[pygame.K_UP]:
        joueur_y -= 5
    if touches[pygame.K_DOWN]:
        joueur_y += 5

    # Dessiner sur l'écran
    ecran.fill(BLANC)
    pygame.draw.rect(ecran, NOIR, (joueur_x, joueur_y, joueur_largeur, joueur_hauteur))

    # Rafraîchir l'écran
    pygame.display.flip()

# Fermer Pygame
pygame.quit()