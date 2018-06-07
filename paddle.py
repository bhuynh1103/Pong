from pygame.draw import *
from constants import *
from random import uniform


class Paddle:
    def __init__(self, x):
        self.w = boardWidth * .02
        self.h = boardHeight * .2
        self.x = x
        self.y = (boardHeight // 2) - self.h // 2 + GUISize
        self.score = 0

    def draw(self, window):
        rect(window, white, (self.x, self.y, self.w, self.h))

    def move(self, direction):
        self.y += paddleSpeed * direction

        if self.y < GUISize + self.w:
            self.y = GUISize + self.w
        elif self.y + self.h > boardHeight - self.w:
            self.y = boardHeight - self.h - self.w

    def hit(self, puck):
        interval = self.h // 8
        y = puck.y

        if self.y <= y < self.y + interval or self.y <= y + puck.w < self.y + interval or self.y > puck.y + puck.w:
            # print(-3)
            puck.bounce(-1)
        elif self.y + interval * 1 <= y < self.y + interval * 2:
            # print(-2)
            puck.bounce(-2/3)
        elif self.y + interval * 2 <= y < self.y + interval * 3:
            # print(-1)
            puck.bounce(-1/3)
        elif self.y + interval * 3 <= y < self.y + interval * 5:
            # print(0)
            puck.bounce(uniform(-1/2, 1/2))
        elif self.y + interval * 5 <= y < self.y + interval * 6:
            # print(1)
            puck.bounce(1/3)
        elif self.y + interval * 6 <= y < self.y + interval * 7:
            # print(2)
            puck.bounce(2/3)
        elif self.y + interval * 7 <= y <= self.y + interval * 8 or self.y + self.h < puck.y:
            # print(3)
            puck.bounce(1)
