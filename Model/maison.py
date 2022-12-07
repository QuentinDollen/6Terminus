from Terminus_project.Model import batiment as b


# class Panneau():
class Maison_1(b.Batiment):
    def __init__(self, x, y):
        b.Batiment.__init__(self, 1, 10, x, y, 10, -3, 1, 1, 3, 0)
        self.name = 'Maison 1'
        self.nb_habitants = 0
        self.nourriture = []
        self.produits = []
        self.acces_eau = 0
        self.des_prev = -99  # cf https://gamefaqs.gamespot.com/pc/63635-caesar-iii/faqs/14466
        self.des_next = -10
        # self.entNeeded = 0
        self.watNeeded = 0
        self.godNeeded = 0
        # self.eduNeeded = 0
        self.marketNeeded = 0
        # self.barberNeeded = 0
        # self.bathNeeded = 0
        # self.medNeeded = 0
        self.foodNeeded = 0
        # self.potNeeded = 0
        # self.oilNeeded = 0
        # self.furNeeded = 0
        # self.wineNeeded = 0
        self.crimeIncrement = 3
        self.crimeBase = 25
        self.prospCap = 5
        self.popLim = 5
        self.taxMultiplier = 1


class Maison_2(b.Batiment):
    def __init__(self, x, y):
        b.Batiment.__init__(self, 1, 11, x, y, 0, -3, 1, 1, 3, 0)
        self.name = 'Maison 2'
        self.nb_habitants = 0
        self.nourriture = []
        self.produits = []
        self.acces_eau = 0
        self.des_prev = -12  # cf https://gamefaqs.gamespot.com/pc/63635-caesar-iii/faqs/14466
        self.des_next = -5
        # self.entNeeded = 0
        self.watNeeded = 1
        self.godNeeded = 0
        # self.eduNeeded = 0
        self.marketNeeded = 0
        # self.barberNeeded = 0
        # self.bathNeeded = 0
        # self.medNeeded = 0
        self.foodNeeded = 0
        # self.potNeeded = 0
        # self.oilNeeded = 0
        # self.furNeeded = 0
        # self.wineNeeded = 0
        self.crimeIncrement = 3
        self.crimeBase = 25
        self.prospCap = 10
        self.popLim = 7
        self.taxMultiplier = 1


class Maison_3(b.Batiment):
    def __init__(self, x, y):
        b.Batiment.__init__(self, 1, 12, x, y, 0, -2, 1, 1, 2, 0)
        self.name = 'Maison 3'
        self.nb_habitants = 0
        self.nourriture = []
        self.produits = []
        self.acces_eau = 0
        self.des_prev = -7  # cf https://gamefaqs.gamespot.com/pc/63635-caesar-iii/faqs/14466
        self.des_next = 0
        # self.entNeeded = 0
        self.watNeeded = 1
        self.godNeeded = 0
        # self.eduNeeded = 0
        self.marketNeeded = 1
        # self.barberNeeded = 0
        # self.bathNeeded = 0
        # self.medNeeded = 0
        self.foodNeeded = 1
        # self.potNeeded = 0
        # self.oilNeeded = 0
        # self.furNeeded = 0
        # self.wineNeeded = 0
        self.crimeIncrement = 3
        self.crimeBase = 25
        self.prospCap = 15
        self.popLim = 9
        self.taxMultiplier = 1


class Maison_4(b.Batiment):
    def __init__(self, x, y):
        b.Batiment.__init__(self, 1, 13, x, y, 0, -2, 1, 1, 2, 0)
        self.name = 'Maison 4'
        self.nb_habitants = 0
        self.nourriture = []
        self.produits = []
        self.acces_eau = 0
        self.des_prev = -2  # cf https://gamefaqs.gamespot.com/pc/63635-caesar-iii/faqs/14466
        self.des_next = 4
        # self.entNeeded = 0
        self.watNeeded = 1
        self.godNeeded = 1
        # self.eduNeeded = 0
        self.marketNeeded = 1
        # self.barberNeeded = 0
        # self.bathNeeded = 0
        # self.medNeeded = 0
        self.foodNeeded = 1
        # self.potNeeded = 0
        # self.oilNeeded = 0
        # self.furNeeded = 0
        # self.wineNeeded = 0
        self.crimeIncrement = 3
        self.crimeBase = 25
        self.prospCap = 20
        self.popLim = 11
        self.taxMultiplier = 1
