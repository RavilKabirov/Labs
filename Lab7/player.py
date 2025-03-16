import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
_songs = ['Brianstorm.mp3', 'Myway.mp3', 'No_buses.mp3']
currently_playing_song = None
clock = pygame.time.Clock()
def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] 
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def play_prev_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1] 
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
running = True
Paused = True
pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play()
while running:
    for event in pygame.event.get():
        
        
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            if Paused:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            Paused = not Paused
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            play_next_song()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            play_prev_song()
    screen.fill((255, 255, 255)) 
    
    pygame.display.flip() 
    clock.tick(60)

pygame.quit()
