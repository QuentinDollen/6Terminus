import math as m
import numpy as np
import batiment as b
import terrain as t
import maison as m
import Walker as w
import Priest as p
import water as wa
import engineering as eng
import security as sec
import herb as h
import delivery_guy as dv



matrix = [
                      [10058, 10054, 10061, 10060, 10055, 10055, 10060, 0, 10036, 10032, 30152, 30172, 30121, 30121, 30121, 30121, 30131, 0, 0, 0, 0, 0, 10055, 10057, 10054, 10058, 10060, 10042, 10047, 10036, 10032, 10052, 10061, 10058, 10060, 10043, 0, 0, 0, 0],
                      [10058, 10058, 10058, 10060, 10051, 10060, 10054, 10053, 10052, 10052, 10052, 30154, 30172, 30121, 30121, 30121, 30170, 30133, 30133, 30133, 30144, 0, 0, 10032, 10031, 10054, 10045, 10047, 10036, 10055, 65, 10036, 10060, 10061, 10054, 10057, 10031, 0, 0, 0],
                      [10057, 10059, 10061, 10059, 10049, 10059, 10057, 10042, 10047, 10036, 10036, 10052, 30153, 30141, 30142, 30143, 30172, 30121, 30121, 30121, 30129, 0, 10056, 10057, 10054, 10055, 10060, 10036, 10036, 10032, 10036, 10061, 10042, 10043, 10047, 10052, 10052, 10031, 0, 0],
                      [10057, 10061, 10060, 10036, 10055, 10054, 10052, 10052, 10038, 10033, 10053, 10061, 10044, 10054, 10045, 10060, 30154, 30143, 30172, 30121, 30170, 30144, 0, 10032, 10036, 10042, 10047, 10043, 10031, 10045, 10054, 10056, 10057, 10050, 10055, 10031, 10031, 10040, 10040, 0],
                      [10050, 10032, 10036, 10055, 10058, 10058, 10059, 10060, 10061, 10044, 10043, 10045, 48, 10031, 0, 10052, 10051, 0, 30154, 30172, 30121, 30170, 30147, 0, 10036, 10036, 10032, 10031, 10040, 0, 0, 0, 10061, 10060, 10057, 10055, 10054, 10056, 10057, 0],
                      [10054, 10051, 10052, 10053, 10057, 10055, 10061, 10033, 10033, 10038, 10053, 10042, 10040, 10036, 10035, 10057, 10045, 0, 0, 30152, 30172, 30121, 30170, 30133, 30144, 10036, 10047, 10045, 10032, 10036, 10043, 10042, 10047, 10055, 10056, 10057, 10060, 10061, 10040, 0],
                      [10054, 10051, 10052, 10047, 10040, 10055, 10042, 10036, 10038, 10036, 10042, 10045, 10036, 10036, 10032, 10040, 10037, 10038, 10033, 0, 30154, 30172, 30121, 30121, 30170, 30133, 30135, 30133, 30133, 30146, 0, 0, 10031, 10032, 0, 10055, 10043, 10058, 10057, 0],
                      [10056, 10060, 10054, 10052, 10053, 10057, 10055, 10042, 10036, 10061, 10045, 10042, 10036, 10042, 0, 10032, 10057, 10036, 10040, 0, 0, 30152, 30172, 30121, 30121, 30121, 30121, 30121, 30121, 30170, 30144, 0, 10060, 10059, 10052, 10053, 10043, 10047, 10032, 0],
                      [10050, 10040, 10055, 10061, 10055, 10045, 48, 10038, 10040, 10036, 10032, 10036, 10042, 10044, 0, 0, 10032, 10057, 10040, 10040, 10040, 0, 30154, 30172, 30121, 30121, 30121, 30121, 30121, 30121, 30170, 30146, 0, 10045, 10054, 10055, 10036, 10031, 10040, 0],
                      [10055, 10060, 10056, 10054, 10037, 10061, 10044, 10044, 10044, 10042, 10036, 10036, 10040, 10044, 0, 0, 0, 0, 10057, 10037, 10040, 10032, 0, 30152, 30172, 30121, 30121, 30121, 30121, 30121, 30121, 30129, 0, 30151, 30145, 0, 10056, 10060, 10031, 0],
                      [10060, 10055, 10060, 10056, 10054, 10042, 10052, 10040, 10053, 10055, 10040, 10037, 10041, 10044, 0, 0, 0, 0, 0, 0, 10037, 10035, 10032, 0, 30152, 30172, 30121, 30121, 30121, 30121, 30121, 30170, 30133, 30171, 30129, 0, 10032, 10040, 10036, 0],
                      [10061, 10041, 10041, 10041, 10036, 10036, 10036, 0, 0, 10033, 10032, 10033, 10047, 10043, 0, 10057, 0, 0, 0, 10040, 10040, 10040, 0, 0, 0, 30152, 30141, 30143, 30142, 30141, 30172, 30121, 30121, 30121, 30170, 30147, 10031, 10032, 10036, 0],
                      [10055, 10038, 10034, 10037, 10053, 10040, 0, 0, 10036, 10034, 10036, 10045, 10045, 10038, 10035, 10037, 10055, 10045, 0, 0, 10038, 10037, 10040, 10032, 10034, 10033, 10034, 10036, 10038, 10040, 30152, 30140, 30172, 30121, 30121, 30170, 30146, 10036, 30165, 10040],
                      [10058, 10036, 10034, 10036, 10035, 0, 0, 0, 10042, 10036, 10061, 10045, 10042, 10045, 10047, 10036, 10032, 10057, 10045, 0, 0, 10052, 10038, 10038, 10032, 10055, 10061, 10043, 10045, 0, 0, 0, 30153, 30143, 30172, 30121, 30170, 30135, 30174, 30134],
                      [10055, 10032, 10036, 10042, 0, 0, 0, 0, 0, 10044, 10045, 10042, 10045, 10047, 10036, 10032, 10061, 10055, 10034, 10037, 0, 10042, 10045, 10047, 10038, 10032, 10057, 10045, 10045, 10036, 0, 0, 10045, 10054, 30154, 30143, 30172, 30121, 30121, 30121],
                      [10052, 10035, 10034, 10041, 10042, 0, 0, 0, 0, 0, 10061, 10045, 10042, 10045, 10047, 10036, 10032, 10057, 10045, 10045, 10036, 0, 10042, 10045, 10045, 10040, 10032, 10057, 10045, 10045, 10036, 0, 0, 10045, 10054, 10040, 30154, 30143, 30172, 30121],
                      [10052, 10038, 10038, 10036, 10036, 10034, 0, 0, 0, 0, 0, 10045, 10045, 10036, 0, 0, 10045, 10054, 10040, 0, 0, 10055, 10054, 10051, 10052, 10045, 10040, 10055, 10042, 10036, 10061, 10045, 10042, 10045, 10036, 0, 10042, 10045, 30154, 30142],
                      [0, 0, 10034, 10036, 10032, 10036, 10045, 0, 0, 0, 0, 0, 10034, 10036, 10032, 10036, 0, 10036, 0, 0, 10045, 10054, 10040, 0, 0, 10055, 10044, 10041, 10052, 10053, 10057, 10055, 10042, 10036, 0, 0, 0, 0, 0, 10054],
                      [0, 0, 0, 0, 0, 10044, 10034, 10040, 0, 0, 0, 0, 0, 0, 0, 10057, 10055, 10042, 10036, 0, 0, 0, 0, 0, 10054, 10036, 10045, 10047, 10042, 10032, 10057, 10045, 10045, 10036, 0, 10042, 10045, 10047, 10036, 10032],
                      [0, 0, 0, 0, 10036, 10036, 10036, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10045, 10054, 10040, 0, 0, 10055, 10054, 10051, 10052, 10053, 10057, 10055, 10042, 10036, 0, 0, 0, 0, 0, 10054, 10036, 10045],
                      [3089, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10042, 10045, 10047, 10036, 10032, 10057, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3087, 0],
                      [2103, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2101],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 10035, 0, 0, 0, 0, 0, 10052, 0, 0, 0, 0, 0, 0, 0, 0, 10033, 10033, 0, 0, 0, 0, 0, 0, 0, 0, 10035, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 10036, 10033, 10033, 10033, 10036, 10036, 10040, 10036, 0, 10036, 10040, 0, 0, 0, 0, 0, 0, 0, 10033, 0, 0, 10033, 10036, 10041, 10041, 10034, 10036, 10036, 10037, 10033, 10033, 10032, 0, 0, 10034],
                      [30146, 0, 0, 10033, 10047, 10053, 10040, 10042, 10053, 10044, 10034, 10034, 10034, 10031, 10036, 0, 0, 0, 0, 10054, 10033, 10035, 10035, 10037, 10040, 10049, 10046, 10044, 10038, 10037, 10045, 10043, 10035, 10040, 10042, 10044, 10040, 10040, 10033, 10031],
                      [30170, 30144, 0, 0, 10036, 10040, 10040, 10040, 10042, 10033, 0, 0, 0, 10052, 0, 0, 0, 0, 0, 10033, 10036, 39, 10041, 10038, 10042, 10035, 10047, 10044, 10044, 10044, 10043, 10042, 10041, 10050, 10040, 0, 10047, 0, 10040, 10044],
                      [30121, 30170, 30147, 0, 0, 10053, 10036, 10036, 10047, 10047, 0, 0, 0, 0, 10047, 0, 10037, 10037, 10037, 10037, 10033, 10035, 10042, 10042, 10042, 10042, 10043, 10045, 10050, 10060, 10060, 10049, 10061, 10040, 10054, 10046, 10050, 0, 10053, 10060],
                      [30141, 30172, 30170, 30135, 30147, 0, 0, 10040, 10040, 10050, 0, 0, 0, 0, 0, 0, 0, 20378, 10054, 10041, 10042, 10043, 10044, 10045, 10044, 10043, 10042, 10041, 10040, 10040, 39, 10038, 10037, 10037, 10038, 10042, 10044, 10037, 10060, 10054],
                      [0, 30152, 30172, 30121, 30131, 0, 0, 10036, 10042, 10043, 10044, 0, 0, 0, 20384, 0, 0, 20383, 20371, 10035, 20377, 0, 0, 0, 0, 10037, 10053, 10053, 10038, 10038, 10053, 10035, 0, 0, 10037, 10050, 10060, 10040, 10054, 10055],
                      [10033, 0, 30152, 30172, 30170, 30133, 30147, 0, 0, 10052, 10053, 0, 0, 0, 0, 0, 0, 10043, 20372, 20372, 0, 10040, 10037, 10038, 48, 10038, 48, 10053, 10053, 10054, 10045, 10044, 10046, 10047, 10058, 10060, 10044, 10042, 10054, 10054],
                      [10030, 10033, 10037, 30139, 30121, 30121, 30131, 0, 0, 10040, 0, 0, 20379, 20372, 0, 0, 0, 10044, 10033, 0, 0, 0, 20381, 10033, 0, 0, 10053, 10037, 10037, 10036, 10056, 10060, 10040, 10050, 0, 0, 10038, 10034, 10054, 10046],
                      [0, 10037, 10044, 30152, 30172, 30121, 30170, 30144, 10036, 0, 0, 0, 0, 20378, 0, 0, 10033, 10037, 10044, 10036, 0, 0, 0, 0, 20380, 10033, 0, 0, 10038, 10053, 48, 10035, 10034, 10034, 10036, 10036, 10040, 10050, 10042, 10038],
                      [10043, 10038, 10036, 10044, 30152, 30172, 30121, 30170, 30146, 0, 0, 0, 0, 20381, 10037, 10036, 10056, 10060, 10060, 10042, 0, 10035, 0, 0, 0, 20378, 0, 0, 0, 10034, 10047, 10042, 10044, 10040, 10050, 10060, 10059, 10058, 10036, 10038],
                      [10042, 10040, 10052, 10033, 0, 30138, 30121, 30121, 30170, 30144, 20374, 0, 0, 0, 10035, 10044, 10042, 10038, 10034, 10043, 48, 10045, 0, 0, 0, 20381, 20374, 0, 0, 0, 0, 10036, 10038, 10040, 10037, 10036, 0, 0, 10047, 10053],
                      [10047, 10036, 10036, 10036, 0, 30154, 30172, 30121, 30121, 30129, 0, 0, 0, 20380, 10040, 10060, 10050, 10055, 10061, 10034, 10040, 10042, 10041, 0, 0, 0, 20372, 20374, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10033],
                      [10037, 10047, 0, 0, 0, 20371, 30152, 30172, 30121, 30170, 30145, 10033, 10060, 10042, 10043, 10058, 10047, 10061, 10061, 10061, 10059, 10056, 10059, 0, 0, 0, 20381, 20372, 20377, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [10036, 0, 20374, 0, 0, 0, 20371, 30152, 30140, 30172, 30170, 30144, 10043, 10059, 10042, 10046, 10046, 10046, 10042, 0, 10050, 10043, 0, 10054, 10055, 20378, 0, 0, 20382, 20375, 0, 20371, 0, 0, 20372, 0, 0, 0, 20382, 20372],
                      [0, 0, 0, 0, 0, 0, 20384, 0, 0, 30137, 30121, 30170, 30133, 30144, 10033, 10044, 10040, 10042, 10041, 10041, 10041, 10058, 10060, 10058, 10034, 10044, 0, 0, 0, 0, 0, 0, 0, 0, 20379, 0, 0, 0, 0, 0],
                      [0, 0, 0, 20384, 0, 0, 20377, 20374, 0, 30138, 30121, 30121, 30121, 30131, 10053, 10036, 10040, 10042, 10044, 10043, 10035, 10057, 10042, 10060, 10043, 10050, 10061, 10061, 20375, 0, 0, 0, 20383, 0, 20371, 0, 0, 0, 20384, 20380],
                      [0, 0, 0, 0, 20372, 20376, 20372, 0, 0, 30139, 30121, 30121, 30121, 30131, 0, 10040, 10036, 0, 10052, 10047, 10036, 0, 0, 10031, 10045, 10040, 10053, 0, 0, 0, 0, 0, 20377, 20372, 20372, 0, 0, 0, 20371, 20372]
                      ]



nb_cases_x = 60
nb_cases_y = 60
nb_cases = 60

def init_matrice_terrain(Mat, x, y):
    assert (Mat == [])
    for i in range(x):
        Mat.append([])
        for j in range(y):
            Mat[i].append(t.Terrain(i, j, 2))


# Mat [i][j] : donne un tableau avec la liste des personnages,
def init_matrice_perso(Mat, x, y):
    assert (Mat == [])
    for i in range(x):
        Mat.append([])
        for j in range(y):
            Mat[i].append([])
            Mat[i][j].append([])
            Mat[i][j][0] = w.Walker(i,j)


def afficher_matrice_bat(Mat, x, y):
    for i in range(x):
        print("[", end='')
        for j in range(y):
            print(Mat[i][j].name, " ", end='')
        print("]")


def afficher_matrice_perso(Mat, x, y):
    for i in range(x):
        print("[", end='')
        for j in range(y):
            for k in range(len(Mat[i][j])):
                print(Mat[i][j][k].name, " ", end='')
            if (j != y - 1):
                print("| ", end='')
        print("]")

def add_bat(x,y,id_bat,Mat):
   
        if(id_bat == 0): 
            Herb = h.Herb(x,y)
            Mat[x][y] = Herb
        if(id_bat == 92): 
            well = wa.Well(x,y)
            Mat[x][y] = well
        if(id_bat == 90): 
            Reservoir = wa.Reservoir(x,y)
            Mat[x][y] = Reservoir
        if(id_bat == 91): Fountain = wa.Fountain(x,y)
        if(id_bat == 8): Aquaduct = wa.Aquaduct(x,y)
        if(id_bat == 81): EngineersPost = eng.EngineersPost(x,y)
        if(id_bat == 55): Prefecture = sec.Prefecture(x,y)


#globals()["Prefecture"+x+y]


def add_perso(x, y, type, Mat):
    if(type == 'Delivery Guy'): 
        DV = dv.Delivery_Guy(x,y)
        Mat[x][y] = DV

#TESTER SI FONCTIONNE
def departureMatrice(Mat):
    map_depart = matrix
    for i in range(nb_cases+1):
        for j in range(nb_cases+1):
            Mat[i][j] = add_bat(i,j,map_depart[i][j])
    afficher_matrice_bat(Mat)


def isPath(x,y,Mat):
    return Mat[x][y].name == 'Path'
        

def SearchforRoad(x,y,Mat): #SearchforRoad donne la route qu'il croise autour (distance de 1) d'un batiment situé en x,y
    n = Mat[x][y].nbr_cases
    x1 = 0
    x2 = 0
    if(x !=0 ):
        x1 = x -1
    if(y != 0):
        y1 = y -1
    for i in range(n+3) :
        if(isPath(x1,y1)):
            return (x1,y1)
        x1 = x1+1
    for j in range(n+3):
        if(isPath(x1,y1)) :
            return (x1,y1)
        y1= y1 +1
    for i in range(0,n+1):
        if(isPath(x1,y1)):
            return (x1,y1)
        x1 = x1-1
    for j in range(n+3):
        if(isPath(x1,y1)) :
            return (x1,y1)
        y1= y1 -1
    return (-1,-1)



#definir calcul de trajectoire 
# attention ! il faut rajouter le cas ou on est sur les bords et aussi s'il y a une boucle c'est la merde
def next_case(x,y,destx,desty, prec_x, prec_y, Mat,t): #calcul par des appels recursif le chemin a parcourir
    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    x3 = -1
    y3 = -1
    x4 = -1
    y4 = -1
    assert(isPath(x,y,Mat))
    assert(isPath(destx,desty,Mat))
    if(x == destx and y == desty):
        return (prec_x, prec_y)
    if(t > destx-x + desty-y + 20): # dans le cas où on a une boucle le temps t va devenir deraisonnablement grand pour un trajet  
        return(-1,-1)
    if(isPath(x+1,y,Mat) and x+1 != prec_x):
        (x1,y1) = next_case(x+1,y,destx,desty,x,y,Mat,t+1)
    if(isPath(x,y+1,Mat) and y+1 != prec_y):
        (x2,y2) = next_case(x,y+1,destx,desty,x,y,Mat,t+1)
    if(isPath(x-1,y,Mat) and x-1 != prec_x):
        (x3,y3) = next_case(x-1,y,destx,desty,x,y,Mat,t+1)
    if(isPath(x-1,y,Mat) and y-1 != prec_y):
        (x4,y4) = next_case(x,y-1,destx,desty,x,y,Mat,t+1)
    
    # faut faire la comparaison des différents resultats (c'est un resultat si c'est différent de -1) et prendre le meilleur en terme de temps t


    else:
        return (-1,-1)
    
    
    

def Deplacement_basique(): # a faire evidemment
    return (0,0)



def deplacement_perso(Mat,i,j):
    if Mat[i][j][0].name != "Walker":
        for k in range(Mat[i][j].len) :
            if (Mat[i][j][k].destination_x != 666 or Mat[i][j][k].destination_y != 666) :
                (nx,ny) = next_case(SearchforRoad(i,j,Mat),SearchforRoad(Mat[i][j][k].destination_x,Mat[i][j][k].destination_y,Mat),-1,-1,Mat,0)
            else:
                (nx,ny) = Deplacement_basique()
            



Mat_batiment = []
Mat_perso = []

bat1 = b.Batiment(1, "", 1, 1, 0, 0, 0, 0, 0, 0)
p1 = p.Priest(1,1)

init_matrice_terrain(Mat_batiment, 3, 3)
Mat_batiment[0][0] = bat1

init_matrice_perso(Mat_perso, 3, 3)

print(Mat_perso[0][0])

afficher_matrice_bat(Mat_batiment, 3, 3)
afficher_matrice_perso(Mat_perso, 3, 3)



