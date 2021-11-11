import pygame
from pygame.display import set_caption
from pygame.version import PygameVersion

from random import randint
pygame.init()
screen = pygame.display.set_mode((400,600))

WIDTH = 400
HEIGHT = 600
pygame.display.set_caption('Helicopter')

running = True
GREEN = (0,200,0)
BLUE = (0,0,255)
RED = (255,0,0)
bird_drop = 0
GRAVITY = 0.5
clock = pygame.time.Clock()

TUBE_GAP = 200
TUBE_WIDTH = 50
tube1_x = 400
tube2_x = 600
tube3_x = 800

BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 50
BIRD_HEIGHT = 50

tube1_pass = False 
tube2_pass = False
pausing = False
tube3_pass = False


tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)
score = 0
font = pygame.font.SysFont('sans',20)
VELOCITY = 3
BLACK =(0,0,0)
YELLOW = (255,255,0)

background = pygame.image.load("background.png")
bird_image = pygame.image.load("mb.png")
bird_image = pygame.transform.scale(bird_image,(BIRD_WIDTH, BIRD_HEIGHT))
while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(background,(0,0 ))
    
    tube1 = pygame.draw.rect(screen,BLUE,(tube1_x,0,TUBE_WIDTH,tube1_height))
    
    tube2 = pygame.draw.rect(screen,BLUE,(tube2_x,0,TUBE_WIDTH,tube2_height))
    
    tube3 = pygame.draw.rect(screen,BLUE,(tube3_x,0,TUBE_WIDTH,tube3_height))

    tube1_invert =  pygame.draw.rect(screen,BLUE,(tube1_x,tube1_height+TUBE_GAP,TUBE_WIDTH,HEIGHT - TUBE_GAP - tube1_height))
    tube2_invert = pygame.draw.rect(screen,BLUE,(tube2_x,tube2_height+TUBE_GAP,TUBE_WIDTH,HEIGHT - TUBE_GAP - tube2_height))
    tube3_invert = pygame.draw.rect(screen,BLUE,(tube3_x,tube3_height+TUBE_GAP,TUBE_WIDTH,HEIGHT - TUBE_GAP - tube3_height))


    tube1_x-= VELOCITY
    tube2_x-= VELOCITY
    tube3_x-= VELOCITY
    bird_y+= bird_drop
    bird_drop+= GRAVITY


    SAND = pygame.draw.rect(screen, YELLOW,(0,550,400,50))

    

    bird_rect = screen.blit(bird_image,(BIRD_X, bird_y))

    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100,400)
        tube1_pass = False
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100,400)
        tube2_pass = False


    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100,400)
        tube3_pass = False


    score_txt = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_txt,(5,5))

    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
        score+=1
        tube1_pass = True
    if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
        score+=1
        tube2_pass = True

    if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
        score+=1
        tube3_pass = True

    for tube in [tube1, tube2, tube3, tube1_invert,SAND, tube2_invert, tube3_invert]:
        if bird_rect.colliderect(tube):
            VELOCITY = 0
            bird_drop = 0
            game_over = font.render("Game over: "+ str(score), True, BLACK)
            screen.blit(game_over,(200,300))        
            press_space = font.render("Press space to continue", True, BLACK)
            screen.blit(press_space,(200,400))
            pausing = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                if pausing:
                    bird_y = 400
                    VELOCITY = 3
                    tube1_x = 600
                    tube2_x = 800
                    tube3_x = 1000
                    score = 0
                    pausing = False
                bird_drop = 0
                bird_drop -=10
    
    pygame.display.flip()
    
pygame.quit()
