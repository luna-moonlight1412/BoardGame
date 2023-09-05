import pygame
import sys
from pygame.locals import*

RED=(255,0,0)
BLUE=(0,0,255)
ORANGE=(255,126,0)
BLACK=(0,0,0)

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
G=[
    pygame.image.load("image/cockroach1.png"),
    pygame.image.load("image/cockroach2.png"),
    pygame.image.load("image/cockroach3.png")
    ]
CORRECT=pygame.image.load("image/correct.png")
WRONG=pygame.image.load("image/wrong.png")
QUESTION=pygame.image.load("image/question.png")

index=0
player=1
tmr=0
mouse_c=0
check=0
x=0
y=0
hide_c=0

board=[]
hide=[]
for y in range(4):
    board.append([0]*9)
    hide.append([0]*9)

def init():
    global player,check,hide_c
    for y in range(4):
        for x in range(9):
            board[y][x]=0
            hide[y][x]=0
            board[y][4]=1
    player=1
    check=0
    hide_c=0

def draw(bg):
    bg.blit(BOARD,[0,0])
    for y in range(4):
        for x in range(0,9):
            if 0<board[y][x] and board[y][x]<4:
                bg.blit(G[board[y][x]%3],[x*100,y*100])
            if board[y][x]==4:
                bg.blit(CORRECT,[x*100,y*100])
            if board[y][x]==5:
                bg.blit(WRONG,[x*100,y*100])

def turn(bg,key):
    global player,check,y,x,index
    draw(bg)
    if check==0:
        for y in range(4):
            board[y][0]=0
            board[y][8]=0
            hide[y][0]=0
            hide[y][8]=0
    if player==1:
        if check==0:
            for y in range(4):
                board[y][8]=4
                hide[y][8]=1
            board[0][8]=5
            check=1
        if mouse_c==1:
            X=int(x/100)
            Y=int(y/100)
            if X!=8:
                return
            for y in range(4):
                board[y][8]=4
                hide[y][8]=1
            board[Y][X]=5
        if key[K_RETURN]:
            index=2

    if player==-1:
        if check==0:
            for y in range(4):
                board[y][0]=4
                hide[y][0]=1
            board[0][0]=5
            check=1
        if mouse_c==1:
            X=int(x/100)
            Y=int(y/100)
            if X!=0:
                return
            for y in range(4):
                board[y][0]=4
            board[Y][X]=5
        if key[K_RETURN]:
            index=2
    
def move_turn(bg):
    global player,x,y,index,check,hide_c
    draw(bg)
    if player==1:
        hide_c=0
        for i in range(4):
            if hide[i][8]==1:
                bg.blit(QUESTION,[800,i*100])
                hide_c+=1
        if hide_c==1:
                player*=-1
                index=1
                check=0
        if mouse_c==1:
            X=int(x/100)
            Y=int(y/100)
            if X!=8 or hide[Y][X]==0:
                return
            hide[Y][8]=0
            if board[Y][8]==4:
                for i in range(7,0,-1):
                    if board[Y][i]>0:
                        board[Y][i]=0
                        board[Y][i+1]=3
            if board[Y][8]==5:
                for i in range(1,8):
                    if board[Y][i]>0:
                        board[Y][i]=0
                        board[Y][i-1]=2
                        player*=-1
                        index=1
                        check=0
    if player==-1:
        hide_c=0
        for i in range(4):
            if hide[i][0]==1:
                bg.blit(QUESTION,[0,i*100])
                hide_c+=1
        if hide_c==1:
                player*=-1
                index=1
                check=0
        if mouse_c==1:
            X=int(x/100)
            Y=int(y/100)
            if X!=0 or hide[Y][X]==0:
                return
            hide[Y][0]=0
            if board[Y][0]==4:
                for i in range(1,8):
                    if board[Y][i]>0:
                        board[Y][i]=0
                        board[Y][i-1]=2
            if board[Y][0]==5:
                for i in range(7,0,-1):
                    if board[Y][i]>0:
                        board[Y][i]=0
                        board[Y][i+1]=3
                        player*=-1
                        index=1
                        check=0

def check_win():
    global index
    for y in range(4):
        if board[y][0]==2:
            index=3
        if board[y][8]==3:
            index=4

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+1,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x,y])
                        
def main():
    global index,tmr,x,y,mouse_c
    pygame.init()
    pygame.display.set_caption("KAKERLAKEN DUELL")
    screen=pygame.display.set_mode((900,400))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,100)
    fontB=pygame.font.Font(None,140)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((900,400),pygame.FULLSCREEN)
                if event.type==K_ESCAPE:
                    screen=pygame.display.set_mode((900,400))

        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,btn2,btn3=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",200,300,font,ORANGE)
            init()
            if key[K_SPACE]:
                index=1
        if index==1:
            turn(screen,key)
        if index==2:
            move_turn(screen)
            check_win()
            tmr=0
        if index==3:
            draw_text(screen,"LOSE...",50,150,fontB,RED)
            draw_text(screen,"WIN!!",600,150,fontB,BLUE)
            if tmr>=50:
                index=0
        if index==4:
            draw_text(screen,"WIN!!",100,150,fontB,RED)
            draw_text(screen,"LOSE...",500,150,fontB,BLUE)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
