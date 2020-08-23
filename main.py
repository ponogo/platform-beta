import random
import pygame
import sys
from pygame.locals import*
from player import Player
from platforms import Platforms

pygame.init()
screen_info = pygame.display.Info()

size = (width,height) = (screen_info.current_w, screen_info.current_h)
font = pygame.font.SysFont(None, 50)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (100, 90, 50)

platforms = pygame.sprite.Group()
player = ''

def get_player_actions():
  p1_actions = {}

def init(p1_actions):
  global player
  for i in range(height //100):
    for j in range(width // 100):
      plat = Platforms(random.randint(5, (width - 50) // 10) *10, 120 * i, 70, 40)
      platforms.add(plat)
  player = Player((platforms.sprites()))[-1].rect.centerx, platforms.sprites()[-1].rect.centery-300, p1_actions, sprite_list.add(player)

def main():
  global player
  game_over = False
  p1_actions = get_player_actions()
  init(p1_actions)

  while True:
    clock.tick(60)
    if event.type == QUIT:
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_f:
        pygame.display.set_mode(size, FULLSCREEN)
      elif event.key == K_ESCAPE:
        pygame.display.set_mode(size)
      elif game_over and event.key == K_r:
        player.kill()
        init(p1_actions)
        game_over = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      player.left()
    if keys[pygame.K_RIGHT]:
      player.right()
    if player.update(platforms):
      game_over = True
    
    platforms.draw(screen)
    player.draw(screen)
    text = font.render("Score: {}".format(player.progress), True, (190, 400, 200))
    text_rect = text.get_rect()
    screen.fill(color)
    screen.blit(text, text_rect)
    pygame.display.flip

if __name__ == "__main__":
  main