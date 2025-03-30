import pygame, sys


pygame.init()
screen = pygame.display.set_mode((640, 480))
basescreen = pygame.Surface((640, 480)) #screen that will be saved on our regular screen to draw on it
clock = pygame.time.Clock()

Thickness = 15

x = 0 #points of our mouse
y = 0
x1 = 0 #points where are mouse is clicked
y1 = 0
mode = 'blue'
LMBP = False
screen.fill((0, 0, 0))
figure = "risovat"
#formulas for points of different figures
def calc_rect(x, y, x1, y1):
    return pygame.Rect(min(x, x1), min(y, y1), abs(x - x1), abs(y - y1))
def calc_square(x, y, x1, y1):
    side = min(abs(x - x1), abs(y - y1))
    rect = pygame.Rect(x1, y1, side, side)
    if x < x1:
        rect.x = x1 - side
    if y < y1:
        rect.y = y1 - side
    return rect
def calc_triangle(x1, y1, x, y):
    side = max(abs(x - x1), abs(y - y1))  

    top = (x1, y1 - side)  
    left = (x1 - side // 2, y1)  
    right = (x1 + side // 2, y1) 

    return [top, left, right]
def right_triangle(x1, y1, x, y):
    return [(x1, y1), (x, y1), (x1, y)]
def calc_rhombus(x1, y1, x, y):
    return [((x + x1) / 2, y1), (x , (y + y1) / 2),((x + x1) / 2, y), (x1 , (y + y1) / 2) ]
while True:
    
    pressed = pygame.key.get_pressed()
    
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # determine if a letter key was pressed to choose colors and figures
            if event.key == pygame.K_1:
                mode = 'red'
            elif event.key == pygame.K_2:
                mode = 'green'
            elif event.key == pygame.K_3:
                mode = 'blue'
            elif event.key == pygame.K_4:
                mode = "black"
            elif event.key == pygame.K_c:
                figure = "circle"
            elif event.key == pygame.K_r:
                figure = "rect"
            elif event.key == pygame.K_s:
                figure = "square"
            elif event.key == pygame.K_a:
                figure = "risovat"
            elif event.key == pygame.K_t:
                figure = "equilateral triangle"
            elif event.key == pygame.K_o:
                figure = "right triangle"
            elif event.key == pygame.K_z:
                figure = "rhombus"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            LMBP = True #Activates LeftMouseButtonPressed and takes coordinates of start
            x1 = event.pos[0]
            y1 = event.pos[1]
         
            
            
            
        
        if event.type == pygame.MOUSEMOTION:
            # if mouse moved, add point to list
            x = event.pos[0]
            y = event.pos[1]
            if LMBP and figure == "rect":
                
                pygame.draw.rect(screen, mode, calc_rect(x1, y1, x, y))
                
                
            elif LMBP and figure == "circle":
                
                rect = calc_rect(x1, y1, x, y)
                pygame.draw.ellipse(screen, mode, rect)
            elif LMBP and figure == "risovat":
                pygame.draw.circle(screen, mode, (x1, y1), Thickness)
                x1, y1 = event.pos  
                basescreen.blit(screen, (0, 0)) #saves basescreen into screen directly in cycle for permanent effect of drawing
            if LMBP and figure == "square":
                
                pygame.draw.rect(screen, mode, calc_square(x, y, x1, y1))
            elif LMBP and figure == "equilateral triangle":
                points = calc_triangle(x1, y1, x, y)
    
                pygame.draw.polygon(screen, mode, points)
            elif LMBP and figure == "right triangle":
                points = right_triangle(x1, y1, x, y)
    
                pygame.draw.polygon(screen, mode, points)
            elif LMBP and figure == "rhombus":
                pygame.draw.polygon(screen, mode, calc_rhombus(x1, y1, x, y))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBP = False #disactivates drawing and draws prepared figures on our screen
            x = event.pos[0]
            y = event.pos[1]
            if figure == "rect":
                pygame.draw.rect(screen, mode, calc_rect(x1, y1, x, y))
            elif figure == "circle":
                rect = calc_rect(x1, y1, x, y)
                pygame.draw.ellipse(screen, mode, rect)
            elif figure == "square":
                pygame.draw.rect(screen, mode, calc_square(x, y, x1, y1))
            elif figure == "equilateral triangle":
                points = calc_triangle(x1, y1, x, y)
                pygame.draw.polygon(screen, mode, points)
            elif figure == "right triangle":
                points = right_triangle(x1, y1, x, y)
    
                pygame.draw.polygon(screen, mode, points)
            elif figure == "rhombus":
                pygame.draw.polygon(screen, mode, calc_rhombus(x1, y1, x, y))
            basescreen.blit(screen, (0, 0)) #saves basescreen on screen
            

        pygame.display.flip()
        screen.blit(basescreen, (0, 0))   
    
    
    clock.tick(100000)
