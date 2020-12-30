import pygame
import random

RADIUS = 5
BALLS = []
BALL_COUNT = 30
WIDTH = 500
HEIGHT = 500
NAME = "Swarm"

def rand(a,b):
    return int(random.randrange(a,b))

class ball:
    def __init__(self,radius,table):
        self.posx = rand(100,400)
        self.posy = rand(100,400)
        self.velx = 0
        self.vely = 0
        self.radius = radius
        self.table = table
        self.accx = 0
        self.accy = 0
        self.color = [rand(0,255),rand(0,255),rand(0,255)]

    def move(self): 
        self.posx = self.posx + self.velx
        self.posy = self.posy + self.vely
        if(self.posx<20 or self.posx>480):
            self.velx = - self.velx
            if(self.posx<20):
                self.posx=21
                self.velx = - self.velx
            elif(self.posx>480):
                self.posx=479
                self.velx = - self.velx 
        if(self.posy<20 or self.posy>480):
            if(self.posy<20):
                self.posy=21
                self.vely = - self.vely
            elif(self.posy>480):
                self.posy=479
                self.vely = - self.vely       
        self.draw(self.table)
        self.velx += self.accx
        self.vely += self.accy

    def draw(self,table):
        pygame.draw.circle(self.table.canvas,(self.color[0],self.color[1],self.color[2]),(self.posx,self.posy),self.radius)       

    def cohesion(self,comx,comy):
        if(self.posx>comx):
            self.accx = -0.05
        else:
            self.accx = 0.05
        if(self.posy>comy):
            self.accy = -0.05
        else:
            self.accy = -0.05      

class table:
    def __init__(self,height,width):
        self.width = width
        self.height = height   
        self.canvas = pygame.display.set_mode((self.width,self.height))

    def draw(self,name):
        pygame.display.set_caption(name)
        self.canvas.fill((0,0,0))
        pygame.draw.rect(self.canvas,(255,255,255),(10,10,self.width-20,self.height-20),2)




TABLE1 = table(WIDTH,HEIGHT)

for i in range(BALL_COUNT):
    BALLS.append(ball(RADIUS,TABLE1))

run = True     

avgx,avgy = 0 , 0
while(run):
    TABLE1.draw(NAME) 
    pygame.time.delay(15)
    pygame.draw.circle(TABLE1.canvas,(255,255,255),(avgx,avgy),15)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False 
    for i in range(BALL_COUNT):
        BALLS[i].move()
    sumx , sumy = 0 , 0
    for i in range(BALL_COUNT):
        sumx += BALLS[i].posx 
        sumy += BALLS[i].posy
    avgx , avgy = sumx//BALL_COUNT , sumy//BALL_COUNT
    for i in range(BALL_COUNT):
        BALLS[i].cohesion(avgx,avgy)  
              
    pygame.display.update()
pygame.QUIT    