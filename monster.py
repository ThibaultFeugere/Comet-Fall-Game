import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('./assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1060 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1060 + random.randint(0, 300)
            self.health = self.max_health

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        bar_position = [self.rect.x + 12, self.rect.y - 20, self.health, 5]

        background_bar_color = (60, 63, 60)
        background_bar_position = [self.rect.x + 12, self.rect.y - 20, self.max_health, 5]

        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack)