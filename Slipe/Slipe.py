import pygame
import sys
from pygame.locals import*

index=0
mode=4
x=0
y=0
mouse_c=0
player=1
X=400
Y=400
xp=5
yp=5
a=0
b=0
check=0
checkp=0
direction=0
tmr=0

BROWN=(185,102,85)
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
PIECE_B=pygame.image.load("image/piece_black.png")
PIECE_W=pygame.image.load("image/piece_white.png")
KING_B=pygame.image.load("image/king_black.png")
KING_W=pygame.image.load("image/king_white.png")
MODE=pygame.image.load("image/mode.png")

board=[]
piece=[]
for y in range(7):
    board.append([9]*7)
    piece.append([9]*7)

def set_mode():
    for y in range(1,6):
        for x in range(1,6):
            board[y][x]=0
            piece[y][x]=0
    board[3][3]=1
    if mode==1:
        for y in range(1,6):
            piece[y][1]=1
            piece[3][1]=2
            piece[y][5]=-1
            piece[3][5]=-2
    if mode==2:
        piece[1][1]=-1
        piece[1][3]=-2
        piece[1][5]=-1
        piece[3][1]=1
        piece[3][2]=-1
        piece[3][4]=1
        piece[3][5]=-1
        piece[5][1]=1
        piece[5][3]=2
        piece[5][5]=1
    if mode==3:
        piece[1][1]=-1
        piece[1][2]=-2
        piece[1][5]=1
        piece[2][1]=-1
        piece[3][1]=1
        piece[3][5]=-1
        piece[4][5]=1
        piece[5][1]=-1
        piece[5][4]=2
        piece[5][5]=1
    if mode==4:
        piece[1][1]=1
        piece[1][5]=-2
        piece[2][3]=-1
        piece[2][4]=-1
        piece[3][2]=1
        piece[3][4]=-1
        piece[4][2]=1
        piece[4][3]=1
        piece[5][1]=2
        piece[5][5]=-1
    if mode==5:
        piece[1][1]=1
        piece[1][3]=-1
        piece[1][5]=1
        piece[2][2]=-2
        piece[3][1]=1
        piece[3][5]=-1
        piece[4][4]=2
        piece[5][1]=-1
        piece[5][3]=1
        piece[5][5]=-1

def select_mode():
    global mode,index
    if mouse_c==1 and 8<=x and x<=128 and 78<=y and y<=198:
        mode=1
        index=2
    if mouse_c==1 and 268<=x and x<=388 and 78<=y and y<=198:
        mode=2
        index=2
    if mouse_c==1 and 132<=x and x<=252 and 182<=y and y<=302:
        mode=3
        index=2
    if mouse_c==1 and 8<=x and x<=128 and 269<=y and y<=389:
        mode=4
        index=2
    if mouse_c==1 and 268<=x and x<=388 and 269<=y and y<=389:
        mode=5
        index=2
    

def draw_piece(bg):
    bg.blit(BOARD,[0,0])
    for y in range(1,6):
        for x in range(1,6):
            if piece[y][x]==1:
                bg.blit(PIECE_B,[80*(x-1)+3,80*(y-1)+2])
            if piece[y][x]==2:
                bg.blit(KING_B,[80*(x-1)+3,80*(y-1)+2])
            if piece[y][x]==-1:
                bg.blit(PIECE_W,[80*(x-1)+3,80*(y-1)+2])
            if piece[y][x]==-2:
                bg.blit(KING_W,[80*(x-1)+3,80*(y-1)+2])

def move_piece(bg,key):
    global player,X,Y,check
    slide_piece(key)
    if player==1:
        if mouse_c==1:
            if piece[int(y/80+1)][int(x/80+1)]>0:
                X=x
                Y=y
                check=1
    if player==-1:
        if mouse_c==1:
            if piece[int(y/80+1)][int(x/80+1)]<0:
                X=x
                Y=y
                check=1
    draw_piece(bg)
    pygame.draw.rect(bg,YELLOW,[int(X/80)*80,int(Y/80)*80,80,80],3)

def slide_piece(key):
    global a,b,player,X,Y,checkp,index,direction,check
    a=int(X/80+1)
    b=int(Y/80+1)
    if key[K_UP] and check==1:
        if (piece[b][a]==1 or piece[b][a]==-1) and a==3 and (b==4 or b==5) and piece[2][3]!=0:
            return
        if piece[b-1][a]==0:
            checkp=piece[b][a]
            piece[b][a]=0
            player*=-1
            X=400
            Y=400
            index=3
            direction=1
            check=0
    if key[K_RIGHT] and check==1:
        if (piece[b][a]==1 or piece[b][a]==-1) and b==3 and (a==1 or a==2) and piece[3][4]!=0:
            return
        if piece[b][a+1]==0:
            checkp=piece[b][a]
            piece[b][a]=0
            player*=-1
            X=400
            Y=400
            index=3
            direction=2
            check=0
    if key[K_LEFT] and check==1:
        if (piece[b][a]==1 or piece[b][a]==-1) and b==3 and (a==4 or a==5) and piece[3][2]!=0:
            return
        if piece[b][a-1]==0:
            checkp=piece[b][a]
            piece[b][a]=0
            player*=-1
            X=400
            Y=400
            index=3
            direction=3
            check=0
    if key[K_DOWN] and check==1:
        if (piece[b][a]==1 or piece[b][a]==-1) and a==3 and (b==1 or b==2) and piece[4][3]!=0:
            return
        if piece[b+1][a]==0:
            checkp=piece[b][a]
            piece[b][a]=0
            player*=-1
            X=400
            Y=400
            index=3
            direction=4
            check=0

def moving_piece(bg):
    global index
    draw_piece(bg)
    if direction==1:
        if checkp==1:
            bg.blit(PIECE_B,[(a-1)*80+3,(b-1)*80-tmr*yp])
        if checkp==2:
            bg.blit(KING_B,[(a-1)*80+3,(b-1)*80-tmr*yp])
        if checkp==-1:
            bg.blit(PIECE_W,[(a-1)*80+3,(b-1)*80-tmr*yp])
        if checkp==-2:
            bg.blit(KING_W,[(a-1)*80+3,(b-1)*80-tmr*yp])
        if piece[int(((b-1)*80-tmr*yp)/80+1)][int(((a-1)*80)/80+1)]!=0:
            piece[int(((b-1)*80-tmr*yp)/80+2)][int(((a-1)*80)/80+1)]=checkp
            index=2
            
    if direction==2:
        if checkp==1:
            bg.blit(PIECE_B,[(a-1)*80+tmr*xp,(b-1)*80+2])
        if checkp==2:
            bg.blit(KING_B,[(a-1)*80+tmr*xp,(b-1)*80+2])
        if checkp==-1:
            bg.blit(PIECE_W,[(a-1)*80+tmr*xp,(b-1)*80+2])
        if checkp==-2:
            bg.blit(KING_W,[(a-1)*80+tmr*xp,(b-1)*80+2])
        if piece[int(((b-1)*80)/80+1)][int(((a-1)*80+tmr*xp)/80+2)]!=0:
            piece[int(((b-1)*80+2)/80+1)][int(((a-1)*80+tmr*xp)/80+1)]=checkp
            index=2

    if direction==3:
        if checkp==1:
            bg.blit(PIECE_B,[(a-1)*80-tmr*xp,(b-1)*80+2])
        if checkp==2:
            bg.blit(KING_B,[(a-1)*80-tmr*xp,(b-1)*80+2])
        if checkp==-1:
            bg.blit(PIECE_W,[(a-1)*80-tmr*xp,(b-1)*80+2])
        if checkp==-2:
            bg.blit(KING_W,[(a-1)*80-tmr*xp,(b-1)*80+2])
        if piece[int(((b-1)*80)/80+1)][int(((a-1)*80-tmr*xp)/80+1)]!=0:
            piece[int(((b-1)*80+2)/80+1)][int(((a-1)*80-tmr*xp)/80+2)]=checkp
            index=2

    if direction==4:
        if checkp==1:
            bg.blit(PIECE_B,[(a-1)*80+3,(b-1)*80+tmr*yp])
        if checkp==2:
            bg.blit(KING_B,[(a-1)*80+3,(b-1)*80+tmr*yp])
        if checkp==-1:
            bg.blit(PIECE_W,[(a-1)*80+3,(b-1)*80+tmr*yp])
        if checkp==-2:
            bg.blit(KING_W,[(a-1)*80+3,(b-1)*80+tmr*yp])
        if piece[int(((b-1)*80+tmr*yp)/80+2)][int(((a-1)*80)/80+1)]!=0:
            piece[int(((b-1)*80+tmr*yp)/80+1)][int(((a-1)*80)/80+1)]=checkp
            index=2
    
            
def init():
    global x,y,mouse_c,player
    x=0
    y=0
    mouse_c=0
    player=1

def draw_text(bg,txt,x,y,fnt,col):
    if index==4:
        sur=fnt.render(txt,True,WHITE)
        bg.blit(sur,[x+1,y+2])
        sur=fnt.render(txt,True,col)
        bg.blit(sur,[x,y])
    if index==5 or index==0:
        sur=fnt.render(txt,True,BLACK)
        bg.blit(sur,[x+1,y+2])
        sur=fnt.render(txt,True,col)
        bg.blit(sur,[x,y])

def main():
    global index,x,y,mouse_c,tmr
    pygame.init()
    pygame.display.set_caption("SLIPE")
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
        mouseX,mouseY=pygame.mouse.get_pos()
        mBtn1,mBtn2,mBtn3=pygame.mouse.get_pressed()
        mouse_c=mBtn1
        x=mouseX
        y=mouseY
        tmr+=1
            
        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",65,320,font,BROWN)
            if key[K_SPACE]:
                index=1
        if index==1:
            screen.blit(MODE,[0,0])
            select_mode()
            set_mode()
        if index==2:
            move_piece(screen,key)
            tmr=0
        if index==3:
            moving_piece(screen)
            if piece[3][3]==2:
                index=4
                tmr=0
            if piece[3][3]==-2:
                index=5
                tmr=0
        if index==4:
            draw_text(screen,"BLACK WIN!!",5,150,fontB,BLACK)
            if tmr>=500:
                index=0
        if index==5:
            draw_text(screen,"WHITE WIN!!",5,150,fontB,WHITE)
            if tmr>=500:
                index=0
        pygame.display.update()
        clock.tick(100)

if __name__=='__main__':
    main()
            
