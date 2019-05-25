# Créé par kbenhallam, le 07/03/2019 en Python 3.2
import pygame
from shapely.geometry import box
pygame.init()
fenetre= pygame.display.set_mode((800, 534)) #1400 934 sur grand écran, 800 534 sur petit écran
pygame.display.set_caption("How sneaky are you?")


#position
expectation=float(input("rate yourself out of 10:"))
reality=10
posPerso= (700,50) #700 919 sur grand écran, 400 519 sur petit écran
posPnjA= (20,20)
posPnjB=(925,20)
posPnjC = (60, 410)
posPnjD = (880, 530)
posItem=(10,10)
posKunai=(-50,-50)
posBalleA=(-50,-50)
posBalleB=(-50,-50)
posBalleC=(-50,-50)
posBalleD=(-50,-50)
obstacles=[]
hitboxPnj=[]
cdv=[]
hitboxBalle=[]


#valeurs variables
jeu=1
largeurFenetre=pygame.Surface.get_width(fenetre)
hauteurFenetre=pygame.Surface.get_height(fenetre)
viePerso=3
spnjA=1
spnjB=1
spnjC=1
spnjD=1
déplacement=1
chgmtDirection=0
sens=0
etatPerso=0
etatPnjA=1
etatPnjB=1
etatPnjC=1
etatPnjD=1
temps=0
tempsA=0
tempsB=0
tempsC=0
tempsD=0
possible=1
possibleA=1
possibleB=1
possibleC=1
possibleD=1
sensKunai=0
sensBalleA=0
sensBalleB=0
sensBalleC=0
sensBalleD=0
dKunai=1
dBalleA=1
dBalleB=1
dBalleC=1
dBalleD=1
kunaiDispo=3
objet=0



#Images
Kunai= pygame.image.load("./Ninja/png/Kunai.png")
Kunai= pygame.transform.scale(Kunai, (10,25))
balle= pygame.image.load("./Robot/png/Bullet.png")
balle= pygame.transform.scale(balle, (25,10))

item= pygame.image.load("item.png")
item= pygame.transform.scale(item,(30,30))

obstacle1=pygame.image.load("./obstacles/obstacleRouge.png")
obstacle1=pygame.transform.scale(obstacle1, (350,200))
obstacle2=pygame.image.load("./obstacles/obstacleBlanc.png")
obstacle2=pygame.transform.rotate(obstacle2, 90)
obstacle2=pygame.transform.scale(obstacle2, (200,350))
obstacle3=pygame.image.load("./obstacles/obstacleCyan.png")
obstacle3=pygame.transform.scale(obstacle3, (320,180))
obstacle4=pygame.image.load("./obstacles/obstacleJaune.png")
obstacle4=pygame.transform.scale(obstacle4, (350,250))
obstacle5=pygame.image.load("./obstacles/obstacleOrange.png")
obstacle5=pygame.transform.rotate(obstacle5, 90)
obstacle5=pygame.transform.scale(obstacle5, (250,380))
obstacle6=pygame.image.load("./obstacles/obstacleBleu.png")
obstacle6=pygame.transform.scale(obstacle6, (300,150))
obstacle7=pygame.image.load("./obstacles/obstacleVert.png")
obstacle7=pygame.transform.scale(obstacle7, (330,150))



marche0= pygame.image.load("./Ninja/png/Run__000.png")
marche0=pygame.transform.scale(marche0, (50,50))
marche1= pygame.image.load("./Ninja/png/Run__001.png")
marche1=pygame.transform.scale(marche1, (50,50))
marche2= pygame.image.load("./Ninja/png/Run__002.png")
marche2=pygame.transform.scale(marche2, (50,50))
marche3= pygame.image.load("./Ninja/png/Run__003.png")
marche3=pygame.transform.scale(marche3, (50,50))
marche4= pygame.image.load("./Ninja/png/Run__004.png")
marche4=pygame.transform.scale(marche4, (50,50))
marche5= pygame.image.load("./Ninja/png/Run__005.png")
marche5=pygame.transform.scale(marche5, (50,50))
marche6= pygame.image.load("./Ninja/png/Run__006.png")
marche6=pygame.transform.scale(marche6, (50,50))
marche7= pygame.image.load("./Ninja/png/Run__007.png")
marche7=pygame.transform.scale(marche7, (50,50))
marche8= pygame.image.load("./Ninja/png/Run__008.png")
marche8=pygame.transform.scale(marche8, (50,50))
marche9= pygame.image.load("./Ninja/png/Run__009.png")
marche9=pygame.transform.scale(marche9, (50,50))

immobile0= pygame.image.load("./Ninja/png/Idle__000.png")
immobile0= pygame.transform.scale(immobile0, (45,45))
immobile1= pygame.image.load("./Ninja/png/Idle__001.png")
immobile1= pygame.transform.scale(immobile1, (45,45))
immobile2= pygame.image.load("./Ninja/png/Idle__002.png")
immobile2= pygame.transform.scale(immobile2, (45,45))
immobile3= pygame.image.load("./Ninja/png/Idle__003.png")
immobile3= pygame.transform.scale(immobile3, (45,45))
immobile4= pygame.image.load("./Ninja/png/Idle__004.png")
immobile4= pygame.transform.scale(immobile4, (45,45))
immobile5= pygame.image.load("./Ninja/png/Idle__005.png")
immobile5= pygame.transform.scale(immobile5, (45,45))
immobile6= pygame.image.load("./Ninja/png/Idle__006.png")
immobile6= pygame.transform.scale(immobile6, (45,45))
immobile7= pygame.image.load("./Ninja/png/Idle__007.png")
immobile7= pygame.transform.scale(immobile7, (45,45))
immobile8= pygame.image.load("./Ninja/png/Idle__008.png")
immobile8= pygame.transform.scale(immobile8, (45,45))
immobile9= pygame.image.load("./Ninja/png/Idle__009.png")
immobile9= pygame.transform.scale(immobile9, (45,45))

jet0= pygame.image.load("./Ninja/png/Throw__000.png")
jet0= pygame.transform.scale(jet0, (50,50))
jet1= pygame.image.load("./Ninja/png/Throw__001.png")
jet1= pygame.transform.scale(jet1, (50,50))
jet2= pygame.image.load("./Ninja/png/Throw__002.png")
jet2= pygame.transform.scale(jet2, (50,50))
jet3= pygame.image.load("./Ninja/png/Throw__003.png")
jet3= pygame.transform.scale(jet3, (50,50))
jet4= pygame.image.load("./Ninja/png/Throw__004.png")
jet4= pygame.transform.scale(jet4, (50,50))
jet5= pygame.image.load("./Ninja/png/Throw__005.png")
jet5= pygame.transform.scale(jet5, (50,50))
jet6= pygame.image.load("./Ninja/png/Throw__006.png")
jet6= pygame.transform.scale(jet6, (50,50))
jet7= pygame.image.load("./Ninja/png/Throw__007.png")
jet7= pygame.transform.scale(jet7, (50,50))
jet8= pygame.image.load("./Ninja/png/Throw__008.png")
jet8= pygame.transform.scale(jet8, (50,50))
jet9= pygame.image.load("./Ninja/png/Throw__009.png")
jet9= pygame.transform.scale(jet9, (50,50))

attaque0= pygame.image.load("./Ninja/png/Attack__000.png")
attaque0= pygame.transform.scale(attaque0, (50,50))
attaque1= pygame.image.load("./Ninja/png/Attack__001.png")
attaque1= pygame.transform.scale(attaque1, (50,50))
attaque2= pygame.image.load("./Ninja/png/Attack__002.png")
attaque2= pygame.transform.scale(attaque2, (50,50))
attaque3= pygame.image.load("./Ninja/png/Attack__003.png")
attaque3= pygame.transform.scale(attaque3, (50,50))
attaque4= pygame.image.load("./Ninja/png/Attack__004.png")
attaque4= pygame.transform.scale(attaque4, (50,50))
attaque5= pygame.image.load("./Ninja/png/Attack__005.png")
attaque5= pygame.transform.scale(attaque5, (50,50))
attaque6= pygame.image.load("./Ninja/png/Attack__006.png")
attaque6= pygame.transform.scale(attaque6, (50,50))
attaque7= pygame.image.load("./Ninja/png/Attack__007.png")
attaque7= pygame.transform.scale(attaque7, (50,50))
attaque8= pygame.image.load("./Ninja/png/Attack__008.png")
attaque8= pygame.transform.scale(attaque8, (50,50))
attaque9= pygame.image.load("./Ninja/png/Attack__009.png")
attaque9= pygame.transform.scale(attaque9, (50,50))

mort0= pygame.image.load("./Ninja/png/Dead__000.png")
mort0= pygame.transform.scale(mort0, (50,50))
mort1= pygame.image.load("./Ninja/png/Dead__001.png")
mort1= pygame.transform.scale(mort1, (50,50))
mort2= pygame.image.load("./Ninja/png/Dead__002.png")
mort2= pygame.transform.scale(mort2, (50,50))
mort3= pygame.image.load("./Ninja/png/Dead__003.png")
mort3= pygame.transform.scale(mort3, (50,50))
mort4= pygame.image.load("./Ninja/png/Dead__004.png")
mort4= pygame.transform.scale(mort4, (50,50))
mort5= pygame.image.load("./Ninja/png/Dead__005.png")
mort5= pygame.transform.scale(mort5, (50,50))
mort6= pygame.image.load("./Ninja/png/Dead__006.png")
mort6= pygame.transform.scale(mort6, (50,50))
mort7= pygame.image.load("./Ninja/png/Dead__007.png")
mort7= pygame.transform.scale(mort7, (50,50))
mort8= pygame.image.load("./Ninja/png/Dead__008.png")
mort8= pygame.transform.scale(mort8, (50,50))
mort9= pygame.image.load("./Ninja/png/Dead__009.png")
mort9= pygame.transform.scale(mort9, (50,50))

gmarche1= pygame.image.load("./Robot/png/Run (1).png")
gmarche1=pygame.transform.scale(gmarche1, (60,55))
gmarche2= pygame.image.load("./Robot/png/Run (2).png")
gmarche2=pygame.transform.scale(gmarche2, (60,55))
gmarche3= pygame.image.load("./Robot/png/Run (3).png")
gmarche3=pygame.transform.scale(gmarche3, (60,55))
gmarche4= pygame.image.load("./Robot/png/Run (4).png")
gmarche4=pygame.transform.scale(gmarche4, (60,55))
gmarche5= pygame.image.load("./Robot/png/Run (5).png")
gmarche5=pygame.transform.scale(gmarche5, (60,55))
gmarche6= pygame.image.load("./Robot/png/Run (6).png")
gmarche6=pygame.transform.scale(gmarche6, (60,55))
gmarche7= pygame.image.load("./Robot/png/Run (7).png")
gmarche7=pygame.transform.scale(gmarche7, (60,55))
gmarche8= pygame.image.load("./Robot/png/Run (8).png")
gmarche8=pygame.transform.scale(gmarche8, (60,55))

gimmobile1= pygame.image.load("./Robot/png/Idle (1).png")
gimmobile1= pygame.transform.scale(gimmobile1, (60,55))
gimmobile2= pygame.image.load("./Robot/png/Idle (2).png")
gimmobile2= pygame.transform.scale(gimmobile2, (60,55))
gimmobile3= pygame.image.load("./Robot/png/Idle (3).png")
gimmobile3= pygame.transform.scale(gimmobile3, (60,55))
gimmobile4= pygame.image.load("./Robot/png/Idle (4).png")
gimmobile4= pygame.transform.scale(gimmobile4, (60,55))
gimmobile5= pygame.image.load("./Robot/png/Idle (5).png")
gimmobile5= pygame.transform.scale(gimmobile5, (60,55))
gimmobile6= pygame.image.load("./Robot/png/Idle (6).png")
gimmobile6= pygame.transform.scale(gimmobile6, (60,55))
gimmobile7= pygame.image.load("./Robot/png/Idle (7).png")
gimmobile7= pygame.transform.scale(gimmobile7, (60,55))
gimmobile8= pygame.image.load("./Robot/png/Idle (8).png")
gimmobile8= pygame.transform.scale(gimmobile8, (60,55))
gimmobile9= pygame.image.load("./Robot/png/Idle (9).png")
gimmobile9= pygame.transform.scale(gimmobile9, (60,55))
gimmobile10= pygame.image.load("./Robot/png/Idle (10).png")
gimmobile10= pygame.transform.scale(gimmobile10, (60,55))

gattaque1= pygame.image.load("./Robot/png/Melee (1).png")
gattaque1= pygame.transform.scale(gattaque1, (60,55))
gattaque2= pygame.image.load("./Robot/png/Melee (2).png")
gattaque2= pygame.transform.scale(gattaque2, (60,55))
gattaque3= pygame.image.load("./Robot/png/Melee (3).png")
gattaque3= pygame.transform.scale(gattaque3, (60,55))
gattaque4= pygame.image.load("./Robot/png/Melee (4).png")
gattaque4= pygame.transform.scale(gattaque4, (60,55))
gattaque5= pygame.image.load("./Robot/png/Melee (5).png")
gattaque5= pygame.transform.scale(gattaque5, (60,55))
gattaque6= pygame.image.load("./Robot/png/Melee (6).png")
gattaque6= pygame.transform.scale(gattaque6, (60,55))
gattaque7= pygame.image.load("./Robot/png/Melee (7).png")
gattaque7= pygame.transform.scale(gattaque7, (60,55))
gattaque8= pygame.image.load("./Robot/png/Melee (8).png")
gattaque8= pygame.transform.scale(gattaque8, (60,55))

gtir1= pygame.image.load("./Robot/png/Shoot (1).png")
gtir1= pygame.transform.scale(gtir1, (60,55))
gtir2= pygame.image.load("./Robot/png/Shoot (2).png")
gtir2= pygame.transform.scale(gtir2, (60,55))
gtir3= pygame.image.load("./Robot/png/Shoot (3).png")
gtir3= pygame.transform.scale(gtir3, (60,55))
gtir4= pygame.image.load("./Robot/png/Shoot (4).png")
gtir4= pygame.transform.scale(gtir4, (60,55))

gmort1= pygame.image.load("./Robot/png/Dead (1).png")
gmort1=pygame.transform.scale(gmort1, (60,55))
gmort2= pygame.image.load("./Robot/png/Dead (2).png")
gmort2=pygame.transform.scale(gmort2, (60,55))
gmort3= pygame.image.load("./Robot/png/Dead (3).png")
gmort3=pygame.transform.scale(gmort3, (60,55))
gmort4= pygame.image.load("./Robot/png/Dead (4).png")
gmort4=pygame.transform.scale(gmort4, (60,55))
gmort5= pygame.image.load("./Robot/png/Dead (5).png")
gmort5=pygame.transform.scale(gmort5, (60,55))
gmort6= pygame.image.load("./Robot/png/Dead (6).png")
gmort6=pygame.transform.scale(gmort6, (60,55))
gmort7= pygame.image.load("./Robot/png/Dead (7).png")
gmort7=pygame.transform.scale(gmort7, (60,55))
gmort8= pygame.image.load("./Robot/png/Dead (8).png")
gmort8=pygame.transform.scale(gmort8, (60,55))
gmort9= pygame.image.load("./Robot/png/Dead (9).png")
gmort9=pygame.transform.scale(gmort9, (60,55))
gmort10= pygame.image.load("./Robot/png/Dead (10).png")
gmort10=pygame.transform.scale(gmort10, (60,55))


#divers rectangles
Salle1=pygame.Rect(150,100,350,200)
Salle2=pygame.Rect(150,500,200,350)
Salle3=pygame.Rect(500,400,320,180)
Salle4=pygame.Rect(960,600,350,250)
Salle5=pygame.Rect(1000,100,250,380)
Salle6=pygame.Rect(600,150,300,150)
Salle7=pygame.Rect(450,650,330,150)

hitboxPerso=pygame.Rect(posPerso[0],posPerso[1],50,50)
hitboxPnjA=pygame.Rect(posPnjA[0],posPnjA[1]+5,50,50)
hitboxPnjB=pygame.Rect(posPnjB[0],posPnjB[1]+5,50,50)
hitboxPnjC = pygame.Rect(posPnjC[0], posPnjC[1]+5, 50, 50)
hitboxPnjD = pygame.Rect(posPnjD[0], posPnjD[1]+5, 50, 50)

hitboxKunai=pygame.Rect(posKunai[0],posKunai[1],12,12)
hitboxBalleA=pygame.Rect(posBalleA[0], posBalleA[1],12,12)
hitboxBalleB=pygame.Rect(posBalleB[0], posBalleB[1],12,12)
hitboxBalleC=pygame.Rect(posBalleC[0], posBalleC[1],12,12)
hitboxBalleD=pygame.Rect(posBalleD[0], posBalleD[1],12,12)

hitboxItem=pygame.Rect(posItem[0], posItem[1],30,30)

cdvA1=pygame.Rect(posPnjA[0]+50,posPnjA[1]-5,130,76)
cdvA2=pygame.Rect(posPnjA[0]-10,posPnjA[1]+55,76,130)
cdvA3=pygame.Rect(posPnjA[0],posPnjA[1]-10,-130,76)
cdvA4=pygame.Rect(posPnjA[0]-15,posPnjA[1]+5,76,-130)
cdvB1=pygame.Rect(posPnjB[0]+50,posPnjB[1]-5,130,76)
cdvB2=pygame.Rect(posPnjB[0]-10,posPnjB[1]+55,76,130)
cdvB3=pygame.Rect(posPnjB[0],posPnjB[1]-10,-130,76)
cdvB4=pygame.Rect(posPnjB[0]-15,posPnjB[1]+5,76,-130)
cdvC1=pygame.Rect(posPnjC[0]+50,posPnjC[1]-5,130,76)
cdvC2=pygame.Rect(posPnjC[0]-10,posPnjC[1]+55,76,130)
cdvC3=pygame.Rect(posPnjC[0],posPnjC[1]-10,-130,76)
cdvC4=pygame.Rect(posPnjC[0]-15,posPnjC[1]+5,76,-130)
cdvD1=pygame.Rect(posPnjD[0]+50,posPnjD[1]-5,130,76)
cdvD2=pygame.Rect(posPnjD[0]-10,posPnjD[1]+55,76,130)
cdvD3=pygame.Rect(posPnjD[0],posPnjD[1]-10,-130,76)
cdvD4=pygame.Rect(posPnjD[0]-15,posPnjD[1]+5,76,-130)




#son
musique=pygame.mixer.music.load("./son/fond.mp3")
pygame.mixer.music.play(15,0.0)




#icone du jeu
pygame.display.set_icon(immobile0)



#liste
obstacles.append(Salle1)
obstacles.append(Salle2)
obstacles.append(Salle3)
obstacles.append(Salle4)
obstacles.append(Salle5)
obstacles.append(Salle6)
obstacles.append(Salle7)

hitboxPnj.append(hitboxPnjA)
hitboxPnj.append(hitboxPnjB)
hitboxPnj.append(hitboxPnjC)
hitboxPnj.append(hitboxPnjD)

cdv.append(cdvA1)
cdv.append(cdvA2)
cdv.append(cdvA3)
cdv.append(cdvA4)
cdv.append(cdvB1)
cdv.append(cdvB2)
cdv.append(cdvB3)
cdv.append(cdvB4)
cdv.append(cdvC1)
cdv.append(cdvC2)
cdv.append(cdvC3)
cdv.append(cdvC4)
cdv.append(cdvD1)
cdv.append(cdvD2)
cdv.append(cdvD3)
cdv.append(cdvD4)

hitboxBalle.append(hitboxBalleA)
hitboxBalle.append(hitboxBalleB)
hitboxBalle.append(hitboxBalleC)
hitboxBalle.append(hitboxBalleD)




#Dessin
def DessinSalles():
    fenetre.blit(obstacle1, (150,100)) #coin haut gauche
    fenetre.blit(obstacle2,(150,500)) #coin bas gauche
    fenetre.blit(obstacle3, (500,400)) #milieu milieu
    fenetre.blit(obstacle4,(960,600)) #coin bas droite
    fenetre.blit(obstacle5,(1000,100)) #coin haut droite
    fenetre.blit(obstacle6,(600,150)) #milieu haut
    fenetre.blit(obstacle7,(450,650)) #milieu bas


def dessinCDV():
    if spnjA==1:
        pygame.draw.rect(fenetre,(255,255,255),cdvA1,1)#visionR
    if spnjA==2:
        pygame.draw.rect(fenetre,(255,255,255),cdvA2,1)#visionD
    if spnjA==3:
        pygame.draw.rect(fenetre,(255,255,255),cdvA3,1)#visionL
    if spnjA==4:
        pygame.draw.rect(fenetre,(255,255,255),cdvA4,1)#visionUp
    if spnjB==1:
        pygame.draw.rect(fenetre,(255,255,255),cdvB1,1)#visionR
    if spnjB==2:
        pygame.draw.rect(fenetre,(255,255,255),cdvB2,1)#visionD
    if spnjB==3:
        pygame.draw.rect(fenetre,(255,255,255),cdvB3,1)#visionL
    if spnjB==4:
        pygame.draw.rect(fenetre,(255,255,255),cdvB4,1)#visionUp
    if spnjC==1:
        pygame.draw.rect(fenetre,(255,255,255),cdvC1,1)#visionR
    if spnjC==2:
        pygame.draw.rect(fenetre,(255,255,255),cdvC2,1)#visionD
    if spnjC==3:
        pygame.draw.rect(fenetre,(255,255,255),cdvC3,1)#visionL
    if spnjC==4:
        pygame.draw.rect(fenetre,(255,255,255),cdvC4,1)#visionUp
    if spnjD==1:
        pygame.draw.rect(fenetre,(255,255,255),cdvD1,1)#visionR
    if spnjD==2:
        pygame.draw.rect(fenetre,(255,255,255),cdvD2,1)#visionD
    if spnjD==3:
        pygame.draw.rect(fenetre,(255,255,255),cdvD3,1)#visionL
    if spnjD==4:
        pygame.draw.rect(fenetre,(255,255,255),cdvD4,1)#visionUp



def dessinPerso():
    global temps
    if etatPerso==0:
        if 0<= pygame.time.get_ticks() - temps <=100:
            fenetre.blit(immobile0, posPerso)
        elif 100<= pygame.time.get_ticks() - temps <=200:
            fenetre.blit(immobile1,posPerso)
        elif 200<= pygame.time.get_ticks() - temps <=300:
            fenetre.blit(immobile2, posPerso)
        elif 300<pygame.time.get_ticks()- temps <=400:
            fenetre.blit (immobile3, posPerso)
        elif 400<pygame.time.get_ticks()- temps <=500:
            fenetre.blit (immobile4, posPerso)
        elif 500<pygame.time.get_ticks()- temps <=600:
            fenetre.blit (immobile5, posPerso)
        elif 600<pygame.time.get_ticks()- temps <=700:
            fenetre.blit (immobile6, posPerso)
        elif 700<pygame.time.get_ticks()- temps <=800:
            fenetre.blit (immobile7, posPerso)
        elif 800<pygame.time.get_ticks()- temps <=900:
            fenetre.blit (immobile8, posPerso)
        elif 900<pygame.time.get_ticks()- temps <=1000:
            fenetre.blit (immobile9, posPerso)
        else: temps= pygame.time.get_ticks()
    if etatPerso==1:
        if sens==1:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(marche0, posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(marche1,posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(marche2, posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (marche3, posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (marche4, posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (marche5, posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (marche6, posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (marche7, posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (marche8, posPerso)
            elif 900<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (marche9, posPerso)
            else: temps= pygame.time.get_ticks()
        if sens==2:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.rotate(marche0,270), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.rotate(marche1,270),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.rotate(marche2,270), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.rotate(marche3,270), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.rotate(marche4,270), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.rotate(marche5,270), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.rotate(marche6,270), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.rotate(marche7,270), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.rotate(marche8,270), posPerso)
            elif 900<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.rotate(marche9,270), posPerso)
            else: temps= pygame.time.get_ticks()
        if sens ==3:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.flip(marche0,True, False), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.flip(marche1,True, False),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.flip(marche2,True, False), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.flip(marche3,True, False), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.flip(marche4,True, False), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.flip(marche5,True, False), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.flip(marche6,True, False), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.flip(marche7,True, False), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.flip(marche8,True, False), posPerso)
            elif 900<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.flip(marche9,True, False), posPerso)
            else: temps= pygame.time.get_ticks()
        if sens ==4:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.rotate(marche0,90), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.rotate(marche1,90),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.rotate(marche2,90), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.rotate(marche3,90), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.rotate(marche4,90), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.rotate(marche5,90), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.rotate(marche6,90), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.rotate(marche7,90), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.rotate(marche8,90), posPerso)
            elif 900<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.rotate(marche9,90), posPerso)
            else: temps= pygame.time.get_ticks()
    if etatPerso==2:
        if sens==1:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(attaque0, posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(attaque1,posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(attaque2, posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (attaque3, posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (attaque4, posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (attaque5, posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (attaque6, posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (attaque7, posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (attaque8, posPerso)
            elif 900<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (attaque9, posPerso)
            else: temps= pygame.time.get_ticks()
        if sens==2:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.rotate(attaque0,270), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.rotate(attaque1,270),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.rotate(attaque2,270), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.rotate(attaque3,270), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.rotate(attaque4,270), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.rotate(attaque5,270), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.rotate(attaque6,270), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.rotate(attaque7,270), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.rotate(attaque8,270), posPerso)
            elif 900<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.rotate(attaque9,270), posPerso)
            else: temps= pygame.time.get_ticks()
        if sens ==3:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.flip(attaque0,True, False), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.flip(attaque1,True, False),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.flip(attaque2,True, False), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.flip(attaque3,True, False), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.flip(attaque4,True, False), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.flip(attaque5,True, False), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.flip(attaque6,True, False), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.flip(attaque7,True, False), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.flip(attaque8,True, False), posPerso)
            elif 900<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.flip(attaque9,True, False), posPerso)
            else: temps= pygame.time.get_ticks()
        if sens==4:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.rotate(attaque0,90), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.rotate(attaque1,90),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.rotate(attaque2,90), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.rotate(attaque3,90), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.rotate(attaque4,90), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.rotate(attaque5,90), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.rotate(attaque6,90), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.rotate(attaque7,90), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.rotate(attaque8,90), posPerso)
            elif 900<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.rotate(attaque9,90), posPerso)
            else: temps= pygame.time.get_ticks()
    if etatPerso==3:
        if sens==1:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(jet0, posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=400:
                fenetre.blit(jet1,posPerso)
            elif 400<= pygame.time.get_ticks() - temps <=600:
                fenetre.blit(jet2, posPerso)
            elif 600<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (jet3, posPerso)
            elif 800<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (jet4, posPerso)
            elif 1000<pygame.time.get_ticks()- temps <=1200:
                fenetre.blit (jet5, posPerso)
            elif 1200<pygame.time.get_ticks()- temps <=1400:
                fenetre.blit (jet6, posPerso)
            elif 1400<pygame.time.get_ticks()- temps <=1600:
                fenetre.blit (jet7, posPerso)
            elif 1600<pygame.time.get_ticks()- temps <=1800:
                fenetre.blit (jet8, posPerso)
            elif 1800<pygame.time.get_ticks()- temps <=2000:
                fenetre.blit (jet9, posPerso)
            else: temps= pygame.time.get_ticks()
        if sens==2:
            if 0<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.rotate(jet0,270), posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=400:
                fenetre.blit(pygame.transform.rotate(jet1,270),posPerso)
            elif 400<= pygame.time.get_ticks() - temps <=600:
                fenetre.blit(pygame.transform.rotate(jet2,270), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.rotate(jet3,270), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.rotate(jet4,270), posPerso)
            elif 1000<pygame.time.get_ticks()- temps <=1200:
                fenetre.blit (pygame.transform.rotate(jet5,270), posPerso)
            elif 1200<pygame.time.get_ticks()- temps <=1400:
                fenetre.blit (pygame.transform.rotate(jet6,270), posPerso)
            elif 1400<pygame.time.get_ticks()- temps <=1600:
                fenetre.blit (pygame.transform.rotate(jet7,270), posPerso)
            elif 1600<pygame.time.get_ticks()- temps <=1800:
                fenetre.blit (pygame.transform.rotate(jet8,270), posPerso)
            elif 1800<pygame.time.get_ticks()- temps <=2000:
                fenetre.blit (pygame.transform.rotate(jet9,270), posPerso)
            else: temps= pygame.time.get_ticks()
        if sens ==3:
            if 0<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.flip(jet0,True, False), posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=400:
                fenetre.blit(pygame.transform.flip(jet1,True, False),posPerso)
            elif 400<= pygame.time.get_ticks() - temps <=600:
                fenetre.blit(pygame.transform.flip(jet2,True, False), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.flip(jet3,True, False), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.flip(jet4,True, False), posPerso)
            elif 1000<pygame.time.get_ticks()- temps <=1200:
                fenetre.blit (pygame.transform.flip(jet5,True, False), posPerso)
            elif 1200<pygame.time.get_ticks()- temps <=1400:
                fenetre.blit (pygame.transform.flip(jet6,True, False), posPerso)
            elif 1400<pygame.time.get_ticks()- temps <=1600:
                fenetre.blit (pygame.transform.flip(jet7,True, False), posPerso)
            elif 1600<pygame.time.get_ticks()- temps <=1800:
                fenetre.blit (pygame.transform.flip(jet8,True, False), posPerso)
            elif 1800<pygame.time.get_ticks()- temps <=2000:
                fenetre.blit (pygame.transform.flip(jet9,True, False), posPerso)
            else: temps= pygame.time.get_ticks()
        if sens ==4:
            if 0<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.rotate(jet0,90), posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=400:
                fenetre.blit(pygame.transform.rotate(jet1,90),posPerso)
            elif 400<= pygame.time.get_ticks() - temps <=600:
                fenetre.blit(pygame.transform.rotate(jet2,90), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.rotate(jet3,90), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=1000:
                fenetre.blit (pygame.transform.rotate(jet4,90), posPerso)
            elif 1000<pygame.time.get_ticks()- temps <=1200:
                fenetre.blit (pygame.transform.rotate(jet5,90), posPerso)
            elif 1200<pygame.time.get_ticks()- temps <=1400:
                fenetre.blit (pygame.transform.rotate(jet6,90), posPerso)
            elif 1400<pygame.time.get_ticks()- temps <=1600:
                fenetre.blit (pygame.transform.rotate(jet7,90), posPerso)
            elif 1600<pygame.time.get_ticks()- temps <=1800:
                fenetre.blit (pygame.transform.rotate(jet8,90), posPerso)
            elif 1800<pygame.time.get_ticks()- temps <=2000:
                fenetre.blit (pygame.transform.rotate(jet9,90), posPerso)
            else: temps= pygame.time.get_ticks()
    if etatPerso==4:
        if sens==1:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(mort0, posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(mort1,posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(mort2, posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (mort3, posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (mort4, posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (mort5, posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (mort6, posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (mort7, posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (mort8, posPerso)
            elif 900<pygame.time.get_ticks()- temps:
                fenetre.blit (mort9, posPerso)
        if sens==2:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.rotate(mort0,270), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.rotate(mort1,270),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.rotate(mort2,270), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.rotate(mort3,270), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.rotate(mort4,270), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.rotate(mort5,270), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.rotate(mort6,270), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.rotate(mort7,270), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.rotate(mort8,270), posPerso)
            elif 900<pygame.time.get_ticks()- temps:
                fenetre.blit (pygame.transform.rotate(mort9,270), posPerso)
        if sens ==3:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.flip(mort0,True, False), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.flip(mort1,True, False),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.flip(mort2,True, False), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.flip(mort3,True, False), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.flip(mort4,True, False), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.flip(mort5,True, False), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.flip(mort6,True, False), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.flip(mort7,True, False), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.flip(mort8,True, False), posPerso)
            elif 900<pygame.time.get_ticks()- temps:
                fenetre.blit (pygame.transform.flip(mort9,True, False), posPerso)
        if sens ==4:
            if 0<= pygame.time.get_ticks() - temps <=100:
                fenetre.blit(pygame.transform.rotate(mort0,90), posPerso)
            elif 100<= pygame.time.get_ticks() - temps <=200:
                fenetre.blit(pygame.transform.rotate(mort1,90),posPerso)
            elif 200<= pygame.time.get_ticks() - temps <=300:
                fenetre.blit(pygame.transform.rotate(mort2,90), posPerso)
            elif 300<pygame.time.get_ticks()- temps <=400:
                fenetre.blit (pygame.transform.rotate(mort3,90), posPerso)
            elif 400<pygame.time.get_ticks()- temps <=500:
                fenetre.blit (pygame.transform.rotate(mort4,90), posPerso)
            elif 500<pygame.time.get_ticks()- temps <=600:
                fenetre.blit (pygame.transform.rotate(mort5,90), posPerso)
            elif 600<pygame.time.get_ticks()- temps <=700:
                fenetre.blit (pygame.transform.rotate(mort6,90), posPerso)
            elif 700<pygame.time.get_ticks()- temps <=800:
                fenetre.blit (pygame.transform.rotate(mort7,90), posPerso)
            elif 800<pygame.time.get_ticks()- temps <=900:
                fenetre.blit (pygame.transform.rotate(mort8,90), posPerso)
            elif 900<pygame.time.get_ticks()- temps:
                fenetre.blit (pygame.transform.rotate(mort9,90), posPerso)







def dessinPnja():
    global tempsA
    if etatPnjA==0:
        if 0<= pygame.time.get_ticks() - tempsA <=100:
            fenetre.blit(gimmobile1, posPnjA)
        elif 100<= pygame.time.get_ticks() - tempsA <=200:
            fenetre.blit(gimmobile2,posPnjA)
        elif 200<= pygame.time.get_ticks() - tempsA <=300:
            fenetre.blit(gimmobile3, posPnjA)
        elif 300<pygame.time.get_ticks()- tempsA <=400:
            fenetre.blit (gimmobile4, posPnjA)
        elif 400<pygame.time.get_ticks()- tempsA <=500:
            fenetre.blit (gimmobile5, posPnjA)
        elif 500<pygame.time.get_ticks()- tempsA <=600:
            fenetre.blit (gimmobile6, posPnjA)
        elif 600<pygame.time.get_ticks()- tempsA <=700:
            fenetre.blit (gimmobile7, posPnjA)
        elif 700<pygame.time.get_ticks()- tempsA <=800:
            fenetre.blit (gimmobile8, posPnjA)
        elif 800<pygame.time.get_ticks()- tempsA <=900:
            fenetre.blit (gimmobile9, posPnjA)
        elif 900<pygame.time.get_ticks()- tempsA <=1000:
            fenetre.blit (gimmobile10, posPnjA)
        else: tempsA= pygame.time.get_ticks()
    if etatPnjA==1:
        if spnjA==1:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(gmarche1, posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(gmarche2,posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(gmarche3, posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (gmarche4, posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (gmarche5, posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (gmarche6, posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA<=700:
                fenetre.blit (gmarche7, posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (gmarche8, posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==2:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.rotate(gmarche1,270), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.rotate(gmarche2,270),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.rotate(gmarche3,270), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.rotate(gmarche4,270), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.rotate(gmarche5,270), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.rotate(gmarche6,270), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.rotate(gmarche7,270), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.rotate(gmarche8,270), posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==3:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.flip(gmarche1,True, False), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.flip(gmarche2,True, False),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.flip(gmarche3,True, False), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.flip(gmarche4,True, False), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.flip(gmarche5,True, False), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.flip(gmarche6,True, False), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.flip(gmarche7,True, False), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.flip(gmarche8,True, False), posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==4:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.rotate(gmarche1,90), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.rotate(gmarche2,90),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.rotate(gmarche3,90), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.rotate(gmarche4,90), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.rotate(gmarche5,90), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.rotate(gmarche6,90), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.rotate(gmarche7,90), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.rotate(gmarche8,90), posPnjA)
            else: tempsA= pygame.time.get_ticks()
    if etatPnjA==2:
        if spnjA==1:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(gattaque1, posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(gattaque2,posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(gattaque3, posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (gattaque4, posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (gattaque5, posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (gattaque6, posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (gattaque7, posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (gattaque8, posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==2:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.rotate(gattaque1,270), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.rotate(gattaque2,270),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.rotate(gattaque3,270), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.rotate(gattaque4,270), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.rotate(gattaque5,270), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.rotate(gattaque6,270), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.rotate(gattaque7,270), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.rotate(gattaque8,270), posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==3:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.flip(gattaque1,True, False), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.flip(gattaque2,True, False),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.flip(gattaque3,True, False), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.flip(gattaque4,True, False), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.flip(gattaque5,True, False), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.flip(gattaque6,True, False), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.flip(gattaque7,True, False), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.flip(gattaque8,True, False), posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==4:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.rotate(gattaque1,90), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.rotate(gattaque2,90),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.rotate(gattaque3,90), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.rotate(gattaque4,90), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.rotate(gattaque5,90), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.rotate(gattaque6,90), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.rotate(gattaque7,90), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.rotate(gattaque8,90), posPnjA)
            else: tempsA= pygame.time.get_ticks()
    if etatPnjA==3:
        if spnjA==1:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(gtir1, posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(gtir2,posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(gtir3, posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (gtir4, posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==2:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.rotate(gtir1,270), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.rotate(gtir2,270),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.rotate(gtir3,270), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.rotate(gtir4,270), posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==3:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.flip(gtir1,True, False), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.flip(gtir2,True, False),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.flip(gtir3,True, False), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.flip(gtir4,True, False), posPnjA)
            else: tempsA= pygame.time.get_ticks()
        if spnjA==4:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.rotate(gtir1,90), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.rotate(gtir2,90),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.rotate(gtir3,90), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.rotate(gtir4,90), posPnjA)
            else: tempsA= pygame.time.get_ticks()
    if etatPnjA==4:
        if spnjA==1:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(gmort1, posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(gmort2,posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(gmort3, posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (gmort4, posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (gmort5, posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (gmort6, posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (gmort7, posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (gmort8, posPnjA)
            elif 800<pygame.time.get_ticks()- tempsA <=900:
                fenetre.blit (gmort9, posPnjA)
            elif 900<pygame.time.get_ticks()- tempsA:
                fenetre.blit (gmort10, posPnjA)
        if spnjA==2:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.rotate(gmort1,270), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.rotate(gmort2,270),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.rotate(gmort3,270), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.rotate(gmort4,270), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.rotate(gmort5,270), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.rotate(gmort6,270), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.rotate(gmort7,270), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.rotate(gmort8,270), posPnjA)
            elif 800<pygame.time.get_ticks()- tempsA <=900:
                fenetre.blit (pygame.transform.rotate(gmort9,270), posPnjA)
            elif 900<pygame.time.get_ticks()- tempsA:
                fenetre.blit (pygame.transform.rotate(gmort10,270), posPnjA) 
        if spnjA==3:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.flip(gmort1,True, False), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.flip(gmort2,True, False),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.flip(gmort3,True, False), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.flip(gmort4,True, False), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.flip(gmort5,True, False), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.flip(gmort6,True, False), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.flip(gmort7,True, False), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.flip(gmort8,True, False), posPnjA)
            elif 800<pygame.time.get_ticks()- tempsA <=900:
                fenetre.blit (pygame.transform.flip(gmort7,True, False), posPnjA)
            elif 900<pygame.time.get_ticks()- tempsA:
                fenetre.blit (pygame.transform.flip(gmort8,True, False), posPnjA)
        if spnjA==4:
            if 0<= pygame.time.get_ticks() - tempsA <=100:
                fenetre.blit(pygame.transform.rotate(gmort1,90), posPnjA)
            elif 100<= pygame.time.get_ticks() - tempsA <=200:
                fenetre.blit(pygame.transform.rotate(gmort2,90),posPnjA)
            elif 200<= pygame.time.get_ticks() - tempsA <=300:
                fenetre.blit(pygame.transform.rotate(gmort3,90), posPnjA)
            elif 300<pygame.time.get_ticks()- tempsA <=400:
                fenetre.blit (pygame.transform.rotate(gmort4,90), posPnjA)
            elif 400<pygame.time.get_ticks()- tempsA <=500:
                fenetre.blit (pygame.transform.rotate(gmort5,90), posPnjA)
            elif 500<pygame.time.get_ticks()- tempsA <=600:
                fenetre.blit (pygame.transform.rotate(gmort6,90), posPnjA)
            elif 600<pygame.time.get_ticks()- tempsA <=700:
                fenetre.blit (pygame.transform.rotate(gmort7,90), posPnjA)
            elif 700<pygame.time.get_ticks()- tempsA <=800:
                fenetre.blit (pygame.transform.rotate(gmort8,90), posPnjA)
            elif 800<pygame.time.get_ticks()- tempsA <=900:
                fenetre.blit (pygame.transform.rotate(gmort8,90), posPnjA)
            elif 900<pygame.time.get_ticks()- tempsA:
                fenetre.blit (pygame.transform.rotate(gmort9,90), posPnjA)
        





def dessinPnjb():
    global tempsB
    if etatPnjB==0:
        if 0<= pygame.time.get_ticks() - tempsB <=100:
            fenetre.blit(gimmobile1, posPnjB)
        elif 100<= pygame.time.get_ticks() - tempsB <=200:
            fenetre.blit(gimmobile2,posPnjB)
        elif 200<= pygame.time.get_ticks() - tempsB <=300:
            fenetre.blit(gimmobile3, posPnjB)
        elif 300<pygame.time.get_ticks()- tempsB <=400:
            fenetre.blit (gimmobile4, posPnjB)
        elif 400<pygame.time.get_ticks()- tempsB <=500:
            fenetre.blit (gimmobile5, posPnjB)
        elif 500<pygame.time.get_ticks()- tempsB <=600:
            fenetre.blit (gimmobile6, posPnjB)
        elif 600<pygame.time.get_ticks()- tempsB <=700:
            fenetre.blit (gimmobile7, posPnjB)
        elif 700<pygame.time.get_ticks()- tempsB <=800:
            fenetre.blit (gimmobile8, posPnjB)
        elif 800<pygame.time.get_ticks()- tempsB <=900:
            fenetre.blit (gimmobile9, posPnjB)
        elif 900<pygame.time.get_ticks()- tempsB <=1000:
            fenetre.blit (gimmobile10, posPnjB)
        else: tempsB= pygame.time.get_ticks()
    if etatPnjB==1:
        if spnjB==1:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(gmarche1, posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(gmarche2,posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(gmarche3, posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (gmarche4, posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (gmarche5, posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (gmarche6, posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB<=700:
                fenetre.blit (gmarche7, posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (gmarche8, posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==2:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.rotate(gmarche1,270), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.rotate(gmarche2,270),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.rotate(gmarche3,270), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.rotate(gmarche4,270), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.rotate(gmarche5,270), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.rotate(gmarche6,270), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.rotate(gmarche7,270), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.rotate(gmarche8,270), posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==3:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.flip(gmarche1,True, False), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.flip(gmarche2,True, False),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.flip(gmarche3,True, False), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.flip(gmarche4,True, False), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.flip(gmarche5,True, False), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.flip(gmarche6,True, False), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.flip(gmarche7,True, False), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.flip(gmarche8,True, False), posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==4:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.rotate(gmarche1,90), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.rotate(gmarche2,90),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.rotate(gmarche3,90), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.rotate(gmarche4,90), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.rotate(gmarche5,90), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.rotate(gmarche6,90), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.rotate(gmarche7,90), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.rotate(gmarche8,90), posPnjB)
            else: tempsB= pygame.time.get_ticks()
    if etatPnjB==2:
        if spnjB==1:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(gattaque1, posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(gattaque2,posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(gattaque3, posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (gattaque4, posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (gattaque5, posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (gattaque6, posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (gattaque7, posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (gattaque8, posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==2:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.rotate(gattaque1,270), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.rotate(gattaque2,270),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.rotate(gattaque3,270), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.rotate(gattaque4,270), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.rotate(gattaque5,270), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.rotate(gattaque6,270), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.rotate(gattaque7,270), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.rotate(gattaque8,270), posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==3:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.flip(gattaque1,True, False), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.flip(gattaque2,True, False),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.flip(gattaque3,True, False), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.flip(gattaque4,True, False), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.flip(gattaque5,True, False), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.flip(gattaque6,True, False), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.flip(gattaque7,True, False), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.flip(gattaque8,True, False), posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==4:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.rotate(gattaque1,90), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.rotate(gattaque2,90),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.rotate(gattaque3,90), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.rotate(gattaque4,90), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.rotate(gattaque5,90), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.rotate(gattaque6,90), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.rotate(gattaque7,90), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.rotate(gattaque8,90), posPnjB)
            else: tempsB= pygame.time.get_ticks()
    if etatPnjB==3:
        if spnjB==1:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(gtir1, posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(gtir2,posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(gtir3, posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (gtir4, posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==2:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.rotate(gtir1,270), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.rotate(gtir2,270),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.rotate(gtir3,270), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.rotate(gtir4,270), posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==3:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.flip(gtir1,True, False), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.flip(gtir2,True, False),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.flip(gtir3,True, False), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.flip(gtir4,True, False), posPnjB)
            else: tempsB= pygame.time.get_ticks()
        if spnjB==4:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.rotate(gtir1,90), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.rotate(gtir2,90),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.rotate(gtir3,90), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.rotate(gtir4,90), posPnjB)
            else: tempsB= pygame.time.get_ticks()
    if etatPnjB==4:
        if spnjB==1:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(gmort1, posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(gmort2,posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(gmort3, posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (gmort4, posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (gmort5, posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (gmort6, posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (gmort7, posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (gmort8, posPnjB)
            elif 800<pygame.time.get_ticks()- tempsB <=900:
                fenetre.blit (gmort9, posPnjB)
            elif 900<pygame.time.get_ticks()- tempsB:
                fenetre.blit (gmort10, posPnjB)
        if spnjB==2:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.rotate(gmort1,270), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.rotate(gmort2,270),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.rotate(gmort3,270), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.rotate(gmort4,270), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.rotate(gmort5,270), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.rotate(gmort6,270), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.rotate(gmort7,270), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.rotate(gmort8,270), posPnjB)
            elif 800<pygame.time.get_ticks()- tempsB <=900:
                fenetre.blit (pygame.transform.rotate(gmort9,270), posPnjB)
            elif 900<pygame.time.get_ticks()- tempsB:
                fenetre.blit (pygame.transform.rotate(gmort10,270), posPnjB) 
        if spnjB==3:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.flip(gmort1,True, False), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.flip(gmort2,True, False),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.flip(gmort3,True, False), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.flip(gmort4,True, False), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.flip(gmort5,True, False), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.flip(gmort6,True, False), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.flip(gmort7,True, False), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.flip(gmort8,True, False), posPnjB)
            elif 800<pygame.time.get_ticks()- tempsB <=900:
                fenetre.blit (pygame.transform.flip(gmort7,True, False), posPnjB)
            elif 900<pygame.time.get_ticks()- tempsB:
                fenetre.blit (pygame.transform.flip(gmort8,True, False), posPnjB)
        if spnjB==4:
            if 0<= pygame.time.get_ticks() - tempsB <=100:
                fenetre.blit(pygame.transform.rotate(gmort1,90), posPnjB)
            elif 100<= pygame.time.get_ticks() - tempsB <=200:
                fenetre.blit(pygame.transform.rotate(gmort2,90),posPnjB)
            elif 200<= pygame.time.get_ticks() - tempsB <=300:
                fenetre.blit(pygame.transform.rotate(gmort3,90), posPnjB)
            elif 300<pygame.time.get_ticks()- tempsB <=400:
                fenetre.blit (pygame.transform.rotate(gmort4,90), posPnjB)
            elif 400<pygame.time.get_ticks()- tempsB <=500:
                fenetre.blit (pygame.transform.rotate(gmort5,90), posPnjB)
            elif 500<pygame.time.get_ticks()- tempsB <=600:
                fenetre.blit (pygame.transform.rotate(gmort6,90), posPnjB)
            elif 600<pygame.time.get_ticks()- tempsB <=700:
                fenetre.blit (pygame.transform.rotate(gmort7,90), posPnjB)
            elif 700<pygame.time.get_ticks()- tempsB <=800:
                fenetre.blit (pygame.transform.rotate(gmort8,90), posPnjB)
            elif 800<pygame.time.get_ticks()- tempsB <=900:
                fenetre.blit (pygame.transform.rotate(gmort8,90), posPnjB)
            elif 900<pygame.time.get_ticks()- tempsB:
                fenetre.blit (pygame.transform.rotate(gmort9,90), posPnjB)




def dessinPnjc():
    global tempsC
    if etatPnjC==0:
        if 0<= pygame.time.get_ticks() - tempsC <=100:
            fenetre.blit(gimmobile1, posPnjC)
        elif 100<= pygame.time.get_ticks() - tempsC <=200:
            fenetre.blit(gimmobile2,posPnjC)
        elif 200<= pygame.time.get_ticks() - tempsC <=300:
            fenetre.blit(gimmobile3, posPnjC)
        elif 300<pygame.time.get_ticks()- tempsC <=400:
            fenetre.blit (gimmobile4, posPnjC)
        elif 400<pygame.time.get_ticks()- tempsC <=500:
            fenetre.blit (gimmobile5, posPnjC)
        elif 500<pygame.time.get_ticks()- tempsC <=600:
            fenetre.blit (gimmobile6, posPnjC)
        elif 600<pygame.time.get_ticks()- tempsC <=700:
            fenetre.blit (gimmobile7, posPnjC)
        elif 700<pygame.time.get_ticks()- tempsC <=800:
            fenetre.blit (gimmobile8, posPnjC)
        elif 800<pygame.time.get_ticks()- tempsC <=900:
            fenetre.blit (gimmobile9, posPnjC)
        elif 900<pygame.time.get_ticks()- tempsC <=1000:
            fenetre.blit (gimmobile10, posPnjC)
        else: tempsC= pygame.time.get_ticks()
    if etatPnjC==1:
        if spnjC==1:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(gmarche1, posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(gmarche2,posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(gmarche3, posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (gmarche4, posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (gmarche5, posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (gmarche6, posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC<=700:
                fenetre.blit (gmarche7, posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (gmarche8, posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==2:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.rotate(gmarche1,270), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.rotate(gmarche2,270),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.rotate(gmarche3,270), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.rotate(gmarche4,270), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.rotate(gmarche5,270), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.rotate(gmarche6,270), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.rotate(gmarche7,270), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.rotate(gmarche8,270), posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==3:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.flip(gmarche1,True, False), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.flip(gmarche2,True, False),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.flip(gmarche3,True, False), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.flip(gmarche4,True, False), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.flip(gmarche5,True, False), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.flip(gmarche6,True, False), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.flip(gmarche7,True, False), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.flip(gmarche8,True, False), posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==4:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.rotate(gmarche1,90), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.rotate(gmarche2,90),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.rotate(gmarche3,90), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.rotate(gmarche4,90), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.rotate(gmarche5,90), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.rotate(gmarche6,90), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.rotate(gmarche7,90), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.rotate(gmarche8,90), posPnjC)
            else: tempsC= pygame.time.get_ticks()
    if etatPnjC==2:
        if spnjC==1:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(gattaque1, posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(gattaque2,posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(gattaque3, posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (gattaque4, posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (gattaque5, posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (gattaque6, posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (gattaque7, posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (gattaque8, posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==2:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.rotate(gattaque1,270), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.rotate(gattaque2,270),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.rotate(gattaque3,270), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.rotate(gattaque4,270), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.rotate(gattaque5,270), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.rotate(gattaque6,270), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.rotate(gattaque7,270), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.rotate(gattaque8,270), posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==3:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.flip(gattaque1,True, False), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.flip(gattaque2,True, False),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.flip(gattaque3,True, False), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.flip(gattaque4,True, False), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.flip(gattaque5,True, False), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.flip(gattaque6,True, False), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.flip(gattaque7,True, False), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.flip(gattaque8,True, False), posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==4:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.rotate(gattaque1,90), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.rotate(gattaque2,90),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.rotate(gattaque3,90), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.rotate(gattaque4,90), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.rotate(gattaque5,90), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.rotate(gattaque6,90), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.rotate(gattaque7,90), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.rotate(gattaque8,90), posPnjC)
            else: tempsC= pygame.time.get_ticks()
    if etatPnjC==3:
        if spnjC==1:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(gtir1, posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(gtir2,posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(gtir3, posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (gtir4, posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==2:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.rotate(gtir1,270), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.rotate(gtir2,270),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.rotate(gtir3,270), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.rotate(gtir4,270), posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==3:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.flip(gtir1,True, False), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.flip(gtir2,True, False),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.flip(gtir3,True, False), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.flip(gtir4,True, False), posPnjC)
            else: tempsC= pygame.time.get_ticks()
        if spnjC==4:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.rotate(gtir1,90), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.rotate(gtir2,90),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.rotate(gtir3,90), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.rotate(gtir4,90), posPnjC)
            else: tempsC= pygame.time.get_ticks()
    if etatPnjC==4:
        if spnjC==1:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(gmort1, posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(gmort2,posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(gmort3, posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (gmort4, posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (gmort5, posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (gmort6, posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (gmort7, posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (gmort8, posPnjC)
            elif 800<pygame.time.get_ticks()- tempsC <=900:
                fenetre.blit (gmort9, posPnjC)
            elif 900<pygame.time.get_ticks()- tempsC:
                fenetre.blit (gmort10, posPnjC)
        if spnjC==2:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.rotate(gmort1,270), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.rotate(gmort2,270),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.rotate(gmort3,270), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.rotate(gmort4,270), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.rotate(gmort5,270), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.rotate(gmort6,270), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.rotate(gmort7,270), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.rotate(gmort8,270), posPnjC)
            elif 800<pygame.time.get_ticks()- tempsC <=900:
                fenetre.blit (pygame.transform.rotate(gmort9,270), posPnjC)
            elif 900<pygame.time.get_ticks()- tempsC:
                fenetre.blit (pygame.transform.rotate(gmort10,270), posPnjC) 
        if spnjC==3:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.flip(gmort1,True, False), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.flip(gmort2,True, False),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.flip(gmort3,True, False), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.flip(gmort4,True, False), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.flip(gmort5,True, False), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.flip(gmort6,True, False), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.flip(gmort7,True, False), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.flip(gmort8,True, False), posPnjC)
            elif 800<pygame.time.get_ticks()- tempsC <=900:
                fenetre.blit (pygame.transform.flip(gmort7,True, False), posPnjC)
            elif 900<pygame.time.get_ticks()- tempsC:
                fenetre.blit (pygame.transform.flip(gmort8,True, False), posPnjC)
        if spnjC==4:
            if 0<= pygame.time.get_ticks() - tempsC <=100:
                fenetre.blit(pygame.transform.rotate(gmort1,90), posPnjC)
            elif 100<= pygame.time.get_ticks() - tempsC <=200:
                fenetre.blit(pygame.transform.rotate(gmort2,90),posPnjC)
            elif 200<= pygame.time.get_ticks() - tempsC <=300:
                fenetre.blit(pygame.transform.rotate(gmort3,90), posPnjC)
            elif 300<pygame.time.get_ticks()- tempsC <=400:
                fenetre.blit (pygame.transform.rotate(gmort4,90), posPnjC)
            elif 400<pygame.time.get_ticks()- tempsC <=500:
                fenetre.blit (pygame.transform.rotate(gmort5,90), posPnjC)
            elif 500<pygame.time.get_ticks()- tempsC <=600:
                fenetre.blit (pygame.transform.rotate(gmort6,90), posPnjC)
            elif 600<pygame.time.get_ticks()- tempsC <=700:
                fenetre.blit (pygame.transform.rotate(gmort7,90), posPnjC)
            elif 700<pygame.time.get_ticks()- tempsC <=800:
                fenetre.blit (pygame.transform.rotate(gmort8,90), posPnjC)
            elif 800<pygame.time.get_ticks()- tempsC <=900:
                fenetre.blit (pygame.transform.rotate(gmort8,90), posPnjC)
            elif 900<pygame.time.get_ticks()- tempsC:
                fenetre.blit (pygame.transform.rotate(gmort9,90), posPnjC)




def dessinPnjd():
    global tempsD
    if etatPnjD==0:
        if 0<= pygame.time.get_ticks() - tempsD <=100:
            fenetre.blit(gimmobile1, posPnjD)
        elif 100<= pygame.time.get_ticks() - tempsD <=200:
            fenetre.blit(gimmobile2,posPnjD)
        elif 200<= pygame.time.get_ticks() - tempsD <=300:
            fenetre.blit(gimmobile3, posPnjD)
        elif 300<pygame.time.get_ticks()- tempsD <=400:
            fenetre.blit (gimmobile4, posPnjD)
        elif 400<pygame.time.get_ticks()- tempsD <=500:
            fenetre.blit (gimmobile5, posPnjD)
        elif 500<pygame.time.get_ticks()- tempsD <=600:
            fenetre.blit (gimmobile6, posPnjD)
        elif 600<pygame.time.get_ticks()- tempsD <=700:
            fenetre.blit (gimmobile7, posPnjD)
        elif 700<pygame.time.get_ticks()- tempsD <=800:
            fenetre.blit (gimmobile8, posPnjD)
        elif 800<pygame.time.get_ticks()- tempsD <=900:
            fenetre.blit (gimmobile9, posPnjD)
        elif 900<pygame.time.get_ticks()- tempsD <=1000:
            fenetre.blit (gimmobile10, posPnjD)
        else: tempsD= pygame.time.get_ticks()
    if etatPnjD==1:
        if spnjD==1:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(gmarche1, posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(gmarche2,posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(gmarche3, posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (gmarche4, posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (gmarche5, posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (gmarche6, posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD<=700:
                fenetre.blit (gmarche7, posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (gmarche8, posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==2:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.rotate(gmarche1,270), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.rotate(gmarche2,270),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.rotate(gmarche3,270), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.rotate(gmarche4,270), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.rotate(gmarche5,270), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.rotate(gmarche6,270), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.rotate(gmarche7,270), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.rotate(gmarche8,270), posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==3:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.flip(gmarche1,True, False), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.flip(gmarche2,True, False),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.flip(gmarche3,True, False), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.flip(gmarche4,True, False), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.flip(gmarche5,True, False), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.flip(gmarche6,True, False), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.flip(gmarche7,True, False), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.flip(gmarche8,True, False), posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==4:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.rotate(gmarche1,90), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.rotate(gmarche2,90),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.rotate(gmarche3,90), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.rotate(gmarche4,90), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.rotate(gmarche5,90), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.rotate(gmarche6,90), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.rotate(gmarche7,90), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.rotate(gmarche8,90), posPnjD)
            else: tempsD= pygame.time.get_ticks()
    if etatPnjD==2:
        if spnjD==1:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(gattaque1, posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(gattaque2,posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(gattaque3, posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (gattaque4, posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (gattaque5, posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (gattaque6, posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (gattaque7, posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (gattaque8, posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==2:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.rotate(gattaque1,270), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.rotate(gattaque2,270),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.rotate(gattaque3,270), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.rotate(gattaque4,270), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.rotate(gattaque5,270), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.rotate(gattaque6,270), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.rotate(gattaque7,270), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.rotate(gattaque8,270), posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==3:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.flip(gattaque1,True, False), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.flip(gattaque2,True, False),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.flip(gattaque3,True, False), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.flip(gattaque4,True, False), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.flip(gattaque5,True, False), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.flip(gattaque6,True, False), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.flip(gattaque7,True, False), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.flip(gattaque8,True, False), posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==4:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.rotate(gattaque1,90), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.rotate(gattaque2,90),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.rotate(gattaque3,90), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.rotate(gattaque4,90), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.rotate(gattaque5,90), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.rotate(gattaque6,90), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.rotate(gattaque7,90), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.rotate(gattaque8,90), posPnjD)
            else: tempsD= pygame.time.get_ticks()
    if etatPnjD==3:
        if spnjD==1:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(gtir1, posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(gtir2,posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(gtir3, posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (gtir4, posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==2:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.rotate(gtir1,270), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.rotate(gtir2,270),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.rotate(gtir3,270), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.rotate(gtir4,270), posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==3:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.flip(gtir1,True, False), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.flip(gtir2,True, False),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.flip(gtir3,True, False), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.flip(gtir4,True, False), posPnjD)
            else: tempsD= pygame.time.get_ticks()
        if spnjD==4:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.rotate(gtir1,90), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.rotate(gtir2,90),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.rotate(gtir3,90), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.rotate(gtir4,90), posPnjD)
            else: tempsD= pygame.time.get_ticks()
    if etatPnjD==4:
        if spnjD==1:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(gmort1, posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(gmort2,posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(gmort3, posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (gmort4, posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (gmort5, posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (gmort6, posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (gmort7, posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (gmort8, posPnjD)
            elif 800<pygame.time.get_ticks()- tempsD <=900:
                fenetre.blit (gmort9, posPnjD)
            elif 900<pygame.time.get_ticks()- tempsD:
                fenetre.blit (gmort10, posPnjD)
        if spnjD==2:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.rotate(gmort1,270), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.rotate(gmort2,270),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.rotate(gmort3,270), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.rotate(gmort4,270), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.rotate(gmort5,270), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.rotate(gmort6,270), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.rotate(gmort7,270), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.rotate(gmort8,270), posPnjD)
            elif 800<pygame.time.get_ticks()- tempsD <=900:
                fenetre.blit (pygame.transform.rotate(gmort9,270), posPnjD)
            elif 900<pygame.time.get_ticks()- tempsD:
                fenetre.blit (pygame.transform.rotate(gmort10,270), posPnjD) 
        if spnjD==3:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.flip(gmort1,True, False), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.flip(gmort2,True, False),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.flip(gmort3,True, False), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.flip(gmort4,True, False), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.flip(gmort5,True, False), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.flip(gmort6,True, False), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.flip(gmort7,True, False), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.flip(gmort8,True, False), posPnjD)
            elif 800<pygame.time.get_ticks()- tempsD <=900:
                fenetre.blit (pygame.transform.flip(gmort7,True, False), posPnjD)
            elif 900<pygame.time.get_ticks()- tempsD:
                fenetre.blit (pygame.transform.flip(gmort8,True, False), posPnjD)
        if spnjD==4:
            if 0<= pygame.time.get_ticks() - tempsD <=100:
                fenetre.blit(pygame.transform.rotate(gmort1,90), posPnjD)
            elif 100<= pygame.time.get_ticks() - tempsD <=200:
                fenetre.blit(pygame.transform.rotate(gmort2,90),posPnjD)
            elif 200<= pygame.time.get_ticks() - tempsD <=300:
                fenetre.blit(pygame.transform.rotate(gmort3,90), posPnjD)
            elif 300<pygame.time.get_ticks()- tempsD <=400:
                fenetre.blit (pygame.transform.rotate(gmort4,90), posPnjD)
            elif 400<pygame.time.get_ticks()- tempsD <=500:
                fenetre.blit (pygame.transform.rotate(gmort5,90), posPnjD)
            elif 500<pygame.time.get_ticks()- tempsD <=600:
                fenetre.blit (pygame.transform.rotate(gmort6,90), posPnjD)
            elif 600<pygame.time.get_ticks()- tempsD <=700:
                fenetre.blit (pygame.transform.rotate(gmort7,90), posPnjD)
            elif 700<pygame.time.get_ticks()- tempsD <=800:
                fenetre.blit (pygame.transform.rotate(gmort8,90), posPnjD)
            elif 800<pygame.time.get_ticks()- tempsD <=900:
                fenetre.blit (pygame.transform.rotate(gmort8,90), posPnjD)
            elif 900<pygame.time.get_ticks()- tempsD:
                fenetre.blit (pygame.transform.rotate(gmort9,90), posPnjD)




def DessinTout():
    fenetre.fill((50,50,50))
    if posKunai!= (-50,-50):
        if sensKunai==1:
            fenetre.blit(pygame.transform.rotate(Kunai,270), posKunai)
        if sensKunai==2:
            fenetre.blit(pygame.transform.flip(Kunai,False,True),posKunai)
        if sensKunai==3:
            fenetre.blit(pygame.transform.rotate(Kunai,90),posKunai)
        if sensKunai==4:
            fenetre.blit(Kunai, posKunai)
    if posBalleA !=(-50,-50):
        if sensBalleA==1:
            fenetre.blit(balle,posBalleA)
        if sensBalleA==2:
            fenetre.blit(pygame.transform.rotate(balle,270), posBalleA)
        if sensBalleA==3:
            fenetre.blit(pygame.transform.flip(balle, True, False), posBalleA)
        if sensBalleA==4:
            fenetre.blit(pygame.transform.rotate(balle,90), posBalleA)
    if posBalleB !=(-50,-50):
        if sensBalleB==1:
            fenetre.blit(balle, posBalleB)
        if sensBalleB==2:
            fenetre.blit(pygame.transform.rotate(balle,270), posBalleB)
        if sensBalleB==3:
            fenetre.blit(pygame.transform.flip(balle, True, False), posBalleB)
        if sensBalleB==4:
            fenetre.blit(pygame.transform.rotate(balle,90), posBalleB)
    if posBalleC !=(-50,-50):
        if sensBalleC==1:
            fenetre.blit(balle, posBalleC)
        if sensBalleC==2:
            fenetre.blit(pygame.transform.rotate(balle,270), posBalleC)
        if sensBalleC==3:
            fenetre.blit(pygame.transform.flip(balle, True, False), posBalleC)
        if sensBalleC==4:
            fenetre.blit(pygame.transform.rotate(balle,90), posBalleC)
    if posBalleD !=(-50,-50):
        if sensBalleD==1:
            fenetre.blit(balle, posBalleD)
        if sensBalleD==2:
            fenetre.blit(pygame.transform.rotate(balle,270), posBalleD)
        if sensBalleD==3:
            fenetre.blit(pygame.transform.flip(balle, True, False), posBalleD)
        if sensBalleD==4:
            fenetre.blit(pygame.transform.rotate(balle,90), posBalleD)
    if objet==0:
        fenetre.blit(item, posItem)
    dessinPerso()
    dessinPnja()
    dessinPnjb()
    dessinPnjc()
    dessinPnjd()
    DessinSalles()
    dessinCDV()
    pygame.display.flip()




#déplacement pnj
def déplacementPnjA():
    global posPnjA, spnjA, hitboxPnjA, posBalleA, cdvA1, cdvA2, cdvA3, cdvA4, etatPnjA, possibleA
    if spnjA==1:
        if etatPnjA==1:
            if posPnjA[0]<520:
                posPnjA=(posPnjA[0]+2, posPnjA[1])
                hitboxPnjA=hitboxPnjA.move(2,0)
                cdvA1=cdvA1.move(2,0)
            else:
                spnjA=2
                cdvA2=pygame.Rect(posPnjA[0]-10,posPnjA[1]+55,76,130)
        if hitboxPnjA.colliderect(hitboxPerso)==True and cdvA1.colliderect(hitboxPerso)==False:
            etatPnjA=0
        if hitboxPnjA.colliderect(hitboxPerso)==False and cdvA1.colliderect(hitboxPerso)==False:
            etatPnjA=1
        if hitboxPnjA.colliderect(hitboxPerso)==True and cdvA1.colliderect(hitboxPerso)==True:
            etatPnjA=2
        if hitboxPnjA.colliderect(hitboxPerso)==False and cdvA1.colliderect(hitboxPerso)==True:
            if possibleA==1:
                etatPnjA=3
                posBalleA=(posPnjA[0]+50,posPnjA[1]+20)
                possibleA=0
    if spnjA==2:
        if etatPnjA==1:
            if posPnjA[1]<330:
                posPnjA=(posPnjA[0],posPnjA[1]+2)
                hitboxPnjA=hitboxPnjA.move(0,2)
                cdvA2=cdvA2.move(0,2)
            else:
                spnjA=3
                cdvA3=pygame.Rect(posPnjA[0],posPnjA[1]-10,-130,76)
        if hitboxPnjA.colliderect(hitboxPerso)==True and cdvA2.colliderect(hitboxPerso)==False:
            etatPnjA=0
        if hitboxPnjA.colliderect(hitboxPerso)==False and cdvA2.colliderect(hitboxPerso)==False:
            etatPnjA=1
        if hitboxPnjA.colliderect(hitboxPerso)==True and cdvA2.colliderect(hitboxPerso)==True:
            etatPnjA=2
        if hitboxPnjA.colliderect(hitboxPerso)==False and cdvA2.colliderect(hitboxPerso)==True:
            if possibleA==1:
                etatPnjA=3
                posBalleA=(posPnjA[0]+20,posPnjA[1]+50)
                possibleA=0
    if spnjA==3:
        if etatPnjA==1:
            if posPnjA[0]>70:
                posPnjA=(posPnjA[0]-2, posPnjA[1])
                hitboxPnjA=hitboxPnjA.move(-2,0)
                cdvA3=cdvA3.move(-2,0)
            else:
                spnjA=4
                cdvA4=pygame.Rect(posPnjA[0]-15,posPnjA[1]+5,76,-130)
        cdvA3_box = box(cdvA3[0], cdvA3[1], cdvA3[0] + cdvA3[2], cdvA3[1] + cdvA3[3])
        hitboxPerso_box = box(hitboxPerso[0], hitboxPerso[1], hitboxPerso[0] + hitboxPerso[2], hitboxPerso[1] + hitboxPerso[3])
        if hitboxPnjA.colliderect(hitboxPerso)==True and cdvA3.colliderect(hitboxPerso)==False:
            etatPnjA=0
        if hitboxPnjA.colliderect(hitboxPerso)==False and cdvA3.colliderect(hitboxPerso)==False:
            etatPnjA=1
        if hitboxPnjA.colliderect(hitboxPerso)==True and cdvA3_box.intersection(hitboxPerso_box):
            etatPnjA=2
        if hitboxPnjA.colliderect(hitboxPerso)==False and cdvA3_box.intersection(hitboxPerso_box):
            if possibleA==1:
                etatPnjA=3
                posBalleA=(posPnjA[0]-20,posPnjA[1]+20)
                possibleA=0
    if spnjA==4:
        if etatPnjA==1:
            if posPnjA[1]>20:
                posPnjA=(posPnjA[0], posPnjA[1]-2)
                hitboxPnjA=hitboxPnjA.move(0,-2)
                cdvA4=cdvA4.move(0,-2)
            else:
                spnjA=1
                cdvA1=pygame.Rect(posPnjA[0]+50,posPnjA[1]-5,130,76)
        hitboxPerso_box = box(hitboxPerso[0], hitboxPerso[1], hitboxPerso[0] + hitboxPerso[2], hitboxPerso[1] + hitboxPerso[3])
        cdvA4_box = box(cdvA4[0], cdvA4[1], cdvA4[0] + cdvA4[2], cdvA4[1] + cdvA4[3])
        if hitboxPnjA.colliderect(hitboxPerso)==True and cdvA4.colliderect(hitboxPerso)==False:
            etatPnjA=0
        if hitboxPnjA.colliderect(hitboxPerso)==False and cdvA4.colliderect(hitboxPerso)==False:
            etatPnjA=1
        if hitboxPnjA.colliderect(hitboxPerso)==True and cdvA4_box.intersection(hitboxPerso_box):
            etatPnjA=2
        if hitboxPnjA.colliderect(hitboxPerso)==False and cdvA4_box.intersection(hitboxPerso_box):
            if possibleA==1:
                etatPnjA=3
                posBalleA=(posPnjA[0]+20,posPnjA[1]-20)
                possibleA=0



def déplacementPnjB():
    global posPnjB, spnjB, hitboxPnjB, posBalleB, cdvB1, cdvB2, cdvB3, cdvB4, etatPnjB,possibleB
    if spnjB==1:
        if etatPnjB==1:
            if posPnjB[0]<1305:
                posPnjB=(posPnjB[0]+2, posPnjB[1])
                hitboxPnjB=hitboxPnjB.move(2,0)
                cdvB1=cdvB1.move(2,0)
            else:
                spnjB=2
                cdvB2=pygame.Rect(posPnjB[0]-10,posPnjB[1]+55,76,130)
        if hitboxPnjB.colliderect(hitboxPerso)==True and cdvB1.colliderect(hitboxPerso)==False:
            etatPnjB=0
        if hitboxPnjB.colliderect(hitboxPerso)==False and cdvB1.colliderect(hitboxPerso)==False:
            etatPnjB=1
        if hitboxPnjB.colliderect(hitboxPerso)==True and cdvB1.colliderect(hitboxPerso)==True:
            etatPnjB=2
        if hitboxPnjB.colliderect(hitboxPerso)==False and cdvB1.colliderect(hitboxPerso)==True:
            if possibleB==1:
                etatPnjB=3
                posBalleB=(posPnjB[0]+50,posPnjB[1]+20)
                possibleB=0
    if spnjB==2:
        if etatPnjB==1:
            if posPnjB[1]<515:
                posPnjB=(posPnjB[0],posPnjB[1]+2)
                hitboxPnjB=hitboxPnjB.move(0,2)
                cdvB2=cdvB2.move(0,2)
            else:
                spnjB=3
                cdvB3=pygame.Rect(posPnjB[0],posPnjB[1]-10,-130,76)
        if hitboxPnjB.colliderect(hitboxPerso)==True and cdvB2.colliderect(hitboxPerso)==False:
            etatPnjB=0
        if hitboxPnjB.colliderect(hitboxPerso)==False and cdvB2.colliderect(hitboxPerso)==False:
            etatPnjB=1
        if hitboxPnjB.colliderect(hitboxPerso)==True and cdvB2.colliderect(hitboxPerso)==True:
            etatPnjB=2
        if hitboxPnjB.colliderect(hitboxPerso)==False and cdvB2.colliderect(hitboxPerso)==True:
            if possibleB==1:
                etatPnjB=3
                posBalleB=(posPnjB[0]+20,posPnjB[1]+50)
                possibleB=0
    if spnjB==3:
        if etatPnjB==1:
            if posPnjB[0]>925:
                posPnjB=(posPnjB[0]-2, posPnjB[1])
                hitboxPnjB=hitboxPnjB.move(-2,0)
                cdvB3=cdvB3.move(-2,0)
            else:
                spnjB=4
                cdvB4=pygame.Rect(posPnjB[0]-15,posPnjB[1]+5,76,-130)
        hitboxPerso_box = box(hitboxPerso[0], hitboxPerso[1], hitboxPerso[0] + hitboxPerso[2], hitboxPerso[1] + hitboxPerso[3])
        cdvB3_box = box(cdvB3[0], cdvB3[1], cdvB3[0] + cdvB3[2], cdvB3[1] + cdvB3[3])
        if hitboxPnjB.colliderect(hitboxPerso)==True and cdvB3.colliderect(hitboxPerso)==False:
            etatPnjB=0
        if hitboxPnjB.colliderect(hitboxPerso)==False and cdvB3.colliderect(hitboxPerso)==False:
            etatPnjB=1
        if hitboxPnjB.colliderect(hitboxPerso)==True and cdvB3_box.intersection(hitboxPerso_box):
            etatPnjB=2
        if hitboxPnjB.colliderect(hitboxPerso)==False and cdvB3_box.intersection(hitboxPerso_box):
            if possibleB==1:
                etatPnjB=3
                posBalleB=(posPnjB[0]-20,posPnjB[1]+20)
                possibleB=0
    if spnjB==4:
        if etatPnjB==1:
            if posPnjB[1]>20:
                posPnjB=(posPnjB[0], posPnjB[1]-2)
                hitboxPnjB=hitboxPnjB.move(0,-2)
                cdvB4=cdvB4.move(0,-2)
            else:
                spnjB=1
                cdvB1=pygame.Rect(posPnjB[0]+50,posPnjB[1]-5,130,76)
        hitboxPerso_box = box(hitboxPerso[0], hitboxPerso[1], hitboxPerso[0] + hitboxPerso[2], hitboxPerso[1] + hitboxPerso[3])
        cdvB4_box = box(cdvB4[0], cdvB4[1], cdvB4[0] + cdvB4[2], cdvB4[1] + cdvB4[3])
        if hitboxPnjB.colliderect(hitboxPerso)==True and cdvB4.colliderect(hitboxPerso)==False:
            etatPnjB=0
        if hitboxPnjB.colliderect(hitboxPerso)==False and cdvB4.colliderect(hitboxPerso)==False:
            etatPnjB=1
        if hitboxPnjB.colliderect(hitboxPerso)==True and cdvB4_box.intersection(hitboxPerso_box):
            etatPnjB=2
        if hitboxPnjB.colliderect(hitboxPerso)==False and cdvB4_box.intersection(hitboxPerso_box):
            if possibleB==1:
                etatPnjB=3
                posBalleB=(posPnjB[0]+20,posPnjB[1]-20)
                possibleB=0


def déplacementPnjC():
    global posPnjC, spnjC, hitboxPnjC, posBalleC, cdvC1, cdvC2, cdvC3, cdvC4, etatPnjC, possibleC
    if spnjC == 1:
        if etatPnjC==1:
            if posPnjC[0] < 380:
                posPnjC = (posPnjC[0] + 2, posPnjC[1])
                hitboxPnjC = hitboxPnjC.move(2, 0)
                cdvC1=cdvC1.move(2,0)
            else:
                spnjC = 2
                cdvC2=pygame.Rect(posPnjC[0]-10,posPnjC[1]+55,76,130)
        if hitboxPnjC.colliderect(hitboxPerso)==True and cdvC1.colliderect(hitboxPerso)==False:
            etatPnjC=0
        if hitboxPnjC.colliderect(hitboxPerso)==False and cdvC1.colliderect(hitboxPerso)==False:
            etatPnjC=1
        if hitboxPnjC.colliderect(hitboxPerso)==True and cdvC1.colliderect(hitboxPerso)==True:
            etatPnjC=2
        if hitboxPnjC.colliderect(hitboxPerso)==False and cdvC1.colliderect(hitboxPerso)==True:
            if possibleC==1:
                etatPnjC=3
                posBalleC=(posPnjC[0]+50,posPnjC[1]+20)
                possibleC=0
    if spnjC == 2:
        if etatPnjC==1:
            if posPnjC[1] < 880:
                posPnjC = (posPnjC[0], posPnjC[1] + 2)
                hitboxPnjC = hitboxPnjC.move(0, 2)
                cdvC2=cdvC2.move(0,2)
            else:
                spnjC = 3
                cdvC3=pygame.Rect(posPnjC[0],posPnjC[1]-10,-130,76)
        if hitboxPnjC.colliderect(hitboxPerso)==True and cdvC2.colliderect(hitboxPerso)==False:
            etatPnjC=0
        if hitboxPnjC.colliderect(hitboxPerso)==False and cdvC2.colliderect(hitboxPerso)==False:
            etatPnjC=1
        if hitboxPnjC.colliderect(hitboxPerso)==True and cdvC2.colliderect(hitboxPerso)==True:
            etatPnjC=2
        if hitboxPnjC.colliderect(hitboxPerso)==False and cdvC2.colliderect(hitboxPerso)==True:
            if possibleC==1:
                etatPnjC=3
                posBalleC=(posPnjC[0]+20,posPnjC[1]+50)
                possibleC=0
    if spnjC == 3:
        if etatPnjC==1:
            if posPnjC[0] > 60:
                posPnjC = (posPnjC[0] - 2, posPnjC[1])
                hitboxPnjC = hitboxPnjC.move(-2, 0)
                cdvC3=cdvC3.move(-2,0)
            else:
                spnjC = 4
                cdvC4=pygame.Rect(posPnjC[0]-15,posPnjC[1]+5,76,-130)
        hitboxPerso_box = box(hitboxPerso[0], hitboxPerso[1], hitboxPerso[0] + hitboxPerso[2], hitboxPerso[1] + hitboxPerso[3])
        cdvC3_box = box(cdvC3[0], cdvC3[1], cdvC3[0] + cdvC3[2], cdvC3[1] + cdvC3[3])
        if hitboxPnjC.colliderect(hitboxPerso)==True and cdvC3.colliderect(hitboxPerso)==False:
            etatPnjC=0
        if hitboxPnjC.colliderect(hitboxPerso)==False and cdvC3.colliderect(hitboxPerso)==False:
            etatPnjC=1
        if hitboxPnjC.colliderect(hitboxPerso)==True and cdvC3_box.intersection(hitboxPerso_box):
            etatPnjC=2
        if hitboxPnjC.colliderect(hitboxPerso)==False and cdvC3_box.intersection(hitboxPerso_box):
            if possibleC==1:
                etatPnjC=3
                posBalleC=(posPnjC[0]-20,posPnjC[1]+20)
                possibleC=0
    if spnjC == 4:
        if etatPnjC==1:
            if posPnjC[1] > 410:
                posPnjC = (posPnjC[0], posPnjC[1] - 2)
                hitboxPnjC = hitboxPnjC.move(0, -2)
                cdvC4=cdvC4.move(0,-2)
            else:
                spnjC = 1
                cdvC1=pygame.Rect(posPnjC[0]+50,posPnjC[1]-5,130,76)
        hitboxPerso_box = box(hitboxPerso[0], hitboxPerso[1], hitboxPerso[0] + hitboxPerso[2], hitboxPerso[1] + hitboxPerso[3])
        cdvC4_box = box(cdvC4[0], cdvC4[1], cdvC4[0] + cdvC4[2], cdvC4[1] + cdvC4[3])
        if hitboxPnjC.colliderect(hitboxPerso)==True and cdvC4.colliderect(hitboxPerso)==False:
            etatPnjC=0
        if hitboxPnjC.colliderect(hitboxPerso)==False and cdvC4.colliderect(hitboxPerso)==False:
            etatPnjC=1
        if hitboxPnjC.colliderect(hitboxPerso)==True and cdvC4_box.intersection(hitboxPerso_box):
            etatPnjC=2
        if hitboxPnjC.colliderect(hitboxPerso)==False and cdvC4_box.intersection(hitboxPerso_box):
            if possibleC==1:
                etatPnjC=3
                posBalleC=(posPnjC[0]+20,posPnjC[1]-20)
                possibleC=0

def déplacementPnjD():
    global posPnjD, spnjD, hitboxPnjD, posBalleD, cdvD1, cdvD2, cdvD3,cdvD4, etatPnjD, possibleD
    if spnjD == 1:
        if etatPnjD==1:
            if posPnjD[0] < 1330:
                posPnjD = (posPnjD[0]+2, posPnjD[1])
                hitboxPnjD = hitboxPnjD.move(2, 0)
                cdvD1=cdvD1.move(2,0)
            else:
                spnjD = 2
                cdvD2=pygame.Rect(posPnjD[0]-10,posPnjD[1]+55,76,130)
        if hitboxPnjD.colliderect(hitboxPerso)==True and cdvD1.colliderect(hitboxPerso)==False:
            etatPnjD=0
        if hitboxPnjD.colliderect(hitboxPerso)==False and cdvD1.colliderect(hitboxPerso)==False:
            etatPnjD=1
        if hitboxPnjD.colliderect(hitboxPerso)==True and cdvD1.colliderect(hitboxPerso)==True:
            etatPnjD=2
        if hitboxPnjD.colliderect(hitboxPerso)==False and cdvD1.colliderect(hitboxPerso)==True:
            if possibleD==1:
                etatPnjD=3
                posBalleD=(posPnjD[0]+50,posPnjD[1]+20)
                possibleD=0
    if spnjD == 2:
        if etatPnjD==1:
            if posPnjD[1] < 880:
                posPnjD = (posPnjD[0], posPnjD[1]+2)
                hitboxPnjD = hitboxPnjD.move(0, 2)
                cdvD2=cdvD2.move(0,2)
            else:
                spnjD = 3
                cdvD3=pygame.Rect(posPnjD[0],posPnjD[1]-10,-130,76)
        if hitboxPnjD.colliderect(hitboxPerso)==True and cdvD2.colliderect(hitboxPerso)==False:
            etatPnjD=0
        if hitboxPnjD.colliderect(hitboxPerso)==False and cdvD2.colliderect(hitboxPerso)==False:
            etatPnjD=1
        if hitboxPnjD.colliderect(hitboxPerso)==True and cdvD2.colliderect(hitboxPerso)==True:
            etatPnjD=2
        if hitboxPnjD.colliderect(hitboxPerso)==False and cdvD2.colliderect(hitboxPerso)==True:
            if possibleD==1:
                etatPnjD=3
                posBalleD=(posPnjD[0]+20,posPnjD[1]+50)
                possibleD=0
    if spnjD == 3:
        if etatPnjD==1:
            if posPnjD[0] > 880:
                posPnjD = (posPnjD[0]-2, posPnjD[1])
                hitboxPnjD = hitboxPnjD.move(-2, 0)
                cdvD3=cdvD3.move(-2,0)
            else:
                spnjD = 4
                cdvD4=pygame.Rect(posPnjD[0]-15,posPnjD[1]+5,76,-130)
        hitboxPerso_box = box(hitboxPerso[0], hitboxPerso[1], hitboxPerso[0] + hitboxPerso[2], hitboxPerso[1] + hitboxPerso[3])
        cdvD3_box = box(cdvD3[0], cdvD3[1], cdvD3[0] + cdvD3[2], cdvD3[1] + cdvD3[3])
        if hitboxPnjD.colliderect(hitboxPerso)==True and cdvD3.colliderect(hitboxPerso)==False:
            etatPnjD=0
        if hitboxPnjD.colliderect(hitboxPerso)==False and cdvD3.colliderect(hitboxPerso)==False:
            etatPnjD=1
        if hitboxPnjD.colliderect(hitboxPerso)==True and cdvD3_box.intersection(hitboxPerso_box):
            etatPnjD=2
        if hitboxPnjD.colliderect(hitboxPerso)==False and cdvD3_box.intersection(hitboxPerso_box):
            if possibleD==1:
                etatPnjD=3
                posBalleD=(posPnjB[0]-20,posPnjB[1]+20)
                possibleD=0
    if spnjD == 4:
        if etatPnjD==1:
            if posPnjD[1] > 530:
                posPnjD = (posPnjD[0], posPnjD[1]-2)
                hitboxPnjD = hitboxPnjD.move(0, -2)
                cdvD4=cdvD4.move(0,-2)
            else:
                spnjD = 1
                cdvD1=pygame.Rect(posPnjD[0]+50,posPnjD[1]-5,130,76)
        hitboxPerso_box = box(hitboxPerso[0], hitboxPerso[1], hitboxPerso[0] + hitboxPerso[2], hitboxPerso[1] + hitboxPerso[3])
        cdvD4_box = box(cdvD4[0], cdvD4[1], cdvD4[0] + cdvD4[2], cdvD4[1] + cdvD4[3])
        if hitboxPnjD.colliderect(hitboxPerso)==True and cdvD4.colliderect(hitboxPerso)==False:
            etatPnjD=0
        if hitboxPnjD.colliderect(hitboxPerso)==False and cdvD4.colliderect(hitboxPerso)==False:
            etatPnjD=1
        if hitboxPnjD.colliderect(hitboxPerso)==True and cdvD4_box.intersection(hitboxPerso_box):
            etatPnjD=2
        if hitboxPnjD.colliderect(hitboxPerso)==False and cdvD4_box.intersection(hitboxPerso_box):
            if possibleD==1:
                etatPnjD=3
                posBalleD=(posPnjD[0]+20,posPnjD[1]-20)
                possibleD=0




#Gestion des clics
def gestionFermeture():
    global jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            jeu = 0

                
def gestionClic():
    global posPerso, hitboxPerso, obstacles, déplacement, chgmtDirection, sens,etatPerso, posKunai, possible, kunaiDispo, objet
    touchePressee=pygame.key.get_pressed()
    if touchePressee[pygame.K_RIGHT]==True and posPerso[0]<largeurFenetre-15 and touchePressee[pygame.K_UP]==False and touchePressee[pygame.K_DOWN]==False:
        etatPerso=1
        if sens!=1:
            for rectangle in obstacles:
                if hitboxPerso.colliderect(rectangle)==True:
                    chgmtDirection=1
                if hitboxPerso.colliderect(rectangle)==False:
                    chgmtDirection=0
            posPerso=(posPerso[0]+2, posPerso[1])
            hitboxPerso=hitboxPerso.move(2,0)
        if sens==1:
                for rectangle in obstacles:
                    if hitboxPerso.colliderect(rectangle)==True:
                        déplacement=0
                if déplacement==1 :
                    posPerso=(posPerso[0]+2, posPerso[1])
                    hitboxPerso=hitboxPerso.move(2,0)
        if chgmtDirection==0:
            sens=1
        déplacement=1

    if touchePressee[pygame.K_LEFT]==True and posPerso[0]>15 and touchePressee[pygame.K_UP]==False and touchePressee[pygame.K_DOWN]==False:
        etatPerso=1
        if sens!=3:
            for rectangle in obstacles:
                if hitboxPerso.colliderect(rectangle)==True:
                    chgmtDirection=1
                if hitboxPerso.colliderect(rectangle)==False:
                    chgmtDirection=0
            posPerso=(posPerso[0]-2, posPerso[1])
            hitboxPerso=hitboxPerso.move(-2,0)
        if sens==3:
                for rectangle in obstacles:
                    if hitboxPerso.colliderect(rectangle)==True:
                        déplacement=0
                if déplacement==1 :
                    posPerso=(posPerso[0]-2, posPerso[1])
                    hitboxPerso=hitboxPerso.move(-2,0)
        if chgmtDirection==0:
            sens=3
        déplacement=1

    if touchePressee [pygame.K_UP]==True and posPerso[1]>15 and touchePressee[pygame.K_RIGHT]==False and touchePressee[pygame.K_LEFT]==False:
        etatPerso=1
        if sens!=4:
            for rectangle in obstacles:
                if hitboxPerso.colliderect(rectangle)==True:
                    chgmtDirection=1
                if hitboxPerso.colliderect(rectangle)==False:
                    chgmtDirection=0
            posPerso=(posPerso[0], posPerso[1]-2)
            hitboxPerso=hitboxPerso.move(0,-2)
        if sens==4:
                for rectangle in obstacles:
                    if hitboxPerso.colliderect(rectangle)==True:
                        déplacement=0
                if déplacement==1 :
                    posPerso=(posPerso[0], posPerso[1]-2)
                    hitboxPerso=hitboxPerso.move(0,-2)
        if chgmtDirection==0:
            sens=4
        déplacement=1


    if touchePressee[pygame.K_DOWN]==True and posPerso[1]<hauteurFenetre-15 and touchePressee[pygame.K_RIGHT]==False and touchePressee[pygame.K_LEFT]==False:
        etatPerso=1
        if sens!=2:
            for rectangle in obstacles:
                if hitboxPerso.colliderect(rectangle)==True:
                    chgmtDirection=1
                if hitboxPerso.colliderect(rectangle)==False:
                    chgmtDirection=0
            posPerso=(posPerso[0], posPerso[1]+2)
            hitboxPerso=hitboxPerso.move(0,2)
        if sens==2:
                for rectangle in obstacles:
                    if hitboxPerso.colliderect(rectangle)==True:
                        déplacement=0
                if déplacement==1 :
                    posPerso=(posPerso[0], posPerso[1]+2)
                    hitboxPerso=hitboxPerso.move(0,2)
        if chgmtDirection==0:
            sens=2
        déplacement=1

    if touchePressee[pygame.K_x]==True:
        for hitbox in hitboxPnj:
            if hitboxPerso.colliderect(hitbox)==True:
                etatPerso=2
        if hitboxPerso.colliderect(hitboxItem)==True:
            etatPerso=2
            objet= objet+1
        if etatPerso!=2 and possible==1 and kunaiDispo>0:
            etatPerso=3
            if sens==1:
                posKunai=(posPerso[0]+50, posPerso[1]+25)
            if sens==2:
                posKunai=(posPerso[0]+25, posPerso[1]+50)
            if sens==3:
                posKunai=(posPerso[0]-25, posPerso[1]+25)
            if sens==4:
                posKunai=(posPerso[0]+25,posPerso[1]-25)
            possible=0
            kunaiDispo=kunaiDispo-1




    elif touchePressee[pygame.K_RIGHT]==False and touchePressee[pygame.K_LEFT]==False and touchePressee[pygame.K_UP]==False and touchePressee[pygame.K_DOWN]==False and touchePressee[pygame.K_x]==False:
        etatPerso=0






# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()
while jeu==1:
    clock.tick(50)
    DessinTout()
    gestionFermeture()
    if viePerso>0:
        gestionClic()
    if etatPnjA!=4:
        déplacementPnjA()
    if etatPnjB!=4:
        déplacementPnjB()
    if etatPnjC!=4:
        déplacementPnjC()
    if etatPnjD!=4:
        déplacementPnjD()


    if possible==1:
        sensKunai=sens

    if posKunai!=(-50,-50):
        if dKunai==1:
            hitboxKunai=hitboxKunai.move(posKunai[0]+50, posKunai[1]+50)
            dKunai=0
        if possible==0:
            if sensKunai==1:
                posKunai=(posKunai[0]+10, posKunai[1])
                hitboxKunai=hitboxKunai.move(10,0)
            if sensKunai==2:
                posKunai=(posKunai[0], posKunai[1]+10)
                hitboxKunai=hitboxKunai.move(0,10)
            if sensKunai==3:
                posKunai=(posKunai[0]-10, posKunai[1])
                hitboxKunai=hitboxKunai.move(-10,0)
            if sensKunai==4:
                posKunai=(posKunai[0], posKunai[1]-10)
                hitboxKunai=hitboxKunai.move(0,-10)

    if posKunai[0]<0 or posKunai[0]>1400 or posKunai[1]<0 or posKunai[1]>934:
        posKunai=(-50,-50)
        hitboxKunai=pygame.Rect(posKunai[0],posKunai[1],12,12)
        possible=1
        dKunai=1

    for rectangle in obstacles:
        if hitboxKunai.colliderect(rectangle)==True:
            posKunai=(-50,-50)
            hitboxKunai=pygame.Rect(posKunai[0],posKunai[1],12,12)
            possible=1
            dKunai=1
    if hitboxKunai.colliderect(hitboxPnjA)==True:
            etatPnjA=4
            posKunai=(-50,-50)
            hitboxKunai=pygame.Rect(posKunai[0],posKunai[1],12,12)
            possible=1
            dKunai=1
    if hitboxKunai.colliderect(hitboxPnjB)==True:
            etatPnjB=4
            posKunai=(-50,-50)
            hitboxKunai=pygame.Rect(posKunai[0],posKunai[1],12,12)
            possible=1
            dKunai=1
    if hitboxKunai.colliderect(hitboxPnjC)==True:
            etatPnjC=4
            posKunai=(-50,-50)
            hitboxKunai=pygame.Rect(posKunai[0],posKunai[1],12,12)
            possible=1
            dKunai=1
    if hitboxKunai.colliderect(hitboxPnjD)==True:
            etatPnjD=4
            posKunai=(-50,-50)
            hitboxKunai=pygame.Rect(posKunai[0],posKunai[1],12,12)
            possible=1
            dKunai=1


    if possibleA==1:
        sensBalleA=spnjA

    if posBalleA!=(-50,-50):
        if dBalleA==1:
            hitboxBalleA=hitboxBalleA.move(posBalleA[0]+50, posBalleA[1]+50)
            dBalleA=0
        if possibleA==0:
            if sensBalleA==1:
                posBalleA=(posBalleA[0]+10, posBalleA[1])
                hitboxBalleA=hitboxBalleA.move(10,0)
            if sensBalleA==2:
                posBalleA=(posBalleA[0], posBalleA[1]+10)
                hitboxBalleA=hitboxBalleA.move(0,10)
            if sensBalleA==3:
                posBalleA=(posBalleA[0]-10, posBalleA[1])
                hitboxBalleA=hitboxBalleA.move(-10,0)
            if sensBalleA==4:
                posBalleA=(posBalleA[0], posBalleA[1]-10)
                hitboxBalleA=hitboxBalleA.move(0,-10)

    if posBalleA[0]<0 or posBalleA[0]>1400 or posBalleA[1]<0 or posBalleA[1]>934:
        posBalleA=(-50,-50)
        hitboxBalleA=pygame.Rect(posBalleA[0], posBalleA[1],12,12)
        possibleA=1
        dBalleA=1

    for rectangle in obstacles:
        if hitboxBalleA.colliderect(rectangle)==True:
            posBalleA=(-50,-50)
            hitboxBalleA=pygame.Rect(posBalleA[0], posBalleA[1],12,12)
            possibleA=1
            dBalleA=1
    if hitboxBalleA.colliderect(hitboxPerso)==True:
        posBalleA=(-50,-50)
        hitboxBalleA=pygame.Rect(posBalleA[0], posBalleA[1],12,12)
        possibleA=1
        dBalleA=1
        viePerso=viePerso-1

    if possibleB==1:
        sensBalleB=spnjB

    if posBalleB!=(-50,-50):
        if dBalleB==1:
            hitboxBalleB=hitboxBalleB.move(posBalleB[0]+50, posBalleB[1]+50)
            dBalleB=0
        if possibleB==0:
            if sensBalleB==1:
                posBalleB=(posBalleB[0]+10, posBalleB[1])
                hitboxBalleB=hitboxBalleB.move(10,0)
            if sensBalleB==2:
                posBalleB=(posBalleB[0], posBalleB[1]+10)
                hitboxBalleB=hitboxBalleB.move(0,10)
            if sensBalleB==3:
                posBalleB=(posBalleB[0]-10, posBalleB[1])
                hitboxBalleB=hitboxBalleB.move(-10,0)
            if sensBalleB==4:
                posBalleB=(posBalleB[0], posBalleB[1]-10)
                hitboxBalleB=hitboxBalleB.move(0,-10)

    if posBalleB[0]<0 or posBalleB[0]>1400 or posBalleB[1]<0 or posBalleB[1]>934:
        posBalleB=(-50,-50)
        hitboxBalleB=pygame.Rect(posBalleB[0], posBalleB[1],12,12)
        possibleB=1
        dBalleB=1

    for rectangle in obstacles:
        if hitboxBalleB.colliderect(rectangle)==True:
            posBalleB=(-50,-50)
            hitboxBalleB=pygame.Rect(posBalleB[0], posBalleB[1],12,12)
            possibleB=1
            dBalleB=1
    if hitboxBalleB.colliderect(hitboxPerso)==True:
        posBalleB=(-50,-50)
        hitboxBalleB=pygame.Rect(posBalleB[0], posBalleB[1],12,12)
        possibleB=1
        dBalleB=1
        viePerso=viePerso-1
            
    if possibleC==1:
        sensBalleC=spnjC

    if posBalleC!=(-50,-50):
        if dBalleC==1:
            hitboxBalleC=hitboxBalleC.move(posBalleC[0]+50, posBalleC[1]+50)
            dBalleC=0
        if possibleC==0:
            if sensBalleC==1:
                posBalleC=(posBalleC[0]+10, posBalleC[1])
                hitboxBalleC=hitboxBalleC.move(10,0)
            if sensBalleC==2:
                posBalleC=(posBalleC[0], posBalleC[1]+10)
                hitboxBalleC=hitboxBalleC.move(0,10)
            if sensBalleC==3:
                posBalleC=(posBalleC[0]-10, posBalleC[1])
                hitboxBalleC=hitboxBalleC.move(-10,0)
            if sensBalleC==4:
                posBalleC=(posBalleC[0], posBalleC[1]-10)
                hitboxBalleC=hitboxBalleC.move(0,-10)

    if posBalleC[0]<0 or posBalleC[0]>1400 or posBalleC[1]<0 or posBalleC[1]>934:
        posBalleC=(-50,-50)
        hitboxBalleC=pygame.Rect(posBalleC[0], posBalleC[1],12,12)
        possibleC=1
        dBalleC=1

    for rectangle in obstacles:
        if hitboxBalleC.colliderect(rectangle)==True:
            posBalleC=(-50,-50)
            hitboxBalleC=pygame.Rect(posBalleC[0], posBalleC[1],12,12)
            possibleC=1
            dBalleC=1
    if hitboxBalleC.colliderect(hitboxPerso)==True:
        posBalleC=(-50,-50)
        hitboxBalleC=pygame.Rect(posBalleC[0], posBalleC[1],12,12)
        possibleC=1
        dBalleC=1
        viePerso=viePerso-1

    if possibleD==1:
        sensBalleD=spnjD

    if posBalleD!=(-50,-50):
        if dBalleD==1:
            hitboxBalleD=hitboxBalleD.move(posBalleD[0]+50, posBalleD[1]+50)
            dBalleD=0
        if possibleD==0:
            if sensBalleD==1:
                posBalleD=(posBalleD[0]+10, posBalleD[1])
                hitboxBalleD=hitboxBalleD.move(10,0)
            if sensBalleD==2:
                posBalleD=(posBalleD[0], posBalleD[1]+10)
                hitboxBalleD=hitboxBalleD.move(0,10)
            if sensBalleD==3:
                posBalleD=(posBalleD[0]-10, posBalleD[1])
                hitboxBalleD=hitboxBalleD.move(-10,0)
            if sensBalleD==4:
                posBalleD=(posBalleD[0], posBalleD[1]-10)
                hitboxBalleD=hitboxBalleD.move(0,-10)

    if posBalleD[0]<0 or posBalleD[0]>1400 or posBalleD[1]<0 or posBalleD[1]>934:
        posBalleD=(-50,-50)
        hitboxBalleD=pygame.Rect(posBalleD[0], posBalleD[1],12,12)
        possibleD=1
        dBalleD=1

    for rectangle in obstacles:
        if hitboxBalleD.colliderect(rectangle)==True:
            posBalleD=(-50,-50)
            hitboxBalleD=pygame.Rect(posBalleD[0], posBalleD[1],12,12)
            possibleD=1
            dBalleD=1
    if hitboxBalleD.colliderect(hitboxPerso)==True:
        posBalleD=(-50,-50)
        hitboxBalleD=pygame.Rect(posBalleD[0], posBalleD[1],12,12)
        possibleD=1
        dBalleD=1
        viePerso=viePerso-1
    
    if viePerso<=0:
        etatPerso=4

pygame.quit()

