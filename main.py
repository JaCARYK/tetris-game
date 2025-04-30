import pygame, sys

pygame.init() #initialize pygame

screen = pygame.display.set_mode((300,600)) #set display surface, 300 is x or width, 600 is length or height
title = pygame.display.set_caption("Jacob's Tetris Game") #title of game

clock = pygame.time.Clock() #speed at which game runs, specifically frame rate

#NOW FOR THE GAME LOOP:
#GAME LOOP HAS:
# ONE: EVENT HANDLING (quitting the game, key pressed during game, etc. basically any event)
# TWO: UPDATING POSITIONS (update the positions of all game objects based on events we detected in step one)
# THREE: DRAWING OBJECTS (draw all new objects in new positions on screen. use pygame graphics functions to render objects in display) 


while True: #runs continuosly until we close the game. It does three things:
    for event in pygame.event.get(): #see notes on this line in NB
        if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()
    pygame.display.update()

