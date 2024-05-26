import random
class Polarm:
    def __init__(self, boss):
        self.boss = boss

    def wybor(self, postac):
        if not self.boss.czy_potwor_zyje():
            return
        wybor = random.randint(1, 4)
        if wybor == 1:
            return self.ataki(postac)
        elif wybor == 2:
            return self.granaty(postac)
        elif wybor == 3:
            return self.regeneracja()
        elif wybor == 4:
            return self.specjalny_atak(postac)

    def ataki(self, postac):
        if not self.boss.czy_potwor_zyje():
            return
        if random.randint(1, 100) < self.boss.atrybuty.critRate:
            print("Boss zadał ci krytyczne obrażenia!")
            dmg = (self.boss.bazowy_atak * self.boss.atrybuty.critDMG) // 150
        else:
            dmg = self.boss.bazowy_atak
        print(f"Tracisz {dmg} HP!")
        postac.odejmij_hp(dmg)

    def granaty(self, postac):
        if not self.boss.czy_potwor_zyje():
            return
        if random.randint(1, 100) < self.boss.atrybuty.critRate:
            print("Boss zadał ci krytyczne obrażenia!")
            dmg = (self.boss.bazowy_atak * self.boss.atrybuty.critDMG) // 110
        else:
            dmg = self.boss.bazowy_atak
        print(f"Tracisz {dmg} HP!")
        postac.odejmij_hp(dmg)

    def regeneracja(self):
        if not self.boss.czy_potwor_zyje():
            return
        self.boss.atrybuty.hp += 40
        print("Boss się regeneruje i zyskuje 40 HP!")

    def specjalny_atak(self, postac):
        if not self.boss.czy_potwor_zyje():
            return
        print("Boss używa specjalnego ataku!")
        dmg = self.boss.bazowy_atak * 2
        print(f"Tracisz {dmg} HP!")
        postac.odejmij_hp(dmg)