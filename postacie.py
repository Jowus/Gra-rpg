from rozdzka import Rozdzka, Miecz, Mikstury

class Gracz:
    def __init__(self):
        self.hp = 0
        self.critDMG = 0
        self.critRate = 0
        self.mora = 0

    def informacje(self):
        print("---" * 5)
        print(f"Hp - {self.hp}")
        print(f"Crit DMG - {self.critDMG}")
        print(f"Crit Rate - {self.critRate}")

    def odejmij_hp(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            print("Zginąłeś!")
    def dodaj_mora(self, mora):
        self.mora += mora
        print(f"Zdobyłes {mora} mory")
    

    def dodaj_hp(self, hp):
        self.hp += hp
        print(f"Uleczono cię o {hp}HP")

class Mag(Gracz):
    def __init__(self):
        super().__init__()
        self.elementDMG = 40
        self.hp += 200
        self.mana = 200
        self.critDMG += 120
        self.critRate += 60
        self.bron = Rozdzka(self)

    def informacje_mag(self):
        self.informacje()
        print(f"Mana - {self.mana}")
        print(f"Element DMG - {self.elementDMG}")
        print("---" * 5)

    def czy_postac_zyje(self):
        return self.hp > 0
    
    def walka_mag(self, opponent):
        while self.czy_postac_zyje() and opponent.czy_potwor_zyje():
            print("-----TWOJ MAG-----")
            self.informacje_mag()
            print("---TWOJ PRZECIWNIK---")
            opponent.informacje_potwory()
            self.bron.wybor_zaklecia(self, opponent)
            if not opponent.czy_potwor_zyje():
                print("Pokonałeś przeciwnika!")
            opponent.atakuj(self)
            if not self.czy_postac_zyje():
                print("Zostałeś pokonany!")
                print("KONIEC GRY")
                break
class Wojownik(Gracz):
    def __init__(self):
        super().__init__()
        self.elementDMG = 50
        self.hp += 500
        self.stamina = 200
        self.critDMG = 100
        self.critRate = 50
        self.bron = Miecz(self)

    def informacje_wojownik(self):
        self.informacje()
        print(f"Stamina - {self.stamina}")
        print("---" * 5)

    def czy_postac_zyje(self):
        return self.hp > 0

    def walka_wojownik(self, opponent):
        while self.czy_postac_zyje() and opponent.czy_potwor_zyje():
            print("-----TWOJ WOJOWNIK-----")
            self.informacje_wojownik()
            print("---TWOJ PRZECIWNIK---")
            opponent.informacje_potwory()
            self.bron.wybor_zaklecia_miecz(self, opponent)
            if not opponent.czy_potwor_zyje():
                print("Pokonałeś przeciwnika!")
                break
            opponent.atakuj(self)
            if not self.czy_postac_zyje():
                print("Zostałeś pokonany!")
                print("KONIEC GRY")
                break
class Alchemik(Gracz):
    def __init__(self):
        super().__init__()
        self.elementDMG = 50
        self.hp += 250
        self.mikstury = 20
        self.critDMG = 100
        self.critRate = 50
        self.bron = Mikstury(self)

    def informacje_alchemik(self):
        self.informacje()
        print(f"Ilość mikstur(w litrach) - {self.mikstury}")
        print("---" * 5)

    def czy_postac_zyje(self):
        return self.hp > 0

    def walka_alchemik(self, opponent):
        while self.czy_postac_zyje() and opponent.czy_potwor_zyje():
            print("-----TWOJ ALCHEMIK-----")
            self.informacje_alchemik()
            print("---TWOJ PRZECIWNIK---")
            opponent.informacje_potwory()
            self.bron.wybor_zaklecia_mikstury(self, opponent)
            if not opponent.czy_potwor_zyje():
                print("Pokonałeś przeciwnika!")
                break
            opponent.atakuj(self)
            if not self.czy_postac_zyje():
                print("Zostałeś pokonany!")
                print("KONIEC GRY")
                break