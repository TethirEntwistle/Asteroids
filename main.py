# this allows us to use code from
# the open-source pygame library
# throughout this file
# use these to get into the virtual machine
# python3 -m venv venv
# source venv/bin/activate
import pygame # type: ignore
from constants import *
from player import Player



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsClock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    mainPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
       for object in updatable:
           object.update(dt)
       screen.fill("black")
       for object in drawable:
           object.draw(screen)
       
       pygame.display.flip()
       
       dt = fpsClock.tick(60) / 1000
       
    
    
       



if __name__ == "__main__":
    main()
