import random

#------------------------------ROZDZKA------------------------------
class Rozdzka:
    def __init__(self, postac):
        self.elementDMG = postac.elementDMG
        self.mana = postac.mana
        self.critDMG = postac.critDMG
        self.critRate = postac.critRate
        self.hp = postac.hp

    def wybor_zaklecia(self, postac, opponent):
        while True:
            print("Wybierz atak:")
            print("r - podstawowy atak")
            print("e - tarcza")
            print("z - regeneracja")
            print("q - specjalny atak")
            wybor_ataku = input()
            if wybor_ataku == "r":
                return self.zwykle_zaklecie(postac, opponent)
            elif wybor_ataku == "e":
                return self.nalozenie_tarczy(postac)
            elif wybor_ataku == "z":
                return self.regeneracja(postac)
            elif wybor_ataku == "q":
                return self.specjalnyy_atak(postac, opponent) 
            else:
                print("Nieprawidłowy wybór.")
        
    def zwykle_zaklecie(self, postac, opponent):
        dmg = 0
        if postac.mana >= 10:
            if random.randint(1, 200) < self.critRate:
                print("Zadano krytyczne obrażenia!")
                dmg += (self.elementDMG * self.critDMG) // 100
            else:
                dmg += self.elementDMG
            postac.mana -= 10
            print(f"Zadałeś {dmg} obrażeń!")
            opponent.odejmij_hp(dmg)
        else:
            print("Za mało many!")
    
    def nalozenie_tarczy(self, postac):
        if postac.mana >= 40:
            postac.hp += 10
            postac.mana -= 40
            print("Nalozyles tarcze!")
        else:
            print("Za mało many!")

    def regeneracja(self, postac):
        if postac.mana >= 40:
            postac.hp += 20
            postac.mana -= 40
            print("Zregenerowano!")
        else:
            print("Za mało many!")
    
    def specjalnyy_atak(self, postac, opponent):  
        dmg = 0
        if postac.mana >= 100:
            if random.randint(1, 200) < self.critRate:
                print("Zadano krytyczne obrażenia!")
                dmg += (self.elementDMG * self.critDMG) // 10
            else:
                dmg += self.elementDMG * 10
            postac.mana -= 100
            print(f"Zadałeś {dmg} obrażeń!")
            opponent.odejmij_hp(dmg)
        else:
            print("Za mało many!")

#------------------------------MIECZ------------------------------
class Miecz:
    def __init__(self, postac):
        self.elementDMG = postac.elementDMG
        self.stamina = postac.stamina
        self.critDMG = postac.critDMG
        self.critRate = postac.critRate
        self.hp = postac.hp

    def wybor_zaklecia_miecz(self,postac, opponent):
        while True:
            print("Wybierz atak:")
            print("r - podstawowy atak")
            print("e - granat")
            print("z - regeneracja")
            print("q - specjalny atak")
            wybor_ataku = input()
            if wybor_ataku == "r":
                return self.zwykle_zaklecie(postac, opponent)
            elif wybor_ataku == "e":
                return self.granaty(postac, opponent)
            elif wybor_ataku == "z":
                return self.regeneracja(opponent)
            elif wybor_ataku == "q":
                return self.specjalnyy_atak(postac, opponent) 
            else:
                print("Nieprawidłowy wybór.")
    
    def zwykle_zaklecie(self,postac, opponent):
        dmg = 0
        if postac.stamina >= 10:
            if random.randint(1, 200) < postac.critRate:
                print("Zadano krytyczne obrażenia!")
                dmg += (postac.elementDMG * postac.critDMG) // 100
            else:
                dmg += postac.elementDMG
            postac.stamina -= 10
            print(f"Zadałeś {dmg} obrażeń!")
            opponent.odejmij_hp(dmg)
        else:
            print("Za mało staminy!")
        
    def granaty(self, opponent):
        dmg = 0
        if self.stamina >= 40:
            if random.randint(1, 400) < self.critRate:
                print("Zadano krytyczne obrażenia!")
                dmg += (self.elementDMG * self.critDMG) // 80
            else:
                dmg += self.elementDMG
            self.stamina -= 40
            print(f"Zadałeś {dmg} obrażeń granatem!")
            opponent.odejmij_hp(dmg)
        else:
            print("Za mało staminy!")

    def regeneracja(self, opponent):
        if self.stamina >= 40:
            self.hp += 10
            self.stamina -= 40
            print("Zregenerowano!")
        else:
            print("Za mało staminy!")
        
    def specjalnyy_atak(self,postac, opponent):
        dmg = 0
        if postac.stamina >= 100:
            if random.randint(1, 200) < postac.critRate:
                print("Zadano krytyczne obrażenia!")
                dmg += (postac.elementDMG * postac.critDMG) // 10
            else:
                dmg += postac.elementDMG
            postac.stamina -= 100
            print(f"Zadałeś {dmg} obrażeń specjalnym atakiem!")
            opponent.odejmij_hp(dmg)
        else:
            print("Za mało staminy!")
#------------------------------Mikstury------------------------------
class Mikstury:
    def __init__(self, postac):
        self.elementDMG = postac.elementDMG
        self.critDMG = postac.critDMG
        self.critRate = postac.critRate
        self.hp = postac.hp

    def wybor_zaklecia_mikstury(self, postac, opponent):
        while True:
            print("Wybierz atak:")
            print("r - plazma")
            print("e - mikstura wybuchu")
            print("z - regeneracja")
            print("q - specjalna mieszanka")
            wybor_ataku = input()
            if wybor_ataku == "r":
                return self.plazma(postac, opponent)
            elif wybor_ataku == "e":
                return self.mikstura_wybuchu(postac, opponent)
            elif wybor_ataku == "z":
                return self.regeneracja(postac)
            elif wybor_ataku == "q":
                return self.specjalna_mieszanka(postac, opponent) 
            else:
                print("Nieprawidłowy wybór.")
    
    def plazma(self, postac, opponent):
        dmg = 0
        if postac.mikstury >= 2:
            if random.randint(1, 200) < postac.critRate:
                print("Zadano krytyczne obrażenia!")
                dmg += (postac.elementDMG * postac.critDMG) // 100
            else:
                dmg += postac.elementDMG
            postac.mikstury -= 2
            print(f"Zadałeś {dmg} obrażeń!")
            opponent.odejmij_hp(dmg)
        else:
            print("Za mało mikstur!")
        
    def mikstura_wybuchu(self, postac, opponent):
        dmg = 0
        if postac.mikstury >= 4:
            if random.randint(1, 400) < postac.critRate:
                print("Zadano krytyczne obrażenia!")
                dmg += (postac.elementDMG * postac.critDMG) // 80
            else:
                dmg += postac.elementDMG
            postac.mikstury -= 4
            print(f"Zadałeś {dmg} obrażeń granatem!")
            opponent.odejmij_hp(dmg)
        else:
            print("Za mało mikstur!")
        
    def regeneracja(self, postac):
        if postac.mikstury >= 3:
            postac.hp += 20
            postac.mikstury -= 3
            print("Zregenerowano!")
        else:
            print("Za mało mikstur!")
        
    def specjalna_mieszanka(self, postac, opponent):
        dmg = 0
        if postac.mikstury >= 10:
            if random.randint(1, 200) < postac.critRate:
                print("Zadano krytyczne obrażenia!")
                dmg += (postac.elementDMG * postac.critDMG) // 10
            else:
                dmg += postac.elementDMG
            postac.mikstury -= 10
            print(f"Zadałeś {dmg} obrażeń specjalnym atakiem!")
            opponent.odejmij_hp(dmg)
        else:
            print("Za mało mikstur!")