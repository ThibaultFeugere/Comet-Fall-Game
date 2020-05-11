import pygame
from game import Game

pygame.init()

# Generer la fenetre du jeu
pygame.display.set_caption('Comet Fall Game')
screen = pygame.display.set_mode((1080, 720))

# Import du background
background = pygame.image.load('assets/bg.jpg')

# Charger le jeu
game = Game()

running = True

while running:
    # Appliquer le background
    screen.blit(background, (0, -200))
    # Appliquer image joueur
    screen.blit(game.player.image, game.player.rect)

    # Mettre a jour ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fin du while et fermeture du jeu")