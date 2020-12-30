import pygame
import random

RADIUS = 5
BALLS = []
BALL_COUNT = 10
WIDTH = 500
HEIGHT = 500
NAME = "Swarm"

def rand(a,b):
    return int(random.randrange(a,b))

class ball:
    def __init__(self,radius,table):
        self.posx = rand(20,480)
        self.posy = rand(20,480)
        self.velx = random.choice([-5,-4,4,5])
        self.vely = random.choice([-5,-4,4,5])
        self.radius = radius
        self.table = table
        self.color = [rand(0,255),rand(0,255),rand(0,255)]

    def move(self):
        if(self.posx<20 or self.posx>480):
            self.velx = - self.velx
        if(self.posy<20 or self.posy>480):
            self.vely = - self.vely    
        self.posx = self.posx + self.velx
        self.posy = self.posy + self.vely
        self.draw(self.table)

    def draw(self,table):
        pygame.draw.circle(self.table.canvas,(self.color[0],self.color[1],self.color[2]),(self.posx,self.posy),self.radius)       


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
while(run):
    TABLE1.draw(NAME) 
    pygame.time.delay(25)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False 
    for i in range(BALL_COUNT):
        BALLS[i].move()
    pygame.display.update()
pygame.QUIT    