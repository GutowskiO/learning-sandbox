def wczytaj_dane(plik):
    odczyt = open(plik,"r")
    dane = odczyt.readlines()
    pierwsze = dane[0]
    drugie = dane[1]

    pierwsze = pierwsze.split(" ")
    drugie = drugie.split(" ")
    for a in range(len(pierwsze)):
        pierwsze[a] = int(pierwsze[a])
    for b in range(len(drugie)):
        drugie[b] = int(drugie[b])

    return pierwsze, drugie
pierwsze, drugie = wczytaj_dane("liczby_przyklad.txt")

def czy_b_jest_dzielnikiem_a(a, b):
    if a % b == 0:
        return True
    else:
        return False

def zad_4_1(pierwsze, drugie):
    wynik = open("wyniki4.txt","w")
    w = 0
    for a in range(len(pierwsze)):
        for b in range(len(drugie)):
            if czy_b_jest_dzielnikiem_a(drugie[b], pierwsze[a]):
                w += 1
                break
    wynik.write("4.1\n"+str(w))
    wynik.close()
zad_4_1(pierwsze, drugie)
def zad_4_2(pierwsze):
    wynik = open("wyniki4.txt", "a")
    pierwsze.sort()
    pierwsze.reverse()

    w = 0
    for a in range(len(pierwsze)):
        if a == 100:
            w = pierwsze[a]
    wynik.write("\n\n4.2\n"+str(w))
    wynik.close()
zad_4_2(pierwsze)

def zad_4_3(pierwsze, drugie):
    wynik = open("wyniki4.txt","a")

    w = []
    for a in range(len(drugie)):
        sprawdzana = drugie[a]
        for b in range(len(pierwsze)):
            if sprawdzana % pierwsze[b] == 0:
                sprawdzana //= pierwsze[b]
        if sprawdzana == 1:
            w.append(drugie[a])
    wynik.write("\n\n4.3\n")
    for liczba in w:
        wynik.write(str(liczba)+" ")
    wynik.close()


zad_4_3(pierwsze, drugie)

def wczytaj_dane(plik):
    odczyt = open(plik,"r")
    dane = odczyt.readlines()
    pierwsze = dane[0]
    drugie = dane[1]

    pierwsze = pierwsze.split(" ")
    drugie = drugie.split(" ")
    for a in range(len(pierwsze)):
        pierwsze[a] = int(pierwsze[a])
    for b in range(len(drugie)):
        drugie[b] = int(drugie[b])

    return pierwsze, drugie
pierwsze, drugie = wczytaj_dane("liczby_przyklad.txt")

def zad_4_4(pierwsze):
    wynik = open("wyniki4.txt", "a")
    najwieksza_srednia = 0
    poczatek_najwiekszego = 0
    dlugosc_najwiekszego = 0
    for a in range(len(pierwsze)):
        poczatek = pierwsze[a]
        dlugosc = 0
        suma = 0
        srednia = 0
        for b in range(a,len(pierwsze)):
           suma += pierwsze[b]
           dlugosc += 1
           if dlugosc >= 50:
               srednia = suma/dlugosc
               if srednia > najwieksza_srednia:
                   najwieksza_srednia = srednia
                   dlugosc_najwiekszego = dlugosc
                   poczatek_najwiekszego = poczatek
    wynik.write("\n\n4.4\n"+str(najwieksza_srednia)+" "+str(dlugosc_najwiekszego)+ " "+str(poczatek_najwiekszego)+"\n")
    wynik.close()




zad_4_4(pierwsze)