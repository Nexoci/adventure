#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys,time


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
fps = 30
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
move_x=40
move_y=40
speed = 5
up = pygame.image.load('images/up.png')
dwn = pygame.image.load('images/down.png')
lft = pygame.image.load('images/lft.png')
rgt= pygame.image.load('images/rgt.png')
scl_up = pygame.transform.scale(up, (20, 20))
scl_dwm = pygame.transform.scale(dwn, (20, 20))
scl_lft = pygame.transform.scale(lft, (20, 20))
scl_rgt = pygame.transform.scale(rgt, (20, 20))
font = pygame.font.SysFont('Consolas', 10)
font2= pygame.font.SysFont('Arial', 20)
font_win=pygame.font.SysFont('Fixedsys',100)
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Adventure")
def display():
    global walls,player,speed,won,btn_rst
    window.fill((255,255,255))#White background
    mz_edge_R=pygame.draw.rect(window,(237,199,95),(670,0,50,700))
    mz_edge_L=pygame.draw.rect(window,(237,199,95),(-20,0,50,700))
    mz_edge_TP=pygame.draw.rect(window,(237,199,95),(-20,-20,700,50))
    mz_edge_BT=pygame.draw.rect(window,(237,199,95),(-20,670,700,50))
    objective=pygame.draw.rect(window,(12,235,56),(650,630,20,40))
    objective1=pygame.draw.rect(window,(12,235,56),(630,630,20,40))
    wall1=pygame.draw.rect(window,(237,199,95),(70,70,300,40))
    wall2=pygame.draw.rect(window,(237,199,95),(590,70,40,300))
    wall3=pygame.draw.rect(window,(237,199,95),(410,70,220,40))
    wall4=pygame.draw.rect(window,(237,199,95),(410,150,40,220))
    wall5=pygame.draw.rect(window,(237,199,95),(490,150,180,40))
    wall6=pygame.draw.rect(window,(237,199,95),(590,590,90,40))
    wall7=pygame.draw.rect(window,(237,199,95),(590,410,40,140))
    wall8=pygame.draw.rect(window,(237,199,95),(490,230,60,180))
    wall9=pygame.draw.rect(window,(237,199,95),(410,410,180,40))
    wall10=pygame.draw.rect(window,(237,199,95),(410,590,140,40))
    wall11=pygame.draw.rect(window,(237,199,95),(410,550,40,40))
    wall12=pygame.draw.rect(window,(237,199,95),(70,150,40,160))
    wall13=pygame.draw.rect(window,(237,199,95),(70,350,40,240))
    wall14=pygame.draw.rect(window,(237,199,95),(30,470,40,40))
    wall15=pygame.draw.rect(window,(237,199,95),(150,470,40,160))
    wall16=pygame.draw.rect(window,(237,199,95),(70,630,40,40))
    wall17=pygame.draw.rect(window,(237,199,95),(150,390,180,40))
    wall18=pygame.draw.rect(window,(237,199,95),(330,370,40,120))
    wall19=pygame.draw.rect(window,(237,199,95),(330,110,40,120))
    wall20=pygame.draw.rect(window,(237,199,95),(330,270,40,60))
    wall21=pygame.draw.rect(window,(237,199,95),(110,150,140,40))
    wall22=pygame.draw.rect(window,(237,199,95),(290,150,60,40))
    wall23=pygame.draw.rect(window,(237,199,95),(240,230,50,120))
    wall24=pygame.draw.rect(window,(237,199,95),(190,230,60,40))
    wall25=pygame.draw.rect(window,(237,199,95),(150,230,50,80))
    wall26=pygame.draw.rect(window,(237,199,95),(150,350,50,40))
    wall27=pygame.draw.rect(window,(237,199,95),(230,470,60,80))
    wall28=pygame.draw.rect(window,(237,199,95),(230,590,60,80))
    wall29=pygame.draw.rect(window,(237,199,95),(330,530,40,160))
    wall30=pygame.draw.rect(window,(237,199,95),(510,630,40,40))
    wall31=pygame.draw.rect(window,(237,199,95),(410,490,140,60))
    player=pygame.draw.rect(window,(50, 102, 168),(move_x,move_y,20,20))
    up_k=window.blit(scl_up,(75, 5))
    dwn_k=window.blit(scl_dwm,(205, 5))
    lft_k=window.blit(scl_lft,(355, 5))
    rgt_k=window.blit(scl_rgt,(495, 5))
    up_txt= window.blit(font2.render("Move Up", True, (0, 0, 0)), (100,5))
    dwn_txt= window.blit(font2.render("Move Down", True, (0, 0, 0)), (230,5))
    lft_txt= window.blit(font2.render("Move Left", True, (0, 0, 0)), (380,5))
    rgt_txt= window.blit(font2.render("Move Right", True, (0, 0, 0)), (520,5))
    goal_txt= window.blit(font2.render("Goal: Reach The Green Square", True, (0, 0, 0)), (205, 675))
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    walls=[mz_edge_BT,mz_edge_L,mz_edge_R,mz_edge_TP,wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31]
    won=False
    if collision(player, objective):
        won=True
    if won:
        window.blit(font_win.render("You Win!", True, (119, 252, 3)), (215, 275))
        btn_rst = window.blit(font_win.render("Play Again", True, (0, 0, 0)), (180, 350))
        speed=0
        
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
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if btn_rst.collidepoint(pos):
                won=False
                move_x=40
                move_y=40
                speed=5
 
#var--------value name-----key Left---speed value--value name------key Right---speed value      
    movex = (key_input[pygame.K_LEFT] * -speed) + (key_input[pygame.K_RIGHT] * speed)
    movey = (key_input[pygame.K_UP] * -speed) + (key_input[pygame.K_DOWN] * speed)
    move_x += movex
    move_y += movey
    
    display()
    for i in walls:
        if collision(player,i):
            move_x -= movex
            move_y -= movey
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
    
