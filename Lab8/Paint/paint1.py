import pygame, sys


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

Thickness = 15

x = 0
y = pygame.mouse.get_pos()
mode = 'blue'
LMBP = False
screen.fill((0, 0, 0))
figure = "rect"
while True:
    
    pressed = pygame.key.get_pressed()
    
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # determine if a letter key was pressed
            if event.key == pygame.K_r:
                mode = 'red'
            elif event.key == pygame.K_g:
                mode = 'green'
            elif event.key == pygame.K_b:
                mode = 'blue'
            elif event.key == pygame.K_e:
                mode = "black"
            elif event.key == pygame.K_c:
                figure = "circle"
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            LMBP = True
            
        
        if event.type == pygame.MOUSEMOTION:
            # if mouse moved, add point to list
            x = event.pos[0]
            y = event.pos[1]
            
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            
            LMBP = False   
            
    
    # draw all points
    if LMBP and figure == "rect":
        pygame.draw.rect(screen, mode, (x, y, Thickness + 15, Thickness))
    elif LMBP and figure == "circle":
        pygame.draw.circle(screen, mode, (x, y), Thickness)
    pygame.display.flip()
    
    clock.tick(360)
