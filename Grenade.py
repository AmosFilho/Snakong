import pygame

pygame.init()


# Create a new grenade
def make_grenade(lis):
    grenade = {'ball_x': 282, 'ball_y': 234, 'ball_dx': 1, 'ball_dy': 1}
    lis.append(grenade)


# Move any balls and return new coordinates
def move_ball(ball_x, ball_y, ball_dx, ball_dy):
    ball_speed = 10
    ball_x += ball_speed * ball_dx
    ball_y += ball_speed * ball_dy
    if ball_y >= 448:
        ball_dy *= -1
    if ball_y <= 20:
        ball_dy *= -1
    if ball_x <= 0:
        ball_dx *= -1
    if ball_x >= 544:
        ball_dx *= -1
    grenades = {'ball_x': ball_x, 'ball_y': ball_y,
                'ball_dx': ball_dx, 'ball_dy': ball_dy}
    return grenades
