import pygame
import random

class Dice():
    def __init__(self, sides):
        self.sides = sides;
        self.side = random.randrange(1,sides)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
base_font = pygame.font.Font(None,32)
output_text = 'Enter a number of sides you\'d like the dice to have:'
user_text = ''
dice_roll = ''

pygame.display.set_caption("Dice")

doExit = False

while doExit == False: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key != pygame.K_RETURN:
                user_text += event.unicode
            else:
                dice_roll = ''
                diceRoll = Dice(int(user_text))
                dice_roll = str(diceRoll.side)
                user_text = ''

    screen.fill((0,0,0)) #render section
    user_text_surface = base_font.render(user_text,True,(255,255,255))
    output_text_surface = base_font.render(output_text,True,(0,0,255))
    dice_roll_surface = base_font.render(dice_roll,True,(255,0,0))
    screen.blit(user_text_surface,(535,30))
    screen.blit(dice_roll_surface,(400,400))
    screen.blit(output_text_surface,(0,30))
            
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()

