import pygame
pygame.init()

Window_Width = 1000
Window_Height = 400
Display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption("Feed the dragon")


FPS = 60
clock = pygame.time.Clock()



PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100


score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

GREEN = (0,255,00)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0 ,0 ,0)


font = pygame.font.Font('AttackGraffiti.ttf', 32)

#Set Text for Score
'''
variable names:  score_text, score_rect
render text: "Score: " + str(score)
antialias: True
color: GREEN
background: DARKGREEN
rect location: topleft = (10, 10)  
'''
score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

#Set Text for Title (Similar to Score)
'''
variable names:  title_text , title_rect 
render text: "Feed the Dragon"
antialias: True
color: GREEN
background: WHITE
rect location: centerx = WINDOW_WIDTH//2
rect location: y = 10 
'''
title_text = font.render("Feed the dragon", True, GREEN, DARKGREEN)
title_rect = title_text.get_rect()
title_rect: centerx = Window_Width//2

#Set Text for Lives (Similar to Score)
'''
variable names:  lives_text, lives_rect
render text: "Lives: " + str(player_lives)
antialias: True
color: GREEN
background: DARKGREEN
rect location: y = 10  
'''



#Set Text for Game Over (Similar to Score)
'''
variable names:  game_over_text , game_over_rect 
render text: "GAMEOVER"
antialias: True
color: GREEN
background: DARKGREEN
rect location: center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) 
'''




#Set Text for Continue (Similar to Score)
'''
variable names:  continue_text, continue_rect  
render text: "Press any key to play again"
antialias: True
color: GREEN
background: DARKGREEN
rect location: center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)
'''





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Display_surface.fill(BLACK)

    Display_surface.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(FPS)



pygame.quit()