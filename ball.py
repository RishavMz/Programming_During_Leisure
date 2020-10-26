import pygame
import random
import math
SQUARE=600
RADIUS = 50
ball_posx = 1000
ball_posy = 1000
GRAVITY = -1
class Table:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.canvas = canvas = pygame.display.set_mode((self.width,self.height))
    def draw(self, st):
        self.canvas = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(st)
        self.canvas.fill((0,0,0))
        pygame.draw.rect(self.canvas, (255,255,255), (30,0, self.width - 60, self.height),2)     
        

class Ball:
    def __init__(self, posx, posy, rad, table):
        self.posx = ball_posx
        self.posy = ball_posy
        self.rad = RADIUS
        self.table = table
        self.velx = 0
        self.vely = 0
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,255,255), (self.posx//10, self.posy//10), self.rad)    
    def move(self,x):
        global point1, point2,GRAVITY
        self.posx += self.velx
        self.posy += self.vely
        self.vely -= GRAVITY
        if(x == 1):
            if(self.vely < 0):
                self.vely = -80
            else:
                self.vely = -80
            self.velx = random.randrange(-10,10)
        if self.posy >= self.table.height*10 - self.rad:
            self.vely = -self.vely
        if(self.posx-RADIUS*2 <0 or self.posx+RADIUS*2 > SQUARE ):
            self.posx = self.posx % (SQUARE *10 )          
        self.draw() 


table1 = Table(SQUARE,SQUARE)
ball1 = Ball(100,5,RADIUS,table1)
Table_name="K(cl)ick the ball"
run = True
while run:
    table1.draw(Table_name)
    pygame.time.delay(10)
    ball1.move(0)
    ball1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False    
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() 
            print(pos)  
            print("Ball",ball1.posx, ball1.posy) 
            ball1.move(1)  
            ball1.draw()                 
    pygame.display.update()
pygame.quit()            

