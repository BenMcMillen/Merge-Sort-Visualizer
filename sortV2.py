import pygame
from numpy import random


pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Merge Sort Visualizer')

numarr = []
run = True

for i in range(1,102):
        numarr.append((0, (29,30,115)))

## Buttons
font = pygame.font.SysFont('Arial',20,bold=True)
surf1 = font.render('Generate', True, 'white')
button1 = pygame.Rect(200,10,110,60)

surf2 = font.render('Solve', True, 'white')
button2 = pygame.Rect(600,10,110,60)


def createArr():
    for i in range(0,101):
        numarr[i]=((random.randint(100), (29,30,115)))

#player = pygame.Rect((300,300,50,50))
def redraw():
    screen.fill((255,255,255))
    drawArr()
    pygame.display.update() 
    pygame.time.delay(20)


def drawArr():
    
    for i in range(1, 101): 
        #pygame.draw.line(screen, (29,30,115), (900/100 * i-3, 100), (900/100 * i-3, numarr[i]*600/100 + 100), (SCREEN_WIDTH-100)//100) 
        pygame.draw.line(screen, numarr[i][1], (900/100 * i-3, SCREEN_HEIGHT), (900/100 * i-3, SCREEN_HEIGHT - numarr[i][0]*600/100), (SCREEN_WIDTH-100)//100) 
def msmain(numarr, left, right):
    if left < right:
        middle = (left + right)//2
        msmain(numarr, left, middle)
        msmain(numarr, middle + 1, right)
        ProcessMerging(numarr, left, middle, middle + 1, right)

def ProcessMerging(array, left ,middleL, middleR, right):
    i = left 
    j = middleR
    temp =[] 
    pygame.event.pump()  
    while i<= middleL and j<= right: 
        array[i] = (array[i][0],(255,0,0))
        array[j] = (array[j][0],(255,0,0))
        redraw()
        array[i] = (array[i][0],(29,30,115))
        array[j] = (array[j][0],(29,30,115))
        if array[i][0]<array[j][0]: 
            temp.append(array[i]) 
            i+= 1
        else: 
            temp.append(array[j]) 
            j+= 1
    while i<= middleL: 
        array[i] = (array[i][0],(255,0,0))
        redraw()
        array[i] = (array[i][0],(29,30,115))
        temp.append(array[i]) 
        i+= 1
    while j<= right: 
        array[j] = (array[j][0],(255,0,0))
        redraw()
        array[j] = (array[j][0],(29,30,115))
        temp.append(array[j]) 
        j+= 1
    j = 0    
    for i in range(left, right + 1):  
        pygame.event.pump()  
        array[i]= temp[j] 
        j+= 1 
        array[i] = (array[i][0],(0, 255, 0))
        redraw()
        # Array is sorted
        if right - left == len(array)-2: 
            array[i]= (array[i][0],(155, 52, 235))
        else:  
            array[i] = (array[i][0],(29,30,115))

arrayAvailable = False

while run:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    createArr()
                    arrayAvailable = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                if button2.collidepoint(event.pos) and arrayAvailable:
                    msmain(numarr,1, 100)
                    arrayAvailable = False
    drawArr()
    
    pygame.draw.rect(screen, (0,0,0),button1)
    screen.blit(surf1,(button1.x +10, button1.y+17))

    pygame.draw.rect(screen, (0,0,0),button2)
    screen.blit(surf2,(button2.x +27, button2.y+17))

    pygame.display.update()

pygame.time.delay(1000)
pygame.quit