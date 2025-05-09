from data import *

class Tower(pygame.Rect):
    def __init__(self,x,y,width,height,image_list):
        super().__init__(x,y,width,height)
        self.image_list = image_list
        self.image = self.image_list
        self.image_now = self.image
        self.image_count = 0

class Enemy(pygame.Rect):
    def __init__(self,x,y,width,height,image_list):
        super().__init__(x,y,width,height)
        self.image_list = image_list
        self.image = self.image_list
        self.image_now = self.image
        self.image_count = 0
