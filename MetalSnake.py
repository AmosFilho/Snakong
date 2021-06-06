import pygame
import sys
from pygame.locals import *
import random
import menu
import game_over_screen
import Grenade

pygame.init()
screen = pygame.display.set_mode((564, 468))
pygame.display.set_caption('Metal Snake-Pong')

# Objects Templates
background_image = pygame.image.load('assets/new_lab_background.png')
background = pygame.transform.scale(background_image, (564, 448))
head_right = pygame.image.load('assets/Solid_Snake_Right.png').convert_alpha()
head_left = pygame.image.load('assets/Solid_Snake_Left.png')
head_1 = pygame.transform.scale(head_right, (30, 25))
head_2 = pygame.transform.scale(head_left, (30, 25))
apple_image = pygame.image.load('assets/Cigar.png').convert_alpha()
apple = pygame.transform.scale(apple_image, (30, 20))
shield_image = pygame.image.load('assets/cardboard.png')
shield = pygame.transform.scale(shield_image, (30, 30))

# Music and Sound Effects Credits
# https://www.youtube.com/watch?v=MsXOdmdhZ08
# https://www.myinstants.com/instant/metal-gear-solid-alert/
# https://www.myinstants.com/instant/metal-gear-solid-game-over/


# Randomize objects screen position
def on_grid_random():
    x = random.randint(0, 26)
    y = random.randint(2, 22)
    return x * 20, y * 20


def collision(c1, c2):
    # Create a definition of collision
    return (c2[0] - 20 <= c1[0] <= c2[0] + 20)\
           and (c2[1] - 20 <= c1[1] <= c2[1] + 20)


# Create the game function
def play_game():
    # Positioning variables
    shield_pos = ((random.randint(0, 524)), random.randint(20, 418))
    apple_pos = ((random.randint(0, 524)), random.randint(20, 418))
    snake = [(300, 300)]

    # Motion variables
    view_direction = 1
    game = True
    up = 0
    down = 1
    left = 2
    right = 3
    my_direction = left
    grenade_control = 0
    grenade_control2 = 0

    # Shield settings
    shield_event = 0
    using_shield = 0
    time = 13.0

    # FPS
    clock = pygame.time.Clock()

    # Ball/Grenade template
    ball_image = pygame.image.load("assets/Grenade.png").convert_alpha()
    ball = pygame.transform.scale(ball_image, (20, 20))
    grenades = [{'ball_x': 282, 'ball_y': 234, 'ball_dx': 1, 'ball_dy': 1}]

    font = pygame.font.Font('freesansbold.ttf', 18)
    font_pause = pygame.font.Font('fonts/Patrima-Outline.otf', 20)

    # Pause Button Settings
    running, pause = 0, 1
    state = running
    pause_text = font_pause.render('Pause', True, (0, 0, 255))
    undone_pause = font_pause.render('Press "S" to continue',
                                     True, (0, 0, 255))

    # Play and Looping game song
    game_song = pygame.mixer.Sound('assets/secret_mission_song.wav')
    game_song.set_volume(0.5)
    game_song.play(-1)

    # Taking the shield sound effect
    shield_sound = pygame.mixer.Sound('assets/snake_spotted.wav')
    shield_sound.set_volume(0.5)

    # Score counter
    score = 0

    while game:
        clock.tick(13)
        # Movements and quit events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    my_direction = up
                    snake[0] = (snake[0][0], snake[0][1] - 10)
                if event.key == K_DOWN:
                    my_direction = down
                    snake[0] = (snake[0][0], snake[0][1] - 10)
                if event.key == K_LEFT:
                    my_direction = left
                if event.key == K_RIGHT:
                    my_direction = right
                if event.key == pygame.K_p:
                    state = pause
                if event.key == pygame.K_s:
                    state = running
        # Not pause condition
        if state == running:
            # Grenade spawn control
            if score > 10 and grenade_control == 0:
                Grenade.make_grenade(grenades)
                grenade_control = 1
            if score > 20 and grenade_control2 == 0:
                Grenade.make_grenade(grenades)
                grenade_control2 = 1
            # Check the shield duration
            if time < 0:
                using_shield = 0
            if using_shield:
                time -= 0.1
            # Snake get the Cigar
            if collision(snake[0], apple_pos):
                if not using_shield:
                    apple_pos = on_grid_random()
                    shield_event = random.choice(range(1, 6))
                else:
                    apple_pos = on_grid_random()
                    shield_event = random.choice(range(3, 6))
                score = score + 1
            # Getting the shield
            if collision(snake[0], shield_pos) and shield_event == 2\
                    and using_shield == 0:
                time = 13.0
                shield_sound.play()
                using_shield = 1
                shield_pos = on_grid_random()
                shield_event = random.choice(range(3, 6))
            # Make grenades move
            for i in range(len(grenades)):
                grenades[i].update(Grenade.move_ball(grenades[i]['ball_x'],
                                                     grenades[i]['ball_y'],
                                                     grenades[i]['ball_dx'],
                                                     grenades[i]['ball_dy']))
                if collision(snake[0], (grenades[i]['ball_x'],
                                        grenades[i]['ball_y'])):
                    if not using_shield:
                        game_song.stop()
                        game_over_screen.game_over(score)
                        game = False
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i - 1][0], snake[i - 1][1])

            # Make the snake move.
            if my_direction == up:
                snake[0] = (snake[0][0], snake[0][1] - 10)
            if my_direction == down:
                snake[0] = (snake[0][0], snake[0][1] + 10)
            if my_direction == right:
                view_direction = 1
                snake[0] = (snake[0][0] + 10, snake[0][1])
            if my_direction == left:
                view_direction = -1
                snake[0] = (snake[0][0] - 10, snake[0][1])
            # Snake Collision with any wall
            if snake[0][0] > 544 or snake[0][1] > 448 or snake[0][0] < 0\
                    or snake[0][1] < 20:
                game_song.stop()
                game_over_screen.game_over(score)
                game = False
            # Spawn objects on the screen
            screen.fill((50, 50, 50))
            screen.blit(background, (0, 20))
            screen.blit(apple, apple_pos)
            score_font = font.render('Score: %s' % score, True,
                                     (255, 255, 255))
            score_rect = score_font.get_rect()
            score_rect.topleft = (600 - 120, 0)
            screen.blit(score_font, score_rect)
            if shield_event == 2 and not using_shield:
                screen.blit(shield, shield_pos)
            for i in range(len(grenades)):
                screen.blit(ball, (grenades[i]['ball_x'],
                                   grenades[i]['ball_y']))
            if using_shield:
                screen.blit(shield, snake[0])
            elif view_direction == 1:
                screen.blit(head_1, snake[0])
            elif view_direction == -1:
                screen.blit(head_2, snake[0])
        elif state == pause:
            screen.fill((0, 0, 0))
            screen.blit(pause_text, (232, 200))
            screen.blit(undone_pause, (180, 234))
        pygame.display.flip()
    pygame.quit()
    pygame.display.update()
    sys.exit()


if __name__ == '__main__':
    menu.access_menu()
