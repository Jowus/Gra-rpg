from postacie import Mag, Alchemik, Wojownik

#------------------------------SKLEP------------------------------
class Sklep:
    def __init__(self):
        self.hp_cost = 10
        self.mana_cost = 10
        self.stamina_cost = 10
        self.mikstury_cost = 5
        self.critRate_cost = 15
        self.critDMG_cost = 20

    def kupowanie(self, gracz):
        print("Co chcesz ulepszyć?:")
        print("1 - HP")
        print("2 - CritRate")
        print("3 - CritDMG")
        if isinstance(gracz, Mag):
            print("4 - Mana")
        elif isinstance(gracz, Wojownik):
            print("4 - Stamina")
        elif isinstance(gracz, Alchemik):
            print("4 - Mikstury")
        
        wybor = input()
        if wybor == "1":
            self.buy_hp(gracz)
        elif wybor == "2":
            self.buy_critRate(gracz)
        elif wybor == "3":
            self.buy_critDMG(gracz)
        elif wybor == "4":
            if isinstance(gracz, Mag):
                self.buy_mana(gracz)
            elif isinstance(gracz, Wojownik):
                self.buy_stamina(gracz)
            elif isinstance(gracz, Alchemik):
                self.buy_mikstury(gracz)
        else:
            print("Nieprawidłowy wybór.")

    def buy_hp(self, gracz):
        if gracz.mora >= self.hp_cost:
            gracz.hp += 40
            gracz.mora -= self.hp_cost
            print(f"Kupiono HP! Nowe HP: {gracz.hp}, Pozostała mora: {gracz.mora}")
        else:
            print("Nie masz wystarczająco mory.")

    def buy_mana(self, mag):
        if isinstance(mag, Mag) and mag.mora >= self.mana_cost:
            mag.mana += 50
            mag.mora -= self.mana_cost
            print(f"Kupiono mana! Nowa mana: {mag.mana}, Pozostała mora: {mag.mora}")
        else:
            print("Nie masz wystarczająco mory.")

    def buy_stamina(self, wojownik):
        if isinstance(wojownik, Wojownik) and wojownik.mora >= self.stamina_cost:
            wojownik.stamina += 50
            wojownik.mora -= self.stamina_cost
            print(f"Kupiono stamina! Nowa stamina: {wojownik.stamina}, Pozostała mora: {wojownik.mora}")
        else:
            print("Nie masz wystarczająco mory.")

    def buy_mikstury(self, alchemik):
        if isinstance(alchemik, Alchemik) and alchemik.mora >= self.mikstury_cost:
            alchemik.mikstury += 20
            alchemik.mora -= self.mikstury_cost
            print(f"Kupiono mikstury! Ilość mikstur: {alchemik.mikstury}, Pozostała mora: {alchemik.mora}")
        else:
            print("Nie masz wystarczająco mory.")

    def buy_critRate(self, gracz):
        if gracz.mora >= self.critRate_cost:
            gracz.critRate += 10
            gracz.mora -= self.critRate_cost
            print(f"Kupiono Crit Rate! Nowy Crit Rate: {gracz.critRate}, Pozostała mora: {gracz.mora}")
        else:
            print("Nie masz wystarczająco mory.")

    def buy_critDMG(self, gracz):
        if gracz.mora >= self.critDMG_cost:
            gracz.critDMG += 15
            gracz.mora -= self.critDMG_cost
            print(f"Kupiono Crit DMG! Nowy Crit DMG: {gracz.critDMG}, Pozostała mora: {gracz.mora}")
        else:
            print("Nie masz wystarczająco mory.")
