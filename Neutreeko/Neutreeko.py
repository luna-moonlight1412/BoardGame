import pygame
import sys
import random
from pygame.locals import*

index=0
tmr=0
x=0
y=0
X=5
Y=5
a=0
b=0
A=5
B=5
mouse_c=0
player=1
check=0
direction=0
piece=0
speed=3
white=0
black=0

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
WHITE_P=pygame.image.load("image/white.png")
BLACK_P=pygame.image.load("image/black.png")

WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)

board=[]
for y in range(7):
    board.append([9]*7)


def draw(bg):
    bg.blit(BOARD,[0,0])
    for y in range(1,6):
        for x in range(1,6):
            if board[y][x]==1:
                bg.blit(WHITE_P,[x*100-100,y*100-100])
            if board[y][x]==-1:
                bg.blit(BLACK_P,[x*100-100,y*100-100])
    pygame.draw.rect(bg,YELLOW,[A*100,B*100,100,100],3)

def click():
    global X,Y,check,a,b,A,B
    if mouse_c==1:
        if player==1:
            if board[int(y/100)+1][int(x/100)+1]==1:
                X=int(x/100)
                Y=int(y/100)
                A=int(x/100)
                B=int(y/100)
                a=X*100+150
                b=Y*100+150
                check=1
        if player==-1:
            if board[int(y/100)+1][int(x/100)+1]==-1:
                X=int(x/100)
                Y=int(y/100)
                A=int(x/100)
                B=int(y/100)
                a=X*100+150
                b=Y*100+150
                check=1

def slide():
    global check,player,X,Y,player,direction,index,piece,A,B
    if check==1 and mouse_c==1:
        for i in range(5):
            if X*100<=x and x<=X*100+100 and (Y-i)*100-100<=y and y<=(Y-i)*100:
                if board[Y][X+1]==0:
                    piece=board[Y+1][X+1]
                    board[Y+1][X+1]=0
                    check=0
                    player*=-1
                    A=5
                    B=5
                    direction=1
                    index=2
                else:
                    return
            if X*100<=x and x<=X*100+100 and (Y+i)*100+100<=y and y<=(Y+i)*100+200:
                if board[Y+2][X+1]==0:
                    piece=board[Y+1][X+1]
                    board[Y+1][X+1]=0
                    check=0
                    player*=-1
                    A=5
                    B=5
                    direction=2
                    index=2
                else:
                    return
            if (X-i)*100-100<=x and x<=(X-i)*100 and Y*100<=y and y<=Y*100+100:
                if board[Y+1][X]==0:
                    piece=board[Y+1][X+1]
                    board[Y+1][X+1]=0
                    check=0
                    player*=-1
                    A=5
                    B=5
                    direction=3
                    index=2
                else:
                    return
            if (X+i)*100+100<=x and x<=(X+i)*100+200 and Y*100<=y and y<=Y*100+100:
                if board[Y+1][X+2]==0:
                    piece=board[Y+1][X+1]
                    board[Y+1][X+1]=0
                    check=0
                    player*=-1
                    A=5
                    B=5
                    direction=4
                    index=2
                else:
                    return
            if (X-i)*100-100<=x and x<=(X-i)*100 and (Y-i)*100-100<=y and y<(Y-i)*100:
                if board[Y][X]==0:
                    piece=board[Y+1][X+1]
                    board[Y+1][X+1]=0
                    check=0
                    player*=-1
                    A=5
                    B=5
                    direction=5
                    index=2
                else:
                    return
            if (X+i)*100+100<=x and x<=(X+i)*100+200 and (Y-i)*100-100<=y and y<=(Y-i)*100:
                if board[Y][X+2]==0:
                    piece=board[Y+1][X+1]
                    board[Y+1][X+1]=0
                    check=0
                    player*=-1
                    A=5
                    B=5
                    direction=6
                    index=2
                else:
                    return
            if (X-i)*100-100<=x and x<=(X-i)*100 and (Y+i)*100+100<=y and y<=(Y+i)*100+200:
                if board[Y+2][X]==0:
                    piece=board[Y+1][X+1]
                    board[Y+1][X+1]=0
                    check=0
                    player*=-1
                    A=5
                    B=5
                    direction=7
                    index=2
                else:
                    return
            if (X+i)*100+100<=x and x<=(X+i)*100+200 and (Y+i)*100+100<=y and y<=(Y+i)*100+200:
                if board[Y+2][X+2]==0:
                    piece=board[Y+1][X+1]
                    board[Y+1][X+1]=0
                    check=0
                    player*=-1
                    A=5
                    B=5
                    direction=8
                    index=2
                else:
                    return

def slide_piece(bg):
    global index
    draw(bg)
    if direction==1:
        if piece==1:
            bg.blit(WHITE_P,[int((a-100)/100)*100,int((b-100)/100)*100-tmr*speed])
        if piece==-1:
            bg.blit(BLACK_P,[int((a-100)/100)*100,int((b-100)/100)*100-tmr*speed])
        if tmr%50!=0:
            if board[int((b-tmr*speed+50)/100)-1][int(a/100)]!=0:
                board[int((b-tmr*speed+50)/100)][int(a/100)]=piece
                index=1
    if direction==2:
        if piece==1:
            bg.blit(WHITE_P,[int((a-100)/100)*100,int((b-100)/100)*100+tmr*speed])
        if piece==-1:
            bg.blit(BLACK_P,[int((a-100)/100)*100,int((b-100)/100)*100+tmr*speed])
        if tmr%50!=0:
            if board[int((b+tmr*speed-50)/100)+1][int(a/100)]!=0:
                board[int((b+tmr*speed-50)/100)][int(a/100)]=piece
                index=1
    if direction==3:
        if piece==1:
            bg.blit(WHITE_P,[int((a-100)/100)*100-tmr*speed,int((b-100)/100)*100])
        if piece==-1:
            bg.blit(BLACK_P,[int((a-100)/100)*100-tmr*speed,int((b-100)/100)*100])
        if tmr%50!=0:
            if board[int(b/100)][int((a-tmr*speed+50)/100)-1]!=0:
                board[int(b/100)][int((a-tmr*speed+50)/100)]=piece
                index=1
    if direction==4:
        if piece==1:
            bg.blit(WHITE_P,[int((a-100)/100)*100+tmr*speed,int((b-100)/100)*100])
        if piece==-1:
            bg.blit(BLACK_P,[int((a-100)/100)*100+tmr*speed,int((b-100)/100)*100])
        if tmr%50!=0:
            if board[int(b/100)][int((a+tmr*speed-50)/100)+1]!=0:
                board[int(b/100)][int((a+tmr*speed-50)/100)]=piece
                index=1
    if direction==5:
        if piece==1:
            bg.blit(WHITE_P,[int((a-100)/100)*100-tmr*speed,int((b-100)/100)*100-tmr*speed])
        if piece==-1:
            bg.blit(BLACK_P,[int((a-100)/100)*100-tmr*speed,int((b-100)/100)*100-tmr*speed])
        if tmr%50!=0:
            if board[int((b-tmr*speed+50)/100)-1][int((a-tmr*speed+50)/100)-1]!=0:
                board[int((b-tmr*speed+50)/100)][int((a-tmr*speed+50)/100)]=piece
                index=1
    if direction==6:
        if piece==1:
            bg.blit(WHITE_P,[int((a-100)/100)*100+tmr*speed,int((b-100)/100)*100-tmr*speed])
        if piece==-1:
            bg.blit(BLACK_P,[int((a-100)/100)*100+tmr*speed,int((b-100)/100)*100-tmr*speed])
        if tmr%50!=0:
            if board[int((b-tmr*speed+50)/100)-1][int((a+tmr*speed-50)/100)+1]!=0:
                board[int((b-tmr*speed+50)/100)][int((a+tmr*speed-50)/100)]=piece
                index=1
    if direction==7:
        if piece==1:
            bg.blit(WHITE_P,[int((a-100)/100)*100-tmr*speed,int((b-100)/100)*100+tmr*speed])
        if piece==-1:
            bg.blit(BLACK_P,[int((a-100)/100)*100-tmr*speed,int((b-100)/100)*100+tmr*speed])
        if tmr%50!=0:
            if board[int((b+tmr*speed-50)/100)+1][int((a-tmr*speed+50)/100)-1]!=0:
                board[int((b+tmr*speed-50)/100)][int((a-tmr*speed+50)/100)]=piece
                index=1
    if direction==8:
        if piece==1:
            bg.blit(WHITE_P,[int((a-100)/100)*100+tmr*speed,int((b-100)/100)*100+tmr*speed])
        if piece==-1:
            bg.blit(BLACK_P,[int((a-100)/100)*100+tmr*speed,int((b-100)/100)*100+tmr*speed])
        if tmr%50!=0:
            if board[int((b+tmr*speed-50)/100)+1][int((a+tmr*speed-50)/100)+1]!=0:
                board[int((b+tmr*speed-50)/100)][int((a+tmr*speed-50)/100)]=piece
                index=1

def win_check():
    global index
    for y in range(1,6):
        for x in range(1,6):
            if board[y][x]==1:
                if board[y-1][x]==1 and board[y+1][x]==1:
                    index=3
                if board[y][x-1]==1 and board[y][x+1]==1:
                    index=3
                if board[y-1][x-1]==1 and board[y+1][x+1]==1:
                    index=3
                if board[y-1][x+1]==1 and board[y+1][x-1]==1:
                    index=3
            if board[y][x]==-1:
                if board[y-1][x]==-1 and board[y+1][x]==-1:
                    index=4
                if board[y][x-1]==-1 and board[y][x+1]==-1:
                    index=4
                if board[y-1][x-1]==-1 and board[y+1][x+1]==-1:
                    index=4
                if board[y-1][x+1]==-1 and board[y+1][x-1]==-1:
                    index=4
            else:
                pass
                
def init():
    global player,white,black,X,Y,a,b,check,direction,A,B
    for y in range(1,6):
        for x in range(1,6):
            board[y][x]=0
    player=1
    white=0
    black=0
    X=5
    Y=5
    a=0
    b=0
    A=5
    B=5
    check=0
    direction=0
    while white<=2:
        rx=random.randint(1,5)
        ry=random.randint(1,5)
        if board[ry][rx]==0:
            board[ry][rx]=1
            white+=1
    while black<=2:
        rx=random.randint(1,5)
        ry=random.randint(1,5)
        if board[ry][rx]==0:
            board[ry][rx]=-1
            black+=1

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+2,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x,y])

def main():
    pygame.init()
    pygame.display.set_caption("NEUTREEKO")
    screen=pygame.display.set_mode((500,500))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,70)
    fontB=pygame.font.Font(None,100)

    while True:
        global index,tmr,mouse_c,x,y
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((500,500),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((500,500))
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,b1,b2=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",70,380,font,BLACK)
            if key[K_SPACE]:
                init()
                index=1
        if index==1:
            draw(screen)
            click()
            slide()
            win_check()
            tmr=0
        if index==2:
            slide_piece(screen)
        if index==3:
            draw_text(screen,"WHITE WIN!!",30,230,fontB,WHITE)
            if tmr>=500:
                index=0
        if index==4:
            draw_text(screen,"BLACK WIN!!",30,230,fontB,BLACK)
            if tmr>=500:
                index=0
        pygame.display.update()
        clock.tick(100)

if __name__=='__main__':
    main()
