import pygame
import sys
import random
from pygame.locals import*

index=0
tmr=0
x=0
y=0
mouse_c=0
X=5
Y=5
player=1
check=0

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
CIRCLE=[
    pygame.image.load("image/circle1.png"),
    pygame.image.load("image/circle2.png"),
    pygame.image.load("image/circle3.png"),
    pygame.image.load("image/circle4.png")
    ]
CROSS=[
    pygame.image.load("image/cross1.png"),
    pygame.image.load("image/cross2.png"),
    pygame.image.load("image/cross3.png"),
    pygame.image.load("image/cross4.png")
    ]
WIN_CIRCLE=pygame.image.load("image/win_circle.png")
WIN_CROSS=pygame.image.load("image/win_cross.png")

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(80,80,80)
YELLOW=(255,255,0)

board=[]
for y in range(7):
    board.append([9]*7)

def draw(bg):
    bg.blit(BOARD,[0,0])
    for y in range(1,6):
        for x in range(1,6):
            if 1<=board[y][x] and board[y][x]<=4:
                bg.blit(CIRCLE[board[y][x]%4],[(x-1)*100,(y-1)*100])
            if board[y][x]<0:
                bg.blit(CROSS[board[y][x]%4],[(x-1)*100,(y-1)*100])
    pygame.draw.rect(bg,YELLOW,[X*100,Y*100-1,100,100],4)

def click():
    global X,Y,check
    a=int(x/100)
    b=int(y/100)
    if mouse_c==1 and (a==0 or a==4 or b==0 or b==4):
        if board[b+1][a+1]==0:
            X=a
            Y=b
            check=1
        if player==1:
            if 0<board[b+1][a+1] and board[b+1][a+1]<=4:
                X=a
                Y=b
                check=2
        if player==-1:
            if board[b+1][a+1]<0:
                X=a
                Y=b
                check=2

def slide(key):
    global check,player,X,Y
    if check>=1:
        if key[K_UP]:
            if Y+1==5:
                return
            if check==2:
                board[Y+1][X+1]=0
            for i in range(Y+1,6):
                if board[i-1][X+1]==0:
                    board[i-1][X+1]=board[i][X+1]
                    board[i][X+1]=0
                if i==5:
                    if player==1:
                        board[5][X+1]=random.randint(1,4)
                        check=0
                        X=5
                        Y=5
                    if player==-1:
                        board[5][X+1]=random.randint(-4,-1)
                        check=0
                        X=5
                        Y=5
                    player*=-1
        if key[K_DOWN]:
            if Y+1==1:
                return
            if check==2:
                board[Y+1][X+1]=0
            for i in range(Y,0,-1):
                if board[i+1][X+1]==0:
                    board[i+1][X+1]=board[i][X+1]
                    board[i][X+1]=0
                if i==1:
                    if player==1:
                        board[1][X+1]=random.randint(1,4)
                        check=0
                        X=5
                        Y=5
                    if player==-1:
                        board[1][X+1]=random.randint(-4,-1)
                        check=0
                        X=5
                        Y=5
                    player*=-1
        if key[K_RIGHT]:
            if X+1==1:
                return
            if check==2:
                board[Y+1][X+1]=0
            for i in range(X,0,-1):
                if board[Y+1][i+1]==0:
                    board[Y+1][i+1]=board[Y+1][i]
                    board[Y+1][i]=0
                if i==1:
                    if player==1:
                        board[Y+1][1]=random.randint(1,4)
                        check=0
                        X=5
                        Y=5
                    if player==-1:
                        board[Y+1][1]=random.randint(-4,-1)
                        check=0
                        X=5
                        Y=5
                    player*=-1
        if key[K_LEFT]:
            if X+1==5:
                return
            if check==2:
                board[Y+1][X+1]=0
            for i in range(X+1,6):
                if board[Y+1][i-1]==0:
                    board[Y+1][i-1]=board[Y+1][i]
                    board[Y+1][i]=0
                if i==5:
                    if player==1:
                        board[Y+1][5]=random.randint(1,4)
                        check=0
                        X=5
                        Y=5
                    if player==-1:
                        board[Y+1][5]=random.randint(-4,-1)
                        check=0
                        X=5
                        Y=5
                    player*=-1

def check_win():
    global index
    for i in range(1,6):
        if board[1][i]>0 and board[2][i]>0 and board[3][i]>0 and board[4][i]>0 and board[5][i]>0:
            index=2
        if board[1][i]<0 and board[2][i]<0 and board[3][i]<0 and board[4][i]<0 and board[5][i]<0:
            index=3
        if board[i][1]>0 and board[i][2]>0 and board[i][3]>0 and board[i][4]>0 and board[i][5]>0:
            index=2
        if board[i][1]<0 and board[i][2]<0 and board[i][3]<0 and board[i][4]<0 and board[i][5]<0:
            index=3
    if board[1][1]>0 and board[2][2]>0 and board[3][3]>0 and board[4][4]>0 and board[5][5]>0:
        index=2
    if board[1][1]<0 and board[2][2]<0 and board[3][3]<0 and board[4][4]<0 and board[5][5]<0:
        index=3
    if board[1][5]>0 and board[2][4]>0 and board[3][3]>0 and board[4][2]>0 and board[5][1]>0:
        index=2
    if board[1][5]<0 and board[2][4]<0 and board[3][3]<0 and board[4][2]<0 and board[5][1]<0:
        index=3
        
def init():
    global player,check,X,Y
    for y in range(1,6):
        for x in range(1,6):
            board[y][x]=0
    player=1
    check=0
    X=5
    Y=5

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,WHITE)
    bg.blit(sur,[x+1,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x,y])
        
def main():
    pygame.init()
    pygame.display.set_caption("QUIXO")
    screen=pygame.display.set_mode((500,500))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,70)
    fontB=pygame.font.Font(None,180)

    while True:
        global index,tmr,mouse_c,x,y,player
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((500,500),pygame.FULLSCREEN)
                if event.type==K_ESCAPE:
                    screen=pygame.display.set_mode((500,500))
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,btn2,btn3=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",60,380,font,BLACK)
            init()
            if key[K_SPACE]:
                index=1
        if index==1:
            click()
            slide(key)
            check_win()
            draw(screen)
            tmr=0
        if index==2:
            screen.blit(WIN_CIRCLE,[10,150])
            draw_text(screen,"WIN!!",160,170,fontB,BLACK)
            if tmr>=50:
                index=0
        if index==3:
            screen.blit(WIN_CROSS,[10,150])
            draw_text(screen,"WIN!!",160,170,fontB,BLACK)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
