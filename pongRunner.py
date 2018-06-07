import pygame, sys
from pygame.locals import *
from constants import *
from paddle import *
from puck import *
from numbers import *

pygame.init()
pygame.key.set_repeat(1)
screen = pygame.display.set_mode((boardWidth, boardHeight))


def winCondition():
    if leftPaddle.score == 10 or rightPaddle.score == 10:
        return True
    else:
        return False


def keyPressed(paddle, up, down):
    keys = pygame.key.get_pressed()

    if keys[up]:
        paddle.move(-1)
    elif keys[down]:
        paddle.move(1)
    else:
        paddle.move(0)


while True:
    # Setup Code

    leftPaddle = Paddle(boardWidth * .01)
    rightPaddle = Paddle(boardWidth - boardWidth * .01 - boardWidth * .02)

    puck = Puck()

    leftScore = Numbers(boardWidth * .25, GUISize * .1, GUISize * .8)
    rightScore = Numbers(boardWidth * .75, GUISize * .1, GUISize * .8)

    gameover = False
    setup = False

    while not setup:
        while not gameover:
            # Game code
            screen.fill(black)

            leftPaddle.draw(screen)
            rightPaddle.draw(screen)

            puck.draw(screen)
            puck.move()

            if puck.collide(leftPaddle):
                leftPaddle.hit(puck)
                puck.x = leftPaddle.x + leftPaddle.w
                puck.speed += .25
                # print(puck.speed)

            if puck.collide(rightPaddle):
                rightPaddle.hit(puck)
                puck.x = rightPaddle.x - leftPaddle.w
                puck.speed += .25
                # print(puck.speed)

            # Edge bouncing and scoring
            if puck.y < GUISize:
                puck.y = GUISize
                puck.yspeed *= -1
            elif puck.y + puck.w > boardHeight:
                puck.y = boardHeight - puck.w
                puck.yspeed *= -1
            elif puck.x < 0:
                puck.x = 0
                rightPaddle.score += 1
                puck.xspeed *= -1
                puck.speed = 5
            elif puck.x + puck.w > boardWidth:
                puck.x = boardWidth - puck.w
                leftPaddle.score += 1
                puck.xspeed *= -1
                puck.speed = 5

            if winCondition():
                gameover = True

            # GUI
            leftScore.draw(screen, leftPaddle.score)
            rightScore.draw(screen, rightPaddle.score)

            lineThickness = boardHeight * .01
            pygame.draw.line(screen, white, (0, GUISize), (boardWidth, GUISize), int(lineThickness))
            pygame.draw.line(screen, white, (0, boardHeight), (boardWidth, boardHeight), int(lineThickness * 2))

            a = GUISize
            while a < boardWidth:
                width = boardWidth// 32
                b = a + width
                pygame.draw.line(screen, white, (boardWidth // 2, a), (boardWidth // 2, b), int(lineThickness))

                a += width * 2

            pygame.display.update()

            # Input loop
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                keyPressed(leftPaddle, K_w, K_s)
                keyPressed(rightPaddle, K_w, K_s)

        # Gameover loop
        screen.fill(black)

        leftPaddle.draw(screen)
        rightPaddle.draw(screen)

        leftScore.draw(screen, leftPaddle.score)
        rightScore.draw(screen, rightPaddle.score)

        lineThickness = boardHeight * .01
        pygame.draw.line(screen, white, (0, GUISize), (boardWidth, GUISize), int(lineThickness))
        pygame.draw.line(screen, white, (0, boardHeight), (boardWidth, boardHeight), int(lineThickness * 2))


        writeText(screen, "Gameover! Press 'ENTER' to play again!", white, boardWidth // 2, boardHeight // 2 + GUISize, boardHeight * .075)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_RETURN:
                gameover = False
                setup = True
