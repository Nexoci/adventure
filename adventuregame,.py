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
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
move_x=350
move_y=350
speed = 10
blue_sq = pygame.image.load('images/blue_sq.jpg') #with .png or .jpb included in the name
player = pygame.transform.scale(blue_sq, (25, 25))
#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Title")
def display():
    global collisions,player_move
    window.fill((255,255,255)) #White background
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    mz_edge_R=pygame.draw.rect(window,(237,199,95),(670,0,50,700))
    mz_edge_L=pygame.draw.rect(window,(237,199,95),(-20,0,50,700))
    mz_edge_TP=pygame.draw.rect(window,(237,199,95),(-20,-20,700,50))
    mz_edge_BT=pygame.draw.rect(window,(237,199,95),(-20,670,700,50))
    
    player_move=window.blit(player,(move_x, move_y))
    collisions=[mz_edge_R,mz_edge_L,mz_edge_TP,mz_edge_BT]
def collision(object1, object2):
    return object1.colliderect(object2)
   

while True:
    display()
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
        if collision(player_move,i):
            move_x -= movex
            move_y -= movey
       
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw