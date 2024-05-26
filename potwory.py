import random
from bron_boss import Polarm
#------------------------------POTWOR ATRYBUTY------------------------------
class PotworAtrybuty:
    def __init__(self, hp, critDMG, critRate, drop_mory):
        self.hp = hp
        self.critDMG = critDMG
        self.critRate = critRate
        self.drop_mory = drop_mory

    def informacje_potwory(self):
        print("---" * 5)
        print(f"Hp - {self.hp}")
        print(f"Crit DMG - {self.critDMG}")
        print(f"Crit Rate - {self.critRate}")
        print("---" * 5)

    def czy_potwor_zyje(self):
        return self.hp > 0

    def odejmij_hp(self, dmg):
        self.hp -= dmg

    def drop_mora(self):
        return self.drop_mory

#------------------------------NIMFA------------------------------
class Nimfa:
    def __init__(self, elementDMG, atrybuty: PotworAtrybuty):
        self.elementDMG = elementDMG
        self.atrybuty = atrybuty

    def informacje_potwory(self):
        self.atrybuty.informacje_potwory()
        print(f"ElementDMG - {self.elementDMG}")
        print("---" * 5)

    def atakuj(self, postac):
        if random.randint(1, 300) < self.atrybuty.critRate:
            print("Nimfa zadała ci krytyczne obrażenia!")
            dmg = (self.elementDMG * self.atrybuty.critDMG) // 50
        else:
            dmg = self.elementDMG
        print(f"Tracisz {dmg}HP!")
        postac.odejmij_hp(dmg)

    def czy_potwor_zyje(self):
        return self.atrybuty.czy_potwor_zyje()

    def odejmij_hp(self, dmg):
        self.atrybuty.odejmij_hp(dmg)

    def drop_mora(self):
        return self.atrybuty.drop_mora()

#------------------------------STRAZNIK------------------------------
class Straznik:
    def __init__(self, pistolet, atrybuty: PotworAtrybuty):
        self.pistolet = pistolet
        self.atrybuty = atrybuty

    def informacje_potwory(self):
        self.atrybuty.informacje_potwory()
        print(f"Pistolet - {self.pistolet}")
        print("---" * 5)

    def atakuj(self, postac):
        ilosc_kul = random.randint(1, 3)
        if random.randint(1, 300) < self.atrybuty.critRate:
            print("Straznik zadał ci krytyczne obrażenia!")
            print(f"Ilość pocisków {ilosc_kul}")
            dmg = (ilosc_kul * self.pistolet * self.atrybuty.critDMG) // 150
        else:
            print(f"Ilość pocisków {ilosc_kul}")
            dmg = (ilosc_kul * self.pistolet)
        print(f"Tracisz {dmg}HP!")
        postac.odejmij_hp(dmg)

    def czy_potwor_zyje(self):
        return self.atrybuty.czy_potwor_zyje()

    def odejmij_hp(self, dmg):
        self.atrybuty.odejmij_hp(dmg)

    def drop_mora(self):
        return self.atrybuty.drop_mora()

#------------------------------SLIME------------------------------
class Slime:
    def __init__(self, klej, atrybuty: PotworAtrybuty):
        self.klej = klej
        self.atrybuty = atrybuty

    def informacje_potwory(self):
        self.atrybuty.informacje_potwory()
        print(f"Klej - {self.klej}")
        print("---" * 5)

    def atakuj(self, postac):
        if random.randint(1, 500) < self.atrybuty.critRate:
            print("Slime zadał ci krytyczne obrażenia!")
            dmg = (self.klej * self.atrybuty.critDMG) // 200
        else:
            dmg = (self.klej)
        print(f"Tracisz {dmg}HP!")
        postac.odejmij_hp(dmg)

    def czy_potwor_zyje(self):
        return self.atrybuty.czy_potwor_zyje()

    def odejmij_hp(self, dmg):
        self.atrybuty.odejmij_hp(dmg)

    def drop_mora(self):
        return self.atrybuty.drop_mora()
#------------------------------BOSS------------------------------
class Boss:
    def __init__(self, bron, bazowy_atak, atrybuty):
        self.bron = bron(self)
        self.bazowy_atak = bazowy_atak
        self.atrybuty = atrybuty

    def informacje_potwory(self):
        self.atrybuty.informacje_potwory()
        print(f"Bron - {self.bron}")
        print("---" * 5)

    def atakuj(self, postac):
        self.bron.wybor(postac)

    def czy_potwor_zyje(self):
        return self.atrybuty.czy_potwor_zyje()

    def odejmij_hp(self, dmg):
        self.atrybuty.odejmij_hp(dmg)

    def drop_mora(self):
        return self.atrybuty.drop_mora()
#------------------------------WILK------------------------------
class Wilk:
    def __init__(self, pazur, atrybuty: PotworAtrybuty):
        self.pazur = pazur
        self.atrybuty = atrybuty

    def informacje_potwory(self):
        self.atrybuty.informacje_potwory()
        print(f"Pazur - {self.pazur}")
        print("---" * 5)

    def atakuj(self, postac):
        if random.randint(1, 200) < self.atrybuty.critRate:
            print("Slime zadał ci krytyczne obrażenia!")
            dmg = (self.pazur * self.atrybuty.critDMG) // 200
        else:
            dmg = (self.pazur)
        print(f"Tracisz {dmg}HP!")
        postac.odejmij_hp(dmg)

    def czy_potwor_zyje(self):
        return self.atrybuty.czy_potwor_zyje()

    def odejmij_hp(self, dmg):
        self.atrybuty.odejmij_hp(dmg)

    def drop_mora(self):
        return self.atrybuty.drop_mora()
#------------------------------KOCUR------------------------------
class Kocur:
    def __init__(self, gryzienie, atrybuty: PotworAtrybuty):
        self.gryzienie = gryzienie
        self.atrybuty = atrybuty

    def informacje_potwory(self):
        self.atrybuty.informacje_potwory()
        print(f"Gryzienie - {self.gryzienie}")
        print("---" * 5)

    def atakuj(self, postac):
        if random.randint(1, 200) < self.atrybuty.critRate:
            print("Slime zadał ci krytyczne obrażenia!")
            dmg = (self.gryzienie * self.atrybuty.critDMG) // 200
        else:
            dmg = (self.gryzienie)
        print(f"Tracisz {dmg}HP!")
        postac.odejmij_hp(dmg)

    def czy_potwor_zyje(self):
        return self.atrybuty.czy_potwor_zyje()

    def odejmij_hp(self, dmg):
        self.atrybuty.odejmij_hp(dmg)

    def drop_mora(self):
        return self.atrybuty.drop_mora()