# Author: RishavMz
# Project description: Simple OOP implementation of classic game PONG using PyGame
# Conatins lots of bugs and limitations compared to the classic game Pong
# Please provide any suggestion if possible for motion of paddle as long as key is kept pressed 
#                               and for displaying the score on the canvas

# Controls : Left paddle: w for up and s for down
# Controls : Right paddle: up arrow key for up and down arrow key for down 
import pygame
import random
pygame.init()
WIDTH = 800
HEIGHT = 500
PADDLE_HEIGHT = 20
PADDLE_WIDTH = 50
BALL_RADIUS = 10
paddle_width = 20
paddle1_speed = 50
paddle1_posx = 10
paddle1_posy = HEIGHT//2
paddle2_posx = 770
paddle2_posy = HEIGHT//2
paddle_height = 100
ball_posx = WIDTH // 2
ball_posy = HEIGHT // 3
point1 = 0
point2 = 0
#declaring the height and width of the canvas

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
        


class Paddle:
    def  __init__(self,table,posx,posy,height,width):
        self.posx = posx
        self.posy = posy
        self.table = table
        self.height = height
        self.width = width
    def draw(self):
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx,self.posy, self.width, self.height))
    def movey(self, key,speed):
        if key == "U":
            if self.posy >= 0:
                self.posy -= speed
            
        elif key == "D":
            if self.posy +  self.height + 30 <= self.table.height:
                self.posy += speed 

class Ball:
    def __init__(self, posx, posy, rad, table, paddle1,paddle2):
        self.posx = ball_posx
        self.posy = ball_posy
        self.rad = BALL_RADIUS
        self.table = table
        self.paddle2 = paddle2
        self.paddle1 = paddle1
        self.velx = random.randrange(1,2)
        self.vely = random.randrange(1,2)
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,255,255), (self.posx, self.posy), self.rad)    
    def move(self):
        global point1, point2
        self.posx += self.velx
        self.posy += self.vely
        if self.posy <= self.rad or self.posy >= self.table.height - self.rad:
            self.vely = -self.vely
        last_touch = 0    
        if (self.posx <= self.rad + self.paddle1.width and self.posx >= 0 )or( self.posx >= self.table.width - self.rad - self.paddle2.width and self.posx <= self.table.width):
            if self.posx <= WIDTH//3 and self.posy >= self.paddle1.posy and self.posy <= self.paddle1.posy + self.paddle1.height:
                self.velx = - self.velx
                last_touch = 1
            elif self.posx >= 2*WIDTH // 3 and self.posy >= self.paddle2.posy and self.posy <= self.paddle2.posy + self.paddle2.height:     
                self.velx = - self.velx
                last_touch = 2
            else:
                self.posx = ball_posx
                self.posy = ball_posy 
                self.velx = - self.velx
                if last_touch == 2:
                    point2 += 1
                elif last_touch == 1:
                    point1 += 1                           
        self.draw()    

             

table1 = Table(WIDTH, HEIGHT)
paddle1 = Paddle(table1, paddle1_posx, paddle1_posy, paddle_height, paddle_width)
paddle2 = Paddle(table1, paddle2_posx, paddle2_posy, paddle_height, paddle_width)
ball1 = Ball(ball_posx, ball_posy, BALL_RADIUS, table1, paddle1,paddle2)
Table_name="Pong(Simplified)"
while True:
    table1.draw(Table_name)
    paddle1.draw()
    paddle2.draw()
    ball1.draw()
    ball1.move()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False    
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                paddle1.movey("U",paddle1_speed)
                paddle1.draw()
            if event.key==pygame.K_s:
                paddle1.movey("D",paddle1_speed)
                paddle1.draw()
            if event.key==pygame.K_UP:
                paddle2.movey("U",paddle1_speed)
                paddle2.draw()
            if event.key==pygame.K_DOWN:
                paddle2.movey("D",paddle1_speed)
                paddle2.draw()
    else:
        ball1.move()
        ball1.draw()                 
    pygame.display.update()
pygame.quit()            
