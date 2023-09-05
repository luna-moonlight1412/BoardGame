import pygame
import sys
import random
from pygame.locals import*

index=0
tmr=0
x=0
y=0
a=0
b=0
mouse_c=0
player=-1
check=0

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
JEWEL=[
    pygame.image.load("image/jewel/jewel1.png"),
    pygame.image.load("image/jewel/jewel2.png"),
    pygame.image.load("image/jewel/jewel3.png"),
    pygame.image.load("image/jewel/jewel4.png"),
    pygame.image.load("image/jewel/jewel5.png"),
    pygame.image.load("image/jewel/jewel6.png"),
    pygame.image.load("image/jewel/jewel7.png"),
    pygame.image.load("image/jewel/jewel8.png")
    ]
SHIP_E=pygame.image.load("image/pirate_ship1.png")
SHIP_S=pygame.image.load("image/pirate_ship2.png")
CARD_E=pygame.image.load("image/card1.png")
CARD_S=pygame.image.load("image/card2.png")

WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)

board=[]
check_e=[0,0,0,0]
check_s=[0,0,0,0]
for y in range(14):
    board.append([10]*15)

def draw(bg):
    bg.blit(BOARD,[0,0])
    for y in range(4,10):
        for x in range(4,11):
            if board[y][x]>1:
                bg.blit(JEWEL[board[y][x]%8],[x*80-320,y*80-170])
            if board[y][x]==1:
                bg.blit(SHIP_S,[x*80-320,y*80-170])
            if board[y][x]==-1:
                bg.blit(SHIP_E,[x*80-320,y*80-170])
    for i in range(4):
        if check_e[i]==1:
            bg.blit(CARD_E,[i*132+31,24])
        if check_s[i]==1:
            bg.blit(CARD_S,[i*132+32,653])

def click():
    global player,check
    if mouse_c==1 and check==0:
        if player==1:
            if 32<=x and x<=132 and 25<=y and y<=125 and check_e[0]==0:
                check=4
                check_e[0]=1
            if 164<=x and x<=264 and 25<=y and y<=125 and check_e[1]==0:
                check=3
                check_e[1]=1
            if 296<=x and x<=396 and 25<=y and y<=125 and check_e[2]==0:
                check=2
                check_e[2]=1
            if 428<=x and x<=528 and 25<=y and y<=125 and check_e[3]==0:
                check=1
                check_e[3]=1
        if player==-1:
            if 32<=x and x<=132 and 680<=y and y<=780 and check_s[0]==0:
                check=1
                check_s[0]=1
            if 164<=x and x<=264 and 680<=y and y<=780 and check_s[1]==0:
                check=2
                check_s[1]=1
            if 296<=x and x<=396 and 680<=y and y<=780 and check_s[2]==0:
                check=3
                check_s[2]=1
            if 428<=x and x<=528 and 680<=y and y<=780 and check_s[3]==0:
                check=4
                check_s[3]=1

def move(key):
    global player,check,a,b
    if 1<=check and check<=4:
        if player==1:
            for j in range(4,10):
                for k in range(4,11):
                    if board[j][k]==-1:
                        a=k
                        b=j
            if key[K_UP]:
                if board[b-check][a]==0:
                    board[b][a]=0
                    board[b-check][a]=-1
                    check=5
            if key[K_DOWN]:
                if board[b+check][a]==0:
                    board[b][a]=0
                    board[b+check][a]=-1
                    check=5
            if key[K_RIGHT]:
                if board[b][a+check]==0:
                    board[b][a]=0
                    board[b][a+check]=-1
                    check=5
            if key[K_LEFT]:
                if board[b][a-check]==0:
                    board[b][a]=0
                    board[b][a-check]=-1
                    check=5
        if player==-1:
            for j in range(4,10):
                for k in range(4,11):
                    if board[j][k]==1:
                        a=k
                        b=j
            if key[K_UP]:
                if board[b-check][a]==0:
                    board[b][a]=0
                    board[b-check][a]=1
                    check=5
            if key[K_DOWN]:
                if board[b+check][a]==0:
                    board[b][a]=0
                    board[b+check][a]=1
                    check=5
            if key[K_RIGHT]:
                if board[b][a+check]==0:
                    board[b][a]=0
                    board[b][a+check]=1
                    check=5
            if key[K_LEFT]:
                if board[b][a-check]==0:
                    board[b][a]=0
                    board[b][a-check]=1
                    check=5
        
def place_jewel():
    global player,check
    if check==5:
        if mouse_c==1 and 0<=x and x<=560 and 150<=y and y<=630:
            if board[int((y-150)/80)+4][int(x/80)+4]==0:
                board[int((y-150)/80)+4][int(x/80)+4]=random.randint(2,9)
                player*=-1
                check=0
                
                if check_e[0]==1 and check_e[1]==1 and check_e[2]==1 and check_e[3]==1:
                    for i in range(4):
                        check_e[i]=0
                if check_s[0]==1 and check_s[1]==1 and check_s[2]==1 and check_s[3]==1:
                    for i in range(4):
                        check_s[i]=0

def win_check():
    global index,tmr
    a=0
    b=0
    if 1<=check and check<=4:
        if player==1:
            for j in range(4,10):
                for k in range(4,11):
                    if board[j][k]==-1:
                        a=k
                        b=j
            if board[b-check][a]!=0 and board[b+check][a]!=0 and board[b][a+check]!=0 and board[b][a-check]!=0:
                index=2
                tmr=0
        if player==-1:
            for j in range(4,10):
                for k in range(4,11):
                    if board[j][k]==1:
                        a=k
                        b=j
            if board[b-check][a]!=0 and board[b+check][a]!=0 and board[b][a+check]!=0 and board[b][a-check]!=0:
                index=3
                tmr=0
        
def init():
    global check_e,check_s,player,check
    for y in range(4,10):
        for x in range(4,11):
            board[y][x]=0
    board[4][10]=-1
    board[9][4]=1
    check_e=[0,0,0,0]
    check_s=[0,0,0,0]
    player=-1
    check=0

def draw_text(bg,txt,x,y,fnt,col):
    if index==0:
        sur=fnt.render(txt,True,WHITE)
        bg.blit(sur,[x+1,y+2])
        sur=fnt.render(txt,True,col)
        bg.blit(sur,[x,y])
    else:
        sur=fnt.render(txt,True,BLACK)
        bg.blit(sur,[x+1,y+2])
        sur=fnt.render(txt,True,col)
        bg.blit(sur,[x,y])
    
def main():
    pygame.init()
    pygame.display.set_caption("HACK STUCK")
    screen=pygame.display.set_mode((560,780))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,70)
    fontB=pygame.font.Font(None,120)

    while True:
        global index,tmr,x,y,mouse_c
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((560,780),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((560,780))
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,b1,b2=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",90,670,font,BLUE)
            if key[K_SPACE]:
                init()
                index=1
        if index==1:
            draw(screen)
            click()
            move(key)
            place_jewel()
            win_check()
        if index==2:
            draw_text(screen,"WHITE WIN!!",20,350,fontB,WHITE)
            if tmr>=50:
                index=0
        if index==3:
            draw_text(screen,"BLACK WIN!!",20,350,fontB,BLACK)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
                
