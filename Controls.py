from pygame.locals import *
import pygame
import menu


# Controls Settings
pygame.init()
window = pygame.display.set_mode((564, 468))
window_rect = window.get_rect()
pygame.display.set_caption("Metal Snake-Pong")


# Controls Function
def access_controls():
    click = True
    while click:
        window.fill((0, 0, 255))
        # Objects templates
        controls_image = pygame.image.load('assets/keyboard.png')
        p_image = pygame.image.load('assets/keyboard_key_p.png')
        s_image = pygame.image.load('assets/keyboard_key_s.png')
        p = pygame.transform.scale(p_image, (50, 50))
        s = pygame.transform.scale(s_image, (50, 50))
        controls = pygame.transform.scale(controls_image, (200, 200))
        title_font = pygame.font.Font('fonts/METAG___.TTF', 30)
        subtitle_font = pygame.font.Font(
            'fonts/Tactical Espionage Action.ttf', 16)
        controls_title = title_font.render('CONTROLS', True, (255, 255, 255))
        up = subtitle_font.render('Up', True, (0, 0, 0))
        down = subtitle_font.render('Down', True, (0, 0, 0))
        left = subtitle_font.render('Left', True, (0, 0, 0))
        right = subtitle_font.render('Right', True, (0, 0, 0))
        s_key = subtitle_font.render('Continue', True, (0, 0, 0))
        p_key = subtitle_font.render('Pause', True, (0, 0, 0))
        play_font = pygame.font.Font('fonts/MGS2MENU.TTF', 20)
        text_1 = 'RETURN'
        text_1 = play_font.render(text_1, True, (255, 255, 255))
        text_1_rect = text_1.get_rect()
        text_1_rect.center = (282, 400)
        pos_mouse = pygame.mouse.get_pos()
        # Collision with mouse
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_1_rect.collidepoint(pos_mouse):
                    menu.access_menu()
                    click = False
            # Spawn objects on the screen
            window.blit(s_key, (410, 165))
            window.blit(s, (350, 150))
            window.blit(p_key, (410, 265))
            window.blit(p, (350, 250))
            window.blit(controls_title, (202, 10))
            window.blit(up, (170, 100))
            window.blit(down, (150, 320))
            window.blit(left, (40, 250))
            window.blit(right, (265, 250))
            window.blit(controls, (80, 120))
            window.blit(text_1, text_1_rect)
            pygame.display.update()


if __name__ == '__main__':
    access_controls()
