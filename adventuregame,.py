#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys


pygame.init()
def gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT):
        spacer = 10
        font = pygame.font.SysFont('Consolas', 10)
        for gridX in range(0, WINDOW_WIDTH, spacer):        
            window.blit(pygame.transform.rotate(font.render(str(gridX), True, (0, 0, 0)),90),(gridX,0))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            window.blit(font.render(str(gridY), True, (0, 0, 0)), (0, gridY))
        for gridX in range(0, WINDOW_WIDTH, spacer):
            pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,WINDOW_HEIGHT))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            pygame.draw.line(window,(255,0,0),(0,gridY),(WINDOW_WIDTH,gridY))     
# Game Setup
fps = 30
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
move_x=40
move_y=40
speed = 5
font = pygame.font.SysFont('Consolas', 10)
#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Adventure")
def display():
    global collisions,player
    window.fill((255,255,255)) #White background
    mz_edge_R=pygame.draw.rect(window,(237,199,95),(670,0,50,700))
    mz_edge_L=pygame.draw.rect(window,(237,199,95),(-20,0,50,700))
    mz_edge_TP=pygame.draw.rect(window,(237,199,95),(-20,-20,700,50))
    mz_edge_BT=pygame.draw.rect(window,(237,199,95),(-20,670,700,50))
    objective=pygame.draw.rect(window,(12,235,56),(630,630,40,40))
    wall1=pygame.draw.rect(window,(237,199,95),(70,70,300,40))
    wall2=pygame.draw.rect(window,(237,199,95),(590,70,40,300))
    wall3=pygame.draw.rect(window,(237,199,95),(410,70,220,40))
    wall4=pygame.draw.rect(window,(237,199,95),(410,150,40,220))
    wall5=pygame.draw.rect(window,(237,199,95),(490,150,180,40))
    wall6=pygame.draw.rect(window,(237,199,95),(590,590,90,40))
    wall7=pygame.draw.rect(window,(237,199,95),(590,410,40,140))
    wall8=pygame.draw.rect(window,(237,199,95),(490,230,60,180))
    wall9=pygame.draw.rect(window,(237,199,95),(410,410,180,40))
    wall10=pygame.draw.rect(window,(237,199,95),(410,490,140,60))
    wall10=pygame.draw.rect(window,(237,199,95),(410,590,140,40))
    wall11=pygame.draw.rect(window,(237,199,95),(410,550,40,40))
    player=pygame.draw.rect(window,(50, 102, 168),(40,40,20,20))
    
    gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    collisions=[mz_edge_R,mz_edge_L,mz_edge_TP,mz_edge_BT]
    window.blit(font.render(f"X: {move_x}", True, (0, 0, 0)), (500, 20))
    window.blit(font.render(f"Y: {move_y}", True, (0, 0, 0)), (550, 20))
def collision(object1, object2):
    return object1.colliderect(object2)
   
display()
while True:
    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        key_input = pygame.key.get_pressed()

 
#var--------value name-----key Left---speed value--value name------key Right---speed value      
        movex = (key_input[pygame.K_LEFT] * -speed) + (key_input[pygame.K_RIGHT] * speed)
        movey = (key_input[pygame.K_UP] * -speed) + (key_input[pygame.K_DOWN] * speed)
    move_x += movex
    move_y += movey
    
    display()
    for i in collisions:
        if collision(player,i):
            move_x -= movex
            move_y -= movey
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
