def wczytaj_dane(plik):
    odczyt = open(plik,"r")
    dane = odczyt.readlines()

    for a in range(len(dane)):
        dane[a] = dane[a].strip()

    return dane

osemkowe = wczytaj_dane("liczby1.txt")
dziesietne = wczytaj_dane("liczby2.txt")

def zad_62_1(osemkowe):
    wynik = open("wyniki.txt","w")
    najmniejsza = osemkowe[0]
    najwieksza = osemkowe[0]

    for a in range(len(osemkowe)):
        if int(osemkowe[a],8) > int(najwieksza,8):
            najwieksza = osemkowe[a]
        if int(osemkowe[a],8) < int(najmniejsza,8)    :
            najmniejsza = osemkowe[a]
    wynik.write("62.1\n"+str(najmniejsza)+"\n"+str(najwieksza)+"\n")
    wynik.close()

zad_62_1(osemkowe)

def zad_62_2(dziesietne):
    wynik = open("wyniki.txt","a")
    for b in range(len(dziesietne)):
        dziesietne[b] = int(dziesietne[b])
    poczatek = dziesietne[0]
    najdluzsza = 1
    sprawdzany_poczatek = dziesietne[0]
    sprawdzana_dlugosc = 1
    for a in range(1, len(dziesietne)):
        if dziesietne[a] >= dziesietne[a-1]:
            sprawdzana_dlugosc += 1
        else:
            if sprawdzana_dlugosc > najdluzsza:
                poczatek = sprawdzany_poczatek
                najdluzsza = sprawdzana_dlugosc
            sprawdzana_dlugosc = 1
            sprawdzany_poczatek = dziesietne[a]
    wynik.write("62.2\n"+str(poczatek)+"\n"+str(najdluzsza)+"\n")
    wynik.close()
zad_62_2(dziesietne)

def zad_62_3(osemkowe, dziesietne):
    wynik = open("wyniki.txt","a")
    for a in range(len(osemkowe)):
        osemkowe[a] = int(osemkowe[a],8)
        dziesietne[a] = int(dziesietne[a])

    taka_sama = 0
    l1wieksza = 0

    for b in range(len(osemkowe)):
        if osemkowe[b] == dziesietne[b]:
            taka_sama += 1
        if osemkowe[b] > dziesietne[b]:
            l1wieksza += 1
    wynik.write("62.3\na)"+str(taka_sama)+"\nb)"+str(l1wieksza)+"\n")
    wynik.close()
zad_62_3(osemkowe, dziesietne)

def dziesietne_to_osemkowe(dziesietna):
    osemkowa = ""

    while dziesietna != 0:
        osemkowa = str((dziesietna % 8)) + osemkowa
        dziesietna //= 8
    return osemkowa


def policz_6(liczba):

    wynik = 0
    for a in range(len(liczba)):
        if liczba[a] == "6":
            wynik += 1
    return wynik


def zad_62_4(dziesietne):
    wynik = open("wyniki.txt","a")
    dzies = 0
    po_osemkowe = 0

    for a in range(len(dziesietne)):
        dzies += policz_6(str(dziesietne[a]))
        po_osemkowe += policz_6(dziesietne_to_osemkowe(dziesietne[a]))
    wynik.write("62.4\n"+str(po_osemkowe)+"\n"+str(dzies)+"\n")
    wynik.close()


zad_62_4(dziesietne)