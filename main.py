import pygame
# from random import randrange
# from config import *
# from block import Block
# from player import Player
# from coin import Coin
# #needed for any pygame
# pygame.init()


# #creates a window
# window= pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))#the tuple determines the dimensions
# #determines the title bar text
# pygame.display.set_caption("First Game")
# #Creates a clock
# clock =pygame.time.Clock()


# text_font=pygame.font.Font(FONT,FONT_SIZE)
# time=0
# frame_count=0

# score=0

# level=1
# #timer = f"{time}"

# #initialises music and sound unit
# pygame.mixer.init()
# #set the current bg music
# current_bg_music=BG_MUSIC1
# #Setup background music
# pygame.mixer.music.load(current_bg_music)

# x=50
# y=WIN_HEIGHT-100
# width=40
# height=60
# vel=60

# # player= Block(x,y,width,height,vel*3,RED)
# player= Player(x,y,width,height,PLAYER_SPEED,RED)


# running=True
# playing=True

# difficulty_increased=False


# #creating blocks
# blocks=[]
# for i in range(WIN_WIDTH//(width)):
#     blocks.append(Block((i*width)+5,FONT_SIZE,width,height,BLOCK_SPEED))

# #used to show blocks one at a time
# unactivated_blocks=[]
# for i in blocks:
#     unactivated_blocks.append(i)

# #creating coins
# coin = Coin((WIN_WIDTH//width+15)* randrange(0,WIN_WIDTH//width+15),FONT_SIZE-height,width,height,COIN_SPEED,YELLOW)


# def change_bg_music(music_file):
#     global current_bg_music
#     if music_file==current_bg_music:
#         return

#     current_bg_music=music_file
#     pygame.mixer.music.stop()
#     pygame.mixer.music.load(current_bg_music)
#     pygame.mixer.music.play(-1)

# def increase_difficulty():
#     global blocks
#     global player
#     global coin
#     global time
#     for block in blocks:
#         block.velocity*=1.5

#     player.velocity *= (1 + (0.5 if (time%(LEVEL_DURATION*2))==0 else 0))
#     coin.velocity  *= (1 + (0.5 if (time%(LEVEL_DURATION*2))==0 else 0))

#     change_bg_music(BG_MUSIC2)    

# def initialise_game(player,x,y,width,height,vel,block_count,blocks,unactivated_blocks):
#     global time
#     global frame_count
#     global playing
#     global score
#     global coin
#     global level

#     coin.reset((WIN_WIDTH//width+15)* randrange(0,WIN_WIDTH//width+15),FONT_SIZE-height)
#     player.reset(x,y)
#     if(len(blocks)==block_count):
#         for i in blocks:
#             i.reset(i.get_x(),FONT_SIZE)

#     elif(len(blocks)>block_count):
#         for i in range(block_count):
#             blocks[i].reset((i*width)+(5*((WIN_WIDTH//width)-block_count+1)),FONT_SIZE)
#         while(block_count<len(blocks)):
#             blocks.pop(block_count)
#             block_count+=1
#     else:

#         for i in range(len(blocks)):
#             blocks[i].reset((i*width)+(5*((WIN_WIDTH//width)-block_count+1)),FONT_SIZE)
#         for i in range(len(blocks),block_count):
#             blocks.append(Block((i*width)+5,FONT_SIZE,width,height,vel))

#     unactivated_blocks.clear()
#     for i in blocks:
#         unactivated_blocks.append(i)


#     time=0
#     frame_count=0
#     score=0
#     playing=True
#     level=1
#     change_bg_music(BG_MUSIC1)


# def redraw_game_window():
#     #Needed to ensure that previous rects dont appear on the screen
#     window.fill(BLACK)
    
#     #displaying blocks
#     for i in blocks:
#         if i.is_activated():
#             pygame.draw.rect(window, i.get_colour(), i.get_draw_dimensions())
    
#     #displaying coin
#     if coin.is_activated():
#         pygame.draw.rect(window,coin.get_colour(),coin.get_draw_dimensions())

#     #Displaying clock on the screen
#     text=text_font.render(f"{time}",False,WHITE,BLACK)
#     text_rect=text.get_rect()
#     text_rect.center= (WIN_WIDTH//2, FONT_SIZE//2)
#     window.blit(text,text_rect)

#     text=text_font.render(f"Score:{score}",False,YELLOW,BLACK)
#     text_rect=text.get_rect()
#     text_rect.center= (WIN_WIDTH-100, FONT_SIZE//2)
#     window.blit(text,text_rect)

#     text = text_font.render(f"Level:{level}",False,WHITE,BLACK)
#     window.blit(text,(10,0))

#     #Creates a rectangle -- pygame window, colour, (startx,starty,endx,endy)
#     pygame.draw.rect(window, player.get_colour(), player.get_draw_dimensions())
    
    
    
#     #updates the screen to show the changes(like drawing the rectangle)
#     pygame.display.update()

# def update_blocks():
#     for i in blocks:
#         i.update()
    


# def check_collisions():
#     global playing
    
#     if coin.check_collision(player):
#         coin.reset((WIN_WIDTH//coin.get_width()+15)* randrange(0,WIN_WIDTH//coin.get_width()+15), 0)
#         global score
#         score+=100
    
#     for i in blocks:
#         if i.check_collision(player):
#             playing=False
#             #print("Collision occured")
#             return

# #play background music
# pygame.mixer.music.play(-1)

# while running:

#     clock.tick(FPS)

#     #handles pygame events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running=False
    
#     #Handles keyboard inputs
#     keys= pygame.key.get_pressed()

#     if playing:
#         frame_count+=1
#         if(frame_count==FPS):
#             time+=1
#             frame_count=0
#             score+=1+time//LEVEL_DURATION

#         if((not coin.is_activated()) and time%5<=1):
#             coin.activate()

#         if(len(unactivated_blocks)>0 and time%3==0 and frame_count==0):
#             index=randrange(0,len(unactivated_blocks))
#             unactivated_blocks[index].activate()
#             unactivated_blocks.pop(index)

#         if(frame_count==0 and time>=LEVEL_DURATION and time%LEVEL_DURATION ==0):
#             increase_difficulty()
#             level+=1
        
#         #processing inputs
#         player.handle_inputs(keys)
        
#         coin.update()
#         update_blocks()
#         check_collisions()
#         redraw_game_window()
    
#     else:
#         if keys[pygame.K_q]:
#             pygame.quit()
#             running=False
#         elif keys[pygame.K_r]:
#             initialise_game(player,x,y,width,height,vel*2,WIN_WIDTH//width,blocks,unactivated_blocks)

# #closes the pygame window
# pygame.quit()

from game import Game
if __name__=="__main__":
    pygame.init()
    
    game_window = Game()

    game_window.play_bg_music()
    while(game_window.get_running()):
        game_window.update()
    
    pygame.quit()