import pygame
import datetime
pygame.init()

screen = pygame.display.set_mode((800, 600))
image = pygame.image.load("clock.png")  
im2 = pygame.image.load("min_hand.png")
im3 = pygame.image.load("sec_hand.png")
image_rect = image.get_rect() 
image_rect2 = im2.get_rect() 
image_rect3 = im3.get_rect()
screen_rect = screen.get_rect() 
image_rect.center = screen_rect.center  
image_rect2.center = screen_rect.center
image_rect3.center = screen_rect.center
clock = pygame.time.Clock()
running = True
now = datetime.datetime.now()

angle1 = 0
angle2 = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((255, 255, 255)) 
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    angle1 = -(seconds * 6 - 60)
    angle2 = -(minutes * 6 + 54)
    screen.blit(image, image_rect)  
    rotated_image2 = pygame.transform.rotate(im2, angle2)
    rotated_image1 = pygame.transform.rotate(im3, angle1)
    rotated_rect1 = rotated_image1.get_rect(center=screen.get_rect().center)
    rotated_rect2 = rotated_image2.get_rect(center=screen.get_rect().center)
    screen.blit(rotated_image1, rotated_rect1)
    screen.blit(rotated_image2, rotated_rect2)
    
    pygame.display.flip() 
    clock.tick(60)

pygame.quit()
