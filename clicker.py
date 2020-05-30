# IMPORT----------------------------------------------------------------------------------------------------------------


import pygame

pygame.init()


# CONSTANTS-------------------------------------------------------------------------------------------------------------


WIGHT = 500
HEIGHT = 500
FPS = 60
screen = pygame.display.set_mode((WIGHT, HEIGHT))
clock = pygame.time.Clock()

fontOBJ = pygame.font.Font(None, 30)

run = True

score = 0
bust = 20
BUST = False

x1 = 10
y1 = 10
x2 = 50
y2 = 10
xb = 10
yb = 50

r = 10


# COLORS----------------------------------------------------------------------------------------------------------------


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# FUNCTIONS-------------------------------------------------------------------------------------------------------------


def draw(circle, text, x, y, value):
    circle = circle
    text = text
    if circle == 1:
        pygame.draw.circle(screen, green, (x, y), r)
    if text == 1:
        text_score = fontOBJ.render(str(value), True, red)
        screen.blit(text_score, (x, y))

# GAME------------------------------------------------------------------------------------------------------------------


while run:
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    draw(0, 1, 0, 485, score)
    # draw(0, 1, 0, 455, bust)
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_q]:
            run = False
        if score >= 0:
            draw(1, 0, x1, x1, 0)
        if score >= 50:
            draw(1, 0, x2, y2, 0)
        if score >= 100 and BUST is False:
            draw(1, 0, xb, yb, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2 < (r ** 2):
                score += 1
                if BUST is True:
                    bust -= 1
                screen.fill((0, 0, 0))
        if score >= 50 and event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x2) ** 2 + (event.pos[1] - y2) ** 2 < (r ** 2):
                score += 5
                if BUST is True:
                    bust -= 5
                screen.fill((0, 0, 0))
        if score >= 100 and event.type == pygame.MOUSEBUTTONDOWN and BUST is False:
            if (event.pos[0] - xb) ** 2 + (event.pos[1] - yb) ** 2 < (r ** 2):
                score -= 100
                screen.fill((0, 0, 0))
                pygame.display.flip()
                BUST = True
        if BUST is True:
            if bust == 0:
                score += 20
                bust += 20

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
