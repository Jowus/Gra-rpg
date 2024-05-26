from postacie import Mag, Wojownik, Alchemik
from potwory import Nimfa, PotworAtrybuty, Straznik, Boss, Slime, Wilk, Kocur
import random 
from bron_boss import Polarm
from random import choice
from sklep import Sklep
from zagadki import zagadka, lista_zagadek

print("Podaj swoje imię")
imię_gracza = input()
print(f"Witam {imię_gracza} w mojej grze")
print("Wybierz klasę swojej postaci:")
print("1 - Mag")
print("2 - Wojownik")
print("3 - Alchemik")
klasa_postaci = input()
if klasa_postaci == "1":
    twoj_bohater = Mag()
    twoj_bohater.informacje_mag()
    print("Gratulacje! Zostałeś magiem!")
elif klasa_postaci == "2":
    twoj_bohater = Wojownik()
    twoj_bohater.informacje_wojownik()
    print("Gratulacje! Zostałeś wojownikiem!")
elif klasa_postaci == "3":
    twoj_bohater = Alchemik()
    twoj_bohater.informacje_alchemik()
    print("Gratulacje! Zostałeś alchemikiem!")
else:
    print("Nieprawidłowa klasa postaci.")

def bitwa(twoj_bohater, przeciwnik):
    if isinstance(twoj_bohater, Mag):
        twoj_bohater.walka_mag(przeciwnik)
    elif isinstance(twoj_bohater, Wojownik):
        twoj_bohater.walka_wojownik(przeciwnik)
    elif isinstance(twoj_bohater, Alchemik):
        twoj_bohater.walka_alchemik(przeciwnik)

sklep = Sklep()

atrybuty_slime = PotworAtrybuty(hp=100, critDMG=150, critRate=20, drop_mory=60)
slime1 = Slime(10, atrybuty=atrybuty_slime)
print("Na sam początek w ramach treningu pokonaj Slima")
bitwa(twoj_bohater, slime1)

def zad1(twoj_bohater):
    print("Gratulacje! Musisz udać się do zamku.")
    print("---" * 5)
    wybor = input("1 - zdobądź przepustkę \n2 - pokonaj strażników\n")

    if wybor == "1":
        print("---" * 5)
        print("Idziesz do urzędnika")
        zaplata = input("Aby zdobyć przepustkę, musisz zapłacić 10 mory. Czy płacisz? tak/nie\n")
        if zaplata == "tak":
            twoj_bohater.mora -= 10
            print("Zapłaciłeś i otrzymujesz przepustkę. Możesz wejść do zamku.")
            return 
        else:
            print("Nie zapłaciłeś, zmierzysz się ze strażnikami.")
    print("---" * 5)
    print("Idziesz do bram zamku i wyzywasz strażników na walkę.")
    atrybuty_straznik = PotworAtrybuty(hp=200, critDMG=100, critRate=40, drop_mory=60)
    straznik1 = Straznik(pistolet=40, atrybuty=atrybuty_straznik)
    print("Rozpoczyna się walka ze Strażnikiem.")
    bitwa(twoj_bohater, straznik1)
    twoj_bohater.dodaj_hp(50)

def zad2():
    print("---" * 5)
    print("Dostales sie do zamku")
    print("Musisz teraz odnalezc krola Edwarda")
    print("Aby to zrobic musisz poruszac sie zgodnie ze wskazowka...")
    lista_droga = ["Lewo", "Prawo", "Przód", "2 razy w Lewo"]
    for el in lista_droga:
        print(el)
    print("Ruszaj w drogę")
    wybor_1 = input("Na samym początku idź lewo/prawo/prosto:")
    if wybor_1 != "lewo":
        print("zla droga trafiasz na straznika")
        atrybuty_straznik = PotworAtrybuty(hp=100, critDMG=70, critRate=40, drop_mory=20)
        straznik2 = Straznik(pistolet=30, atrybuty=atrybuty_straznik)
        bitwa(twoj_bohater, straznik2)
    wybor2 = input("Teraz udaj się lewo/prawo/prosto:")
    if wybor2 != "prawo":
        print("zla droga trafiasz na slima")
        atrybuty_slime = PotworAtrybuty(hp=80, critDMG=90, critRate=40, drop_mory=10)
        slime2 = Slime(10, atrybuty=atrybuty_slime)
        bitwa(twoj_bohater, slime2)
    wybor3 = input("Następnie idziesz lewo/prawo/prosto:")
    if wybor3 != "prosto":
        print("zla droga trafiasz na straznika")
        straznik3 = Straznik(pistolet=34, atrybuty=atrybuty_straznik)
        bitwa(twoj_bohater, straznik3)
    wybor4 = input("Na koniec 2 razy w lewo/prawo/prosto:")
    if wybor4 != "lewo":
        print("Wbiegając do pokoju trafiasz w dziurę do kopalni i giniesz...")
        print("KONIEC GRY")
        breakpoint()

def zad3():
    print("-----KROL-----")
    print("Teraz musisz udać się do Wodnych Nimf")
    print("Po pokonaniu ich będziesz gotowy na starcie z Krolem mroku")
    print("*Wychodzisz z zamku...*")
    print("Na drodzę do oceanu spotykasz Wiedźmę!")
    print("-----WIEDZMA-----")
    print("Aby przejsc musisz odgadnąć 3 zagadki jednak za kazda nieodgadnięta tracisz jakis licznik umiejetnosci!")
    zagadka(lista_zagadek, twoj_bohater)
    zagadka(lista_zagadek, twoj_bohater)
    zagadka(lista_zagadek, twoj_bohater)
    print("Stan twojego bohatera")
    if isinstance(twoj_bohater, Mag):
        twoj_bohater.informacje_mag()
    elif isinstance(twoj_bohater, Wojownik):
        twoj_bohater.informacje_wojownik()
    elif isinstance(twoj_bohater, Alchemik):
        twoj_bohater.informacje_alchemik()
    print("Wiedzma puszcza cie dalej i w ramach tego mozesz ulepszyc u niej 2 kolejne rzeczy!")
    sklep.kupowanie(twoj_bohater)
    sklep.kupowanie(twoj_bohater)

def zad4():
    print("*Idziesz plaza*")
    print("Nagle z wody wynurza sie Nimfa")
    print("-----Nimfa-----")
    print("Witaj wędrowniku, co cie tu sprowadza")
    wybor = input("1 - Chce informacji o pobycie Krola Mroku(bez walki)\n2 - Chce zawalczyc z wami w zamian za informacje na temat Krola Mroku")
    if wybor == "1":
        twoj_bohater.odejmij_hp(150)
        print("Tracisz 150HP(bo nie chciałes walczyć)")
    elif wybor == "2":
        print("Niestety... Nic nie jest za darmo, musisz sie z NAMI zmierzyć")
        print("Atakuje cie 1 z 3 nimf")
        atrybuty_nimfa = PotworAtrybuty(hp=100, critDMG=60, critRate=40,drop_mory=30)
        nimfa1 = Nimfa(elementDMG=30, atrybuty=atrybuty_nimfa)
        bitwa(twoj_bohater,nimfa1)
        print("Atakuje cie 2 nimfa")
        atrybuty_nimfa2 = PotworAtrybuty(hp=100, critDMG=60, critRate=40,drop_mory=30)
        nimfa2 = Nimfa(elementDMG=35, atrybuty=atrybuty_nimfa2)
        bitwa(twoj_bohater, nimfa2)
        print("Walczysz juz z ostatnia... krolowa nimf")
        atrybuty_nimfa3 = PotworAtrybuty(hp=100, critDMG=60, critRate=40,drop_mory=30)
        nimfa3 = Nimfa(elementDMG=40,atrybuty=atrybuty_nimfa3)
        bitwa(twoj_bohater, nimfa3)
        print("W ramach tego ze mnie pokonales dostaniesz mozliwosc ulepszenia swoich umiejetnosci w podwodnym sklepie")
        twoj_bohater.dodaj_mora(150)
        sklep.kupowanie(twoj_bohater)
        sklep.kupowanie(twoj_bohater)
        sklep.kupowanie(twoj_bohater)
    print("-----KROLOWA-----")
    print("Krola mroku znajdziesz w lesie niedaleko morza gdy pojdziesz droga z kamieniami")

def zad5(twoj_bohater):
    print("-----LAS-----")
    print("Wchodzisz do mrocznego lasu. Przed tobą trzy drogi:")
    print("1 - Droga z kamieniami")
    print("2 - Droga z kwiatami")
    print("3 - Droga w cieniu drzew")

    wybor = input("Wybierz drogę (1/2/3): ")

    if wybor == "1":
        print("Idziesz drogą z kamieniami...")
        print("Natrafiasz na Króla Mroku!")
        atrybuty_boss = PotworAtrybuty(hp=300, critDMG=200, critRate=50, drop_mory=150)
        boss = Boss(bron=Polarm, bazowy_atak=50, atrybuty=atrybuty_boss)
        bitwa(twoj_bohater, boss)
        if not twoj_bohater.czy_postac_zyje():
            print("Przegrałeś")
        elif not boss.czy_potwor_zyje():
            print("Gratulacje! Pokonałeś Króla Mroku i wygrałeś grę!")
    elif wybor == "2":
        print("Idziesz drogą z kwiatami...")
        print("Natrafiasz na Wilka!")
        atrybuty_wilk = PotworAtrybuty(hp=150, critDMG=80, critRate=40, drop_mory=40)
        wilk = Wilk(15, atrybuty=atrybuty_wilk)
        bitwa(twoj_bohater, wilk)
        if wilk.czy_potwor_zyje():
            print("Wilk pokonał cię. Spróbuj jeszcze raz!")
        else:
            print("Pokonałeś Wilka. Możesz wrócić i spróbować innej drogi.")
            zad5(twoj_bohater)
    elif wybor == "3":
        print("Idziesz drogą w cieniu drzew...")
        print("Natrafiasz na Kocura!")
        atrybuty_kocur = PotworAtrybuty(hp=150, critDMG=100, critRate=45, drop_mory=50)
        kocur = Kocur(20, atrybuty=atrybuty_kocur)
        bitwa(twoj_bohater, kocur)
        if kocur.czy_potwor_zyje():
            print("Kocur pokonał cię. Spróbuj jeszcze raz!")
        else:
            print("Pokonałeś Kocura. Możesz wrócić i spróbować innej drogi.")
            zad5(twoj_bohater)
    else:
        print("Niepoprawny wybór. Spróbuj jeszcze raz.")
        zad5(twoj_bohater)

zad1(twoj_bohater)
zad2()
print("Gratulacje dotarłeś na miejsce")
twoj_bohater.dodaj_mora(20)
print("Mozesz teraz ulepszyc 1 rzecz u krolewskiego kupca")
sklep.kupowanie(twoj_bohater)
print("-----KROL-----")
print(f"Witaj {imię_gracza}!")
print("Sprowadziłem cię tu abys zdobył dla mnie Miecz Nieśmiertelności którego posiadaczem jest krol mroku!")
wyborpomocy = input("Czy chcesz pomoc? tak/nie:")
if wyborpomocy == "tak":
    zad3()
    zad4()
    zad5(twoj_bohater)
else:
    print("Zatem kończymy grę...")
    breakpoint()
