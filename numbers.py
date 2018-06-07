from pygame.draw import *
from constants import *


class Numbers:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        self.segments = [True, True, True, True, True, True, True]

    def draw(self, window, num):
        x = self.x
        y = self.y
        w = self.w // 9

        self.segments = [True, True, True, True, True, True, True]

        if num == 0:
            self.segments[6] = False
        elif num == 1:
            self.segments = [False, True, True, False, False, False, False]
        elif num == 2:
            self.segments[5] = False
            self.segments[2] = False
        elif num == 3:
            self.segments[5] = False
            self.segments[4] = False
        elif num == 4:
            self.segments[0] = False
            self.segments[3] = False
            self.segments[4] = False
        elif num == 5:
            self.segments[1] = False
            self.segments[4] = False
        elif num == 6:
            self.segments[1] = False
        elif num == 7:
            self.segments[3] = False
            self.segments[4] = False
            self.segments[5] = False
            self.segments[6] = False
        elif num == 8:
            pass
        elif num == 9:
            self.segments[4] = False
        elif num == 10:
            self.segments[6] = False
            rect(window, white, (x + w * 4 - w * 7, y + w, w, w * 3))
            rect(window, white, (x + w * 4 - w * 7, y + w * 5, w, w * 3))

        if self.segments[0]:
            rect(window, white, (x + w, y, w * 3, w))
        if self.segments[1]:
            rect(window, white, (x + w * 4, y + w, w, w * 3))
        if self.segments[2]:
            rect(window, white, (x + w * 4, y + w * 5, w, w * 3))
        if self.segments[3]:
            rect(window, white, (x + w, y + w * 8, w * 3, w))
        if self.segments[4]:
            rect(window, white, (x, y + w * 5, w, w * 3))
        if self.segments[5]:
            rect(window, white, (x, y + w, w, w * 3))
        if self.segments[6]:
            rect(window, white, (x + w, y + w * 4, w * 3, w))
