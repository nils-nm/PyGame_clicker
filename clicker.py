# IMPORT----------------------------------------------------------------------------------------------------------------


import pygame

pygame.init()


# CONSTANTS-------------------------------------------------------------------------------------------------------------


a = False
aa = False
b = False

WIGHT = 500
HEIGHT = 500
FPS = 60
screen = pygame.display.set_mode((WIGHT, HEIGHT))
clock = pygame.time.Clock()

fontOBJ = pygame.font.Font(None, 30)

run = True

score = 0
bust = 100
BUST = False
time = 60
TIME = False
time2 = 40
TIME2 = False

x1 = 5
y1 = 5
x2 = 45
y2 = 5
xb = 5
yb = 45
xt1 = 5
yt1 = 70
xt2 = 45
yt2 = 70

r = 10


# COLORS----------------------------------------------------------------------------------------------------------------


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# FUNCTIONS-------------------------------------------------------------------------------------------------------------


def draw(g_text, text, x, y, value, t):
    g_text = g_text
    text = text
    if g_text == 1:
        game_text = fontOBJ.render(str(value), True, green)
        screen.blit(game_text, (x, y))
    if text == 1:
        text_score = fontOBJ.render(str(t) + " " + str(value), True, red)
        screen.blit(text_score, (x, y))

# GAME------------------------------------------------------------------------------------------------------------------


while run:

    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    pygame.draw.rect(screen, (0, 0, 0), (0, 400, 500, 200))

    draw(0, 1, 0, 485, score, "score:")
    if aa is True:
        draw(0, 1, 0, 455, bust, "bust:")
    if a is True:
        draw(0, 1, 0, 425, time, "auto_1:")
    if b is True:
        draw(0, 1, 0, 425, time2, "auto_2:")
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_q]:
            run = False
        if score >= 0:
            draw(1, 0, x1, x1, 1, 0)
        if score >= 1000:
            draw(1, 0, x2, y2, 5, 0)
        if score >= 100 and BUST is False:
            draw(1, 0, xb, yb, "B", 0)
        if score >= 2000 and TIME is False:
            draw(1, 0, xt1, yt1, "A1", 0)
        if score >= 5 and TIME2 is False:
            draw(1, 0, xt2, yt2, "A2", 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x1 - 5) ** 2 + (event.pos[1] - y1 - 5) ** 2 < (r ** 2):
                score += 1
                if BUST is True:
                    bust -= 1

        if score >= 1000 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (event.pos[0] - x2 - 5) ** 2 + (event.pos[1] - y2 - 5) ** 2 < (r ** 2):
                score += 5

        if score >= 100 and event.type == pygame.MOUSEBUTTONDOWN and BUST is False:
            if (event.pos[0] - xb - 5) ** 2 + (event.pos[1] - yb - 5) ** 2 < (r ** 2):
                score -= 100
                aa = True
                screen.fill((0, 0, 0))
                BUST = True
        if score >= 2000 and event.type == pygame.MOUSEBUTTONDOWN and TIME is False:
            if (event.pos[0] - xt1 - 5) ** 2 + (event.pos[1] - yt1 - 5) ** 2 < (r ** 2):
                TIME = True
                a = True
                score -= 1500
                screen.fill((0, 0, 0))
        if score >= 5 and event.type == pygame.MOUSEBUTTONDOWN and TIME2 is False:
            if (event.pos[0] - xt2 - 5) ** 2 + (event.pos[1] - yt2 - 5) ** 2 < (r ** 2):
                TIME2 = True
                a = False
                b = True
                score -= 0
                screen.fill((0, 0, 0))

        if BUST is True:
            if bust <= 0:
                score += 50
                bust += 100

    if TIME is True:
        time -= 1
        if time <= 0:
            time = 60
            score += 1
    if TIME2 is True:
        TIME = False
        time2 -= 1
        if time2 <= 0:
            score += 1
            time2 = 30

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
