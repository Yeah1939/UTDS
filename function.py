from data import *

class Tower(pygame.Rect):
    def __init__(self,x,y,width,height,image_list):
        super().__init__(x,y,width,height)
        self.image_list = image_list
        self.image = self.image_list
        self.image_now = self.image
        self.image_count = 0

    def tower_choose(Tower):
        pass

    
# Заготовки для прокачки
#турель лвл 1:5 урона за 1 секунду(250$) / лвл 2: 15 урона за 1 секунду (1000$) + возможность бачить теневих зомби / лвл 3: 45 урона за 1 секунду (4000$)
#мортира лвл 1:25 урона за 3 секунди(550$)/ лвл 2: 100 урона за 3 секунди (2250$)/ лвл 3: 300 урона за 3 секунди (9999$)



class Enemy(pygame.Rect):
    def __init__(self,x,y,width,height,image_list):
        super().__init__(x,y,width,height)
        self.image_list = image_list
        self.image = self.image_list
        self.image_now = self.image
        self.image_count = 0
    
    #def move():

class Maps(pygame.Rect):
    def __init__(self,x,y,width,height,image):
        super().__init__(x,y,width,height)
        self.image = image

    def make_map(self,maps):
        x,y = 0,0
        length = len(maps)
        i = 0
        j = 0
        tmp = True
        while tmp:
            if i == length -1:
                tmp = False
            if j == len(maps[i]) -1:
                j=0
                i+= 1
                x = 0
                y += 20

            if maps[i][j] == "1":
                while tmp:
                    print(temp_map,i,j)
                    if i + 1 == length - 1 or j + 1 == len(maps[i]) - 1:
                        tmp = False
                    if maps[i+1][j] == "1":
                        i += 1
                        y += 20
                        tmp = False
                    elif maps[i][j+1] == "1":
                        j += 1
                        x += 20
                    elif maps[i+1][j+1] == "1":
                        j += 1
                        i += 1
                        y += 20
                        x += 20
                    elif maps[i-1][j+1] == "1":
                        j += 1
                        i -= 1
                        y -= 20
                        x += 20
                        print(2)
                    elif maps[i-1][j] == "1":
                        i -= 1
                        y -= 20
                    elif maps[i][j-1] == "1":
                        j -= 1
                        x -= 20
                    elif maps[i-1][j-1] == "1":
                        j -= 1
                        i -= 1
                        y -= 20
                        x -= 20
                    temp_map.append((x,y))
                    
    
