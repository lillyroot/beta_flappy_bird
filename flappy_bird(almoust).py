from random import *
import pygame
pygame.init()

width, height = 900, 600
fps = 70
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
bird_x = width // 6
bird_y = height // 2
bird = pygame.Rect(bird_x, bird_y, 50, 50)
tube1 = pygame.Rect(width, -300, 100, 550)
tube2 = pygame.Rect(width, 400, 100, 650)
tube_x = width
tubes = [tube1, tube2]
playing = True
play = False
cause = random
score = 0
font_name = pygame.font.match_font('arial')
bg = pygame.image.load('bg.jpg')


def tubes_position():
    tube1.x = tube_x
    tube2.x = tube_x
    tube1.y = -300
    tube2.y = 400


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, 'white')
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    good_actions = pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[pygame.K_SPACE]

    if not play:
        bird_y = height // 2
    if good_actions:
        play = True
        bird_y -= 5
    else:
        bird_y += 5

    if bird.top < 0 or bird.bottom > height:
        bird_y = height // 2
        play = False

    bird.y = bird_y

    screen.blit(bg, (0, 0))

    if play:
        for tube in tubes:
            pygame.draw.rect(screen, 'green', tube)
            tube.x -= 5
            if cause:
                tube.y += 1
            else:
                tube.y -= 1
            if tube2.x == -100:
                cause = not cause
                tubes_position()
    else:
        cause = not cause
        tubes_position()

    if bird.colliderect(tube1) or bird.colliderect(tube2):
        play = False

    pygame.draw.rect(screen, 'yellow', bird)
    clock.tick(fps)
    pygame.display.update()

