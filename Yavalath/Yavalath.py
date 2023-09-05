import pygame
import sys
from pygame.locals import*

index=0
tmr=0
x=0
y=0
mouse_c=0
player=1

TITLE=pygame.image.load("image/title.png")
BOARD=pygame.image.load("image/board.png")
WHITE_P=pygame.image.load("image/white.png")
BLACK_P=pygame.image.load("image/black.png")

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(192,192,192)

board=[]
for y in range(9):
    board.append([0]*9)

def draw(bg):
    bg.blit(BOARD,[0,0])
    for y in range(9):
        for x in range(9):
            if board[y][x]==1:
                if y==0:
                    bg.blit(WHITE_P,[x*54+220,y*48+30])
                if y==1:
                    bg.blit(WHITE_P,[x*54+193,y*48+30])
                if y==2:
                    bg.blit(WHITE_P,[x*54+166,y*48+30])
                if y==3:
                    bg.blit(WHITE_P,[x*54+139,y*48+30])
                if y==4:
                    bg.blit(WHITE_P,[x*54+112,y*48+30])
                if y==5:
                    bg.blit(WHITE_P,[(x-1)*54+139,y*48+30])
                if y==6:
                    bg.blit(WHITE_P,[(x-2)*54+166,y*48+30])
                if y==7:
                    bg.blit(WHITE_P,[(x-3)*54+193,y*48+30])
                if y==8:
                    bg.blit(WHITE_P,[(x-4)*54+220,y*48+30])
            if board[y][x]==-1:
                if y==0:
                    bg.blit(BLACK_P,[x*54+220,y*48+30])
                if y==1:
                    bg.blit(BLACK_P,[x*54+193,y*48+30])
                if y==2:
                    bg.blit(BLACK_P,[x*54+166,y*48+30])
                if y==3:
                    bg.blit(BLACK_P,[x*54+139,y*48+30])
                if y==4:
                    bg.blit(BLACK_P,[x*54+112,y*48+30])
                if y==5:
                    bg.blit(BLACK_P,[(x-1)*54+139,y*48+30])
                if y==6:
                    bg.blit(BLACK_P,[(x-2)*54+166,y*48+30])
                if y==7:
                    bg.blit(BLACK_P,[(x-3)*54+193,y*48+30])
                if y==8:
                    bg.blit(BLACK_P,[(x-4)*54+220,y*48+30])

def place():
    global player
    if mouse_c==1:
        if 225<=x and x<500 and 45<=y and y<=75:
            if board[0][int((x-225)/55)]==0:
                board[0][int((x-225)/55)]=player
                player*=-1
        if 195<=x and x<525 and 95<=y and y<=125:
            if board[1][int((x-195)/55)]==0:
                board[1][int((x-195)/55)]=player
                player*=-1
        if 165<=x and x<550 and 145<=y and y<=175:
            if board[2][int((x-165)/55)]==0:
                board[2][int((x-165)/55)]=player
                player*=-1
        if 135<=x and x<575 and 195<=y and y<=225:
            if board[3][int((x-135)/55)]==0:
                board[3][int((x-135)/55)]=player
                player*=-1
        if 105<=x and x<600 and 245<=y and y<=275:
            if board[4][int((x-105)/55)]==0:
                board[4][int((x-105)/55)]=player
                player*=-1
        if 135<=x and x<575 and 280<=y and y<=310:
            if board[5][int((x-135)/55)+1]==0:
                board[5][int((x-135)/55)+1]=player
                player*=-1
        if 165<=x and x<550 and 330<=y and y<=365:
            if board[6][int((x-165)/55)+2]==0:
                board[6][int((x-165)/55)+2]=player
                player*=-1
        if 195<=x and x<525 and 380<=y and y<=415:
            if board[7][int((x-195)/55)+3]==0:
                board[7][int((x-195)/55)+3]=player
                player*=-1
        if 225<=x and x<500 and 430<=y and y<=460:
            if board[8][int((x-225)/55)+4]==0:
                board[8][int((x-225)/55)+4]=player
                player*=-1

def win_check():
    global index
    blank=0
    for y in range(9):
        for x in range(9):
            if board[y][x]==0:
                blank+=1
    if blank==20:
        index=4
    try:
        for y in range(9):
            for x in range(9):
                if board[y][x]==1:
                    if board[y][x+1]==1 and board[y][x+2]==1:
                        index=3
                        break
                    if board[y+1][x]==1 and board[y+2][x]==1:
                        index=3
                        break
                    if board[y+1][x+1]==1 and board[y+2][x+2]==1:
                        index=3
                        break
                if board[y][x]==-1:
                    if board[y][x+1]==-1 and board[y][x+2]==-1:
                        index=2
                        break
                    if board[y+1][x]==-1 and board[y+2][x]==-1:
                        index=2
                        break
                    if board[y+1][x+1]==-1 and board[y+2][x+2]==-1:
                        index=2
                        break
        for y in range(9):
            for x in range(9):
                if board[y][x]==1:
                    if board[y][x+1]==1 and board[y][x+2]==1 and board[y][x+3]==1:
                        index=2
                        break
                    if board[y+1][x]==1 and board[y+2][x]==1 and board[y+3][x]==1:
                        index=2
                        break
                    if board[y+1][x+1]==1 and board[y+2][x+2]==1 and board[y+3][x+3]==1:
                        index=2
                        break
                if board[y][x]==-1:
                    if board[y][x+1]==-1 and board[y][x+2]==-1 and board[y][x+3]==-1:
                        index=3
                        break
                    if board[y+1][x]==-1 and board[y+2][x]==-1 and board[y+3][x]==-1:
                        index=3
                        break
                    if board[y+1][x+1]==-1 and board[y+2][x+2]==-1 and board[y+3][x+3]==-1:
                        index=3
                        break
    except:
        pass

def init():
    global player
    for y in range(9):
        for x in range(9):
            board[y][x]=0
    player=1

def draw_text(bg,txt,x,y,fnt,col):
    sur=fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+2,y+2])
    sur=fnt.render(txt,True,col)
    bg.blit(sur,[x,y])
                    
def main():
    pygame.init()
    pygame.display.set_caption("YAVALATH")
    screen=pygame.display.set_mode((700,500))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,90)
    fontB=pygame.font.Font(None,150)

    while True:
        global index,tmr,x,y,mouse_c
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((700,500),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((700,500))
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,b1,b2=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            screen.blit(TITLE,[0,0])
            draw_text(screen,"Press space key",120,400,font,WHITE)
            if key[K_SPACE]:
                init()
                index=1
        if index==1:
            place()
            win_check()
            draw(screen)
            tmr=0
        if index==2:
            draw_text(screen,"WHITE WIN!!",20,200,fontB,WHITE)
            if tmr>=50:
                index=0
        if index==3:
            draw_text(screen,"BLACK WIN!!",20,200,fontB,BLACK)
            if tmr>=50:
                index=0
        if index==4:
            draw_text(screen,"DRAW",190,180,fontB,GRAY)
            if tmr>=50:
                index=0
        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()
