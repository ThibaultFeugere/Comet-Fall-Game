import pygame
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen, ):
        # Appliquer image joueur
        screen.blit(self.player.image, self.player.rect)
        # Actualiser barre de vie
        self.player.update_health_bar(screen)
        # Recuperer projeciles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Recuêrer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        # Appliquer image projectiles
        self.player.all_projectiles.draw(screen)
        # Appliquer image monstres
        self.all_monsters.draw(screen)
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 910:
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -30:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))
