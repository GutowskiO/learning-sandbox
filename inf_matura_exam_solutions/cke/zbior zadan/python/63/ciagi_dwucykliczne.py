def wczytaj_dane(plik):
    odczyt = open(plik, "r")
    dane = odczyt.readlines()

    for a in range(len(dane)):
        dane[a] = dane[a].strip()
    return dane
dane = wczytaj_dane("ciagi.txt")

def czy_dwucykliczny(ciag):
    if len(ciag) % 2 != 0:
        return False

    polowa_1 = ""
    polowa_2 = ""
    polowa = len(ciag) // 2
    for a in range(polowa):
        polowa_1 += ciag[a]

    for b in range(polowa, len(ciag)):
        polowa_2 += ciag[b]

    if polowa_1 == polowa_2:
        return True
    return False


def zad_63_1(dane):
    wynik = open("wynik_ciagi.txt", "w")

    dwucykliczne = []
    for a in range(len(dane)):
        if czy_dwucykliczny(dane[a]):
            dwucykliczne.append(dane[a])
    wynik.write("63.1\n")
    for b in range(len(dwucykliczne)):
        wynik.write(dwucykliczne[b] + "\n")
    wynik.close()

zad_63_1(dane)

def czy_nie_wystepuje_obok_dwie_jedynki(ciag):
    if ciag[0] == "1" and ciag[1] == "1":
        return False
    for a in range(1,len(ciag)-1):
        if ciag[a] == "1":
            if ciag[a+1] == "0" and ciag[a-1] == "0":
                continue
            else:
                return False
    return True

def zad_63_2(dane):
    wynik = open("wynik_ciagi.txt", "a")

    liczba_ciagow = 0

    for a in range(len(dane)):
        if czy_nie_wystepuje_obok_dwie_jedynki(dane[a]):
            liczba_ciagow+=1
    wynik.write("63.2\n"+str(liczba_ciagow) + "\n")

    wynik.close()
zad_63_2(dane)

def czy_l_pierwsza(liczba):
    if liczba <=1:
        return False
    czynnik = 2
    while czynnik*czynnik<=liczba:

        if liczba % czynnik == 0:
            return False
        czynnik += 1
    return True



def czy_polpierwsza(liczba):

    for a in range(2, liczba):
        if liczba % a == 0:

            if czy_l_pierwsza(a) and czy_l_pierwsza(liczba//a):
                return True
            return False
    return False

def zad_63_3(dane):
    wynik = open("wynik_ciagi.txt", "a")
    liczba_ciagow = 0
    najmniejsza = int(dane[0],2)
    najwieksza = int(dane[0],2)
    for a in range(len(dane)):

        liczba = int(dane[a],2)

        if czy_polpierwsza(liczba):
            liczba_ciagow += 1
            if liczba > najwieksza:
                najwieksza = liczba
            if liczba < najmniejsza:
                najmniejsza = liczba
    wynik.write("63.3\n"+str(liczba_ciagow) + "\n"+str(najwieksza) + "\n"+str(najmniejsza) + "\n")
    wynik.close()


zad_63_3(dane)