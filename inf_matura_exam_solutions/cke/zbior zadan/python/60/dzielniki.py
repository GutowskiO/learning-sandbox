import math



def wczytaj_dane(plik):
    odczyt = open(plik, 'r')
    dane = odczyt.readlines()
    odczyt.close()
    for a in range(len(dane)):
        dane[a] = int(dane[a].strip())
    return dane
dane = wczytaj_dane("liczby.txt")

def zad_60_1(dane):
    wynik = open("wyniki.txt", "w")

    mniejsze_od_1000 = 0
    mniejsze = []
    for a in range(len(dane)):
        if dane[a] < 1000:
            mniejsze_od_1000 += 1
            mniejsze.append(dane[a])

    wynik.write("60.1\nMniejsze o 1000: "+str(mniejsze_od_1000) + "\nDwie ostatnie liczby:\n" + str(mniejsze[len(mniejsze)-2]))
    wynik.write("\n"+str(mniejsze[len(mniejsze)-1])            )
    wynik.close()

zad_60_1(dane)

#def znajdz_dzielniki(liczba):
 #   dzielniki = []
  #  for a in range(1, liczba+1):
   #     if liczba % a == 0:
   #        dzielniki.append(a)

   # return dzielniki

def znajdz_dzielniki(liczba):
    dzielniki = []
    for a in range(1, int(math.sqrt(liczba))+1):
        if liczba % a == 0:
           dzielniki.append(a)
           if a != (liczba // a):
               dzielniki.append(liczba // a)


    return sorted(dzielniki)




def zad_60_2(dane):
    wynik = open("wyniki.txt", "a")
    wynik.write("\n60.2\n")
    for a in range(len(dane)):
        liczba = dane[a]
        dzielniki = znajdz_dzielniki(liczba)
        if len(dzielniki) == 18:
            wynik.write(str(liczba))
            wynik.write("\n")
            for b in range(len(dzielniki)):
                wynik.write(str(dzielniki[b])+" ")
            wynik.write("\n")
    wynik.close()

zad_60_2(dane)

def czy_posiadaja_wspolne_dzielniki(liczba_1, liczba_2):
    dzielniki_1 = znajdz_dzielniki(liczba_1)
    dzielniki_2 = znajdz_dzielniki(liczba_2)
    for a in range(1, len(dzielniki_1)):
        dzielnik_1 = dzielniki_1[a]

        for b in range(1,len(dzielniki_2)):
            dzielnik_2 = dzielniki_2[b]

            if dzielnik_1 == dzielnik_2:
                return True
    return False




def zad_60_3(dane):
    wynik = open("wyniki.txt", "a")

    najwieksza_w = 0

    for a in range(len(dane)):
        sprawdzana = dane[a]
        for b in range(a, len(dane)):
            if a == b:
                continue
            srodkowa = dane[b]
            if not czy_posiadaja_wspolne_dzielniki(sprawdzana,srodkowa):
                if b == len(dane)-1:
                    if dane[a] > najwieksza_w:
                        najwieksza_w = dane[a]
                continue
            else:
                break
    wynik.write("\n60.3\n"+str(najwieksza_w))
zad_60_3(dane)