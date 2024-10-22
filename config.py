import os
#Screen
WIN_WIDTH=600
WIN_HEIGHT=800
FPS =60

#Assets
ASSET_DIR=".\\Python_Test\\Pygame_Tryout\\Assets"

#Font
FONT =os.path.join(ASSET_DIR,"MonospaceTypewriter.ttf")
FONT_SIZE=32

BG_MUSIC1=os.path.join(ASSET_DIR,"DST-TowerDefenseTheme.mp3")
BG_MUSIC2=os.path.join(ASSET_DIR,"fight.wav")
DASH_SFX=os.path.join(ASSET_DIR,"slime1.wav")


#Colours
GREY=(127,127,127)
BLACK=(0,0,0)
WHITE=(250,250,250)
RED=(250,0,0)
GREEN=(0,250,0)
BLUE=(0,0,250)
YELLOW=(250,250,0)

#Game specific

BLOCK_WIDTH = 40
BLOCK_HEIGHT = 60

PLAYER_SPEED = 180//FPS
BLOCK_SPEED = 120//FPS
COIN_SPEED = 240//FPS

LEVEL_DURATION = 30

PLAYER_START = {"x":50, "y":WIN_HEIGHT-100}