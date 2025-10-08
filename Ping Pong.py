import pygame as pg
import sys
import random as r
import time

screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
pg.display.set_caption("Ping Pong")

#player1, player2
player1 = pg.Rect(20, 250, 10, 40)
player2 = pg.Rect(480, 250, 10, 40)

ball = pg.Rect(250, 250, 10, 10)

#The walls (borders)
wallYT = pg.Rect(0, 0, 500, 10)
wallYB = pg.Rect(0, 490, 500, 10)
wallXR = pg.Rect(490, 0, 10, 500)
wallXL = pg.Rect(0, 0, 10, 500)

#The Displayable lives
Live11 = pg.Rect(5, 5, 10, 10)
Live12 = pg.Rect(20, 5, 10, 10)
Live13 = pg.Rect(35, 5, 10, 10)
Live14 = pg.Rect(50, 5, 10, 10)
Live15 = pg.Rect(65, 5, 10, 10)

Live21 = pg.Rect(425, 5, 10, 10)
Live22 = pg.Rect(440, 5, 10, 10)
Live23 = pg.Rect(455, 5, 10, 10)
Live24 = pg.Rect(470, 5, 10, 10)
Live25 = pg.Rect(485, 5, 10, 10)

#Variabels
BspeedX = 5
BspeedY = 0

speedY = 5

LivesP1 = 5
LivesP2 = 5



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()
    #Player movement
    if keys[pg.K_w]:
        player1.y = player1.y - speedY
    if keys[pg.K_s]:
        player1.y = player1.y + speedY

    if keys[pg.K_UP]:
        player2.y = player2.y - speedY
    if keys [pg.K_DOWN]:
        player2.y = player2.y + speedY
    #Ball movement
    ball.x = ball.x + BspeedX
    ball.y = ball.y + BspeedY

    #Made bg clr
    screen.fill((0, 0, 0))

    #Collisions: (Ball, players, walls)
    if player1.colliderect(ball):
        BspeedX = 5
        BspeedY = r.randint(-3, 3)
    if player2.colliderect(ball):
        BspeedX = -5
        BspeedY = r.randint(-3, 3)
    if ball.colliderect(wallYT):
        BspeedY = BspeedY + 5
    if ball.colliderect(wallYB):
        BspeedY = BspeedY - 5

    if LivesP1 == 5:
        pg.draw.rect(screen, (150, 0, 0), Live15)
        pg.draw.rect(screen, (150, 0, 0), Live14)
        pg.draw.rect(screen, (150, 0, 0), Live11)
        pg.draw.rect(screen, (150, 0, 0), Live12)
        pg.draw.rect(screen, (150, 0, 0), Live13)
        if ball.colliderect(wallXL):
            time.sleep(1)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            LivesP1 = 4
    if LivesP1 == 4:
        pg.draw.rect(screen, (150, 0, 0), Live14)
        pg.draw.rect(screen, (150, 0, 0), Live11)
        pg.draw.rect(screen, (150, 0, 0), Live12)
        pg.draw.rect(screen, (150, 0, 0), Live13)
        if ball.colliderect(wallXL):
            time.sleep(1)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            LivesP1 = 3
    if LivesP1 == 3:
        pg.draw.rect(screen, (150, 0, 0), Live11)
        pg.draw.rect(screen, (150, 0, 0), Live12)
        pg.draw.rect(screen, (150, 0, 0), Live13)
        if ball.colliderect(wallXL):
            time.sleep(1)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            LivesP1 = 2
    if LivesP1 == 2:
        pg.draw.rect(screen, (150, 0, 0), Live11)
        pg.draw.rect(screen, (150, 0, 0), Live12)
        if ball.colliderect(wallXL):
            time.sleep(1)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            LivesP1 = 1
    if LivesP1 == 1:
        pg.draw.rect(screen, (150, 0, 0), Live11)
        if ball.colliderect(wallXL):
            time.sleep(2)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            LivesP1 = 0
            pg.quit()
            sys.exit()

    if LivesP2 == 5:
        pg.draw.rect(screen, (150, 0, 0), Live21)
        pg.draw.rect(screen, (150, 0, 0), Live22)
        pg.draw.rect(screen, (150, 0, 0), Live23)
        pg.draw.rect(screen, (150, 0, 0), Live24)
        pg.draw.rect(screen, (150, 0, 0), Live25)
        if ball.colliderect(wallXR):
            time.sleep(1)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            LivesP2 = 4
    if LivesP2 == 4:
        pg.draw.rect(screen, (150, 0, 0), Live21)
        pg.draw.rect(screen, (150, 0, 0), Live22)
        pg.draw.rect(screen, (150, 0, 0), Live23)
        pg.draw.rect(screen, (150, 0, 0), Live24)
        if ball.colliderect(wallXR):
            time.sleep(1)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            LivesP2 = 3
    if LivesP2 == 3:
        pg.draw.rect(screen, (150, 0, 0), Live21)
        pg.draw.rect(screen, (150, 0, 0), Live22)
        pg.draw.rect(screen, (150, 0, 0), Live23)
        if ball.colliderect(wallXR):
            time.sleep(1)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            LivesP2 = 2
    if LivesP2 == 2:
            pg.draw.rect(screen, (150, 0, 0), Live21)
            pg.draw.rect(screen, (150, 0, 0), Live22)
            if ball.colliderect(wallXR):
                time.sleep(1)
                player1.y = 250
                player2.y = 250
                ball.x = 250
                ball.y = 250
                BspeedX = 5
                BspeedY = 0
                LivesP2 = 1
    if LivesP2 == 1:
        pg.draw.rect(screen, (150, 0, 0), Live21)
        if ball.colliderect(wallXR):
            time.sleep(2)
            player1.y = 250
            player2.y = 250
            ball.x = 250
            ball.y = 250
            BspeedX = 5
            BspeedY = 0
            pg.quit()
            sys.exit()
        

    
    #Draw all the rectangles to screen (exept for the lives)
    pg.draw.rect(screen, (200, 0, 0), player1)
    pg.draw.rect(screen, (200, 0, 0), player2)
    
    pg.draw.rect(screen, (0, 0, 200), ball)
    
    pg.draw.rect(screen, (0, 200, 0), wallYT)
    pg.draw.rect(screen, (0, 200, 0), wallYB)
    pg.draw.rect(screen, (0, 200, 0), wallXR)
    pg.draw.rect(screen, (0, 200, 0), wallXL)

    #Flipped display
    pg.display.flip()

    #FPS SET TO 60
    clock.tick(60)
