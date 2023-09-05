import pygame
import sys
from pygame.locals import*

index=0
tmr=0
check=0
player=1
mouse_c=0
x=0
y=0
a=0
b=0
A=0
B=0
BL1=1
BL2=1
BM1=1
BM2=1
BS1=1
BS2=1
OL1=1
OL2=1
OM1=1
OM2=1
OS1=1
OS2=1

BLACK=(0,0,0)
YELLOW=(255,255,0)
ORANGE_C=(253,126,0)
BLUE_C=(169,206,236)
BLINK = [(224,255,255), (192,240,255), (128,224,255), (64,192,255), (128,224,255), (192,240,255),
         (255,247,239),(255,198,140),(253,126,0),(255,198,140),(255,247,239)]

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
BLUE=[
    pygame.image.load("image/blueL.png"),
    pygame.image.load("image/blueS.png"),
    pygame.image.load("image/blueM.png")
    ]
ORANGE=[
    pygame.image.load("image/orangeL.png"),
    pygame.image.load("image/orangeM.png"),
    pygame.image.load("image/orangeS.png")
    ]
BLUEC=pygame.image.load("image/bc.png")
ORANGEC=pygame.image.load("image/oc.png")
CHECK=[
    pygame.image.load("image/checkBL.png"),
    pygame.image.load("image/checkBL.png"),
    pygame.image.load("image/checkBM.png"),
    pygame.image.load("image/checkBM.png"),
    pygame.image.load("image/checkBS.png"),
    pygame.image.load("image/checkBS.png"),
    pygame.image.load("image/checkOL.png"),
    pygame.image.load("image/checkOL.png"),
    pygame.image.load("image/checkOM.png"),
    pygame.image.load("image/checkOM.png"),
    pygame.image.load("image/checkOS.png"),
    pygame.image.load("image/checkOS.png")
    ]

board=[]
boardS=[]
boardM=[]
def init():
    global player,check,BL1,BL2,BM1,BM2,BS1,BS2,OL1,OL2,OM1,OM2,OS1,OS2
    for y in range(5):
        board.append([9]*5)
        boardS.append([9]*5)
        boardM.append([9]*5)
    for y in range(1,4):
        for x in range(1,4):
            board[y][x]=0
            boardS[y][x]=0
            boardM[y][x]=0
    player=1
    check=0
    BL1=1
    BL2=1
    BM1=1
    BM2=1
    BS1=1
    BS2=1
    OL1=1
    OL2=1
    OM1=1
    OM2=1
    OS1=1
    OS2=1

def key_click(key):
    global check
    if key[K_DOWN]:
        check=0

def move_piece():
    global a,b,player,check
    a=int(A/150)
    b=int(B/150+1)
    if check>12 and mouse_c==1:
        if a*150<=x and x<=a*150+150 and b*150-150<=y and y<=b*150:
            return
        if board[b][a]==1 or board[b][a]==-1:
            if board[int(y/150+1)][int(x/150)]!=0:
                return
        if board[b][a]==2 or board[b][a]==-2:
            if board[int(y/150+1)][int(x/150)]==2 or board[int(y/150+1)][int(x/150)]==-2 or board[int(y/150+1)][int(x/150)]==3 or board[int(y/150+1)][int(x/150)]==-3:
                return
            if board[int(y/150+1)][int(x/150)]==1 or board[int(y/150+1)][int(x/150)]==-1:
                boardS[int(y/150+1)][int(x/150)]=board[int(y/150+1)][int(x/150)]
        if board[b][a]==3 or board[b][a]==-3:
            if board[int(y/150+1)][int(x/150)]==3 or board[int(y/150+1)][int(x/150)]==-3:
                return
            if board[int(y/150+1)][int(x/150)]==2 or board[int(y/150+1)][int(x/150)]==-2:
                boardM[int(y/150+1)][int(x/150)]=board[int(y/150+1)][int(x/150)]
            if board[int(y/150+1)][int(x/150)]==1 or board[int(y/150+1)][int(x/150)]==-1:
                boardS[int(y/150+1)][int(x/150)]=board[int(y/150+1)][int(x/150)]
        board[int(y/150+1)][int(x/150)]=board[b][a]
        if boardM[b][a]==0:
            board[b][a]=boardS[b][a]
            boardS[b][a]=0
        if boardM[b][a]!=0:
            board[b][a]=boardM[b][a]
            boardM[b][a]=0
        check=0
        player*=-1

def click(key):
    global check,player,A,B
    key_click(key)
    X=int(x/150)
    Y=int(y/150+1)
    if player==1:
        if mouse_c==1 and BL1==1 and 0<=x and x<=67 and 22<=y and y<=170: check=1
        if mouse_c==1 and BL2==1 and 70<=x and x<=137 and 22<=y and y<=170: check=2
        if mouse_c==1 and BM1==1 and 11<=x and x<=63 and 200<=y and y<=294: check=3
        if mouse_c==1 and BM2==1 and 77<=x and x<=137 and 200<=y and y<=294: check=4
        if mouse_c==1 and BS1==1 and 27<=x and x<=65 and 328<=y and y<=399: check=5
        if mouse_c==1 and BS2==1 and 78<=x and x<=114 and 328<=y and y<=399: check=6
        if check==0 and mouse_c==1 and 150<x and x<300 and 0<y and y<150 and board[Y][X]>0:
            check=13
            A=x
            B=y
        if check==0 and mouse_c==1 and 300<x and x<450 and 0<y and y<150 and board[Y][X]>0:
            check=14
            A=x
            B=y
        if check==0 and mouse_c==1 and 450<x and x<600 and 0<y and y<150 and board[Y][X]>0:
            check=15
            A=x
            B=y
        if check==0 and mouse_c==1 and 150<x and x<300 and 150<y and y<300 and board[Y][X]>0:
            check=16
            A=x
            B=y
        if check==0 and mouse_c==1 and 300<x and x<450 and 150<y and y<300 and board[Y][X]>0:
            check=17
            A=x
            B=y
        if check==0 and mouse_c==1 and 450<x and x<600 and 150<y and y<300 and board[Y][X]>0:
            check=18
            A=x
            B=y
        if check==0 and mouse_c==1 and 150<x and x<300 and 300<y and y<450 and board[Y][X]>0:
            check=19
            A=x
            B=y
        if check==0 and mouse_c==1 and 300<x and x<450 and 300<y and y<450 and board[Y][X]>0:
            check=20
            A=x
            B=y
        if check==0 and mouse_c==1 and 450<x and x<600 and 300<y and y<450 and board[Y][X]>0:
            check=21
            A=x
            B=y
        
    if player==-1:
        if mouse_c==1 and OL1==1 and 608<=x and x<=663 and 26<=y and y<=166: check=7
        if mouse_c==1 and OL2==1 and 675<=x and x<=741 and 26<=y and y<=166: check=8
        if mouse_c==1 and OM1==1 and 614<=x and x<=658 and 196<=y and y<=290: check=9
        if mouse_c==1 and OM2==1 and 679<=x and x<=733 and 196<=y and y<=290: check=10
        if mouse_c==1 and OS1==1 and 631<=x and x<=665 and 328<=y and y<=399: check=11
        if mouse_c==1 and OS2==1 and 679<=x and x<=713 and 328<=y and y<=399: check=12
        if check==0 and mouse_c==1 and 150<x and x<300 and 0<y and y<150 and board[Y][X]<0:
            check=13
            A=x
            B=y
        if check==0 and mouse_c==1 and 300<x and x<450 and 0<y and y<150 and board[Y][X]<0:
            check=14
            A=x
            B=y
        if check==0 and mouse_c==1 and 450<x and x<600 and 0<y and y<150 and board[Y][X]<0:
            check=15
            A=x
            B=y
        if check==0 and mouse_c==1 and 150<x and x<300 and 150<y and y<300 and board[Y][X]<0:
            check=16
            A=x
            B=y
        if check==0 and mouse_c==1 and 300<x and x<450 and 150<y and y<300 and board[Y][X]<0:
            check=17
            A=x
            B=y
        if check==0 and mouse_c==1 and 450<x and x<600 and 150<y and y<300 and board[Y][X]<0:
            check=18
            A=x
            B=y
        if check==0 and mouse_c==1 and 150<x and x<300 and 300<y and y<450 and board[Y][X]<0:
            check=19
            A=x
            B=y
        if check==0 and mouse_c==1 and 300<x and x<450 and 300<y and y<450 and board[Y][X]<0:
            check=20
            A=x
            B=y
        if check==0 and mouse_c==1 and 450<x and x<600 and 300<y and y<450 and board[Y][X]<0:
            check=21
            A=x
            B=y

def draw_check(bg):
    bg.blit(BOARD,[0,0])
    if check==1: bg.blit(CHECK[0],[-30,20])
    if check==2: bg.blit(CHECK[1],[40,20])
    if check==3: bg.blit(CHECK[2],[-40,170])
    if check==4: bg.blit(CHECK[3],[30,170])
    if check==5: bg.blit(CHECK[4],[-30,290])
    if check==6: bg.blit(CHECK[5],[20,290])
    if check==7: bg.blit(CHECK[6],[570,20])
    if check==8: bg.blit(CHECK[7],[640,20])
    if check==9: bg.blit(CHECK[8],[560,170])
    if check==10: bg.blit(CHECK[9],[630,170])
    if check==11: bg.blit(CHECK[10],[570,290])
    if check==12: bg.blit(CHECK[11],[620,290])
    if check==13: pygame.draw.rect(bg,YELLOW,[150,0,140,142],3)
    if check==14: pygame.draw.rect(bg,YELLOW,[310,0,130,142],3)
    if check==15: pygame.draw.rect(bg,YELLOW,[460,0,135,142],3)
    if check==16: pygame.draw.rect(bg,YELLOW,[150,162,140,132],3)
    if check==17: pygame.draw.rect(bg,YELLOW,[310,162,130,132],3)
    if check==18: pygame.draw.rect(bg,YELLOW,[460,162,135,132],3)
    if check==19: pygame.draw.rect(bg,YELLOW,[150,315,140,132],3)
    if check==20: pygame.draw.rect(bg,YELLOW,[310,315,130,132],3)
    if check==21: pygame.draw.rect(bg,YELLOW,[460,315,135,132],3)

def draw(bg):
    for y in range(1,4):
        for x in range(1,4):
            if board[y][x]>0:
                bg.blit(BLUE[board[y][x]%3],[x*150,(y-1)*150])
            if board[y][x]<0:
                bg.blit(ORANGE[board[y][x]%3],[x*150,(y-1)*150])
    if BL1==1: bg.blit(BLUEC,[-30,20])
    if BL2==1: bg.blit(BLUEC,[40,20])
    if BM1==1: bg.blit(BLUE[2],[-40,170])
    if BM2==1: bg.blit(BLUE[2],[30,170])
    if BS1==1: bg.blit(BLUE[1],[-30,290])
    if BS2==1: bg.blit(BLUE[1],[20,290])
    if OL1==1: bg.blit(ORANGEC,[570,20])
    if OL2==1: bg.blit(ORANGEC,[640,20])
    if OM1==1: bg.blit(ORANGE[1],[560,170])
    if OM2==1: bg.blit(ORANGE[1],[630,170])
    if OS1==1: bg.blit(ORANGE[2],[570,290])
    if OS2==1: bg.blit(ORANGE[2],[620,290])

def clear_piece():
    global BL1,BL2,BM1,BM2,BS1,BS2,OL1,OL2,OM1,OM2,OS1,OS2
    if check==1: BL1=0
    if check==2: BL2=0
    if check==3: BM1=0
    if check==4: BM2=0
    if check==5: BS1=0
    if check==6: BS2=0
    if check==7: OL1=0
    if check==8: OL2=0
    if check==9: OM1=0
    if check==10: OM2=0
    if check==11: OS1=0
    if check==12: OS2=0
        

def turn():
    global check,player
    X=int(x/150)
    Y=int(y/150+1)
    move_piece()
    if (check==1 or check==2) and 150<x and x<600 and 0<y and y<450 and mouse_c==1:
        if board[Y][X]==3 or board[Y][X]==-3:
            return
        if board[Y][X]==2 or board[Y][X]==-2:
            boardM[Y][X]=board[Y][X]
        if board[Y][X]==1 or board[Y][X]==-1:
            boardS[Y][X]=board[Y][X]
        board[Y][X]=3
        clear_piece()
        player*=-1
        check=0
    if (check==3 or check==4) and 150<x and x<600 and 0<y and y<450 and mouse_c==1:
        if board[Y][X]==3 or board[Y][X]==-3 or board[Y][X]==2 or board[Y][X]==-2:
            return
        if board[Y][X]==1 or board[Y][X]==-1:
            boardS[Y][X]=board[Y][X]
        board[Y][X]=2
        clear_piece()
        player*=-1
        check=0
    if (check==5 or check==6) and 150<x and x<600 and 0<y and y<450 and mouse_c==1:
        if board[Y][X]!=0:
            return
        board[Y][X]=1
        clear_piece()
        player*=-1
        check=0
    if (check==7 or check==8) and 150<x and x<600 and 0<y and y<450 and mouse_c==1:
        if board[Y][X]==3 or board[Y][X]==-3:
            return
        if board[Y][X]==2 or board[Y][X]==-2:
            boardM[Y][X]=board[Y][X]
        if board[Y][X]==1 or board[Y][X]==-1:
            boardS[Y][X]=board[Y][X]
        board[Y][X]=-3
        clear_piece()
        player*=-1
        check=0
    if (check==9 or check==10) and 150<x and x<600 and 0<y and y<450 and mouse_c==1:
        if board[Y][X]==3 or board[Y][X]==-3 or board[Y][X]==2 or board[Y][X]==-2:
            return
        if board[Y][X]==1 or board[Y][X]==-1:
            boardS[Y][X]=board[Y][X]
        board[Y][X]=-2
        clear_piece()
        player*=-1
        check=0
    if (check==11 or check==12) and 150<x and x<600 and 0<y and y<450 and mouse_c==1:
        if board[Y][X]!=0:
            return
        board[Y][X]=-1
        clear_piece()
        player*=-1
        check=0

def check_win():
    global index
    for y in range(1,4):
        if board[y][1]>0 and board[y][2]>0 and board[y][3]>0:
            index=3
        if board[y][1]<0 and board[y][2]<0 and board[y][3]<0:
            index=4
    for x in range(1,4):
        if board[1][x]>0 and board[2][x]>0 and board[3][x]>0:
            index=3
        if board[1][x]<0 and board[2][x]<0 and board[3][x]<0:
            index=4
    if board[1][1]>0 and board[2][2]>0 and board[3][3]>0:
        index=3
    if board[1][1]<0 and board[2][2]<0 and board[3][3]<0:
        index=4
    if board[1][3]>0 and board[2][2]>0 and board[3][1]>0:
        index=3
    if board[1][3]<0 and board[2][2]<0 and board[3][1]<0:
        index=4

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+1,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x,y])

def main():
    global tmr,index,x,y,mouse_c
    pygame.init()
    pygame.display.set_caption("GOBBLET GOBBLERS")
    screen=pygame.display.set_mode((750,450))
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
                    screen=pygame.display.set_mode((750,450),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((750,450))

        key=pygame.key.get_pressed()
        tmr+=1
        x,y=pygame.mouse.get_pos()
        mouse_c,btn2,btn3=pygame.mouse.get_pressed()

        if index==0:
            screen.blit(TITLE,[0,0])
            init()
            draw_text(screen,"Press space key",100,300,font,BLINK[tmr%11])
            if key[K_SPACE]:
                index=1
        if index==1:
            screen.blit(BOARD,[0,0])
            draw(screen)
            index=2
        if index==2:
            click(key)
            turn()
            draw_check(screen)
            draw(screen)
            check_win()
            tmr=0
        if index==3:
            draw_text(screen,"BLUE WIN!!",100,180,fontB,BLUE_C)
            if tmr>=50:
                index=0
        if index==4:
            draw_text(screen,"ORANGE WIN!!",10,180,fontB,ORANGE_C)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
