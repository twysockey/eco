
import pygame
from pygame.locals import *
from player import Player
from block import Block

import pygame
import random
import time
import random
class game:
    def __init__(self,debug):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1080, 1920
        self.width=1920
        self.height=1080
        self.playerQuit=False

    def ApplyGravity(self,all_sprites_list):
        for sprite in all_sprites_list:
            if(sprite.gravity==True):
                sprite.rect.y+=2
        time.sleep(0.01)

    def ClimbObsticle(self,player,block_list):
        blocks_hit = pygame.sprite.spritecollide(player, block_list,False)
        for hit_block in blocks_hit:
            if(player.rect.y+player.height < hit_block.rect.y or
                player.rect.y < hit_block.rect.y+player.height
                ):
                player.rect.y = hit_block.rect.y-player.height
    def run(self):

        BLACK = ( 27, 100,  142)
        WHITE = (27, 100,142 )
        RED  = (255,   255,  255)
        pygame.init()

        screen_width = 1920
        screen_height = 1080
        screen = pygame.display.set_mode([screen_width, screen_height])

        player = Player(RED, 10, 15)
        player.rect.y=screen_height/5

        subblocks_list = pygame.sprite.Group()

        block_list = pygame.sprite.Group()

        all_sprites_list = pygame.sprite.Group()

        lag = screen_height/4
        for i in range(int(screen_width/player.width)):
            # This represents a block
            block = Block(BLACK, 20, 215)

            # Set a random location for the block
            block.rect.x = i*block.width
            block.rect.y = (lag-15) + random.randrange(40)
            height=block.rect.y
            while(height < screen_height ):
                subblock = Block(BLACK, 60, 60)
                subblock.rect.x=block.rect.x
                height = height + subblock.height
                subblock.rect.y= height
                subblocks_list.add(subblock)
                all_sprites_list.add(subblock)


            lag = block.rect.y
            # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)

        all_sprites_list.add(player)

        done = False
        clock = pygame.time.Clock()
        back_ground= pygame.image.load("Memes.jpg")
        pygame.mixer.music.load("Cod.mp3.mp3")

        pygame.mixer.music.play(10,0.0)

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # Clear the screen
            screen.blit(back_ground, [0,0])
            self.ApplyGravity(all_sprites_list)
            self.ClimbObsticle(player,block_list)

            keys=pygame.key.get_pressed()
            player.flush()
            if keys[K_LEFT]:
                player.moveleft(screen_width)

            if keys[K_RIGHT]:
                player.moveright(screen_width)

            # Get the current mouse position. This returns the position
            # as a list of two numbers.
            '''pos = pygame.mouse.get_pos()

            # Fetch the x and y out of the list,
               # just like we'd fetch letters out of a string.
            # Set the player object to the mouse location

            player.rect.x = pos[0]
            player.rect.y = pos[1]
            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

            # Check the list of collisions.
            for block in blocks_hit_list:
                score += 1
                print(score)
            '''
            # Draw all the spites that may need to be drawn
            all_sprites_list.draw(screen)



            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 60 frames per second
            clock.tick(60)
        pygame.quit()
#############################################
if __name__ == "__main__" :
    theApp = game(False)

#this is the game code containing the game loop and all apspects of controls
