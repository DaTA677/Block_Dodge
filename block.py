from config import *


class Block():

    def __init__(self, x, y, width, height,velocity,colour=GREY):
        self._x =x
        self._y =y
        self._width =width
        self._height=height
        self.velocity=velocity
        self.__activated = False
        self._colour=colour

    
    def wrap_object(self):
        if(self._y>WIN_HEIGHT+1):
                self._y= FONT_SIZE-self._height

    def update(self):
        if self.__activated:
            self._y+=self.velocity
            self.wrap_object()

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def get_x(self): 
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self,x):
        self._x= x if x>0 and x+self._width< WIN_WIDTH else self._x
    
    def set_y(self,y):
        self._y=y

    def is_activated(self):
        return self.__activated
    
    def activate(self):
        self.__activated=True

    def deactivate(self):
        self.__activated=False

    def get_draw_dimensions(self):
        return (self._x,self._y,self._width,self._height)
    
    def get_colour(self):
        return self._colour
    
    def check_collision(self,other):
        if(self.__activated and isinstance(other,Block)):
            #print("Checking collision")
            if((other._x>self._x and other._x<self._x+self._width) or 
               (other._x+other._width>self._x and other._x+other._width<self._x+self._width)):
                if((other._y>self._y and other._y<self._y+self._height) or 
                    (other._y+other._height>self._y and other._y+other._height<self._y+self._height)):
                        return True
        return False
    
    def reset(self,x,y):
        self._x=x
        self._y=y
        self.__activated = False
        self.velocity=BLOCK_SPEED