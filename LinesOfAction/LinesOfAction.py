import pygame
import sys
from pygame.locals import*

index=0
tmr=0
x=0
y=0
X=0
Y=0
a=8
b=8
mouse_c=0
player=1
check=0

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
WHITE_P=[
    pygame.image.load("image/white1.png"),
    pygame.image.load("image/white2.png")
    ]
BLACK_P=[
    pygame.image.load("image/black1.png"),
    pygame.image.load("image/black2.png")
    ]

WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)

direction=[0,0,0,0]
board=[]
for y in range(10):
    board.append([9]*10)

def draw(bg):
    bg.blit(BOARD,[0,0])
    for y in range(1,9):
        for x in range(1,9):
            if 0<board[y][x] and board[y][x]<3:
                bg.blit(WHITE_P[board[y][x]%2],[(x-1)*80+2,(y-1)*80+2])
            if board[y][x]<0:
                bg.blit(BLACK_P[board[y][x]%2],[(x-1)*80+2,(y-1)*80+2])
    pygame.draw.rect(bg,YELLOW,[a*80,b*80,80,80],3)

def click():
    global X,Y,check,a,b
    if mouse_c==1:
        if player==1:
            if board[int(y/80)+1][int(x/80)+1]>0:
                X=int(x/80)+1
                Y=int(y/80)+1
                a=int(x/80)
                b=int(y/80)
                check=1
                time=0
        if player==-1:
            if board[int(y/80)+1][int(x/80)+1]<0:
                X=int(x/80)+1
                Y=int(y/80)+1
                a=int(x/80)
                b=int(y/80)
                check=1
                time=0

def move():
    global direction,check,player,X,Y,a,b
    direction=[0,0,0,0]
    try:
        for i in range(1,9):
            if board[i][X]!=0:
                direction[0]+=1
            if board[Y][i]!=0:
                direction[1]+=1
        for i in range(8):
            if board[Y+i][X+i]==9:
                break
            if board[Y+i][X+i]!=0:
                direction[2]+=1
        for i in range(8):
            if board[Y+i][X-i]==9:
                break
            if board[Y+i][X-i]!=0:
                direction[3]+=1
        for i in range(1,8):
            if board[Y-i][X-i]==9:
                break
            if board[Y-i][X-i]!=0:
                direction[2]+=1
        for i in range(1,8):
            if board[Y-i][X+i]==9:
                break
            if board[Y-i][X+i]!=0:
                direction[3]+=1
    except:
        pass
    if mouse_c==1:
        if check==1:
            if a*80<=x and x<=a*80+80 and (b-direction[0])*80<=y and y<=(b-direction[0])*80+80:
                try:
                    if board[Y-direction[0]][X]!=9:
                        if player==1:
                            if board[Y-direction[0]][X]<=0:
                                for k in range(1,direction[0]):
                                    if board[Y-k][X]<0:
                                        return
                                board[Y-direction[0]][X]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                        if player==-1:
                            if board[Y-direction[0]][X]>=0:
                                for k in range(1,direction[0]):
                                    if board[Y-k][X]>0:
                                        return
                                board[Y-direction[0]][X]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                except:
                    return
            if a*80<=x and x<=a*80+80 and (b+direction[0])*80<=y and y<=(b+direction[0])*80+80:
                try:
                    if board[Y+direction[0]][X]!=9:
                        if player==1:
                            if board[Y+direction[0]][X]<=0:
                                for k in range(1,direction[0]):
                                    if board[Y+k][X]<0:
                                        return
                                board[Y+direction[0]][X]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                        if player==-1:
                            if board[Y+direction[0]][X]>=0:
                                for k in range(1,direction[0]):
                                    if board[Y+k][X]>0:
                                        return
                                board[Y+direction[0]][X]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                except:
                    return
            if (a-direction[1])*80<=x and x<=(a-direction[1])*80+80 and b*80<=y and y<=b*80+80:
                try:
                    if board[Y][X-direction[1]]!=9:
                        if player==1:
                            if board[Y][X-direction[1]]<=0:
                                for k in range(1,direction[1]):
                                    if board[Y][X-k]<0:
                                        return
                                board[Y][X-direction[1]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                        if player==-1:
                            if board[Y][X-direction[1]]>=0:
                                for k in range(1,direction[1]):
                                    if board[Y][X-k]>0:
                                        return
                                board[Y][X-direction[1]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                except:
                    return
            if (a+direction[1])*80<=x and x<=(a+direction[1])*80+80 and b*80<=y and y<=b*80+80:
                try:
                    if board[Y][X+direction[1]]!=9:
                        if player==1:
                            if board[Y][X+direction[1]]<=0:
                                for k in range(1,direction[1]):
                                    if board[Y][X+k]<0:
                                        return
                                board[Y][X+direction[1]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                        if player==-1:
                            if board[Y][X+direction[1]]>=0:
                                for k in range(1,direction[1]):
                                    if board[Y][X+k]>0:
                                        return
                                board[Y][X+direction[1]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                except:
                    return
            if (a-direction[2])*80<=x and x<=(a-direction[2])*80+80 and (b-direction[2])*80<=y and y<=(b-direction[2])*80+80:
                try:
                    if board[Y-direction[2]][X-direction[2]]!=9:
                        if player==1:
                            if board[Y-direction[2]][X-direction[2]]<=0:
                                for k in range(1,direction[2]):
                                    if board[Y-k][X-k]<0:
                                        return
                                board[Y-direction[2]][X-direction[2]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                        if player==-1:
                            if board[Y-direction[2]][X-direction[2]]>=0:
                                for k in range(1,direction[2]):
                                    if board[Y-k][X-k]>0:
                                        return
                                board[Y-direction[2]][X-direction[2]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                except:
                    return
            if (a+direction[2])*80<=x and x<=(a+direction[2])*80+80 and (b+direction[2])*80<=y and y<=(b+direction[2])*80+80:
                try:
                    if board[Y+direction[2]][X+direction[2]]!=9:
                        if player==1:
                            if board[Y+direction[2]][X+direction[2]]<=0:
                                for k in range(1,direction[2]):
                                    if board[Y+k][X+k]<0:
                                        return
                                board[Y+direction[2]][X+direction[2]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                        if player==-1:
                            if board[Y+direction[2]][X+direction[2]]>=0:
                                for k in range(1,direction[2]):
                                    if board[Y+k][X+k]>0:
                                        return
                                board[Y+direction[2]][X+direction[2]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                except:
                    return
            if (a-direction[3])*80<=x and x<=(a-direction[3])*80+80 and (b+direction[3])*80<=y and y<=(b+direction[3])*80+80:
                try:
                    if board[Y+direction[3]][X-direction[3]]!=9:
                        if player==1:
                            if board[Y+direction[3]][X-direction[3]]<=0:
                                for k in range(1,direction[3]):
                                    if board[Y+k][X-k]<0:
                                        return
                                board[Y+direction[3]][X-direction[3]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                        if player==-1:
                            if board[Y+direction[3]][X-direction[3]]>=0:
                                for k in range(1,direction[3]):
                                    if board[Y+k][X-k]>0:
                                        return
                                board[Y+direction[3]][X-direction[3]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                except:
                    return
            if (a+direction[3])*80<=x and x<=(a+direction[3])*80+80 and (b-direction[3])*80<=y and y<=(b-direction[3])*80+80:
                try:
                    if board[Y-direction[3]][X+direction[3]]!=9:
                        if player==1:
                            if board[Y-direction[3]][X+direction[3]]<=0:
                                for k in range(1,direction[3]):
                                    if board[Y-k][X+k]<0:
                                        return
                                board[Y-direction[3]][X+direction[3]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                        if player==-1:
                            if board[Y-direction[3]][X+direction[3]]>=0:
                                for k in range(1,direction[3]):
                                    if board[Y-k][X+k]>0:
                                        return
                                board[Y-direction[3]][X+direction[3]]=board[Y][X]
                                board[Y][X]=0
                                check=0
                                player*=-1
                                X=10
                                Y=10
                                a=10
                                b=10
                except:
                    return

def win_check():
    global index,tmr
    white1=0
    white2=0
    black1=0
    black2=0
    white_c=[]
    black_c=[]
    for y in range(10):
        white_c.append([0]*10)
        black_c.append([0]*10)
    for y in range(1,9):
        for x in range(1,9):
            if board[y][x]==1 or board[y][x]==2:
                white_c[y][x]=1
                break
        else:
            continue
        break
    for y in range(1,9):
        for x in range(1,9):
            if board[y][x]<0:
                black_c[y][x]=1
                break
        else:
            continue
        break
    for y in range(1,9):
        for x in range(1,9):
            if white_c[y][x]==1:
                if board[y-1][x-1]==1 and board[y-1][x-1]<=2:
                    white_c[y-1][x-1]=1
                if 1<=board[y-1][x] and board[y-1][x]<=2:
                    white_c[y-1][x]=1
                if 1<=board[y-1][x+1] and board[y-1][x+1]<=2:
                    white_c[y-1][x+1]=1
                if 1<=board[y][x-1] and board[y][x-1]<=2:
                    white_c[y][x-1]=1
                if 1<=board[y][x+1] and board[y][x+1]<=2:
                    white_c[y][x+1]=1
                if 1<=board[y+1][x-1] and board[y+1][x-1]<=2:
                    white_c[y+1][x-1]=1
                if 1<=board[y+1][x] and board[y+1][x]<=2:
                    white_c[y+1][x]=1
                if 1<=board[y+1][x+1] and board[y+1][x+1]<=2:
                    white_c[y+1][x+1]=1
            if black_c[y][x]==1:
                if board[y-1][x-1]<0:
                    black_c[y-1][x-1]=1
                if board[y-1][x]<0:
                    black_c[y-1][x]=1
                if board[y-1][x+1]<0:
                    black_c[y-1][x+1]=1
                if board[y][x-1]<0:
                    black_c[y][x-1]=1
                if board[y][x+1]<0:
                    black_c[y][x+1]=1
                if board[y+1][x-1]<0:
                    black_c[y+1][x-1]=1
                if board[y+1][x]<0:
                    black_c[y+1][x]=1
                if board[y+1][x+1]<0:
                    black_c[y+1][x+1]=1
    for y in range(1,9):
        for x in range(1,9):
            if white_c[y][x]==1:
                white1+=1
            if black_c[y][x]==1:
                black1+=1
            if board[y][x]>0:
                white2+=1
            if board[y][x]<0:
                black2+=1
    if white1==white2:
        index=2
        tmr=0
    if black1==black2:
        index=3
        tmr=0

def init():
    global player,check,X,Y,a,b
    for y in range(1,9):
        for x in range(1,9):
            board[y][x]=0
    for i in range(2,8):
        board[8][i]=1
        board[1][i]=2
        board[i][1]=-1
        board[i][8]=-2
    X=0
    Y=0
    a=8
    b=8
    player=1
    check=0

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+2,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x,y])

def main():
    pygame.init()
    pygame.display.set_caption("LINES OF ACTION")
    screen=pygame.display.set_mode((640,640))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,100)
    fontB=pygame.font.Font(None,120)

    while True:
        global index,tmr,mouse_c,x,y
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((640,640),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.displya.set_mode((640,640))
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,b1,b2=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",50,480,font,WHITE)
            if key[K_SPACE]:
                index=1
                init()
        if index==1:
            move()
            click()
            win_check()
            draw(screen)
        if index==2:
            draw_text(screen,"WHITE WIN!!",60,280,fontB,WHITE)
            if tmr>=50:
                index=0
        if index==3:
            draw_text(screen,"BLACK WIN!!",60,280,fontB,BLACK)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
