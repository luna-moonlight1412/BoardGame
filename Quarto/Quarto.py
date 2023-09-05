import pygame
import sys
from pygame.locals import*

index=0
tmr=0
x=0
y=0
X=10
Y=10
mouse_c=0
player=1
check=0
quarto=0
miss1=0
miss2=0
miss_check=0

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
BUTTON=pygame.image.load("image/quarto_button.png")
PIECE=[
    None,
    pygame.image.load("image/piece/piece1.png"),
    pygame.image.load("image/piece/piece2.png"),
    pygame.image.load("image/piece/piece3.png"),
    pygame.image.load("image/piece/piece4.png"),
    pygame.image.load("image/piece/piece5.png"),
    pygame.image.load("image/piece/piece6.png"),
    pygame.image.load("image/piece/piece7.png"),
    pygame.image.load("image/piece/piece8.png"),
    pygame.image.load("image/piece/piece9.png"),
    pygame.image.load("image/piece/piece10.png"),
    pygame.image.load("image/piece/piece11.png"),
    pygame.image.load("image/piece/piece12.png"),
    pygame.image.load("image/piece/piece13.png"),
    pygame.image.load("image/piece/piece14.png"),
    pygame.image.load("image/piece/piece15.png"),
    pygame.image.load("image/piece/piece16.png")
    ]
PIECE_C=[
    None,
    pygame.image.load("image/piece_c/piece1.png"),
    pygame.image.load("image/piece_c/piece2.png"),
    pygame.image.load("image/piece_c/piece3.png"),
    pygame.image.load("image/piece_c/piece4.png"),
    pygame.image.load("image/piece_c/piece5.png"),
    pygame.image.load("image/piece_c/piece6.png"),
    pygame.image.load("image/piece_c/piece7.png"),
    pygame.image.load("image/piece_c/piece8.png"),
    pygame.image.load("image/piece_c/piece9.png"),
    pygame.image.load("image/piece_c/piece10.png"),
    pygame.image.load("image/piece_c/piece11.png"),
    pygame.image.load("image/piece_c/piece12.png"),
    pygame.image.load("image/piece_c/piece13.png"),
    pygame.image.load("image/piece_c/piece14.png"),
    pygame.image.load("image/piece_c/piece15.png"),
    pygame.image.load("image/piece_c/piece16.png")
    ]

board=[]
white=[]
black=[]
high=[]
low=[]
circle=[]
square=[]
hole=[]
non_hole=[]
list=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
for y in range(4):
    board.append([0]*4)
    white.append([0]*4)
    black.append([0]*4)
    high.append([0]*4)
    low.append([0]*4)
    circle.append([0]*4)
    square.append([0]*4)
    hole.append([0]*4)
    non_hole.append([0]*4)

GRAY=(192,192,192)
BROWN=(180,123,75)
BLACK=(0,0,0)
YELLOW=(255,255,0)

def draw(bg,fnt):
    bg.blit(BOARD,[0,0])
    if quarto==0:
        bg.blit(BUTTON,[670,500])
    for y in range(4):
        for x in range(4):
            if board[y][x]>0:
                bg.blit(PIECE[board[y][x]],[x*150+60,y*150+25])
            if list[y][x]>0:
                bg.blit(PIECE_C[list[y][x]],[x*80+650,y*100+50])
    pygame.draw.rect(bg,YELLOW,[X*80+670,Y*100+50,60,100],3)
    if player==1:
        draw_text(bg,"PLAYER1",200,0,fnt,BROWN)
    if player==-1:
        draw_text(bg,"PLAYER2",200,0,fnt,BROWN)

def click():
    global player,check,X,Y,quarto
    if check==0:
        if mouse_c==1:
            if 670<=x and x<=970 and 50<=y and y<=450:
                if list[int((y-50)/100)][int((x-670)/80)]!=0:
                    X=int((x-670)/80)
                    Y=int((y-50)/100)
                    check=list[Y][X]
                    player*=-1

def place():
    global check,X,Y,quarto,miss_check
    if check>0:
        if mouse_c==1:
            if 670<=x and x<=970 and 500<=y and y<=600:
                quarto=1
                miss_check=1
            if 35<=x and x<=635 and 25<=y and y<=625:
                if board[int((y-25)/150)][int((x-35)/150)]==0:
                    board[int((y-25)/150)][int((x-35)/150)]=check
                    list[Y][X]=0
                    X=10
                    Y=10
                    check=0
                    win_check()
                    quarto=0

def win_check():
    global index,quarto,miss1,miss2,miss_check
    blank=0
    if quarto==1:
        for y in range(4):
            for x in range(4):
                if board[y][x]>0:
                    if board[y][x]==1:
                        white[y][x]=1
                        low[y][x]=1
                        square[y][x]=1
                        non_hole[y][x]=1
                    if board[y][x]==2:
                        white[y][x]=1
                        high[y][x]=1
                        square[y][x]=1
                        non_hole[y][x]=1
                    if board[y][x]==3:
                        white[y][x]=1
                        low[y][x]=1
                        circle[y][x]=1
                        non_hole[y][x]=1
                    if board[y][x]==4:
                        white[y][x]=1
                        high[y][x]=1
                        circle[y][x]=1
                        non_hole[y][x]=1
                    if board[y][x]==5:
                        black[y][x]=1
                        low[y][x]=1
                        square[y][x]=1
                        non_hole[y][x]=1
                    if board[y][x]==6:
                        black[y][x]=1
                        high[y][x]=1
                        square[y][x]=1
                        non_hole[y][x]=1
                    if board[y][x]==7:
                        black[y][x]=1
                        low[y][x]=1
                        circle[y][x]=1
                        non_hole[y][x]=1
                    if board[y][x]==8:
                        black[y][x]=1
                        high[y][x]=1
                        circle[y][x]=1
                        non_hole[y][x]=1
                    if board[y][x]==9:
                        white[y][x]=1
                        low[y][x]=1
                        square[y][x]=1
                        hole[y][x]=1
                    if board[y][x]==10:
                        white[y][x]=1
                        high[y][x]=1
                        square[y][x]=1
                        hole[y][x]=1
                    if board[y][x]==11:
                        white[y][x]=1
                        low[y][x]=1
                        circle[y][x]=1
                        hole[y][x]=1
                    if board[y][x]==12:
                        white[y][x]=1
                        high[y][x]=1
                        circle[y][x]=1
                        hole[y][x]=1
                    if board[y][x]==13:
                        black[y][x]=1
                        low[y][x]=1
                        square[y][x]=1
                        hole[y][x]=1
                    if board[y][x]==14:
                        black[y][x]=1
                        high[y][x]=1
                        square[y][x]=1
                        hole[y][x]=1
                    if board[y][x]==15:
                        black[y][x]=1
                        low[y][x]=1
                        circle[y][x]=1
                        hole[y][x]=1
                    if board[y][x]==16:
                        black[y][x]=1
                        high[y][x]=1
                        circle[y][x]=1
                        hole[y][x]=1
        for i in range(4):
            if white[i][0]==1 and white[i][1]==1 and white[i][2]==1 and white[i][3]==1:
                index=2
            elif black[i][0]==1 and black[i][1]==1 and black[i][2]==1 and black[i][3]==1:
                index=2
            elif high[i][0]==1 and high[i][1]==1 and high[i][2]==1 and high[i][3]==1:
                index=2
            elif low[i][0]==1 and low[i][1]==1 and low[i][2]==1 and low[i][3]==1:
                index=2
            elif circle[i][0]==1 and circle[i][1]==1 and circle[i][2]==1 and circle[i][3]==1:
                index=2
            elif square[i][0]==1 and square[i][1]==1 and square[i][2]==1 and square[i][3]==1:
                index=2
            elif hole[i][0]==1 and hole[i][1]==1 and hole[i][2]==1 and hole[i][3]==1:
                index=2
            elif non_hole[i][0]==1 and non_hole[i][1]==1 and non_hole[i][2]==1 and non_hole[i][3]==1:
                index=2
                
            elif white[0][i]==1 and white[1][i]==1 and white[2][i]==1 and white[3][i]==1:
                index=2
            elif black[0][i]==1 and black[1][i]==1 and black[2][i]==1 and black[3][i]==1:
                index=2
            elif high[0][i]==1 and high[1][i]==1 and high[2][i]==1 and high[3][i]==1:
                index=2
            elif low[0][i]==1 and low[1][i]==1 and low[2][i]==1 and low[3][i]==1:
                index=2
            elif circle[0][i]==1 and circle[1][i]==1 and circle[2][i]==1 and circle[3][i]==1:
                index=2
            elif square[0][i]==1 and square[1][i]==1 and square[2][i]==1 and square[3][i]==1:
                index=2
            elif hole[0][i]==1 and hole[1][i]==1 and hole[2][i]==1 and hole[3][i]==1:
                index=2
            elif non_hole[0][i]==1 and non_hole[1][i]==1 and non_hole[2][i]==1 and non_hole[3][i]==1:
                index=2

            elif white[0][0]==1 and white[1][1]==1 and white[2][2]==1 and white[3][3]==1:
                index=2
            elif black[0][0]==1 and black[1][1]==1 and black[2][2]==1 and black[3][3]==1:
                index=2
            elif high[0][0]==1 and high[1][1]==1 and high[2][2]==1 and high[3][3]==1:
                index=2
            elif low[0][0]==1 and low[1][1]==1 and low[2][2]==1 and low[3][3]==1:
                index=2
            elif circle[0][0]==1 and circle[1][1]==1 and circle[2][2]==1 and circle[3][3]==1:
                index=2
            elif square[0][0]==1 and square[1][1]==1 and square[2][2]==1 and square[3][3]==1:
                index=2
            elif hole[0][0]==1 and hole[1][1]==1 and hole[2][2]==1 and hole[3][3]==1:
                index=2
            elif non_hole[0][0]==1 and non_hole[1][1]==1 and non_hole[2][2]==1 and non_hole[3][3]==1:
                index=2

            elif white[0][3]==1 and white[1][2]==1 and white[2][1]==1 and white[3][0]==1:
                index=2
            elif black[0][3]==1 and black[1][2]==1 and black[2][1]==1 and black[3][0]==1:
                index=2
            elif high[0][3]==1 and high[1][2]==1 and high[2][1]==1 and high[3][0]==1:
                index=2
            elif low[0][3]==1 and low[1][2]==1 and low[2][1]==1 and low[3][0]==1:
                index=2
            elif circle[0][3]==1 and circle[1][2]==1 and circle[2][1]==1 and circle[3][0]==1:
                index=2
            elif square[0][3]==1 and square[1][2]==1 and square[2][1]==1 and square[3][0]==1:
                index=2
            elif hole[0][3]==1 and hole[1][2]==1 and hole[2][1]==1 and hole[3][0]==1:
                index=2
            elif non_hole[0][3]==1 and non_hole[1][2]==1 and non_hole[2][1]==1 and non_hole[3][0]==1:
                index=2

            else:
                if player==1 and miss_check==1:
                    miss1+=1
                    miss_check=0
                if player==-1 and miss_check==1:
                    miss2+=1
                    miss_check=0
    for y in range(4):
        for x in range(4):
            if board[y][x]==0:
                blank+=1
    if blank==0:
        index=3
    if miss1==2:
        index=2
    if miss2==2:
        index=2

def init():
    global list,player,check,X,Y,quarto,miss1,miss2
    for y in range(4):
        for x in range(4):
            board[y][x]=0
            white[y][x]=0
            black[y][x]=0
            high[y][x]=0
            low[y][x]=0
            circle[y][x]=0
            square[y][x]=0
            hole[y][x]=0
            non_hole[y][x]=0
    list=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
    player=1
    check=0
    X=10
    Y=10
    quarto=0
    miss1=0
    miss2=0

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+2,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x,y])
        
def main():
    pygame.init()
    pygame.display.set_caption("QUARTO")
    screen=pygame.display.set_mode((1000,650))
    clock=pygame.time.Clock()
    fontS=pygame.font.Font(None,80)
    font=pygame.font.Font(None,120)
    fontB=pygame.font.Font(None,180)

    while True:
        global index,tmr,x,y,mouse_c
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((1000,650),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((1000,650))
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,b1,b2=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",180,500,font,BROWN)
            if key[K_SPACE]:
                init()
                index=1
        if index==1:
            click()
            place()
            draw(screen,fontS)
            tmr=0
        if index==2:
            if miss1<2 and miss2<2:
                if player==1:
                    draw_text(screen,"PLAYER1 WIN!!",40,300,fontB,BROWN)
                if player==-1:
                    draw_text(screen,"PLAYER2 WIN!!",40,300,fontB,BROWN)
            if miss2==2:
                draw_text(screen,"PLAYER1 WIN!!",40,300,fontB,BROWN)
            if miss1==2:
                draw_text(screen,"PLAYER2 WIN!!",40,300,fontB,BROWN)
            if tmr>=50:
                index=0
        if index==3:
            draw_text(screen,"DRAW",300,280,fontB,GRAY)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
