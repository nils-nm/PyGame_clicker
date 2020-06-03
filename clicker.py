# IMPORT----------------------------------------------------------------------------------------------------------------


import pygame

pygame.init()


# CONSTANTS-------------------------------------------------------------------------------------------------------------


a = False
aa = False
aaa = False
b = False
bb = False
bbb = True

info = False

WIGHT = 500
HEIGHT = 500
FPS = 60
screen = pygame.display.set_mode((WIGHT, HEIGHT))
clock = pygame.time.Clock()

fontOBJ = pygame.font.Font(None, 30)
fontOBJ1 = pygame.font.Font(None, 25)

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


def draw(g_text, text, x, y, value, t, version):
    g_text = g_text
    text = text
    if g_text == 1:
        game_text = fontOBJ.render(str(value), True, green)
        screen.blit(game_text, (x, y))
    if text == 1:
        text_score = fontOBJ.render(str(t) + " " + str(value), True, red)
        screen.blit(text_score, (x, y))
    if version == 1:
        version_text = fontOBJ1.render(str(value) + " " + str(t), False, green)
        screen.blit(version_text, (x, y))

# GAME------------------------------------------------------------------------------------------------------------------


while run:

    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    if bb is False:
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 500, 500))
        draw(0, 1, 10, 10, "", "click on the 'i' button to exit the info", 0)
        pygame.draw.line(screen, (25, 20, 50), (0, 30), (500, 30), 3)
        draw(0, 1, 10, 40, "", "click on the numbers to get points", 0)
        pygame.draw.line(screen, (25, 20, 50), (0, 60), (500, 60), 3)
        draw(0, 1, 10, 70, "", "B = every 100 clicks on the '1' gives you 50 points", 0)
        draw(0, 1, 10, 100, "", "it costs: 100 points", 0)
        pygame.draw.line(screen, (25, 20, 50), (0, 120), (500, 120), 3)
        draw(0, 1, 10, 130, "", "A1 and A2 = gives points automatically", 0)
        draw(0, 1, 10, 160, "", "it costs: 2000 and 5000 points", 0)
        pygame.draw.line(screen, (25, 20, 50), (0, 180), (500, 180), 3)
    if keys[pygame.K_i]:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        bb = True
        aa = True
    if bb is True:
        pygame.draw.rect(screen, (0, 0, 0), (0, 400, 500, 200))
        draw(0, 0, 350, 475, "BETA", "version 0.4", 1)
    if aa is True:
        draw(0, 1, 0, 485, score, "score:", 0)
    if aaa is True:
        draw(0, 1, 0, 455, bust, "bust:", 0)
    if a is True:
        draw(0, 1, 0, 425, time, "auto_1:", 0)
    if b is True:
        draw(0, 1, 0, 425, time2, "auto_2:", 0)
    if bb is True:
        for event in events:

            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_q]:
                run = False
            if score >= 0:
                draw(1, 0, x1, x1, 1, 0, 0)
            if score >= 1000:
                draw(1, 0, x2, y2, 5, 0, 0)
            if score >= 100 and BUST is False:
                draw(1, 0, xb, yb, "B", 0, 0)
            if score >= 2000 and TIME is False and TIME2 is False:
                draw(1, 0, xt1, yt1, "A1", 0, 0)
            if score >= 5000 and TIME2 is False:
                draw(1, 0, xt2, yt2, "A2", 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                    aaa = True
                    screen.fill((0, 0, 0))
                    BUST = True
            if score >= 2000 and event.type == pygame.MOUSEBUTTONDOWN and TIME is False:
                if (event.pos[0] - xt1 - 5) ** 2 + (event.pos[1] - yt1 - 5) ** 2 < (r ** 2):
                    TIME = True
                    a = True
                    score -= 2000
                    screen.fill((0, 0, 0))

            if score >= 5000 and event.type == pygame.MOUSEBUTTONDOWN and TIME2 is False:
                if (event.pos[0] - xt2 - 5) ** 2 + (event.pos[1] - yt2 - 5) ** 2 < (r ** 2):
                    TIME2 = True
                    a = False
                    b = True
                    score -= 5000
                    screen.fill((0, 0, 0))

            if BUST is True:
                if bust <= 0:
                    score += 50
                    bust += 100

    if TIME is True:
        time -= 1
        if time <= 0:
            time = 60
            score += 2
    if TIME2 is True:
        TIME = False
        time2 -= 1
        if time2 <= 0:
            score += 2
            time2 = 30

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
