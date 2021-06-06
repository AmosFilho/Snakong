import sys
import pygame
import MetalSnake
import Controls


# Menu Assets
pygame.init()
window = pygame.display.set_mode((564, 468))
window_rect = window.get_rect()
pygame.display.set_caption("Metal Snake-Pong")


# Menu Function
def access_menu():
    click = True
    while click:
        window.fill((0, 0, 0))
        # Menu templates
        title_font = pygame.font.Font('fonts/METAG___.TTF', 60)
        menu_text = title_font.render('Metal Snake', True, (255, 255, 255))
        menu_text_rect = menu_text.get_rect()
        menu_text_rect.center = (292, 100)
        bar_text = title_font.render('$', True, (255, 255, 255))
        bar_text_rect = bar_text.get_rect()
        bar_text_rect.center = (292, 110)
        subtitle_font = pygame.font.Font(
            'fonts/Tactical Espionage Action.ttf', 16)
        credit = subtitle_font.render('Based on Konami game series',
                                      True, (255, 255, 255))
        subtitle_text = subtitle_font.render('Pong', True, (0, 0, 0),
                                             (255, 255, 255))
        subtitle_text_rect = subtitle_text.get_rect()
        subtitle_text_rect.center = (292, 140)
        play_font = pygame.font.Font('fonts/MGS2MENU.TTF', 20)
        text_1 = 'PLAY'
        text_2 = 'CONTROLS'
        text_3 = 'EXIT'
        text_1 = play_font.render(text_1, True, (255, 255, 255))
        text_2 = play_font.render(text_2, True, (255, 255, 255))
        text_3 = play_font.render(text_3, True, (255, 255, 255))
        text_1_rect = text_1.get_rect()
        text_2_rect = text_2.get_rect()
        text_3_rect = text_3.get_rect()
        text_1_rect.center = (292, 234)
        text_2_rect.center = (292, 264)
        text_3_rect.center = (292, 294)
        # Get the mouse position and verifies collision with buttons
        pos_mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_1_rect.collidepoint(pos_mouse):
                    MetalSnake.play_game()
                    click = False
                if text_2_rect.collidepoint(pos_mouse):
                    Controls.access_controls()
                    click = False
                if text_3_rect.collidepoint(pos_mouse):
                    pygame.quit()
                    sys.exit()
            # Spawn objects on screen
            window.blit(credit, (10, 448))
            window.blit(menu_text, menu_text_rect)
            window.blit(bar_text, bar_text_rect)
            window.blit(subtitle_text, subtitle_text_rect)
            window.blit(text_1, text_1_rect)
            window.blit(text_2, text_2_rect)
            window.blit(text_3, text_3_rect)
            pygame.display.update()


if __name__ == '__main__':
    access_menu()
