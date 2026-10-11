def wczytaj_dane(plik):
    odczyt = open(plik, 'r')
    dane = odczyt.readlines()

    for a in range(len(dane)):
        dane[a] = dane[a].strip().split(" ")

    return dane

dane = wczytaj_dane("prostokaty.txt")

def zad_4_1(dane):
    wynik = open("wyniki4.txt", "w")
    najwieksze = 0
    najmniejsze = int(dane[0][0]) * int(dane[0][1])

    for wymiary in dane:
        pole = int(wymiary[0]) * int(wymiary[1])
        if pole > najwieksze:
            najwieksze = pole
        if pole < najmniejsze:
            najmniejsze = pole
    wynik.write("4.1\n"+str(najmniejsze) + "\n"+str(najwieksze)+"\n")


zad_4_1(dane)

def zad_4_2(dane):
    wynik = open("wyniki4.txt", "a")
    dlugosc = 0
    ostatni_element = dane[0]
    aktualna_dlugosc = 1
    aktualny_ostatni = []
    for a in range(1, len(dane)):
        if (int(dane[a-1][0]) >= int(dane[a][0])) and (int(dane[a-1][1]) >= int(dane[a][1])):

            aktualna_dlugosc += 1
            aktualny_ostatni = dane[a]
        else:
            if aktualna_dlugosc > dlugosc:
                dlugosc = aktualna_dlugosc
                ostatni_element = aktualny_ostatni

            aktualna_dlugosc = 1
    wynik.write("4.2\n"+str(dlugosc) + " "+str(ostatni_element[0])+" "+str(ostatni_element[1])+"\n")

zad_4_2(dane)

def zad_4_3(dane):
    wynik = open("wyniki4.txt", "a")
    wysokosci = []
    podstawy = []
    l_podstaw = -1

    for a in range(len(dane)):

        wysokosc = dane[a][0]
        if wysokosc in wysokosci:
            continue
        wysokosci.append(wysokosc)
        podstawy.append([])
        l_podstaw += 1
        for b in range(len(dane)):
            if dane[b][0] == wysokosc:
                podstawy[l_podstaw].append(dane[b][1])

    nowe_podstawy = []
    for lista in podstawy:
        lista.sort()
        rosnaca = []
        for d in range(len(lista)-1,-1,-1):
            rosnaca.append(lista[d])
        nowe_podstawy.append(rosnaca)


    po_sklejeniu_2 = 0
    po_sklejeniu_3 = 0
    po_sklejeniu_5 = 0
    sumy_2 = []
    sumy_3 = []
    sumy_5 = []

    for elementy in nowe_podstawy:
        if len(elementy) >=2:
            sumy_2.append(int(elementy[0])+int(elementy[1]))
        if len(elementy) >= 3:
            sumy_3.append(int(elementy[0]) + int(elementy[1])+int(elementy[2]))
        if len(elementy) >= 5:
            sumy_5.append(int(elementy[0]) + int(elementy[1])+int(elementy[2])+ int(elementy[3])+int(elementy[4]))
    wynik.write("4.3\n")
    n_2 = 0
    n_3 = 0
    n_5 = 0
    for z in range(len(sumy_2)):
        if sumy_2[z] > n_2:
            n_2 = sumy_2[z]
    for x in range(len(sumy_3)):
        if sumy_3[x] > n_3:
            n_3 = sumy_3[x]
    for y in range(len(sumy_5)):
        if sumy_5[y] > n_5:
            n_5 = sumy_5[y]
    wynik.write(str(n_2)+" "+str(n_3)+" "+str(n_5)+"\n")

zad_4_3(dane)