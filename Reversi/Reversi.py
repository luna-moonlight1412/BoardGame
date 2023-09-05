import pygame
import sys
from pygame.locals import*

index=0
tmr=0
x=0
y=0
X=0
Y=0
mouse_c=0
player=1
finish=0

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
WHITE_P=pygame.image.load("image/white.png")
BLACK_P=pygame.image.load("image/black.png")

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(192,192,192)

board=[]
for y in range(10):
    board.append([9]*10)

def draw(bg,font):
    bg.blit(BOARD,[0,0])
    for y in range(1,9):
        for x in range(1,9):
            if board[y][x]==1:
                bg.blit(BLACK_P,[(x-1)*80,(y-1)*80])
            if board[y][x]==-1:
                bg.blit(WHITE_P,[(x-1)*80,(y-1)*80])
    if player==1:
        draw_text(bg,"BLACK",235,10,font,BLACK,WHITE)
    if player==-1:
        draw_text(bg,"WHITE",235,10,font,WHITE,BLACK)

def place():
    global X,Y,index
    if mouse_c==1:
        X=int(x/80)+1
        Y=int(y/80)+1
        if board[Y][X]==0:
            if board[Y-1][X]==player*-1:
                for i in range(2,8):
                    if board[Y-i][X]==player:
                        index=2
                    if board[Y-i][X]==9:
                        break
            if board[Y+1][X]==player*-1:
                for i in range(2,8):
                    if board[Y+i][X]==player:
                        index=2
                    if board[Y+i][X]==9:
                        break
            if board[Y][X-1]==player*-1:
                for i in range(2,8):
                    if board[Y][X-i]==player:
                        index=2
                    if board[Y][X-i]==9:
                        break
            if board[Y][X+1]==player*-1:
                for i in range(2,8):
                    if board[Y][X+i]==player:
                        index=2
                    if board[Y][X+i]==9:
                        break
            if board[Y-1][X-1]==player*-1:
                for i in range(2,8):
                    if board[Y-i][X-i]==player:
                        index=2
                    if board[Y-i][X-i]==9:
                        break
            if board[Y-1][X+1]==player*-1:
                for i in range(2,8):
                    if board[Y-i][X+i]==player:
                        index=2
                    if board[Y-i][X+i]==9:
                        break
            if board[Y+1][X-1]==player*-1:
                for i in range(2,8):
                    if board[Y+i][X-i]==player:
                        index=2
                    if board[Y+i][X-i]==9:
                        break
            if board[Y+1][X+1]==player*-1:
                for i in range(2,8):
                    if board[Y+i][X+i]==player:
                        index=2
                    if board[Y+i][X+i]==9:
                        break
            
def flip():
    global finish,player,index
    board[Y][X]=player
    if board[Y-1][X]==player*-1:
        for i in range(2,8):
            if board[Y-i][X]==player:
                for k in range(1,8):
                    if board[Y-k][X]!=player*-1:
                        break
                    board[Y-k][X]=player
            if board[Y-i][X]==9:
                break
    if board[Y+1][X]==player*-1:
        for i in range(2,8):
            if board[Y+i][X]==player:
                for k in range(1,8):
                    if board[Y+k][X]!=player*-1:
                        break
                    board[Y+k][X]=player
            if board[Y+i][X]==9:
                break
    if board[Y][X-1]==player*-1:
        for i in range(2,8):
            if board[Y][X-i]==player:
                for k in range(1,8):
                    if board[Y][X-k]!=player*-1:
                        break
                    board[Y][X-k]=player
            if board[Y][X-i]==9:
                break
    if board[Y][X+1]==player*-1:
        for i in range(2,8):
            if board[Y][X+i]==player:
                for k in range(1,8):
                    if board[Y][X+k]!=player*-1:
                        break
                    board[Y][X+k]=player
            if board[Y][X+i]==9:
                break
    if board[Y-1][X-1]==player*-1:
        for i in range(2,8):
            if board[Y-i][X-i]==player:
                for k in range(1,8):
                    if board[Y-k][X-k]!=player*-1:
                        break
                    board[Y-k][X-k]=player
            if board[Y-i][X-i]==9:
                break
    if board[Y-1][X+1]==player*-1:
        for i in range(2,8):
            if board[Y-i][X+i]==player:
                for k in range(1,8):
                    if board[Y-k][X+k]!=player*-1:
                        break
                    board[Y-k][X+k]=player
            if board[Y-i][X+i]==9:
                break
    if board[Y+1][X-1]==player*-1:
        for i in range(2,8):
            if board[Y+i][X-i]==player:
                for k in range(1,8):
                    if board[Y+k][X-k]!=player*-1:
                        break
                    board[Y+k][X-k]=player
            if board[Y+i][X-i]==9:
                break
    if board[Y+1][X+1]==player*-1:
        for i in range(2,8):
            if board[Y+i][X+i]==player:
                for k in range(1,8):
                    if board[Y+k][X+k]!=player*-1:
                        break
                    board[Y+k][X+k]=player
            if board[Y+i][X+i]==9:
                break
    finish=0
    player*=-1
    index=1

def finish_check():
    global player,index,finish,tmr
    blank=0
    help=0
    for y in range(1,9):
        for x in range(1,9):
            if board[y][x]==0:
                blank+=1
    for Y in range(1,9):
        for X in range(1,9):
            if board[Y][X]==0:
                if board[Y-1][X]==player*-1:
                    for i in range(2,8):
                        if board[Y-i][X]==player:
                            help+=1
                            break
                        if board[Y-i][X]==9:
                            break
                if board[Y+1][X]==player*-1:
                    for i in range(2,8):
                        if board[Y+i][X]==player:
                            help+=1
                            break
                        if board[Y+i][X]==9:
                            break
                if board[Y][X-1]==player*-1:
                    for i in range(2,8):
                        if board[Y][X-i]==player:
                            help+=1
                            break
                        if board[Y][X-i]==9:
                            break
                if board[Y][X+1]==player*-1:
                    for i in range(2,8):
                        if board[Y][X+i]==player:
                            help+=1
                            break
                        if board[Y][X+i]==9:
                            break
                if board[Y-1][X-1]==player*-1:
                    for i in range(2,8):
                        if board[Y-i][X-i]==player:
                            help+=1
                            break
                        if board[Y-i][X-i]==9:
                            break
                if board[Y-1][X+1]==player*-1:
                    for i in range(2,8):
                        if board[Y-i][X+i]==player:
                            help+=1
                            break
                        if board[Y-i][X+i]==9:
                            break
                if board[Y+1][X-1]==player*-1:
                    for i in range(2,8):
                        if board[Y+i][X-i]==player:
                            help+=1
                            break
                        if board[Y+i][X-i]==9:
                            break
                if board[Y+1][X+1]==player*-1:
                    for i in range(2,8):
                        if board[Y+i][X+i]==player:
                            help+=1
                            break
                        if board[Y+i][X+i]==9:
                            break
    if help==0:
        player*=-1
        finish+=1
    if finish==2 or blank==0:
        index=3
        tmr=0
        
def init():
    global player,finish
    for y in range(1,9):
        for x in range(1,9):
            board[y][x]=0
    board[4][4]=-1
    board[4][5]=1
    board[5][4]=1
    board[5][5]=-1
    player=1
    finish=0

def draw_text(bg,txt,x,y,fnt,col1,col2):
    sur=fnt.render(txt,True,col2)
    bg.blit(sur,[x+2,y+2])
    sur=fnt.render(txt,True,col2)
    bg.blit(sur,[x-2,y-2])
    sur=fnt.render(txt,True,col1)
    bg.blit(sur,[x,y])
        
def main():
    global index,tmr,x,y,mouse_c
    pygame.init()
    pygame.display.set_caption("REVERSI")
    screen=pygame.display.set_mode((640,640))
    clock=pygame.time.Clock()
    fontS=pygame.font.Font(None,70)
    font=pygame.font.Font(None,100)
    fontB=pygame.font.Font(None,120)
    fontH=pygame.font.Font(None,150)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((640,640),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((640,640))

        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,Btn2,Btn3=pygame.mouse.get_pressed()
        tmr+=1
        
        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",50,500,font,BLACK,WHITE)
            if key[K_SPACE]:
                init()
                index=1
        if index==1:
           draw(screen,fontS)
           place()
           finish_check()
        if index==2:
            flip()
        if index==3:
            black=0
            white=0
            for y in range(1,9):
                for x in range(1,9):
                    if board[y][x]==1:
                        black+=1
                    if board[y][x]==-1:
                        white+=1
            draw_text(screen,str(black),160,200,fontH,BLACK,WHITE)
            draw_text(screen,"_",290,150,fontH,GRAY,BLACK)
            draw_text(screen,str(white),390,200,fontH,WHITE,BLACK)
            if black>white:
                draw_text(screen,"BLACK WIN!!",60,330,fontB,BLACK,WHITE)
            if black==white:
                draw_text(screen,"DRAW",160,330,fontH,GRAY,BLACK)
            if black<white:
                draw_text(screen,"WHITE WIN!!",60,330,fontB,WHITE,BLACK)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
