import pygame
import sys
from pygame.locals import*

index=0
x=0
y=0
X=400
Y=400
check=0
black=0
white=0
mouse_c=0
player=1
tmr=0

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
P_B=pygame.image.load("image/piece_black.png")
P_W=pygame.image.load("image/piece_white.png")
HOLE=pygame.image.load("image/hole.png")

WHITE=(255,255,255)
BLACK=(0,0,0)
BROWN=(185,102,85)
YELLOW=(255,255,0)

board=[]
check_b=[]
judge1=[]
judge2=[]
for y in range(7):
    board.append([9]*7)
    check_b.append([9]*7)
    judge1.append([9]*7)
    judge2.append([9]*7)

def draw(bg):
    bg.blit(BOARD,[0,0])
    for y in range(1,6):
        for x in range(1,6):
            if board[y][x]==1:
                bg.blit(P_B,[(x-1)*80+3,(y-1)*80+2])
            if board[y][x]==-1:
                bg.blit(P_W,[(x-1)*80+3,(y-1)*80+2])
            if board[y][x]==8:
                bg.blit(HOLE,[(x-1)*80,(y-1)*80])
    pygame.draw.rect(bg,YELLOW,[int(X/80)*80,int(Y/80)*80,80,80],3)

def init():
    global player,check,black,white,X,Y
    for y in range(1,6):
        for x in range(1,6):
            board[y][x]=0
    for y in range(1,6):
        board[y][1]=1
        board[y][5]=-1
    board[3][3]=8

    X=400
    Y=400
    check=0
    player=1
    black=0
    white=0

def click():
    global X,Y,check,a,b
    if mouse_c==1:
        if board[int(y/80)+1][int(x/80+1)]==8:
            X=x
            Y=y
            a=int(X/80)+1
            b=int(Y/80)+1
            check=1
        if player==1:
            if board[int(y/80)+1][int(x/80+1)]==1:
                X=x
                Y=y
                a=int(X/80)+1
                b=int(Y/80)+1
                check=1
        if player==-1:
            if board[int(y/80)+1][int(x/80+1)]==-1:
                X=x
                Y=y
                a=int(X/80)+1
                b=int(Y/80)+1
                check=1


def same():
    if player==1 and check==0:
        for y in range(7):
            for x in range(7):
                judge1[y][x]=board[y][x]
    if player==-1 and check==0:
        for y in range(7):
            for x in range(7):
                judge2[y][x]=board[y][x]

def restart():
    global player,check
    judge=0
    if check==2:
        if player==1:
            for y in range(7):
                for x in range(7):
                    if judge1[y][x]==board[y][x]:
                        judge+=1
        if player==-1:
            for y in range(7):
                for x in range(7):
                    if judge2[y][x]==board[y][x]:
                        judge+=1
        check=0
        if judge==49:
            for y in range(7):
                for x in range(7):
                    board[y][x]=check_b[y][x]
                    check=1
                    player*=-1

def slide(key):
    global check,player,X,Y,black,white
    for y in range(7):
        for x in range(7):
            check_b[y][x]=board[y][x]
    if check==1:
        if board[b][a]==8:
            if key[K_UP]:
                if board[b-1][a]!=0:
                    return
                board[b-1][a]=8
                board[b][a]=0
                player*=-1
                check=2
                X=400
                Y=400
            if key[K_DOWN]:
                if board[b+1][a]!=0:
                    return
                board[b+1][a]=8
                board[b][a]=0
                player*=-1
                check=2
                X=400
                Y=400
            if key[K_RIGHT]:
                if board[b][a+1]!=0:
                    return
                board[b][a+1]=8
                board[b][a]=0
                player*=-1
                check=2
                X=400
                Y=400
            if key[K_LEFT]:
                if board[b][a-1]!=0:
                    return
                board[b][a-1]=8
                board[b][a]=0
                player*=-1
                check=2
                X=400
                Y=400

    if check==1:
        if key[K_UP]:
            if board[b-1][a]==9 or board[b-1][a]==8:
                return
            for i in range(b,-1,-1):
                if board[i][a]==8:
                    if board[i+1][a]==1:
                        black+=1
                    if board[i+1][a]==-1:
                        white+=1
                    board[i+1][a]=0
                    break
                elif abs(check_b[i][a])==1 and abs(check_b[i-1][a])==1:
                    board[i-1][a]=check_b[i][a]
                elif check_b[i-1][a]==0 or check_b[i-1][a]==9:
                    if check_b[i-1][a]==9:
                        if board[i][a]==1:
                            black+=1
                        if board[i][a]==-1:
                            white+=1
                    board[i-1][a]=check_b[i][a]
                    break
            board[b-1][a]=check_b[b][a]
            board[b][a]=0
            for i in range(1,6):
                board[0][i]=9
            player*=-1
            check=2
            X=400
            Y=400
        if key[K_DOWN]:
            if board[b+1][a]==9 or board[b+1][a]==8:
                return
            for i in range(b,6):
                if board[i][a]==8:
                    if board[i-1][a]==1:
                        black+=1
                    if board[i-1][a]==-1:
                        white+=1
                    board[i-1][a]=0
                    break
                elif abs(check_b[i][a])==1 and abs(check_b[i+1][a])==1:
                    board[i+1][a]=check_b[i][a]
                elif check_b[i+1][a]==0 or check_b[i+1][a]==9:
                    if check_b[i+1][a]==9:
                        if board[i][a]==1:
                            black+=1
                        if board[i][a]==-1:
                            white+=1
                    board[i+1][a]=check_b[i][a]
                    break
            board[b+1][a]=check_b[b][a]
            board[b][a]=0
            for i in range(1,6):
                board[6][i]=9
            player*=-1
            check=2
            X=400
            Y=400
        if key[K_RIGHT]:
            if board[b][a+1]==9 or board[b][a+1]==8:
                return
            for i in range(a,6):
                if board[b][i]==8:
                    if board[b][i-1]==1:
                        black+=1
                    if board[b][i-1]==-1:
                        white+=1
                    board[b][i-1]=0
                    break
                elif abs(check_b[b][i])==1 and abs(check_b[b][i+1])==1:
                    board[b][i+1]=check_b[b][i]
                elif check_b[b][i+1]==0 or check_b[b][i+1]==9:
                    if check_b[b][i+1]==9:
                        if board[b][i]==1:
                            black+=1
                        if board[b][i]==-1:
                            white+=1
                    board[b][i+1]=check_b[b][i]
                    break
            board[b][a+1]=check_b[b][a]
            board[b][a]=0
            for i in range(1,6):
                board[i][6]=9
            player*=-1
            check=2
            X=400
            Y=400
        if key[K_LEFT]:
            if board[b][a-1]==9 or board[b][a-1]==8:
                return
            for i in range(a,-1,-1):
                if board[b][i]==8:
                    if board[b][i+1]==1:
                        black+=1
                    if board[b][i+1]==-1:
                        white+=1
                    board[b][i+1]=0
                    break
                elif abs(check_b[b][i])==1 and abs(check_b[b][i-1])==1:
                    board[b][i-1]=check_b[b][i]
                elif check_b[b][i-1]==0 or check_b[b][i-1]==9:
                    if check_b[b][i-1]==9:
                        if board[b][i]==1:
                            black+=1
                        if board[b][i]==-1:
                            white+=1
                    board[b][i-1]=check_b[b][i]
                    break
            board[b][a-1]=check_b[b][a]
            board[b][a]=0
            for i in range(1,6):
                board[i][0]=9
            player*=-1
            check=2
            X=400
            Y=400

def draw_text(bg,txt,x,y,fnt,col):
    if index==3:
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
    global index,x,y,mouse_c,tmr
    pygame.init()
    pygame.display.set_caption("OSTLE")
    screen=pygame.display.set_mode((400,400))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,50)
    fontB=pygame.font.Font(None,90)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((400,400),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((400,400))

        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,b1,b2=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",70,315,font,BROWN)
            if key[K_SPACE]:
                init()
                index=1
        if index==1:
            same()
            click()
            slide(key)
            if black==2:
                index=2
            if white==2:
                index=3
            tmr=0
            restart()
            draw(screen)
        if index==2:
            draw_text(screen,"WHITE WIN!!",5,150,fontB,WHITE)
            if tmr>=50:
                index=0
        if index==3:
            draw_text(screen,"BLACK WIN!!",5,150,fontB,BLACK)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
