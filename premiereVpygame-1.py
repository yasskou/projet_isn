# Créé par kbenhallam, le 07/03/2019 en Python 3.2
import pygame
pygame.init()
fenetre= pygame.display.set_mode((800,534)) #1400 934 sur grand écran, 800 534 sur petit écran
pygame.display.set_caption("How sneaky are you?")

#position
posPerso= (700,919) #700 919 sur grand écran, 400 519 sur petit écran
posPnjA= (50,50)
posPnjB=(950,50)
posSalle1= (200,200)
balle= (-1,-1)
obstacles=[]



#valeurs variables
jeu=1
largeurFenetre=pygame.Surface.get_width(fenetre)
hauteurFenetre=pygame.Surface.get_height(fenetre)
pnjA=1
pnjB=1
déplacement=1
chgmtDirection=0
sens=0



#Images
Kunai= pygame.image.load("./Ninja/png/Kunai.png")

marche0= pygame.image.load("./Ninja/png/Run__000.png")
marche1= pygame.image.load("./Ninja/png/Run__001.png")
marche2= pygame.image.load("./Ninja/png/Run__002.png")
marche3= pygame.image.load("./Ninja/png/Run__003.png")
marche4= pygame.image.load("./Ninja/png/Run__004.png")
marche5= pygame.image.load("./Ninja/png/Run__005.png")
marche6= pygame.image.load("./Ninja/png/Run__006.png")
marche7= pygame.image.load("./Ninja/png/Run__007.png")
marche8= pygame.image.load("./Ninja/png/Run__008.png")
marche9= pygame.image.load("./Ninja/png/Run__009.png")

immobile0= pygame.image.load("./Ninja/png/Idle__000.png")
immobile1= pygame.image.load("./Ninja/png/Idle__001.png")
immobile2= pygame.image.load("./Ninja/png/Idle__002.png")
immobile3= pygame.image.load("./Ninja/png/Idle__003.png")
immobile4= pygame.image.load("./Ninja/png/Idle__004.png")
immobile5= pygame.image.load("./Ninja/png/Idle__005.png")
immobile6= pygame.image.load("./Ninja/png/Idle__006.png")
immobile7= pygame.image.load("./Ninja/png/Idle__007.png")
immobile8= pygame.image.load("./Ninja/png/Idle__008.png")
immobile9= pygame.image.load("./Ninja/png/Idle__009.png")

jet0= pygame.image.load("./Ninja/png/Throw__000.png")
jet1= pygame.image.load("./Ninja/png/Throw__001.png")
jet2= pygame.image.load("./Ninja/png/Throw__002.png")
jet3= pygame.image.load("./Ninja/png/Throw__003.png")
jet4= pygame.image.load("./Ninja/png/Throw__004.png")
jet5= pygame.image.load("./Ninja/png/Throw__005.png")
jet6= pygame.image.load("./Ninja/png/Throw__006.png")
jet7= pygame.image.load("./Ninja/png/Throw__007.png")
jet8= pygame.image.load("./Ninja/png/Throw__008.png")
jet9= pygame.image.load("./Ninja/png/Throw__009.png")

attaque0= pygame.image.load("./Ninja/png/Attack__000.png")
attaque1= pygame.image.load("./Ninja/png/Attack__001.png")
attaque2= pygame.image.load("./Ninja/png/Attack__002.png")
attaque3= pygame.image.load("./Ninja/png/Attack__003.png")
attaque4= pygame.image.load("./Ninja/png/Attack__004.png")
attaque5= pygame.image.load("./Ninja/png/Attack__005.png")
attaque6= pygame.image.load("./Ninja/png/Attack__006.png")
attaque7= pygame.image.load("./Ninja/png/Attack__007.png")
attaque8= pygame.image.load("./Ninja/png/Attack__008.png")
attaque9= pygame.image.load("./Ninja/png/Attack__009.png")


#divers rectangles
Salle1=pygame.Rect(150,100,350,200)
Salle2=pygame.Rect(150,500,200,350)
Salle3=pygame.Rect(500,400,320,180)
Salle4=pygame.Rect(960,600,350,250)
Salle5=pygame.Rect(1000,100,250,380)
Salle6=pygame.Rect(600,150,300,150)
Salle7=pygame.Rect(450,650,330,150)

hitboxPerso=pygame.Rect(posPerso[0]-15,posPerso[1]-15,30,30)



#liste
obstacles.append(Salle1)
obstacles.append(Salle2)
obstacles.append(Salle3)
obstacles.append(Salle4)
obstacles.append(Salle5)
obstacles.append(Salle6)
obstacles.append(Salle7)



#Dessin
def DessinSalles():
    pygame.draw.rect(fenetre,(255,255,255), Salle1,1) #coin haut gauche
    pygame.draw.rect(fenetre,(255,255,255),Salle2,1) #coin bas gauche
    pygame.draw.rect(fenetre,(255,255,255), Salle3,1) #milieu milieu
    pygame.draw.rect(fenetre,(255,255,255),Salle4,1) #coin bas droite
    pygame.draw.rect(fenetre, (255,255,255), Salle5,1) #coin haut droite
    pygame.draw.rect(fenetre,(255,255,255), Salle6,1) #milieu haut
    pygame.draw.rect(fenetre,(255,255,255), Salle7,1) #milieu bas


def dessinCDV():
    global sens
    if sens==4:
        pygame.draw.rect(fenetre,(255,255,255),[posPerso[0]-25,posPerso[1]-10,50,-100],1)#visionUp
    if sens==1:
        pygame.draw.rect(fenetre,(255,255,255),[posPerso[0]+10,posPerso[1]-25,100,50],1)#visionR
    if sens==3:
        pygame.draw.rect(fenetre,(255,255,255),[posPerso[0]-10,posPerso[1]-25,-100,50],1)#visionL
    if sens==2:
        pygame.draw.rect(fenetre,(255,255,255),[posPerso[0]-25,posPerso[1]+10,50,100],1)#visionD



def DessinTout():
    fenetre.fill((50,50,50))
    pygame.draw.circle(fenetre,(255,255,255), posPerso, 15) #dessin du joueur
    pygame.draw.circle(fenetre,(255,182,193), posPnjA, 15)
    pygame.draw.circle(fenetre,(255,182,193), posPnjB, 15) #dessin du premier pnj
    pygame.draw.rect(fenetre,(250,250,250),hitboxPerso,1)
    DessinSalles()
    dessinCDV()
    if balle != (-1, -1):
        pygame.draw.circle(fenetre, (255,255,255), balle, 2)
    pygame.display.flip()

#def dessinPerso():




#déplacement pnj
def déplacementPnjA():
    global posPnjA, pnjA
    if pnjA==1:
        if posPnjA[0]<550:
            posPnjA=(posPnjA[0]+2, posPnjA[1])
        else:
            pnjA=2
    if pnjA==2:
        if posPnjA[1]<350:
            posPnjA=(posPnjA[0],posPnjA[1]+2)
        else:
            pnjA=3
    if pnjA==3:
        if posPnjA[0]>100:
            posPnjA=(posPnjA[0]-2, posPnjA[1])
        else:
            pnjA=4
    if pnjA==4:
        if posPnjA[1]>50:
            posPnjA=(posPnjA[0], posPnjA[1]-2)
        else:
            pnjA=1


def déplacementPnjB():
    global posPnjB, pnjB
    if pnjB==1:
        if posPnjB[0]<1300:
            posPnjB=(posPnjB[0]+2, posPnjB[1])
        else:
            pnjB=2
    if pnjB==2:
        if posPnjB[1]<535:
            posPnjB=(posPnjB[0],posPnjB[1]+2)
        else:
            pnjB=3
    if pnjB==3:
        if posPnjB[0]>950:
            posPnjB=(posPnjB[0]-2, posPnjB[1])
        else:
            pnjB=4
    if pnjB==4:
        if posPnjB[1]>50:
            posPnjB=(posPnjB[0], posPnjB[1]-2)
        else:
            pnjB=1





#Gestion des clics
def gestionClic():
    global posPerso, jeu, hitboxPerso, obstacles, déplacement, chgmtDirection, sens
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            jeu = 0
    touchePressee=pygame.key.get_pressed()
    if touchePressee[pygame.K_RIGHT]==True and posPerso[0]<largeurFenetre-15 and touchePressee[pygame.K_UP]==False and touchePressee[pygame.K_DOWN]==False:
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




# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()
while jeu==1:
    clock.tick(50)
    DessinTout()
    gestionClic()
    déplacementPnjA()
    déplacementPnjB()

pygame.quit()

