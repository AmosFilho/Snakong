import sys
import pygame
import menu
import MetalSnake


# Game over Assets
pygame.init()
window = pygame.display.set_mode((564, 468))
window_rect = window.get_rect()
pygame.display.set_caption("Metal Snake-Pong")
click = False
score = 0


# Game over function
def game_over(points):
    # Game over sound effect
    death_sound = pygame.mixer.Sound('assets/metalgear_game_over.wav')
    death_sound.set_volume(0.5)
    death_sound.play()
    mouse_click = True
    while mouse_click:
        # Game over templates
        title_font = pygame.font.Font('fonts/METAG___.TTF', 60)
        menu_text = title_font.render('Metal Snake', True, (255, 255, 255))
        menu_text_rect = menu_text.get_rect()
        menu_text_rect.center = (292, 100)
        menu_font = pygame.font.Font('fonts/MGS2MENU.TTF', 20)
        window.fill((0, 0, 0))
        text_0 = 'GAME OVER'
        text_1 = 'RESTART'
        text_2 = "MENU"
        text_3 = 'EXIT'
        text_0 = title_font.render(text_0, True, (0, 0, 200))
        text_1 = menu_font.render(text_1, True, (255, 255, 255))
        text_2 = menu_font.render(text_2, True, (255, 255, 255))
        text_3 = menu_font.render(text_3, True, (255, 255, 255))
        text_4 = menu_font.render('Your Score:' + str(points), True,
                                  (0, 0, 90))
        text_0_rect = text_0.get_rect()
        text_1_rect = text_1.get_rect()
        text_2_rect = text_2.get_rect()
        text_3_rect = text_3.get_rect()
        text_4_rect = text_4.get_rect()
        text_0_rect.center = (282, 100)
        text_1_rect.center = (282, 234)
        text_2_rect.center = (282, 264)
        text_3_rect.center = (282, 294)
        text_4_rect.center = (282, 180)
        # Get mouse position and verifies collision
        pos_mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_1_rect.collidepoint(pos_mouse):
                    death_sound.stop()
                    MetalSnake.play_game()
                    mouse_click = False
                if text_2_rect.collidepoint(pos_mouse):
                    death_sound.stop()
                    menu.access_menu()
                    mouse_click = False
                    pygame.display.update()
                if text_3_rect.collidepoint(pos_mouse):
                    pygame.quit()
                    sys.exit()
            # Spawn the text and button objects
            window.blit(text_0, text_0_rect)
            window.blit(text_1, text_1_rect)
            window.blit(text_2, text_2_rect)
            window.blit(text_3, text_3_rect)
            window.blit(text_4, text_4_rect)
            pygame.display.update()


if __name__ == '__main__':
    game_over(score)
