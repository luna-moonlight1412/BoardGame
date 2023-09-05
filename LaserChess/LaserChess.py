import pygame
import sys
from pygame.locals import*

# ＋=RED, －=WHITE, 1=RED_LASER↓, 2=RED_LASER→, -1=WHITE_LASER↑, -2=WHITE_LASER←
# 3=↗, 4=↘, 5=↙, 6=↖
# 7=SHIELD↓, 8=SHIELD→, 9=SHIELD↑, 10=SHIELD←
# 11=BOTHSIDE_MIRROR／, 12=BOTHSIDE_MIRROR＼, 13=KING, 14=WALL

index=0
tmr=0
mode=0
player=1
mouse_c=0
check=0
x=0
y=0
X=800
Y=800
a=0
b=0
A=0
B=0
L_x=0
L_y=0
l_x=0
l_y=0
cl_x=40
cl_y=40
xp=40
yp=40
l_check=0
reflect=0

RED=(255,0,0)
WHITE=(255,255,255)
YELLOW=(255,255,0)
BLACK=(0,0,0)
BLINK = [(224,255,255), (192,240,255), (128,224,255), (64,192,255), (128,224,255), (192,240,255)]

Board=pygame.image.load("image/board.png")
MIRROR_R=[
    pygame.image.load("image/mirror_red1.png"),
    pygame.image.load("image/mirror_red2.png"),
    pygame.image.load("image/mirror_red3.png"),
    pygame.image.load("image/mirror_red4.png")
    ]

MIRROR_W=[
    pygame.image.load("image/mirror_white1.png"),
    pygame.image.load("image/mirror_white2.png"),
    pygame.image.load("image/mirror_white3.png"),
    pygame.image.load("image/mirror_white4.png")
    ]

BOTH_MIRROR_R=[
    pygame.image.load("image/both_mirror_red1.png"),
    pygame.image.load("image/both_mirror_red2.png")
    ]

BOTH_MIRROR_W=[
    pygame.image.load("image/both_mirror_white1.png"),
    pygame.image.load("image/both_mirror_white2.png")
    ]

LASER_R=[
    pygame.image.load("image/laser_red1.png"),
    pygame.image.load("image/laser_red2.png")
    ]

LASER_W=[
    pygame.image.load("image/laser_white1.png"),
    pygame.image.load("image/laser_white2.png")
    ]

SHIELD_R=[
    pygame.image.load("image/shield_red1.png"),
    pygame.image.load("image/shield_red2.png"),
    pygame.image.load("image/shield_red3.png"),
    pygame.image.load("image/shield_red4.png")
    ]

SHIELD_W=[
    pygame.image.load("image/shield_white1.png"),
    pygame.image.load("image/shield_white2.png"),
    pygame.image.load("image/shield_white3.png"),
    pygame.image.load("image/shield_white4.png")
    ]
KING_R=pygame.image.load("image/king_red.png")
KING_W=pygame.image.load("image/king_white.png")
TITLE=pygame.image.load("image/title.png")
MODE=pygame.image.load("image/title2.png")
HELP=pygame.image.load("image/help.png")


board=[
        [14,14,14,14,14,14,14,14,14,14,14,14],
        [14,0,1,0,0,0,0,0,0,2,1,14],
        [14,2,0,0,0,0,0,0,0,0,1,14],
        [14,2,0,0,0,0,0,0,0,0,1,14],
        [14,2,0,0,0,0,0,0,0,0,1,14],
        [14,2,0,0,0,0,0,0,0,0,1,14],
        [14,2,0,0,0,0,0,0,0,0,1,14],
        [14,2,0,0,0,0,0,0,0,0,1,14],
        [14,2,1,0,0,0,0,0,0,2,0,14],
        [14,14,14,14,14,14,14,14,14,14,14,14]
        ]

checkp=[]
piece=[]
for y in range(10):
    piece.append([14]*12)
    checkp.append([0]*12)
for y in range(1,9):
    for x in range(1,11):
        piece[y][x]=0

def piece_init():
    for y in range(1,9):
        for x in range(1,11):
            piece[y][x]=0
    if mode==1: #ACE
        piece[1][1]=1
        piece[1][5]=7
        piece[1][6]=13
        piece[1][7]=7
        piece[1][8]=4
        piece[2][3]=5
        piece[3][4]=-6
        piece[4][1]=3
        piece[4][3]=-5
        piece[4][5]=12
        piece[4][6]=11
        piece[4][8]=4
        piece[4][10]=-6
        piece[5][1]=4
        piece[5][3]=-6
        piece[5][5]=-11
        piece[5][6]=-12
        piece[5][8]=3
        piece[5][10]=-5
        piece[6][7]=4
        piece[7][8]=-3
        piece[8][3]=-6
        piece[8][4]=-9
        piece[8][5]=-13
        piece[8][6]=-9
        piece[8][10]=-1

    if mode==2: #CURIOSITY
        piece[1][1]=1
        piece[1][5]=7
        piece[1][6]=13
        piece[1][7]=7
        piece[1][8]=11
        piece[3][4]=-6
        piece[3][7]=3
        piece[4][1]=3
        piece[4][2]=-5
        piece[4][5]=-4
        piece[4][6]=11
        piece[4][9]=4
        piece[4][10]=-6
        piece[5][1]=4
        piece[5][2]=-6
        piece[5][5]=-11
        piece[5][6]=6
        piece[5][9]=3
        piece[5][10]=-5
        piece[6][4]=-5
        piece[6][7]=4
        piece[8][3]=-11
        piece[8][4]=-9
        piece[8][5]=-13
        piece[8][6]=-9
        piece[8][10]=-1

    if mode==3: #GRAIL
        piece[1][1]=1
        piece[1][5]=5
        piece[1][6]=7
        piece[1][7]=4
        piece[2][6]=13
        piece[3][1]=3
        piece[3][5]=5
        piece[3][6]=7
        piece[3][7]=11
        piece[4][1]=4
        piece[4][3]=12
        piece[4][5]=-6
        piece[4][7]=-4
        piece[5][4]=6
        piece[5][6]=4
        piece[5][8]=-12
        piece[5][10]=-6
        piece[6][4]=-11
        piece[6][5]=-9
        piece[6][6]=-3
        piece[6][10]=-5
        piece[7][5]=-13
        piece[8][4]=-6
        piece[8][5]=-9
        piece[8][6]=-3
        piece[8][10]=-1

    if mode==4: #MERCURY
        piece[1][1]=2
        piece[1][5]=5
        piece[1][6]=13
        piece[1][7]=4
        piece[1][10]=-11
        piece[2][6]=7
        piece[2][7]=4
        piece[3][1]=4
        piece[3][4]=11
        piece[3][6]=7
        piece[4][1]=3
        piece[4][5]=-6
        piece[4][9]=-5
        piece[5][2]=3
        piece[5][6]=4
        piece[5][10]=-5
        piece[6][5]=-9
        piece[6][7]=-11
        piece[6][10]=-6
        piece[7][4]=-6
        piece[7][5]=-9
        piece[8][1]=11
        piece[8][4]=-6
        piece[8][5]=-13
        piece[8][6]=-3
        piece[8][10]=-2

    if mode==5: #SOPHIE
        piece[1][1]=1
        piece[1][5]=13
        piece[1][6]=-6
        piece[1][7]=4
        piece[2][4]=7
        piece[2][6]=10
        piece[2][10]=-5
        piece[3][1]=3
        piece[3][5]=5
        piece[3][6]=4
        piece[3][8]=-11
        piece[3][10]=-6
        piece[4][8]=12
        piece[5][3]=-12
        piece[6][1]=4
        piece[6][3]=11
        piece[6][5]=-6
        piece[6][6]=-3
        piece[6][10]=-5
        piece[7][1]=3
        piece[7][5]=-8
        piece[7][7]=-9
        piece[8][4]=-6
        piece[8][5]=4
        piece[8][6]=-13
        piece[8][10]=-1

def set_mode():
    global mode,index
    if mouse_c==1 and 13<=x and x<=262 and 106<=y and y<=306:
        mode=1
        index=2
    if mouse_c==1 and 537<=x and x<=787 and 106<=y and y<=306:
        mode=2
        index=2
    if mouse_c==1 and 274<=x and x<=524 and 259<=y and y<=459:
        mode=3
        index=2
    if mouse_c==1 and 13<=x and x<=262 and 417<=y and y<=617:
        mode=4
        index=2
    if mouse_c==1 and 537<=x and x<=787 and 417<=y and y<=617:
        mode=5
        index=2
    

def draw_piece(bg):
    bg.blit(Board,[0,0])
    for y in range(1,9):
        for x in range(1,11):
            if piece[y][x]>0:
                if 1<=piece[y][x] and piece[y][x]<=2:
                    bg.blit(LASER_R[piece[y][x]%2],[80*(x-1),80*(y-1)])
                if 3<=piece[y][x] and piece[y][x]<=6:
                    bg.blit(MIRROR_R[piece[y][x]%4],[80*(x-1),80*(y-1)])
                if 7<=piece[y][x] and piece[y][x]<=10:
                    bg.blit(SHIELD_R[piece[y][x]%4],[80*(x-1),80*(y-1)])
                if 11<=piece[y][x] and piece[y][x]<=12:
                    bg.blit(BOTH_MIRROR_R[piece[y][x]%2],[80*(x-1),80*(y-1)])
                if piece[y][x]==13:
                    bg.blit(KING_R,[80*(x-1),80*(y-1)])
            if piece[y][x]<0:
                if -2<=piece[y][x] and piece[y][x]<=-1:
                    bg.blit(LASER_W[piece[y][x]%2],[80*(x-1),80*(y-1)])
                if -6<=piece[y][x] and piece[y][x]<=-3:
                    bg.blit(MIRROR_W[piece[y][x]*(-1)%4],[80*(x-1),80*(y-1)])
                if -10<=piece[y][x] and piece[y][x]<=-7:
                    bg.blit(SHIELD_W[piece[y][x]*(-1)%4],[80*(x-1),80*(y-1)])
                if -12<=piece[y][x] and piece[y][x]<=-11:
                    bg.blit(BOTH_MIRROR_W[piece[y][x]%2],[80*(x-1),80*(y-1)])
                if piece[y][x]==-13:
                    bg.blit(KING_W,[80*(x-1),80*(y-1)])

def rotate_piece(key):
    global X,Y,check,player,a,b,index
    a=int(X/80+1)
    b=int(Y/80+1)
    if key[K_DOWN]:
        X=800
        Y=800
        check=0
        
    if key[K_RIGHT] and check==1 and player==1:
        if 1<=piece[b][a] and piece[b][a]<=2:
            piece[b][a]+=1
            if piece[b][a]==3:
                piece[b][a]=1
        if 3<=piece[b][a] and piece[b][a]<=6:
            piece[b][a]+=1
            if piece[b][a]==7:
                piece[b][a]=3
        if 7<=piece[b][a] and piece[b][a]<=10:
            piece[b][a]+=1
            if piece[b][a]==11:
                piece[b][a]=7
        if 11<=piece[b][a] and piece[b][a]<=12:
            piece[b][a]+=1
            if piece[b][a]==13:
                piece[b][a]=11
        if piece[b][a]==13:
            return
        X=800
        Y=800
        check=0
        player*=-1
        index=4
            
    if key[K_LEFT] and check==1 and player==1:
        if 1<=piece[b][a] and piece[b][a]<=2:
            piece[b][a]+=-1
            if piece[b][a]==0:
                piece[b][a]=2
        if 3<=piece[b][a] and piece[b][a]<=6:
            piece[b][a]+=-1
            if piece[b][a]==2:
                piece[b][a]=6
        if 7<=piece[b][a] and piece[b][a]<=10:
            piece[b][a]+=-1
            if piece[b][a]==6:
                piece[b][a]=10
        if 11<=piece[b][a] and piece[b][a]<=12:
            piece[b][a]+=-1
            if piece[b][a]==10:
                piece[b][a]=12
        if piece[b][a]==13:
            return
        X=800
        Y=800
        check=0
        player*=-1
        index=4

    if key[K_RIGHT] and check==1 and player==-1:
        if -2<=piece[b][a] and piece[b][a]<=-1:
            piece[b][a]+=-1
            if piece[b][a]==-3:
                piece[b][a]=-1
        if -6<=piece[b][a] and piece[b][a]<=-3:
            piece[b][a]+=-1
            if piece[b][a]==-7:
                piece[b][a]=-3
        if -10<=piece[b][a] and piece[b][a]<=-7:
            piece[b][a]+=-1
            if piece[b][a]==-11:
                piece[b][a]=-7
        if -12<=piece[b][a] and piece[b][a]<=-11:
            piece[b][a]+=-1
            if piece[b][a]==-13:
                piece[b][a]=-11
        if piece[b][a]==-13:
            return
        X=800
        Y=800
        check=0
        player*=-1
        index=4
            
    if key[K_LEFT] and check==1 and player==-1:
        if -2<=piece[b][a] and piece[b][a]<=-1:
            piece[b][a]+=1
            if piece[b][a]==0:
                piece[b][a]=-2
        if -6<=piece[b][a] and piece[b][a]<=-3:
            piece[b][a]+=1
            if piece[b][a]==-2:
                piece[b][a]=-6
        if -10<=piece[b][a] and piece[b][a]<=-7:
            piece[b][a]+=1
            if piece[b][a]==-6:
                piece[b][a]=-10
        if -12<=piece[b][a] and piece[b][a]<=-11:
            piece[b][a]+=1
            if piece[b][a]==-10:
                piece[b][a]=-12
        if piece[b][a]==-13:
            return
        X=800
        Y=800
        check=0
        player*=-1
        index=4

def move_piece():
    global X,Y,x,y,a,b,check,mouse_c,player,index
    if check==1 and a*80-160<=x and x<=a*80+80 and b*80-160<=y and y<=b*80+80:
        if a*80-80<=x and x<=a*80 and b*80-80<=y and y<=b*80:
            return
        elif piece[b][a]==1 or piece[b][a]==-1 or piece[int(y/80+1)][int(x/80+1)]==1 or piece[int(y/80+1)][int(x/80+1)]==-1:
            return
        elif mouse_c==1:
            if player==1:
                if board[int(y/80+1)][int(x/80+1)]==1:
                    return
                if board[b][a]==2 and piece[int(y/80+1)][int(x/80+1)]<0:
                    return
            elif player==-1:
                if board[int(y/80+1)][int(x/80+1)]==2:
                    return
                if board[b][a]==1 and piece[int(y/80+1)][int(x/80+1)]>0:
                    return
            piece[b][a]=checkp[int(y/80+1)][int(x/80+1)]
            piece[int(y/80+1)][int(x/80+1)]=checkp[b][a]
            check=0
            X=800
            Y=800
            player*=-1
            index=4
            
def turn(bg,key):
    global player,X,Y,check
    for k in range(10):
            for l in range(12):
                checkp[k][l]=piece[k][l]
    rotate_piece(key)
    move_piece()
    if player==1 and check==0:
        if mouse_c==1:
            if piece[int(y/80+1)][int(x/80+1)]>0:
                X=x
                Y=y
                check=1
    if player==-1 and check==0:
        if mouse_c==1:
            if piece[int(y/80+1)][int(x/80+1)]<0:
                X=x
                Y=y
                check=1
    draw_piece(bg)
    pygame.draw.rect(bg,YELLOW,[int(X/80)*80,int(Y/80)*80,80,80],3)
                
        
def draw_laser(bg):
    global l_x,l_y,l_check,A,B,xp,yp,tmr,cl_x,cl_y,L_x,L_y,index,reflect
    for k in range(10):
            for l in range(12):
                checkp[k][l]=piece[k][l]
    if l_check==0:
        if player==-1:
            if piece[1][1]==1:
                A=[40,80]
                l_x=40
                l_y=80
                cl_x=l_x
                cl_y=l_y
                B=[l_x,l_y]
                l_check=1
            if piece[1][1]==2:
                A=[80,40]
                l_x=80
                l_y=40
                cl_x=l_x
                cl_y=l_y
                B=[l_x,l_y]
                l_check=2
        if player==1:
            if piece[8][10]==-1:
                A=[760,560]
                l_x=760
                l_y=560
                cl_x=l_x
                cl_y=l_y
                B=[l_x,l_y]
                l_check=3
            if piece[8][10]==-2:
                A=[720,600]
                l_x=720
                l_y=600
                cl_x=l_x
                cl_y=l_y
                B=[l_x,l_y]
                l_check=4
                
    L_x=int(l_x/80+1)
    L_y=int(l_y/80+1)
    
    if l_check==1:
        l_y=tmr*yp+cl_y
        B=[l_x,l_y]
        if piece[L_y][L_x]==1 or piece[L_y][L_x]==-1 or piece[L_y][L_x]==2 or piece[L_y][L_x]==-2:
            l_check=5
        if piece[2][1]==3 or piece[2][1]==-3:
            if reflect==0 and player==-1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=2
                reflect=1
        if piece[L_y][L_x]==3 or piece[L_y][L_x]==-3:
            if tmr>1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=2
        if piece[L_y][L_x]==4 or piece[L_y][L_x]==-4:
            if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[L_y][L_x]==5 or piece[L_y][L_x]==-5:
            if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[2][1]==6 or piece[2][1]==-6:
            if reflect==0 and player==-1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=4
                reflect=1
        if piece[L_y][L_x]==6 or piece[L_y][L_x]==-6:
            if tmr>1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=4
        if piece[L_y][L_x]==7 or piece[L_y][L_x]==-7:
            if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[L_y][L_x]==8 or piece[L_y][L_x]==-8:
            if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[L_y][L_x]==9 or piece[L_y][L_x]==-9:
            l_check=5
        if piece[L_y][L_x]==10 or piece[L_y][L_x]==-10:
            if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[2][1]==11 or piece[2][1]==-11:
            if reflect==0 and player==-1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=4
                reflect=1
        if piece[L_y][L_x]==11 or piece[L_y][L_x]==-11:
            if tmr>1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=4
        if piece[2][1]==12 or piece[2][1]==-12:
            if reflect==0 and player==-1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=2
                reflect=1
        if piece[L_y][L_x]==12 or piece[L_y][L_x]==-12:
            if tmr>1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=2
        if piece[L_y][L_x]==13:
            if tmr>1:
                piece[L_y][L_x]=0
                index=5
                tmr=0
        if piece[L_y][L_x]==-13:
            if tmr>1:
                piece[L_y][L_x]=0
                index=6
                tmr=0
        if piece[L_y][L_x]==14 or piece[L_y][L_x]==-14:
            l_check=5
                    
    if l_check==2:
        l_x=tmr*xp+cl_x
        B=[l_x,l_y]
        if piece[L_y][L_x]==1 or piece[L_y][L_x]==-1 or piece[L_y][L_x]==2 or piece[L_y][L_x]==-2:
            l_check=5
        if piece[L_y][L_x]==3 or piece[L_y][L_x]==-3:
             if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[L_y][L_x]==4 or piece[L_y][L_x]==-4:
            if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[1][2]==5 or piece[1][2]==-5:
            if player==-1 and reflect==0:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                reflect=1
                l_check=1
        if piece[L_y][L_x]==5 or piece[L_y][L_x]==-5:
            if tmr>1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=1
        if piece[1][2]==6 or piece[1][2]==-6:
            if player==-1 and reflect==0:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                reflect=1
                l_check=3
        if piece[L_y][L_x]==6 or piece[L_y][L_x]==-6:
            if tmr>1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=3
        if piece[L_y][L_x]==7 or piece[L_y][L_x]==-7:
            if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[L_y][L_x]==8 or piece[L_y][L_x]==-8:
            l_check=5
        if piece[L_y][L_x]==9 or piece[L_y][L_x]==-9:
            if tmr>1:
                piece[L_y][L_x]=0
                l_check=5
        if piece[L_y][L_x]==10 or piece[L_y][L_x]==-10:
            piece[L_y][L_x]=0
            l_check=5
        if piece[1][2]==11 or piece[1][2]==-11:
            if player==-1 and reflect==0:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                reflect=1
                l_check=3
        if piece[L_y][L_x]==11 or piece[L_y][L_x]==-11:
            if tmr>1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=3
        if piece[1][2]==12 or piece[1][2]==-12:
            if player==-1 and reflect==0:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                reflect=1
                l_check=1
        if piece[L_y][L_x]==12 or piece[L_y][L_x]==-12:
            if tmr>1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=1
        if piece[L_y][L_x]==13:
            if tmr>1:
                piece[L_y][L_x]=0
                index=5
                tmr=0
        if  piece[L_y][L_x]==-13:
            if tmr>1:
                piece[L_y][L_x]=0
                index=6
                tmr=0
        if piece[L_y][L_x]==14 or piece[L_y][L_x]==-14:
            l_check=5

    if l_check==3:
        l_y=tmr*yp*(-1)+cl_y
        B=[l_x,l_y]
        if piece[L_y-1][L_x]==1 or piece[L_y-1][L_x]==-1 or piece[L_y-1][L_x]==2 or piece[L_y-1][L_x]==-2:
            l_check=5
        if piece[L_y-1][L_x]==3 or piece[L_y-1][L_x]==-3:
            if tmr>0:
                piece[L_y-1][L_x]=0
                l_check=5
        if piece[7][10]==4 or piece[7][10]==-4:
            if reflect==0 and player==1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=2
                reflect=1
        if piece[L_y-1][L_x]==4 or piece[L_y-1][L_x]==-4:
            if tmr>0:
                l_y-=40
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=2
        if piece[7][10]==5 or piece[7][10]==-5:
            if reflect==0 and player==1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=4
                reflect=1
        if piece[L_y-1][L_x]==5 or piece[L_y-1][L_x]==-5:
            if tmr>0:
                l_y-=40
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=4
        if piece[L_y-1][L_x]==6 or piece[L_y-1][L_x]==-6:
            if tmr>0:
                piece[L_y-1][L_x]=0
                l_check=5
        if piece[L_y-1][L_x]==7 or piece[L_y-1][L_x]==-7:
            l_check=5
        if piece[L_y-1][L_x]==8 or piece[L_y-1][L_x]==-8:
            if tmr>0:
                piece[L_y-1][L_x]=0
                l_check=5
        if piece[L_y-1][L_x]==9 or piece[L_y-1][L_x]==-9:
            if tmr>0:
                piece[L_y-1][L_x]=0
                l_check=5
        if piece[L_y-1][L_x]==10 or piece[L_y-1][L_x]==-10:
            if tmr>0:
                piece[L_y-1][L_x]=0
                l_check=5
        if piece[7][10]==11 or piece[7][10]==-11:
            if reflect==0 and player==1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=2
                reflect=1
        if piece[L_y-1][L_x]==11 or piece[L_y-1][L_x]==-11:
            if tmr>0:
                l_y-=40
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=2
        if piece[7][10]==12 or piece[7][10]==-12:
            if reflect==0 and player==1:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=4
                reflect=1
        if piece[L_y-1][L_x]==12 or piece[L_y-1][L_x]==-12:
            if tmr>0:
                l_y-=40
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=4
        if piece[L_y-1][L_x]==13:
            if tmr>0:
                piece[L_y-1][L_x]=0
                index=5
                tmr=0
        if piece[L_y-1][L_x]==-13:
            if tmr>0:
                piece[L_y-1][L_x]=0
                index=6
                tmr=0
        if piece[L_y-1][L_x]==14 or piece[L_y-1][L_x]==-14:
            l_check=5
                    
    if l_check==4:
        l_x=tmr*xp*(-1)+cl_x
        B=[l_x,l_y]
        if piece[L_y][L_x-1]==1 or piece[L_y][L_x-1]==-1 or piece[L_y][L_x-1]==2 or piece[L_y][L_x-1]==-2:
            l_check=5
        if piece[8][9]==3 or piece[8][9]==-3:
            if reflect==0 and player==1 and piece[8][10]==-2:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                reflect=1
                l_check=3
        if piece[L_y][L_x-1]==3 or piece[L_y][L_x-1]==-3:
            if tmr>0:
                l_x-=40
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=3
        if piece[8][9]==4 or piece[8][9]==-4:
            if reflect==0 and player==1 and piece[8][10]==-2:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                reflect=1
                l_check=1
        if piece[L_y][L_x-1]==4 or piece[L_y][L_x-1]==-4:
            if tmr>0:
                l_x-=40
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=1
        if piece[L_y][L_x-1]==5 or piece[L_y][L_x-1]==-5:
            if tmr>0:
                piece[L_y][L_x-1]=0
                l_check=5
        if piece[L_y][L_x-1]==6 or piece[L_y][L_x-1]==-6:
            if tmr>0:
                piece[L_y][L_x-1]=0
                l_check=5
        if piece[L_y][L_x-1]==7 or piece[L_y][L_x-1]==-7:
            if tmr>0:
                piece[L_y][L_x-1]=0
                l_check=5
        if piece[L_y][L_x-1]==8 or piece[L_y][L_x-1]==-8:
            piece[L_y][L_x-1]=0
            l_check=5
        if piece[L_y][L_x-1]==9 or piece[L_y][L_x-1]==-9:
            if tmr>0:
                piece[L_y][L_x-1]=0
                l_check=5
        if piece[L_y][L_x-1]==10 or piece[L_y][L_x-1]==-10:
            l_check=5
        if piece[8][9]==11 or piece[8][9]==-11:
            if reflect==0 and player==1 and piece[8][10]==-2:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                reflect=1
                l_check=1
        if piece[L_y][L_x-1]==11 or piece[L_y][L_x-1]==-11:
            if tmr>0:
                l_x-=40
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=1
        if piece[8][9]==12 or piece[8][9]==-12:
            if reflect==0 and player==1 and piece[8][10]==-2:
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                reflect=1
                l_check=3
        if piece[L_y][L_x-1]==12 or piece[L_y][L_x-1]==-12:
            if tmr>0:
                l_x-=40
                A=[l_x,l_y]
                cl_x=l_x
                cl_y=l_y
                tmr=0
                l_check=3
        if piece[L_y][L_x-1]==13:
            if tmr>0:
                piece[L_y][L_x-1]=0
                index=5
                tmr=0
        if  piece[L_y][L_x-1]==-13:
            if tmr>0:
                piece[L_y][L_x-1]
                index=6
                tmr=0
        if piece[L_y][L_x-1]==14 or piece[L_y][L_x-1]==-14:
            l_check=5
    if player==-1:
        pygame.draw.lines(bg,RED,False,[A,B],5)
    if player==1:
        pygame.draw.lines(bg,WHITE,False,[A,B],5)

def init():
    global mode,player,mouse_c,check
    global x,y,X,Y,a,b,A,B,L_x,L_y,l_x,l_y
    global cl_x,cl_y,xp,yp,l_check,reflect
    mode=0
    player=1
    mouse_c=0
    check=0
    x=0
    y=0
    X=800
    Y=800
    a=0
    b=0
    A=0
    B=0
    L_x=0
    L_y=0
    l_x=0
    l_y=0
    cl_x=40
    cl_y=40
    xp=40
    yp=40
    l_check=0
    reflect=0

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+1,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x, y])

def main():
    global index,tmr,player,mouse_c,x,y,l_check,reflect
    pygame.init()
    pygame.display.set_caption("LASER CHESS")
    screen=pygame.display.set_mode((800,640))
    clock=pygame.time.Clock()
    
    fontS=pygame.font.Font(None,40)
    font=pygame.font.Font(None, 80)
    fontB=pygame.font.Font(None, 160)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((800,640),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((800,640))
        tmr+=1
        key=pygame.key.get_pressed()
        mouseX,mouseY=pygame.mouse.get_pos()
        mBtn1,mBtn2,mBtn3=pygame.mouse.get_pressed()
        mouse_c=mBtn1
        x=mouseX
        y=mouseY
        
        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",180,430,font,BLINK[tmr%6])
            draw_text(screen,"[H]elp",700,10,fontS,WHITE)
            init()
            if key[K_SPACE]:
                index=1
            if key[K_h]:
                index=7
        elif index==1:
            screen.blit(MODE,[0,0])
            set_mode()
        elif index==2:
            piece_init()
            draw_piece(screen)
            index=3
        elif index==3:
            turn(screen,key)
            reflect=0
            tmr=0
        elif index==4:
            draw_laser(screen)
            if l_check==5:
                l_check=0
                index=3
        elif index==5:
            draw_text(screen,"WHITE WIN!!",50,250,fontB,WHITE)
            if tmr>=50:
                index=0
        elif index==6:
            draw_text(screen,"RED WIN!!",120,250,fontB,RED)
            if tmr>=50:
                index=0
        elif index==7:
            screen.blit(HELP,[0,0])
            if key[K_BACKSPACE]:
                index=0
        pygame.display.update()
        clock.tick(10)
            
if __name__=='__main__':
    main()
