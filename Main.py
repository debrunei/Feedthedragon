import pygame, random
pygame.init()

Window_Width = 1000
Window_Height = 400
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
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

score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

#Set Text for Title (Similar to Score)

title_text = font.render("Feed the dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = Window_Width//2
title_rect.y = 10

#Set Text for Lives (Similar to Score)

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (Window_Width - 10, 10)

#Set Text for Game Over (Similar to Score)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (Window_Width//2, Window_Height//2)

#Set Text for Continue (Similar to Score)

continue_text = font.render("Press any key to continue", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (Window_Width//2, Window_Height//2 + 32)

coin_sound = pygame.mixer.Sound("coin_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(0.1)
pygame.mixer.music.load("ftd_background_music.wav")

player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = Window_Height // 2

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = Window_Width + BUFFER_DISTANCE
coin_rect.y = random.randint(64, Window_Width - 32)

pygame.mixer.music.play(-1, 0.0)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < Window_Height:
        player_rect.y += PLAYER_VELOCITY

    if coin_rect.x < 0:
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = Window_Width + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, Window_Height - 32)
    else:
        coin_rect.x -= coin_velocity

    if player_rect .colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x  = Window_Width + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, Window_Height - 32)


    score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
    lives_text = font.render("lives: " + str(player_lives), True, GREEN, DARKGREEN)

    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = Window_Height // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False

    #Fill the display
    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)
    pygame.draw.line(display_surface, WHITE, (0, 64), (Window_Width, 64), 2)

    #Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()