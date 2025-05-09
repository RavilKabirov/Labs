#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
pygame.mixer.music.load("RacerUpd/background.wav") #loading music
pygame.mixer.music.play(-1)
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE2 = 0
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("RacerUpd/AnimatedStreet.png") #loading background

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite): #Creating enemy class
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("RacerUpd/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0) #characteristics of enemy sprite

      def move(self): 
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600): # If top of the enemys car is on the bottom of playing space, we have score + 1 and we restart enemy in random position
            SCORE += 1
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("RacerUpd/coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) #Scaling of image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        
        self.rect.move_ip(0,SPEED) #Speed increases as enemies, with time and score2
        if (self.rect.top > 600):
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
      
        

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("RacerUpd/Player.png")
        
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins = pygame.sprite.Group()
coins.add(C1)


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000) #timer that activates increase in speed every second
flag = 0
#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if SCORE2 >= flag + 10: #increasing speed every 10 coins
        flag += 10
        SPEED += 1
        
    
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK) #2 counters
    scores2 = font_small.render(str(SCORE2), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(scores2, (SCREEN_WIDTH - 30, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('RacerUpd/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    if pygame.sprite.spritecollideany(P1, coins):
        SCORE2 += random.randint(1, 3) #coins with random weight and code resets their position
        C1.rect.bottom = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    if pygame.sprite.spritecollideany(E1, coins): #if coins are spawned on enemy, they respawned

        C1.rect.bottom = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    pygame.display.update()
    FramePerSec.tick(FPS)
