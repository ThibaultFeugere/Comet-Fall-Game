import pygame

pygame.init()

# Generer la fenetre du jeu
pygame.display.set_caption('Comet Fall Game')
screen = pygame.display.set_mode((1080, 720))

# import du background
background = pygame.image.load('assets/bg.jpg')

running = True

while running:
    # Appliquer le background
    screen.blit(background, (0, -200))
    # Mettre a jour ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fin du while et fermeture du jeu")