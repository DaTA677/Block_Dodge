from config import *
from block import Block
from player import Player
from coin import Coin
from random import randrange
import pygame

class Game:

    def __init__(self):
        self.__window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        pygame.display.set_caption("Block Dodge")
        self.__clock = pygame.time.Clock()
        self.__current_bg_music = BG_MUSIC1
        self.__is_running = True
        self.__is_playing = True
        self.__player = Player(PLAYER_START["x"],PLAYER_START["y"],BLOCK_WIDTH,BLOCK_HEIGHT,PLAYER_SPEED,RED)
        self.__blocks =[]
        self.__block_count=WIN_WIDTH//(BLOCK_WIDTH)
        for i in range(self.__block_count):
            self.__blocks.append(Block((i*BLOCK_WIDTH)+5,FONT_SIZE,BLOCK_WIDTH,BLOCK_HEIGHT,BLOCK_SPEED))
        self.__unactivated_blocks =[]
        for i in self.__blocks:
            self.__unactivated_blocks.append(i)
        self.__coin = Coin((WIN_WIDTH//BLOCK_WIDTH+15)* randrange(0,WIN_WIDTH//BLOCK_WIDTH+15),FONT_SIZE-BLOCK_HEIGHT,BLOCK_WIDTH,BLOCK_HEIGHT,COIN_SPEED,YELLOW)
        self.__time = 0
        self.__frame_count= 0
        self.__level = 1
        self.__score = 0
        self.__text_font=pygame.font.Font(FONT,FONT_SIZE)

    def change_bg_music(self, music_file):
        if music_file==self.__current_bg_music:
            return

        self.__current_bg_music=music_file
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.__current_bg_music)
        pygame.mixer.music.play(-1)

    def increase_difficulty(self):
        for block in self.__blocks:
            block.velocity *= 1.1 + (0.1 * randrange(0,3))
        self.__player.velocity *= (1 + (0.5 if (self.__time%(LEVEL_DURATION*2))==0 else 0))
        self.__coin.velocity *= (1 + (0.5 if (self.__time%(LEVEL_DURATION*2))==0 else 0))

        self.__level+=1

        self.change_bg_music(BG_MUSIC2)

    
    def initialise_game(self):
        self.__coin.reset((WIN_WIDTH//BLOCK_WIDTH+15)* randrange(0,WIN_WIDTH//BLOCK_WIDTH+15),FONT_SIZE-BLOCK_HEIGHT)
        self.__player.reset(PLAYER_START["x"],PLAYER_START["y"])
        if(len(self.__blocks)==self.__block_count):
            for i in self.__blocks:
                i.reset(i.get_x(),FONT_SIZE)

        elif(len(self.__blocks)>self.__block_count):
            for i in range(self.__block_count):
                self.__blocks[i].reset((i*BLOCK_WIDTH)+(5*((WIN_WIDTH//BLOCK_WIDTH)-self.__block_count+1)),FONT_SIZE)
            while(self.__block_count<len(self.__blocks)):
                self.__blocks.pop(self.__block_count)
                self.__block_count+=1
        else:

            for i in range(len(self.__blocks)):
                self.__blocks[i].reset((i*BLOCK_WIDTH)+(5*((WIN_WIDTH//BLOCK_WIDTH)-self.__block_count+1)),FONT_SIZE)
            for i in range(len(self.__blocks),self.__block_count):
                self.__blocks.append(Block((i*BLOCK_WIDTH)+5,FONT_SIZE,BLOCK_WIDTH,BLOCK_HEIGHT,BLOCK_SPEED))

        self.__unactivated_blocks.clear()
        for i in self.__blocks:
            self.__unactivated_blocks.append(i)


        self.__time=0
        self.__frame_count=0
        self.__score=0
        self.__is_playing=True
        self.__level=1
        self.change_bg_music(BG_MUSIC1)

    def redraw_game_window(self):
        #Needed to ensure that previous rects dont appear on the screen
        self.__window.fill(BLACK)
        
        #displaying blocks
        for i in self.__blocks:
            if i.is_activated():
                pygame.draw.rect(self.__window, i.get_colour(), i.get_draw_dimensions())
        
        #displaying coin
        if self.__coin.is_activated():
            pygame.draw.rect(self.__window,self.__coin.get_colour(),self.__coin.get_draw_dimensions())

        #Displaying clock on the screen
        text=self.__text_font.render(f"{self.__time}",False,WHITE,BLACK)
        text_rect=text.get_rect()
        text_rect.center= (WIN_WIDTH//2, FONT_SIZE//2)
        self.__window.blit(text,text_rect)
        #Display score
        text=self.__text_font.render(f"Score:{self.__score}",False,YELLOW,BLACK)
        text_rect=text.get_rect()
        text_rect.center= (WIN_WIDTH-100, FONT_SIZE//2)
        self.__window.blit(text,text_rect)
        #Display level
        text = self.__text_font.render(f"Level:{self.__level}",False,WHITE,BLACK)
        self.__window.blit(text,(10,0))

        #Creates a rectangle -- pygame window, colour, (startx,starty,endx,endy)
        pygame.draw.rect(self.__window, self.__player.get_colour(), self.__player.get_draw_dimensions())

        #updates the screen to show the changes(like drawing the rectangle)
        pygame.display.update() 

    def check_collisions(self):
        if self.__coin.check_collision(self.__player):
            self.__coin.reset((WIN_WIDTH//BLOCK_WIDTH+15)* randrange(0,WIN_WIDTH//BLOCK_WIDTH+15), 0)
            self.__score+=100
        
        for i in self.__blocks:
            if i.check_collision(self.__player):
                self.__is_playing=False
                #print("Collision occured")
                return
            
    def play_bg_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.__current_bg_music)
            pygame.mixer.music.play(-1)
    
    def get_running(self):
        return self.__is_running

    def update(self):
        self.__clock.tick(60)

        #handles pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running=False
        
        #Handles keyboard inputs
        keys= pygame.key.get_pressed()

        if self.__is_playing:
            self.__frame_count+=1
            if(self.__frame_count>=FPS):
                self.__time+=1
                self.__frame_count=0
                self.__score+=self.__level

            if((not self.__coin.is_activated()) and self.__time%5<=1):
                self.__coin.activate()

            if(len(self.__unactivated_blocks)>0 and self.__time%3==0 and self.__frame_count==0):
                index=randrange(0,len(self.__unactivated_blocks))
                self.__unactivated_blocks[index].activate()
                self.__unactivated_blocks.pop(index)

            if(self.__frame_count==0 and self.__time>=LEVEL_DURATION and self.__time%LEVEL_DURATION ==0):
                self.increase_difficulty()
                
            
            #processing inputs
            self.__player.handle_inputs(keys)
            
            self.__coin.update()
            
            for i in self.__blocks:
                i.update()

            self.check_collisions()
            self.redraw_game_window()
        
        else:
            if keys[pygame.K_q]:
                pygame.quit()
                self.__is_running=False
            elif keys[pygame.K_r]:
                self.initialise_game()


   