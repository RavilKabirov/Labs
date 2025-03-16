import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))


clock = pygame.time.Clock()

running = True
x = screen.get_width() / 2
y = screen.get_height() / 2


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 40: y -= 20
    if pressed[pygame.K_DOWN] and y < screen.get_height() - 40 : y += 20
    if pressed[pygame.K_LEFT] and x > 40: x -= 20
    if pressed[pygame.K_RIGHT] and x < screen.get_width() - 40: x += 20
    screen.fill((255, 255, 255))     

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    
    
    pygame.display.flip() 
    clock.tick(60)

pygame.quit()