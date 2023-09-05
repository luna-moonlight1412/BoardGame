import pygame
import sys
from pygame.locals import*
import random

WHITE=(255,255,255)
BLUE=(169,206,236)
RED=(255,0,0)
YELLOW=(255,255,0)
BROWN=(180,123,75)
BLACK=(0,0,0)

TITLE=pygame.image.load("image/title.png")
PIECE=[
    None,
    pygame.image.load("image/piece1.png"),
    pygame.image.load("image/piece2.png"),
    pygame.image.load("image/piece3.png"),
    pygame.image.load("image/piece4.png"),
    pygame.image.load("image/piece5.png"),
    pygame.image.load("image/piece6.png"),
    pygame.image.load("image/piece7.png"),
    pygame.image.load("image/piece8.png"),
    pygame.image.load("image/piece9.png"),
    pygame.image.load("image/piece10.png")
    ]

index=0
tmr=0
x=0
y=0
mouse_c=0
check=0
line=0
finish=0
np1=0
np2=0
np3=0
np4=0
piece_p=0
next_piece_check=0

next_piece=[0,0,0,0]
piece=[1,2,3,4,5,6,7,8,9,10]
board=[]
board_c=[]
for y in range(12):
    board.append([9]*12)
    board_c.append([9]*12)

def init():
    global line,finish,np1,np2,np3,np4,piece_p,next_piece_check
    line=0
    finish=0
    np1=0
    np2=0
    np3=0
    np4=0
    piece_p=0
    next_piece_check=0
    for y in range(1,11):
        for x in range(1,11):
            board[y][x]=0
            board_c[y][x]=0

def draw(bg,font):
    bg.fill(WHITE)
    for y in range(10):
                for x in range(10):
                    pygame.draw.rect(bg,BLUE,[x*50,y*50,50,50],3)
                    
    for y in range(1,11):
        for x in range(1,11):
            if board[y][x]==1:
                pygame.draw.rect(bg,BROWN,[(x-1)*50+2,(y-1)*50+2,46,46])
    next_piece(bg)
    draw_text(bg,str(line)+" LINES",180,0,font,BLACK)
                
def next_piece(bg):
    global check,np1,np2,np3,np4
    if check==0:
        next_piece=random.sample(piece,4)
        np1=next_piece[0]
        np2=next_piece[1]
        np3=next_piece[2]
        np4=next_piece[3]
        check=1
    if np1>0:
        bg.blit(PIECE[np1],[50,500])
    if np2>0:
        bg.blit(PIECE[np2],[150,500])
    if np3>0:
        bg.blit(PIECE[np3],[250,500])
    if np4>0:
        bg.blit(PIECE[np4],[350,500])

    if np1==0 and np2==0 and np3==0 and np4==0:
        check=0
    
def place_piece(bg,font):
    global piece_p,next_piece_check,np1,np2,np3,np4
    draw(bg,font)
    if mouse_c==1:
        if 500<=y and y<=700:
            if 50<x and x<150:
                piece_p=np1
                next_piece_check=1
            if 150<x and x<250:
                piece_p=np2
                next_piece_check=2
            if 250<x and x<350:
                piece_p=np3
                next_piece_check=3
            if 350<x and x<450:
                piece_p=np4
                next_piece_check=4
    if next_piece_check>0 and piece_p>0:
        pygame.draw.rect(bg,YELLOW,[(next_piece_check-1)*100+50,500,100,200],3)
    if piece_p>0:
        if 0<=x and x<=500 and 0<=y and y<=500:
            X=int(x/50)
            Y=int(y/50)
            if piece_p==1:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 or board[Y+3][X+1]!=0 or board[Y+4][X+1]!=0 or board[Y+5][X+1]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+2)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+3)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+4)*50+2,46,46])
                
                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0

                    board[Y+1][X+1]=1
                    board[Y+2][X+1]=1
                    board[Y+3][X+1]=1
                    board[Y+4][X+1]=1
                    board[Y+5][X+1]=1
                
            if piece_p==2:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 or board[Y+3][X+1]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+2)*50+2,46,46])
                
                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0

                    board[Y+1][X+1]=1
                    board[Y+2][X+1]=1
                    board[Y+3][X+1]=1
                
            if piece_p==3:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 :
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                
                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0

                    board[Y+1][X+1]=1
                    board[Y+2][X+1]=1
                
            if piece_p==4:
                if board[Y+1][X+1]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                
                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0

                    board[Y+1][X+1]=1
                
            if piece_p==5:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 or board[Y+3][X+1]!=0 or board[Y+3][X+2]!=0 or board[Y+3][X+3]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+2)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,(Y+2)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+2)*50+2,(Y+2)*50+2,46,46])
                
                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0

                    board[Y+1][X+1]=1
                    board[Y+2][X+1]=1
                    board[Y+3][X+1]=1
                    board[Y+3][X+2]=1
                    board[Y+3][X+3]=1
                
            if piece_p==6:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 or board[Y+3][X+1]!=0 or board[Y+2][X+2]!=0 or board[Y+2][X]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+2)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X-1)*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,(Y+1)*50+2,46,46])

                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0

                    board[Y+1][X+1]=1
                    board[Y+2][X+1]=1
                    board[Y+3][X+1]=1
                    board[Y+2][X+2]=1
                    board[Y+2][X]=1
                
            if piece_p==7:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 or board[Y+3][X+1]!=0 or board[Y+4][X+1]!=0 or board[Y+4][X+2]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+2)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+3)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,(Y+3)*50+2,46,46])

                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0

                    board[Y+1][X+1]=1
                    board[Y+2][X+1]=1
                    board[Y+3][X+1]=1
                    board[Y+4][X+1]=1
                    board[Y+4][X+2]=1
                
            if piece_p==8:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 or board[Y+2][X+2]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,(Y+1)*50+2,46,46])

                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0
                    
                    board[Y+1][X+1]=1
                    board[Y+2][X+1]=1
                    board[Y+2][X+2]=1

            if piece_p==9:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 or board[Y+1][X+2]!=0 or board[Y+2][X+2]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,(Y+1)*50+2,46,46])

                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0
                    
                    board[Y+1][X+1]=1
                    board[Y+1][X+2]=1
                    board[Y+2][X+1]=1
                    board[Y+2][X+2]=1

            if piece_p==10:
                if board[Y+1][X+1]!=0 or board[Y+2][X+1]!=0 or board[Y+1][X+2]!=0 or board[Y+2][X+2]!=0 or board[Y+3][X+1]!=0 or board[Y+3][X+2]!=0:
                    return
                pygame.draw.rect(bg,BROWN,[X*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,Y*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,(Y+1)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[X*50+2,(Y+2)*50+2,46,46])
                pygame.draw.rect(bg,BROWN,[(X+1)*50+2,(Y+2)*50+2,46,46])
                

                if mouse_c==1:
                    if next_piece_check==1:
                        np1=0
                    if next_piece_check==2:
                        np2=0
                    if next_piece_check==3:
                        np3=0
                    if next_piece_check==4:
                        np4=0
                    piece_p=0
                    next_piece_check=0
                    
                    board[Y+1][X+1]=1
                    board[Y+1][X+2]=1
                    board[Y+2][X+1]=1
                    board[Y+2][X+2]=1
                    board[Y+3][X+1]=1
                    board[Y+3][X+2]=1

def delete_piece():
    global line
    for y in range(1,11):
        for x in range(1,11):
            board_c[y][x]=board[y][x]
    for y in range(1,11):
        if board_c[y][1]==1 and board_c[y][2]==1 and board_c[y][3]==1 and board_c[y][4]==1 and board_c[y][5]==1 and board_c[y][6]==1 and board_c[y][7]==1 and board_c[y][8]==1 and board_c[y][9]==1 and board_c[y][10]==1:
            for x in range(1,11):
                board[y][x]=0
            line+=1
    for x in range(1,11):
        if board_c[1][x]==1 and board_c[2][x]==1 and board_c[3][x]==1 and board_c[4][x]==1 and board_c[5][x]==1 and board_c[6][x]==1 and board_c[7][x]==1 and board_c[8][x]==1 and board_c[9][x]==1 and board_c[10][x]==1:
            for y in range(1,11):
                board[y][x]=0
            line+=1

def judge_finish():
    global finish,index
    finish=0
    if np1==0 and np2==0 and np3==0 and np4==0:
                finish=1
    for y in range(1,11):
        for x in range(1,11):
            if np1==1 or np2==1 or np3==1 or np4==1:
                if board[y][x]==0 and board[y+1][x]==0 and board[y+2][x]==0 and board[y+3][x]==0 and board[y+4][x]==0:
                    finish=1
                    break
            if np1==2 or np2==2 or np3==2 or np4==2:
                if board[y][x]==0 and board[y+1][x]==0 and board[y+2][x]==0:
                    finish=1
                    break
            if np1==3 or np2==3 or np3==3 or np4==3:
                if board[y][x]==0 and board[y+1][x]==0:
                    finish=1
                    break
            if np1==4 or np2==4 or np3==4 or np4==4:
                if board[y][x]==0:
                    finish=1
                    break
            if np1==5 or np2==5 or np3==5 or np4==5:
                if board[y][x]==0 and board[y+1][x]==0 and board[y+2][x]==0 and board[y+2][x+1]==0 and board[y+2][x+2]==0:
                    finish=1
                    break
            if np1==6 or np2==6 or np3==6 or np4==6:
                if board[y][x]==0 and board[y+1][x]==0 and board[y+2][x]==0 and board[y+1][x+1]==0 and board[y+1][x-1]==0:
                    finish=1
                    break
            if np1==7 or np2==7 or np3==7 or np4==7:
                if board[y][x]==0 and board[y+1][x]==0 and board[y+2][x]==0 and board[y+3][x]==0 and board[y+3][x+1]==0:
                    finish=1
                    break
            if np1==8 or np2==8 or np3==8 or np4==8:
                if board[y][x]==0 and board[y+1][x]==0 and board[y+1][x+1]==0:
                    finish=1
                    break
            if np1==9 or np2==9 or np3==9 or np4==9:
                if board[y][x]==0 and board[y][x+1]==0 and board[y+1][x]==0 and board[y+1][x+1]==0:
                    finish=1
                    break
            if np1==10 or np2==10 or np3==10 or np4==10:
                if board[y][x]==0 and board[y][x+1]==0 and board[y+1][x]==0 and board[y+1][x+1]==0 and board[y+2][x]==0 and board[y+2][x+1]==0:
                    finish=1
                    break
    if finish==0:
        index=2

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+1,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x,y])
                
def main():
    pygame.init()
    pygame.display.set_caption("BLOCK PUZZLE")
    screen=pygame.display.set_mode((500,700))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,50)
    fontM=pygame.font.Font(None,80)
    fontB=pygame.font.Font(None,100)
    fontH=pygame.font.Font(None,120)

    while True:
        global index,tmr,mouse_c,x,y
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((500,700),pygame.FULLSCREEN)
                if event.type==K_ESCAPE:
                    screen=pygame.display.set_mode((500,700))
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,btn2,btn3=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",25,630,fontM,BROWN)
            init()
            if key[K_SPACE]:
                index=1
        if index==1:
            place_piece(screen,font)
            delete_piece()
            judge_finish()
            tmr=0
        if index==2:
            draw_text(screen,"GAMEOVER",10,150,fontH,RED)
            draw_text(screen,str(line)+" LINES",130,250,fontB,BLACK)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
