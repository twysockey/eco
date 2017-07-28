'''
Use sprites to collect blocks.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/4W2AqUetBi4
'''

import pygame
from block import Block


class Player(Block):

    '''This class represents the ball.
    It derives from the "Sprite" class in Pygame.'''

    def __init__(self, color, width, height):
        #Block.__init__(self, color, width, height)
         super(self.__class__, self,).__init__(color, width, height)
         self.move_ticker = 0
         self.gravity=True
    def moveleft(self,screen_width):
        if self.move_ticker == 0:
            self.move_ticker = 10
            self.rect.x -= self.width*self.speed
            if self.rect.x == -10:
                self.rect.x = 0

    def moveright(self,screen_width):
        if self.move_ticker == 0:
            self.move_ticker = 10
            self.rect.x+=self.width*self.speed
            if self.rect.x >= screen_width:
                self.rect.x = screen_width

    def jump(self):
        #move player up their height

        pass

        pass
    def flush(self):
        self.move_ticker=0
