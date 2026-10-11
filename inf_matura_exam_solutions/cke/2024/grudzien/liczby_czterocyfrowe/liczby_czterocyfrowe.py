from math import sqrt


def wczytaj_dane(plik):
    odczyt = open(plik, "r")
    dane = odczyt.readlines()

    for a in range(len(dane)):
        dane[a] = int(dane[a].strip())
    return dane
dane = wczytaj_dane("liczby.txt")

def czy_kwadrat(liczba):
    for a in range(1, int(sqrt(liczba))+1):
        if a*a == liczba:
            return True
    return False

def zad_3_1(dane):
    wynik = open("wyniki3.txt", "w")
    liczby_w = []
    for liczba in dane:
        if czy_kwadrat(liczba):
            liczby_w.append(liczba)
    wynik.write("3.1\n"+str(len(liczby_w))+"\n"+str(liczby_w[0])+"\n")

zad_3_1(dane)

def ile_dzielnikow(liczba):
    dzielniki = []
    a = 2
    while liczba > 1:

        if liczba % a == 0:
            dzielniki.append(a)
            while liczba % a == 0:
                liczba //= a

        a += 1
    return dzielniki

def zad_3_2(dane):
    wynik = open("wyniki3.txt", "a")
    liczby_w = []
    for liczba in dane:

        if len(ile_dzielnikow(liczba)) >= 5:
            liczby_w.append(liczba)

    wynik.write("3.2\n")
    for w in liczby_w:
        wynik.write(str(w)+"\n")

zad_3_2(dane)


def obroc_w_najmniejsza(liczba):
    liczba = str(liczba)
    l_t = []
    for a in range(len(liczba)):
        l_t.append(int(liczba[a]))
    l_t.sort()
    nowa_l = ""
    for element in l_t:
        nowa_l += str(element)
    nowa_l = int(nowa_l)
    print(nowa_l)
    return nowa_l

def obroc_w_najmniejsza(liczba):
    liczba = str(liczba)
    l_t = []
    for a in range(len(liczba)):
        l_t.append(int(liczba[a]))
    l_t.sort()
    nowa_l = ""
    for element in l_t:
        nowa_l += str(element)
    nowa_l = int(nowa_l)

    return nowa_l

def obroc_w_najwieksza(liczba):
    liczba = str(liczba)
    l_t = []
    for a in range(len(liczba)):
        l_t.append(int(liczba[a]))
    l_t.sort()
    obrocona_l_t = []
    for b in range(len(l_t)-1,-1,-1):
        obrocona_l_t.append(l_t[b])

    nowa_l = ""
    for element in obrocona_l_t:
        nowa_l += str(element)
    nowa_l = int(nowa_l)

    return nowa_l

def zad_3_3(dane):
    wynik = open("wyniki3.txt", "a")
    roznica_mniejsza = 0
    roznica_wieksza = 0
    roznica_rowna = 0
    rowne = []

    for element in dane:
        najwieksza = obroc_w_najwieksza(element)
        najmniejsza = obroc_w_najmniejsza(element)
        if najwieksza - najmniejsza == element:
            roznica_rowna += 1
            rowne.append(element)
        if najwieksza - najmniejsza > element:
            roznica_wieksza += 1
        if najwieksza - najmniejsza < element:
            roznica_mniejsza += 1
    wynik.write("3.3\n"+str(roznica_mniejsza)+"\n"+str(roznica_wieksza)+"\n"+str(roznica_rowna)+"\n")
    for liczba in rowne:
        wynik.write(str(liczba)+"\n")
zad_3_3(dane)