def wczytaj_dane(plik):
    odczyt = open(plik,"r")
    dane = odczyt.readlines()
    odczyt.close()
    for a in range(len(dane)):
        dane[a] = int(dane[a].strip())
    return dane

dane = wczytaj_dane("liczby.txt")



def zlicz_unikalne_czynniki(liczba):
    sprawdzana = liczba
    czynnik = 2
    liczba_czynnikow = 0

    while czynnik*czynnik<=liczba:

        if sprawdzana % czynnik == 0:
            liczba_czynnikow += 1
            print(czynnik)

            while sprawdzana % czynnik == 0:
                sprawdzana //= czynnik


        czynnik += 1
    if sprawdzana > 1:
        sprawdzana += 1

    return liczba_czynnikow

print(zlicz_unikalne_czynniki(13150087))

def zad_59_1(dane):
    wynik = open("wyniki_liczby.txt","w")
    wynikowy = 0

    for a in range(len(dane)):
        liczba = dane[a]

        if liczba % 2 != 0:

            l_czynnikow = zlicz_unikalne_czynniki(liczba)

            if l_czynnikow == 3:
                print(liczba)
                wynikowy += 1
    wynik.write("59.1\n"+str(wynikowy)+"\n")
    wynik.close()

#zad_59_1(dane)

#wynik = open("wyniki_liczby.txt","w")
#wynik.close()

def odwroc(liczba):
    liczba = str(liczba)
    odwrocona = ""
    for a in range(len(liczba)):
        odwrocona = liczba[a] + odwrocona
    return odwrocona
def czy_palindrom(liczba):
    if str(liczba) == odwroc(liczba):
        return True
    return False

def zad_59_2(dane):
    wynik = open("wyniki_liczby.txt","a")

    sumy = 0

    for a in range(len(dane)):
        liczba = dane[a]
        suma = liczba + int(odwroc(liczba))

        if czy_palindrom(suma):
            sumy += 1

    wynik.write("59.2\n"+str(sumy)+"\n")
    wynik.close()
zad_59_2(dane)

def policz_moc_liczby(liczba):
    liczba = str(liczba)
    moc = 0

    while len(liczba)>1:
        testowana = liczba

        nowa = 1
        for cyfra in testowana:
            nowa *= int(cyfra)
        liczba = str(nowa)
        moc += 1
    return moc
def zad_59_3(dane):
    wynik = open("wyniki_liczby.txt", "a")
    min_1 = dane[0]
    max_1 = dane[0]
    moce = []
    for b in range(8):
        moce.append(0)

    for liczba in dane:
        moc = policz_moc_liczby(liczba)
        if moc == 1:
            if min_1 > liczba:
                min_1 = liczba
            if max_1 < liczba:
                max_1 = liczba
        moce[moc-1] += 1
    wynik.write("59.3\n")
    for a in range(len(moce)):
        wynik.write(str(a+1)+" "+str(moce[a])+"\n")


    wynik.write("najmniejsza\n"+str(min_1)+"\nnajwieksza\n"+str(max_1)+"\n")
    wynik.close()




zad_59_3(dane)





