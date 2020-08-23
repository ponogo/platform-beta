import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, images):
      self.image = pygame.image.load('PlatformCube.png')
      self.rect = self.image.get_rect()
      self.rect.center = pos
      self.xy_speed = pygame.math.Vector2(0,0)
      self.facing = "R"
      self.jump_speed = -14
      self.world_y = 0
      self.progress = 0

    def update(self, platforms):
      screen_info = pygame.display.Info()

      if self.rect.top >= screen_info.current_h-80:
        print("You Died")
      else:
        print()

      self.rect.move_ip(self.xy_speed)

      self.xy_speed[0] = 0
      self.world_y += self.xy_speed[1]*-1

      if self.world_y > self.progress:
        self.progress = self.world_y

      if self.rect.top < 100:
        self.rect.top = 100
        for plat in platforms.sprites():
          plat.scroll
          (-1*self.xy_speed[1])

      hit_list = pygame.sprite.spritecollide(self, platforms, False)
      for plat in hit_list:
        if self.xy_speed[1] > 0 and abs(self.rect.bottom - plat.rect.top) <= self.xy_speed[1]:
              self.rect.bottom = plat.rect.bottom
              self.xy_speed[1] = self.jump_speed

        self.xy_speed[1] += .5

    def left(self):
      self.facing = 'L'
      self.xy_speed = -6

    def right(self):
      self.facing = 'R'
      self.xy_speed = 6
