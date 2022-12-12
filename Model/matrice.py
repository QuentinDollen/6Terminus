from Terminus_project.Model import terrain as t
from Terminus_project.Model import maison as mais
from Terminus_project.Model import Walker as w
from Terminus_project.Model import water as wa
from Terminus_project.Model import engineering as eng
from Terminus_project.Model import security as sec
from Terminus_project.Model import herb as h
from Terminus_project.Model import delivery_guy as dv
from Terminus_project.Model import administration as admin
from Terminus_project.Model import path as pa
from Terminus_project.Model import tree as tr
from Terminus_project.Model import ferme as f
from Terminus_project.Model import granary as g
from Terminus_project.Model import warehouse as war


matrix = [ [3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         0, 0, 0, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 65, 3, 3, 3, 3,
         3, 3, 0, 0, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 3, 0, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3,
         3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 0, 3,
         3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3,
         3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3,
         3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
         3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
         3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1,
         1, 3, 1, 3],
        [3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1,
         1, 1, 1, 1],
        [3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 1, 1,
         1, 1, 1, 1],
        [3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3,
         1, 1, 1, 1],
        [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
         3, 3, 1, 1],
        [0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
         0, 0, 0, 3],
        [0, 0, 0, 0, 0, 3, 3, 3, 0, 5, 5, 5, 5, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3,
         3, 3, 3, 3],
        [0, 0, 7, 7, 3, 3, 3, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0,
         0, 3, 3, 3],
        [3089, 0, 7, 7, 7, 7, 7, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 3087, 0],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5, 5],
        [0, 5, 0, 5, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0,
         0, 0, 0, 0],
        [0, 5, 5, 5, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 0, 0, 3],
        [1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 3, 3, 3],
        [1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 39, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         0, 3, 0, 3, 3],
        [1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 0, 3, 3],
        [1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 39, 3, 3, 3, 3,
         3, 3, 3, 3, 3],
        [0, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 0, 0, 0, 2, 0, 0, 2, 2, 3, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3,
         3, 3, 3, 3],
        [3, 0, 1, 1, 1, 1, 1, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 2, 2, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3,
         3, 3, 3, 3, 3],
        [3, 3, 3, 1, 1, 1, 1, 0, 0, 3, 0, 0, 2, 2, 0, 0, 0, 3, 3, 0, 0, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
         3, 3, 3, 3],
        [0, 3, 3, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 2, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 2, 3, 0, 0, 3, 3, 0, 3, 3, 3, 3,
         3, 3, 3, 3, 3],
        [3, 3, 3, 3, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3,
         3, 3, 3, 3],
        [3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 3, 3, 3, 3,
         3, 0, 0, 3, 3],
        [3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 3],
        [3, 3, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0],
        [3, 0, 2, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 2, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0,
         0, 0, 2, 2],
        [0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
         0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 2, 2, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 2, 0,
         0, 0, 2, 2],
        [0, 0, 0, 0, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 3, 3, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 2, 2, 2, 0,
         0, 0, 2, 2]
        ]

nb_cases_x = 40
nb_cases_y = 40
nb_cases = 40


def init_matrice_terrain(Mat, x, y):
    assert (Mat == [])
    for i in range(x):
        Mat.append([])
        for j in range(y):
            Mat[i].append(h.Herb(i,j))


# Mat [i][j] : donne un tableau avec la liste des personnages, si y en a aucun c'est le type walker par défaut. (parce qu'on a besoin de l'attribut name)
def init_matrice_perso(Mat, x, y):
    assert (Mat == [])
    for i in range(x):
        Mat.append([])
        for j in range(y):
            Mat[i].append([])
            Mat[i][j].append([])
            Mat[i][j][0] = w.Walker(i, j, None)


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


id_size = {0: 1, 92: 1, 90: 3, 91: 1, 8: 1, 81: 1, 55: 1, 5: 1, 84: 2, 71: 3, 72: 3, 100: 3, 101: 3, 103: 3, 109: 2,
           111: 2, 114: 2, 0: 1, 1: 1, 2: 1, 3: 3, 115: 1, 116: 1, 7: 1}

def put_bat_mat(x,y,bat,Mat):
    for i in range(0,bat.nbr_cases):
        for j in range(0,bat.nbr_cases):
            Mat[x+i][y+j] = bat


def add_bat(x, y, id_bat, Mat):
    
    if (id_bat == 92):
        well = wa.Well(x, y)
        Mat[x][y] = well
    if (id_bat == 90):
        Reservoir = wa.Reservoir(x, y)
        put_bat_mat(x,y,Reservoir, Mat)
    if (id_bat == 91):
        Fountain = wa.Fountain(x, y)
        Mat[x][y] = Fountain
    if (id_bat == 8):
        Aquaduct = wa.Aquaduct(x, y)
        Mat[x][y] = Aquaduct
    if (id_bat == 81):
        EngineersPost = eng.EngineersPost(x, y)
        Mat[x][y] = EngineersPost
    if (id_bat == 55):
        Prefecture = sec.Prefecture(x, y)
        Mat[x][y] = Prefecture
    if (id_bat == 5):
        Route = pa.Path(x, y)
        Mat[x][y] = Route
    if (id_bat == 84):
        Forum = admin.Forum1(x, y)
        put_bat_mat(x,y,Forum,Mat)
    if(id_bat == 1):
        Mat[x][y] = t.Water(x,y)
    if(id_bat == 2):
        Mat[x][y] = t.Rock(x,y)
    if(id_bat == 3):
        Mat[x][y] = tr.tree(x,y)
    if(id_bat == 4):
        Senate = admin.Senate1(x,y)
        put_bat_mat(x,y,Senate,Mat)
    if(id_bat == 10):
        Maison_1=mais.Maison_1(x,y)
        put_bat_mat(x,y, Maison_1, Mat)
    if(id_bat == 11):
        Maison_2=mais.Maison_2(x,y)
        put_bat_mat(x,y,Maison_2, Mat)
    if(id_bat == 12):
        Maison_3=mais.Maison_3(x,y)
        put_bat_mat(x,y,Maison_3, Mat)
    if(id_bat == 13):
        Maison_4=mais.Maison_4(x,y)
        put_bat_mat(x,y,Maison_4, Mat)
    if(id_bat == 100):
        Ferme=f.Ferme(x,y)
        put_bat_mat(x,y,Ferme,Mat)
    if(id_bat == 71):
        Granary = g.Granary(x,y)
        put_bat_mat(x,y,Granary,Mat)
    if (id_bat == 72):
        Warehouse = war.Warehouse(x,y)
        put_bat_mat(Warehouse)
    if(id_bat == 0):
        Herb = h.Herb(x, y)
        Mat[x][y] = Herb



# globals()["Prefecture"+x+y] # truc interessant dont on se sert pas, à conserver pour plus tard

def add_perso_mat(Mat, perso,x,y):
    if(Mat[x][y][0].name == "no Walker"):
        Mat[x][y][0] = perso
    else:
        Mat[x][y].append(perso)



def add_perso(x,y, type, Mat, Bat):
    if (type == 'Delivery Guy'):
        DV = dv.Delivery_Guy(x, y, Bat)
        add_perso_mat(Mat, DV ,x,y)
        Bat.Walk.append(DV)



def departureMatrice(Mat):
    map_depart = matrix
    for i in range(0, nb_cases_x):
        for j in range(0, nb_cases_y):
            if(map_depart[i][j] ):
                add_bat(i, j, map_depart[i][j], Mat)
    afficher_matrice_bat(Mat, nb_cases_x, nb_cases_y)


def isPath(x, y, Mat):
    return Mat[x][y].name == 'Path'


def SearchforRoad(x, y, Mat):  # SearchforRoad donne la route qu'il croise autour (distance de 1) d'un batiment situé en x,y
    n = Mat[x][y].nbr_cases
    x1 = 0
    y1 = 0
    if (x != 0):
        x1 = x - 1
    if (y != 0):
        y1 = y - 1
    for i in range(n + 3):
        if (isPath(x1, y1, Mat)):
            return (x1, y1)
        x1 = x1 + 1
    for j in range(n + 3):
        if (isPath(x1, y1, Mat)):
            return (x1, y1)
        y1 = y1 + 1
    for i in range(0, n + 1):
        if (isPath(x1, y1, Mat)):
            return (x1, y1)
        x1 = x1 - 1
    for j in range(n + 3):
        if (isPath(x1, y1, Mat)):
            return (x1, y1)
        y1 = y1 - 1
    return (-1, -1)


def InTable(x, tab):
    bool = 1
    for i in range(len(tab)):
        if (x == tab[i]):
            bool = 0
    return bool


def min_tab_tab_notnull(tab):  # take a tab of tab and return the tab in the tab of tab, with the smallest size, exept if null
    n = len(tab)
    min = tab[0]
    for i in range(n):
        if (len(min) < len(tab[i]) and len(tab[i]) != 0):
            min = tab[i]
    return min


def next_case(x, y, tab_path, dest_x, dest_y, Mat):
    assert (isPath(x, y, Mat))
    if (x == dest_x and y == dest_y):
        return tab_path
    else:
        tab1 = []
        tab2 = []
        tab3 = []
        tab4 = []
        if (isPath(x + 1, y, Mat) and InTable((x + 1, y), tab_path)):
            tab1 = tab_path
            tab1.append((x + 1, y))
            tab1 = next_case(x + 1, y, tab1, dest_x, dest_y, Mat)
        if (isPath(x, y + 1, Mat) and InTable((x, y + 1), tab_path)):
            tab2 = tab_path
            tab2.append((x, y + 1))
            tab2 = next_case(x, y + 1, tab1, dest_x, dest_y, Mat)
        if (isPath(x - 1, y, Mat) and InTable((x + 1, y), tab_path)):
            tab3 = tab_path
            tab3.append((x - 1, y))
            tab3 = next_case(x - 1, y, tab1, dest_x, dest_y, Mat)
        if (isPath(x, y - 1, Mat) and InTable((x, y - 1), tab_path)):
            tab4 = tab_path
            tab4.append((x, y - 1))
            tab4 = next_case(x, y - 1, tab1, dest_x, dest_y, Mat)
        if ((isPath(x + 1, y, Mat) and InTable((x + 1, y), tab_path)) or (
                isPath(x, y + 1, Mat) and InTable((x, y + 1), tab_path)) or (
                isPath(x - 1, y, Mat) and InTable((x + 1, y), tab_path)) or (
                isPath(x, y - 1, Mat) and InTable((x, y - 1), tab_path)) == 0):
            return []
        tab = []
        tab.append(tab1)
        tab.append(tab2)
        tab.append(tab3)
        tab.append(tab4)
        return min_tab_tab_notnull(tab)


def Deplacement_basique():  # a faire evidemment
    return (0, 0)


def deplacement_perso(Mat, i, j):
    if Mat[i][j][0].name != "Walker":
        for k in range(Mat[i][j].len):
            if (Mat[i][j][k].destination_x != 666 and Mat[i][j][k].destination_y != 666):
                if (Mat[i][j][k].tab_path == []):
                    Mat[i][j][k].tab_path = next_case(i, j, [(i, j)], Mat[i][j][k].destination_x,
                                                      Mat[i][j][k].destination_y, Mat)
                else:
                    Mat[i][j][k].tab_path.pop(0)
                    (nx, ny) = Mat[i][j][k].tab_path(0)
            else:
                (nx, ny) = Deplacement_basique()


Mat_batiment = []
Mat_perso = []


init_matrice_terrain(Mat_batiment, nb_cases_x, nb_cases_y)
init_matrice_perso(Mat_perso, nb_cases_x, nb_cases_y)
add_bat(1,1,5,Mat_batiment)
add_perso(1,1,"Delivery Guy", Mat_perso, Mat_batiment[1][1])

#
#
afficher_matrice_bat(Mat_batiment, 3, 3)
afficher_matrice_perso(Mat_perso, 3, 3)

