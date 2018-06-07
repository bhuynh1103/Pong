from pygame.draw import *
from constants import *
from random import uniform, choice


class Puck:
    def __init__(self):
        self.w = (boardHeight * .2) // 8
        self.x = boardWidth // 2 - self.w // 2
        self.y = boardHeight // 2 - self.w // 2 + GUISize
        self.xspeed = choice([-1, 1])
        self.yspeed = uniform(-1, 1)
        self.speed = 5

    def draw(self, window):
        rect(window, white, (self.x, self.y, self.w, self.w))

    def move(self):
        self.x += self.xspeed * self.speed
        self.y += self.yspeed * self.speed

    def bounce(self, yspeed):
        self.yspeed = yspeed
        self.xspeed *= -1

    def collide(self, other):
        myTop = self.y
        myRight = self.x + self.w
        myBottom = self.y + self.w
        myLeft = self.x

        otherTop = other.y
        otherRight = other.x + other.w
        otherBottom = other.y + other.h
        otherLeft = other.x

        if myTop > otherBottom:
            return False
        elif myRight < otherLeft:
            return False
        elif myBottom < otherTop:
            return False
        elif myLeft > otherRight:
            return False
        else:
            return True
