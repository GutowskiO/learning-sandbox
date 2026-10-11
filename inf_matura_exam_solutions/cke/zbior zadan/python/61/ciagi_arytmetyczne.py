def wczytaj_dane(plik):
    odczyt = open(plik,"r")
    dane = odczyt.readlines()
    odczyt.close()
    ciagi = []
    for a in range(len(dane)):
        if a % 2 != 0:
            ciagi.append(dane[a].split(" "))
    for b in range(len(ciagi)):
       for c in range(len(ciagi[b])):
           ciagi[b][c] = int(ciagi[b][c].strip())
    return ciagi

dane = wczytaj_dane("ciagi.txt")
bledne = wczytaj_dane("bledne.txt")

def czy_arytmetyczny(ciag):
    roznica = ciag[1] - ciag[0]
    for a in range(1, len(ciag)):
        if ciag[a] - ciag[a-1] != roznica:
            return False
    return True

def roznica_ciagu(ciag):
    roznica = ciag[1] - ciag[0]
    return roznica
def zad_61_1(dane):
    wynik = open("wynik1.txt","w")

    arytmetyczne = 0
    naj_roznica = 0
    for a in range(len(dane)):
        if czy_arytmetyczny(dane[a]):
            arytmetyczne += 1
            roznica = roznica_ciagu(dane[a])
            if roznica> naj_roznica:
                naj_roznica = roznica
    wynik.write(str(arytmetyczne)+"\n"+str(naj_roznica))
    wynik.close()
zad_61_1(dane)

def szescian_jakiej_liczby(liczba):
    czynnik = 1

    while czynnik**3<=liczba:
        if liczba == czynnik**3:
            return czynnik
        czynnik += 1
    return 0

def zad_61_2(dane):
    wynik = open("wynik2.txt","w")
    podstawy = []
    for a in range(len(dane)):
        najwieksza = 0
        for b in range(len(dane[a])):
            if szescian_jakiej_liczby(dane[a][b]) > najwieksza:
                najwieksza = szescian_jakiej_liczby(dane[a][b])
        if najwieksza >0:
            podstawy.append(najwieksza)
    for c in range(len(podstawy)):
        wynik.write(str(podstawy[c]**3)+"\n")
    wynik.close()
zad_61_2(dane)

def znajdz_bledna(ciag):

    roznice = []
    wystapienia = []

    for a in range(1, len(ciag)):
        roznica = ciag[a] - ciag[a-1]
        if roznica not in roznice:
            roznice.append(roznica)
            wystapienia.append(1)
        else:
            for b in range(len(roznice)):
                if roznice[b] == roznica:
                    wystapienia[b] += 1

    poprawna = 0

    najczestsza = 0
    for e in range(len(roznice)):
        if wystapienia[e] > najczestsza:
            najczestsza = wystapienia[e]
            poprawna  = roznice[e]


    for d in range(2, len(ciag)):
        roznica = ciag[d] - ciag[d - 1]
        if ciag[1] - ciag[0] != poprawna:
            if roznica != poprawna:
                return ciag[1]
            else:
                return ciag[0]


        if roznica != poprawna:

            if ciag[d-1] - ciag[d-2] != poprawna:
                return ciag[d-1]
            else:
                return ciag[d]


def zad_61_3(bledne):

    wynik = open("wynik3.txt","w")
    wynikowe = []
    for a in range(len(bledne)):
        bledna = znajdz_bledna(bledne[a])
        wynikowe.append(bledna)
    for b in range(len(wynikowe)):
        wynik.write(str(wynikowe[b])+"\n")

zad_61_3(bledne)