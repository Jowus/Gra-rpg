import random
#------------------------------ZAGADKI------------------------------
lista_zagadek = ["jutro", "trójkąt", "deszcz", "koty", "talia kart"]
def zagadka(lista, bohater):
    proby = 0
    wybor_zagadki = random.choice(lista)
    print("Zgadnij zagadkę:")
    if wybor_zagadki == "jutro":
        print("Zawsze przyjdzie, ale nigdy nie przyjdzie dzisiaj. Co to takiego?")
        while proby < 3:
            rozwiązanie = input()
            if rozwiązanie == "jutro":
                bohater.dodaj_mora(50)
                print("Poprawna odpowiedź")
                proby += 3
            else:
                print("Zła odpowiedź!")
                proby += 1
                if proby == 3:
                    bohater.hp -= 50
                    print("Tracisz 50hp")
        lista.remove("jutro")
    elif wybor_zagadki == "trójkąt":
        print("Co to jest: małe, czerwone, trójkątne?")
        while proby < 3:
            rozwiązanie = input()
            if rozwiązanie == "maly czerwony trojkat":
                bohater.dodaj_mora(50)
                print("Poprawna odpowiedź")
                proby += 3
            else:
                print("Zła odpowiedź!")
                proby += 1
                if proby == 3:
                    bohater.hp -= 50
                    print("Tracisz 50hp")
        lista.remove("trójkąt")
    elif wybor_zagadki == "deszcz":
        print("Jeśli troje dzieci i ich trzy psy nie znajdowało się pod parasolem, to jak to się stało, że żadne z nich nie zmokło?")
        while proby < 3:
            rozwiązanie = input()
            if rozwiązanie == "nie padalo":
                bohater.dodaj_mora(50)
                print("Poprawna odpowiedź")
                proby += 3
            else:
                print("Zła odpowiedź!")
                proby += 1
                if proby == 3:
                    bohater.hp -= 50
                    print("Tracisz 50hp")
        lista.remove("deszcz")
    elif wybor_zagadki == "koty":
        print("W pokoju są 4 kąty i kilka kotów. Każdy z kotów widzi pozostałe koty w trzech pozostałych kątach pokoju. Ile jest kotów?")
        while proby < 3:
            rozwiązanie = input()
            if rozwiązanie == "4":
                bohater.dodaj_mora(50)
                print("Poprawna odpowiedź")
                proby += 3
            else:
                print("Zła odpowiedź!")
                proby += 1
                if proby == 3:
                    bohater.hp -= 50
                    print("Tracisz 50hp")
        lista.remove("koty")
    elif wybor_zagadki == "talia kart":
        print("Co ma 13 serc, ale żadnych innych organów?")
        while proby < 3:
            rozwiązanie = input()
            if rozwiązanie == "talia kart":
                bohater.dodaj_mora(50)
                print("Poprawna odpowiedź")
                proby += 3
            else:
                print("Zła odpowiedź!")
                proby += 1
                if proby == 3:
                    bohater.hp -= 50
                    print("Tracisz 50hp")
        lista.remove("talia kart")
