# Flappy bird with pygame

import pygame
import random
import time
import os.path

pygame.init()

mypath = os.path.dirname( os.path.realpath( __file__ ) )

#screen width height
screen = pygame.display.set_mode((800,600))

#bird creation
birdy = pygame.image.load( os.path.join(mypath, 'peace.png') )
birdy = pygame.transform.scale(birdy, (34,34))


#obstacles
ob = pygame.image.load( os.path.join(mypath, 'pipe.png') )
ob = pygame.transform.scale(ob, (100,400))

#title and icon
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load( os.path.join(mypath, 'peace (1).png') )
pygame.display.set_icon(icon)

#global variable SCORE
score=0
lscore=0
hscore=0

menurunning=True


def game() :
    global birdy
    global ob
    global score
    global lscore
    global hscore

    birdyx=300
    birdyy=300

    birdy = pygame.image.load( os.path.join(mypath, 'peace (1).png') )
    birdy = pygame.transform.scale(birdy, (34,34))


    pygame.mixer.music.load( os.path.join(mypath, 'bgm.mp3') )
    pygame.mixer.music.play(-1)

    ups = pygame.mixer.Sound( os.path.join(mypath, 'up.wav') )
    crash = pygame.mixer.Sound( os.path.join(mypath, 'crash.wav') )

    scrollspeed=0.3

    running=True

    def birdraw(x,y):
        screen.blit(birdy,(x,y))

    def obgen(x,y):
        screen.blit(ob,(x,y))

    birdyychange = 9
    a=0
    obx=800
    oby=-100
    oby2=-100
    obx2=1200

    bb=0
    bb2=0
    gamerun=True

    font = pygame.font.Font('freesansbold.ttf', 32)

    clock=pygame.time.Clock()


    while running :
        dt=clock.tick(60)


        sc=str(score)
        text = font.render(sc, True , (0,0,0))

        screen.fill((0,255,255))

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.mixer.music.pause()
                running=False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                    a=1
                    birdyychange=-0.25*dt
                    #pygame.mixer.Sound.play(up)





        birdraw(birdyx,birdyy)



        obgen(obx,oby)
        obgen(obx,(oby+600))
        obgen(obx2,oby2)
        obgen(obx2,(oby2+600))
        obx-=scrollspeed*dt
        obx2-=scrollspeed*dt

        if obx<0 :
            obx=800
            oby=random.randint(-300,0)
            bb=0

        if obx2<0 :
            obx2=800
            oby2=random.randint(-300,0)
            bb2=0

        if birdyx >= obx and birdyx <= (obx+50) and (birdyy<=(oby+390) or birdyy>=(oby+580)):
             sc='CRASHED YOUR SCORE IS'+str(score)
             text = font.render(sc, True , (0,0,0))
             birdy = pygame.transform.scale(birdy, (50,14))
             lscore=score
             pygame.mixer.Sound.play(ups)
             if score>hscore :
                 hscore=score
             time.sleep(1)
             running=False

        if birdyx >= obx2 and birdyx <= (obx2+50) and (birdyy<=(oby2+390) or birdyy>=(oby2+580)):
             sc='CRASHED YOUR SCORE IS'+str(score)
             text = font.render(sc, True , (0,0,0))
             birdy = pygame.transform.scale(birdy, (50,14))
             lscore=score
             pygame.mixer.Sound.play(ups)
             if score>hscore :
                 hscore=score
             time.sleep(1)
             running=False

        if birdyx >= (obx+5) :
            bb+=1
        if bb==1 :
            score+=1
            scrollspeed+=0.02
            if (score%29==0 or score%29==1) and score!=0 and score!=1:
                scrollspeed=scrollspeed-0.16
                print('ha')


        if birdyx >= (obx2+5) :
            bb2+=1
        if bb2==1 :
            score+=1

        screen.blit(text,(400,150))




        if birdyy < 0 :
            birdyy=0
        if birdyy > 566 :
            birdyy=566
        birdyy+=birdyychange
        if a>=1 :
            a+=1
        if a>=10 :
            birdyychange=0.3*dt
            a=0

        pygame.display.update()

menurunning=True
a=0
while menurunning :



    screen.fill((0,255,255))

    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render('Flappy Bird', True , (0,0,0))
    screen.blit(text,(330,20))

    text2 = font.render('click spacebar to play', True , (0,0,0))
    screen.blit(text2,(300,200))
    hc='session Highscore : '+str(hscore)
    text3 = font.render(hc, True , (0,0,0))
    screen.blit(text3,(330,440))



    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            menurunning=False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                a=1
                game()
                #gameover()

                score=0
    if a==1 :
        sc='your last score was : ' + str(lscore)
        text2 = font.render(sc, True , (0,0,0))
        screen.blit(text2,(300,400))



    pygame.display.update()
