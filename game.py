# Créé par kbenhallam, le 07/03/2019 en Python 3.2
import pygame
pygame.init()
fenetre = pygame.display.set_mode((1400,934)) # 1400 934 sur grand écran, 800 534 sur petit écran
pygame.display.set_caption("How sneaky are you?")

# position
posPerso = (700, 719)  # 700 919 sur grand écran, 400 519 sur petit écran
posPnjA = (50, 50)
posPnjB = (950, 50)
posPnjC = (80, 450)
posPnjD = (900, 550)
posSalle1 = (200, 200)
balle = (-1, -1)
obstacles = []


# valeurs variables
jeu = 1
largeurFenetre = pygame.Surface.get_width(fenetre)
hauteurFenetre = pygame.Surface.get_height(fenetre)
spnjA = 1
spnjB = 1
spnjC = 1
spnjD = 1
déplacement = 1
chgmtDirection = 0
sens = 0


# Images
Kunai = pygame.image.load("./Ninja/png/Kunai.png")
balle = pygame.image.load("./Robot/png/Bullet.png")

marche0 = pygame.image.load("./Ninja/png/Run__000.png")
marche1 = pygame.image.load("./Ninja/png/Run__001.png")
marche2 = pygame.image.load("./Ninja/png/Run__002.png")
marche3 = pygame.image.load("./Ninja/png/Run__003.png")
marche4 = pygame.image.load("./Ninja/png/Run__004.png")
marche5 = pygame.image.load("./Ninja/png/Run__005.png")
marche6 = pygame.image.load("./Ninja/png/Run__006.png")
marche7 = pygame.image.load("./Ninja/png/Run__007.png")
marche8 = pygame.image.load("./Ninja/png/Run__008.png")
marche9 = pygame.image.load("./Ninja/png/Run__009.png")

immobile0 = pygame.image.load("./Ninja/png/Idle__000.png")
immobile1 = pygame.image.load("./Ninja/png/Idle__001.png")
immobile2 = pygame.image.load("./Ninja/png/Idle__002.png")
immobile3 = pygame.image.load("./Ninja/png/Idle__003.png")
immobile4 = pygame.image.load("./Ninja/png/Idle__004.png")
immobile5 = pygame.image.load("./Ninja/png/Idle__005.png")
immobile6 = pygame.image.load("./Ninja/png/Idle__006.png")
immobile7 = pygame.image.load("./Ninja/png/Idle__007.png")
immobile8 = pygame.image.load("./Ninja/png/Idle__008.png")
immobile9 = pygame.image.load("./Ninja/png/Idle__009.png")

jet0 = pygame.image.load("./Ninja/png/Throw__000.png")
jet1 = pygame.image.load("./Ninja/png/Throw__001.png")
jet2 = pygame.image.load("./Ninja/png/Throw__002.png")
jet3 = pygame.image.load("./Ninja/png/Throw__003.png")
jet4 = pygame.image.load("./Ninja/png/Throw__004.png")
jet5 = pygame.image.load("./Ninja/png/Throw__005.png")
jet6 = pygame.image.load("./Ninja/png/Throw__006.png")
jet7 = pygame.image.load("./Ninja/png/Throw__007.png")
jet8 = pygame.image.load("./Ninja/png/Throw__008.png")
jet9 = pygame.image.load("./Ninja/png/Throw__009.png")

attaque0 = pygame.image.load("./Ninja/png/Attack__000.png")
attaque1 = pygame.image.load("./Ninja/png/Attack__001.png")
attaque2 = pygame.image.load("./Ninja/png/Attack__002.png")
attaque3 = pygame.image.load("./Ninja/png/Attack__003.png")
attaque4 = pygame.image.load("./Ninja/png/Attack__004.png")
attaque5 = pygame.image.load("./Ninja/png/Attack__005.png")
attaque6 = pygame.image.load("./Ninja/png/Attack__006.png")
attaque7 = pygame.image.load("./Ninja/png/Attack__007.png")
attaque8 = pygame.image.load("./Ninja/png/Attack__008.png")
attaque9 = pygame.image.load("./Ninja/png/Attack__009.png")

gmarche1 = pygame.image.load("./Robot/png/Run (1).png")
gmarche2 = pygame.image.load("./Robot/png/Run (2).png")
gmarche3 = pygame.image.load("./Robot/png/Run (3).png")
gmarche4 = pygame.image.load("./Robot/png/Run (4).png")
gmarche5 = pygame.image.load("./Robot/png/Run (5).png")
gmarche6 = pygame.image.load("./Robot/png/Run (6).png")
gmarche7 = pygame.image.load("./Robot/png/Run (7).png")
gmarche8 = pygame.image.load("./Robot/png/Run (8).png")

gimmobile1 = pygame.image.load("./Robot/png/Idle (1).png")
gimmobile2 = pygame.image.load("./Robot/png/Idle (2).png")
gimmobile3 = pygame.image.load("./Robot/png/Idle (3).png")
gimmobile4 = pygame.image.load("./Robot/png/Idle (4).png")
gimmobile5 = pygame.image.load("./Robot/png/Idle (5).png")
gimmobile6 = pygame.image.load("./Robot/png/Idle (6).png")
gimmobile7 = pygame.image.load("./Robot/png/Idle (7).png")
gimmobile8 = pygame.image.load("./Robot/png/Idle (8).png")
gimmobile9 = pygame.image.load("./Robot/png/Idle (9).png")
gimmobile10 = pygame.image.load("./Robot/png/Idle (10).png")

gattaque1 = pygame.image.load("./Robot/png/Melee (1).png")
gattaque2 = pygame.image.load("./Robot/png/Melee (2).png")
gattaque3 = pygame.image.load("./Robot/png/Melee (3).png")
gattaque4 = pygame.image.load("./Robot/png/Melee (4).png")
gattaque5 = pygame.image.load("./Robot/png/Melee (5).png")
gattaque6 = pygame.image.load("./Robot/png/Melee (6).png")
gattaque7 = pygame.image.load("./Robot/png/Melee (7).png")
gattaque8 = pygame.image.load("./Robot/png/Melee (8).png")

# divers rectangles
Salle1 = pygame.Rect(150, 100, 350, 200)
Salle2 = pygame.Rect(150, 500, 200, 350)
Salle3 = pygame.Rect(500, 400, 320, 180)
Salle4 = pygame.Rect(960, 600, 350, 250)
Salle5 = pygame.Rect(1000, 100, 250, 380)
Salle6 = pygame.Rect(600, 150, 300, 150)
Salle7 = pygame.Rect(450, 650, 330, 150)

hitboxPerso = pygame.Rect(posPerso[0]-15, posPerso[1]-15, 30, 30)
hitboxPnjA = pygame.Rect(posPnjA[0]-15, posPnjA[1]-15, 30, 30)
hitboxPnjB = pygame.Rect(posPnjB[0]-15, posPnjB[1]-15, 30, 30)
hitboxPnjC = pygame.Rect(posPnjA[0]-15, posPnjA[1]-15, 30, 30)
hitboxPnjD = pygame.Rect(posPnjA[0]-15, posPnjA[1]-15, 30, 30)


# liste
obstacles.append(Salle1)
obstacles.append(Salle2)
obstacles.append(Salle3)
obstacles.append(Salle4)
obstacles.append(Salle5)
obstacles.append(Salle6)
obstacles.append(Salle7)


# Dessin
def DessinSalles():
    pygame.draw.rect(fenetre, (255, 255, 255), Salle1, 1)  # coin haut gauche
    pygame.draw.rect(fenetre, (255, 255, 255), Salle2, 1)  # coin bas gauche
    pygame.draw.rect(fenetre, (255, 255, 255), Salle3, 1)  # milieu milieu
    pygame.draw.rect(fenetre, (255, 255, 255), Salle4, 1)  # coin bas droite
    pygame.draw.rect(fenetre, (255, 255, 255), Salle5, 1)  # coin haut droite
    pygame.draw.rect(fenetre, (255, 255, 255), Salle6, 1)  # milieu haut
    pygame.draw.rect(fenetre, (255, 255, 255), Salle7, 1)  # milieu bas


def dessinCDV():
    global spnjA, spnjB, spnjC, spnjD
    if spnjA == 1:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]+14, posPnjA[1]-38, 130, 76], 1)  # visionR
    if spnjA == 2:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-38, posPnjA[1]+14, 76, 130], 1)  # visionD
    if spnjA == 3:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-14, posPnjA[1]-38, -130, 76], 1)  # visionL
    if spnjA == 4:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-38, posPnjA[1]-14, 76, -130], 1)  # visionUp

    if spnjB == 1:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjB[0]+14, posPnjB[1]-38, 130, 76], 1)  # visionR
    if spnjB == 2:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjB[0]-38, posPnjB[1]+14, 76, 130], 1)  # visionD
    if spnjB == 3:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjB[0]-14, posPnjB[1]-38, -130, 76], 1)  # visionL
    if spnjB == 4:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjB[0]-38, posPnjB[1]-14, 76, -130], 1)  # visionUp

    if spnjC == 1:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0] + 14, posPnjA[1] - 38, 130, 76], 1)  # visionR
    if spnjC == 2:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-38, posPnjA[1]+14, 76, 130], 1)  # visionD
    if spnjC == 3:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-14, posPnjA[1]-38, -130, 76], 1)  # visionL
    if spnjC == 4:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-38, posPnjA[1]-14, 76, -130], 1)  # visionUp

    if spnjD == 1:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]+14, posPnjA[1]-38, 130, 76], 1)  # visionR
    if spnjD == 2:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-38, posPnjA[1]+14, 76, 130], 1)  # visionD
    if spnjD == 3:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-14, posPnjA[1]-38, -130, 76], 1)  # visionL
    if spnjD == 4:
        pygame.draw.rect(fenetre, (255, 255, 255), [posPnjA[0]-38, posPnjA[1]-14, 76, -130], 1)  # visionUp


def DessinTout():
    fenetre.fill((50, 50, 50))
    pygame.draw.circle(fenetre, (255, 255, 255), posPerso, 15)  # dessin du joueur
    pygame.draw.circle(fenetre, (255, 182, 193), posPnjA, 15)
    pygame.draw.circle(fenetre, (255, 182, 193), posPnjB, 15)  # dessin du premier pnj
    pygame.draw.circle(fenetre, (255, 182, 193), posPnjC, 15)
    pygame.draw.circle(fenetre, (255, 182, 193), posPnjD, 15)
    pygame.draw.rect(fenetre, (250, 250, 250), hitboxPerso, 1)
    pygame.draw.rect(fenetre, (250, 250, 250), hitboxPnjA, 1)
    pygame.draw.rect(fenetre, (250, 250, 250), hitboxPnjB, 1)
    DessinSalles()
    dessinCDV()
    # if balle != (-1, -1):
    # pygame.draw.circle(fenetre, (255,255,255), balle, 2)
    pygame.display.flip()

# def dessinPerso():


# déplacement pnj
def déplacementPnjA():
    global posPnjA, spnjA, hitboxPnjA
    if spnjA == 1:
        if posPnjA[0] < 550:
            posPnjA = (posPnjA[0]+2, posPnjA[1])
            hitboxPnjA = hitboxPnjA.move(2, 0)
        else:
            spnjA = 2
    if spnjA == 2:
        if posPnjA[1] < 350:
            posPnjA = (posPnjA[0], posPnjA[1]+2)
            hitboxPnjA = hitboxPnjA.move(0, 2)
        else:
            spnjA = 3
    if spnjA == 3:
        if posPnjA[0] > 100:
            posPnjA = (posPnjA[0]-2, posPnjA[1])
            hitboxPnjA = hitboxPnjA.move(-2, 0)
        else:
            spnjA = 4
    if spnjA == 4:
        if posPnjA[1] > 50:
            posPnjA = (posPnjA[0], posPnjA[1]-2)
            hitboxPnjA=hitboxPnjA.move(0, -2)
        else:
            spnjA = 1


def déplacementPnjB():
    global posPnjB, spnjB, hitboxPnjB
    if spnjB == 1:
        if posPnjB[0] < 1325:
            posPnjB = (posPnjB[0]+2, posPnjB[1])
            hitboxPnjB = hitboxPnjB.move(2, 0)
        else:
            spnjB = 2
    if spnjB == 2:
        if posPnjB[1] < 535:
            posPnjB = (posPnjB[0], posPnjB[1]+2)
            hitboxPnjB = hitboxPnjB.move(0, 2)
        else:
            spnjB = 3
    if spnjB == 3:
        if posPnjB[0] > 950:
            posPnjB = (posPnjB[0]-2, posPnjB[1])
            hitboxPnjB = hitboxPnjB.move(-2, 0)
        else:
            spnjB = 4
    if spnjB == 4:
        if posPnjB[1] > 50:
            posPnjB = (posPnjB[0], posPnjB[1]-2)
            hitboxPnjB = hitboxPnjB.move(0, -2)
        else:
            spnjB = 1

def déplacementPnjC():
    global posPnjC, spnjC, hitboxPnjC
    if spnjC == 1:
        if posPnjC[0] < 400:
            posPnjC = (posPnjC[0] + 2, posPnjC[1])
            hitboxPnjC = hitboxPnjC.move(2, 0)
        else:
            spnjC = 2
    if spnjC == 2:
        if posPnjC[1] < 950:
            posPnjC = (posPnjC[0], posPnjC[1] + 2)
            hitboxPnjC = hitboxPnjC.move(0, 2)
        else:
            spnjC = 3
    if spnjC == 3:
        if posPnjC[0] > 80:
            posPnjC = (posPnjC[0] - 2, posPnjC[1])
            hitboxPnjC = hitboxPnjC.move(-2, 0)
        else:
            spnjC = 4
    if spnjC == 4:
        if posPnjC[1] > 450:
            posPnjC = (posPnjC[0], posPnjC[1] - 2)
            hitboxPnjC = hitboxPnjC.move(0, -2)
        else:
            spnjC = 1

def déplacementPnjD():
    global posPnjD, spnjD, hitboxPnjD
    if spnjD == 1:
        if posPnjD[0] < 1350:
            posPnjD = (posPnjD[0]+2, posPnjD[1])
            hitboxPnjD = hitboxPnjD.move(2, 0)
        else:
            spnjD = 2
    if spnjD == 2:
        if posPnjD[1] < 900:
            posPnjD = (posPnjD[0], posPnjD[1]+2)
            hitboxPnjD = hitboxPnjD.move(0, 2)
        else:
            spnjD = 3
    if spnjD == 3:
        if posPnjD[0] > 900:
            posPnjD = (posPnjD[0]-2, posPnjD[1])
            hitboxPnjD = hitboxPnjD.move(-2, 0)
        else:
            spnjD = 4
    if spnjD == 4:
        if posPnjD[1] > 550:
            posPnjD = (posPnjD[0], posPnjD[1]-2)
            hitboxPnjD = hitboxPnjD.move(0, -2)
        else:
            spnjD = 1


# Gestion des clics
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
while jeu == 1:
    clock.tick(50)
    DessinTout()
    gestionClic()
    déplacementPnjA()
    déplacementPnjB()
    déplacementPnjC()
    déplacementPnjD()
pygame.quit()

