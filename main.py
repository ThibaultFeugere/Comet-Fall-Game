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
    # Actualiser barre de vie
    game.player.update_health_bar(screen)
    # Recuperer projeciles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # Recuêrer les monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
    # Appliquer image projectiles
    game.player.all_projectiles.draw(screen)
    # Appliquer image monstres
    game.all_monsters.draw(screen)
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 910:
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -30:
        game.player.move_left()

    print(game.player.rect.x)

    # Mettre a jour ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fin du while et fermeture du jeu")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False