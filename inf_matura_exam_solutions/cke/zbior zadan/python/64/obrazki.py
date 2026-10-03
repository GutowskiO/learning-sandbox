

def wczytaj_dane(plik):
    odczyt = open(plik, 'r')
    dane = odczyt.readlines()
    obrazki = []
    linia = 0

    while linia < 4400:
        ciagi = []

        for a in range(linia, linia+21):

            ciagi.append(dane[a].strip())
        obrazki.append(ciagi)

        linia += 22
    return obrazki

dane = wczytaj_dane("dane_obrazki.txt")



def rewers(obrazek):
    czarne = 0
    biale = 0

    for a in range(20):
        for b in range(20):
            if obrazek[a][b] == "1":
                czarne += 1
            else:
                biale += 1

    if czarne > biale:
        return True
    return False
def policz_czarne(obrazek):
    czarne = 0
    biale = 0

    for a in range(20):
        for b in range(20):
            if obrazek[a][b] == "1":
                czarne += 1
            else:
                biale += 1

    return czarne

def zad_64_1(dane):

    wynik = open("wyniki_obrazki.txt","w")
    l_rewersow = 0
    najwiecej_cz = 0
    for obrazek in dane:
        czarne = policz_czarne(obrazek)
        if czarne > najwiecej_cz:
            najwiecej_cz = czarne
        if rewers(obrazek):
            l_rewersow += 1
    wynik.write("64.1\n"+str(l_rewersow) + "\n"+str(najwiecej_cz)+"\n")
    wynik.close()


zad_64_1(dane)

def czy_rek(obrazek):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    for a in range(10):
        for e in range(10):
            k1.append(obrazek[a][e])
    for b in range(10):
        for f in range(10,20):
            k2.append(obrazek[b][f])
    for c in range(10,20):
        for g in range(10):
            k3.append(obrazek[c][g])
    for d in range(10,20):
        for h in range(10,20):
            k4.append(obrazek[d][h])

    if k1 == k2 == k3 == k4:
        return True
    return False



def zad_64_2(dane):

    wynik = open("wyniki_obrazki.txt","a")
    liczba_obrazkow = 0
    for obrazek in dane:
        if czy_rek(obrazek):
            liczba_obrazkow +=1
    wynik.write("64.2\n"+str(liczba_obrazkow)+"\n")
    wynik.close()
zad_64_2(dane)

def sprawdz_czy_bit_poprawny(bit, ciag):
    liczba_0 = 0
    liczba_1 = 0

    for element in ciag:
        if element == "0":
            liczba_0 += 1
        if element == "1":
            liczba_1 += 1

    if bit == "1":
        if liczba_1 % 2 != 0:
            return True
        else:
            return False
    if liczba_1 % 2 == 0:
        return True
    return False

#print(sprawdz_czy_bit_poprawny("0",["0,0,1,1,1,1,0"]))

def zad_64_3(dane):
    wynik = open("wyniki_obrazki.txt","a")
    l_poprawnych = 0
    l_do_naprawy = 0
    l_niepoprawnych = 0




    for obrazek in dane:

        bity_w = []
        wiersze = []
        ciagi_w = []
        for wiersz in obrazek:
            wiersze.append(wiersz)

        kolumnowe_ciagi = []
        for b in range(20):
            kolumnowe_ciagi.append([])


        for w in wiersze:
            if len(w) < 21:
                continue



            ciag_w = []
            for a in range(20):

                ciag_w.append(w[a])

                kolumnowe_ciagi[a].append(w[a])
            bity_w.append(w[20])
            ciagi_w.append(ciag_w)
        bity_k =wiersze[20]

        l_bledow_kolumn = 0
        l_bledow_wierszy = 0
        for c in range(20):
            if not sprawdz_czy_bit_poprawny(bity_w[c], ciagi_w[c]):
                l_bledow_wierszy += 1
            if not sprawdz_czy_bit_poprawny(bity_k[c],kolumnowe_ciagi[c]):
                l_bledow_kolumn += 1


        if l_bledow_kolumn == 0 and l_bledow_wierszy == 0:
            l_poprawnych += 1
            continue
        if l_bledow_kolumn <= 1 and l_bledow_wierszy <= 1:
            l_do_naprawy += 1
            continue
        if l_bledow_kolumn > 1 or l_bledow_wierszy > 1:
            l_niepoprawnych += 1



    print(l_poprawnych)
    print(l_niepoprawnych)
    print(l_do_naprawy)



zad_64_3(dane)

def zad_64_4(dane):
    wynik = open("wyniki_obrazki.txt", "a")

    nr = 1  # numer obrazka (od 1)

    for obrazek in dane:

        bity_w = []
        ciagi_w = []
        kolumnowe_ciagi = [[] for _ in range(20)]

        # budowanie danych
        for wiersz in obrazek:
            if len(wiersz) < 21:
                continue

            ciag = []
            for i in range(20):
                ciag.append(wiersz[i])
                kolumnowe_ciagi[i].append(wiersz[i])

            bity_w.append(wiersz[20])
            ciagi_w.append(ciag)

        bity_k = obrazek[20]

        # szukanie błędnych wierszy i kolumn
        bledne_wiersze = []
        bledne_kolumny = []

        for i in range(20):
            if not sprawdz_czy_bit_poprawny(bity_w[i], ciagi_w[i]):
                bledne_wiersze.append(i)

            if not sprawdz_czy_bit_poprawny(bity_k[i], kolumnowe_ciagi[i]):
                bledne_kolumny.append(i)

        # sprawdzamy czy naprawialny
        if len(bledne_wiersze) <= 1 and len(bledne_kolumny) <= 1:

            # przypadek: 1 wiersz i 1 kolumna
            if len(bledne_wiersze) == 1 and len(bledne_kolumny) == 1:
                w = bledne_wiersze[0] + 1
                k = bledne_kolumny[0] + 1
                wynik.write(f"{nr} {w} {k}\n")

            # przypadek: tylko wiersz
            elif len(bledne_wiersze) == 1:
                w = bledne_wiersze[0] + 1
                wynik.write(f"{nr} {w} 21\n")

            # przypadek: tylko kolumna
            elif len(bledne_kolumny) == 1:
                k = bledne_kolumny[0] + 1
                wynik.write(f"{nr} 21 {k}\n")

        nr += 1

    wynik.close()

zad_64_4(dane)