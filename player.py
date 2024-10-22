from block import Block
from config import *
import pygame

class Player(Block):
    def __init__(self, x, y, width, height, velocity, colour=GREY):
        super().__init__(x, y, width, height, velocity, colour)
        self.is_dashing =False
        self.is_jumping =False
        self.jumping_time=10
        self.dash_count=10
        self.jump_direction=-1
        self.dash_direction=1
        self.__dash_cooldown=0
        self.__jump_cooldown=0

    def handle_inputs(self, keys):
        self.__dash_cooldown -= (1 if self.__dash_cooldown>0 else 0)
        self.__jump_cooldown -= (1 if self.__jump_cooldown>0 else 0)

        if not self.is_dashing:
            if keys[pygame.K_LEFT] and self._x>self.velocity:
                self._x=(self._x-self.velocity)
                self.dash_direction=-1
            if keys[pygame.K_RIGHT] and self._x+self.velocity<WIN_WIDTH-self._width:
                self._x=self._x+self.velocity
                self.dash_direction=1
            if keys[pygame.K_LSHIFT] and not self.is_jumping and not self.__dash_cooldown:
                self.is_dashing=True
            
        else:
            self.__dash_cooldown=10
            if self.dash_count>7:
                self._x=min(self._x+self.dash_count**2*0.5*self.dash_direction, WIN_WIDTH-self._width) if self.dash_direction==1 else max(self._x+self.dash_count**2*0.5*self.dash_direction, 0)
                self.dash_count-=1
            else:
                self.is_dashing=False
                self.dash_count=10
        
        if not self.is_jumping:
            if keys[pygame.K_UP] and self._y>self.velocity:
                self.set_y(self._y-self.velocity)
                self.jump_direction=-1
            if keys[pygame.K_DOWN] and self._y+self._height+self.velocity<WIN_HEIGHT:
                self.set_y(self._y+self.velocity)
                self.jump_direction=1
                
            if keys[pygame.K_SPACE] and not self.is_dashing and not self.__jump_cooldown:
                self.is_jumping=True
        else:
            self.__jump_cooldown=10
            if self.jumping_time>=7:
                self._y= min(self.get_y()+self.jumping_time**2*0.5*self.jump_direction, WIN_HEIGHT-self._height) if self.jump_direction==1 else max(self.get_y()+self.jumping_time**2*0.5*self.jump_direction, 0)
                self.jumping_time-=1
            else:
                self.jumping_time=10
                self.is_jumping=False

    def reset(self,x,y):
        super().reset(x,y)
        self.is_dashing =False
        self.is_jumping =False
        self.jumping_time=10
        self.dash_count=10
        self.dash_direction=1
        self.jump_direction=-1
        self.__jump_cooldown=0
        self.__dash_cooldown=0
        self.velocity=PLAYER_SPEED