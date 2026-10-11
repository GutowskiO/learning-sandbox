import math


def wczytaj_dane(plik):
    odczyt = open(plik,"r")
    dane = odczyt.readlines()

    for a in range(len(dane)):
        dane[a] = dane[a].strip().split(" ")
    odczyt.close()
    return dane

s1 = wczytaj_dane("dane_systemy1.txt")
s2 = wczytaj_dane("dane_systemy2.txt")
s3 = wczytaj_dane("dane_systemy3.txt")

def dec_to_bin(liczba):
    liczba = int(liczba)
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba = liczba//2

    return wynik

def zad_58_1(s1,s2,s3):
    wynik = open("wyniki_systemy.txt","w")
    najnizszas1 = s1[0][1]
    najnizszas2 = s2[0][1]
    najnizszas3 = s3[0][1]



    for a in range(len(s1)):
        wartosc = int(s1[a][1],2)
        if wartosc < int(najnizszas1):
            najnizszas1 = wartosc
    for b in range(len(s2)):
        wartosc = int(s2[b][1],4)
        if wartosc < int(najnizszas2):
            najnizszas2 = wartosc
    for c in range(len(s3)):
        wartosc = int(s3[c][1],8)
        if wartosc < int(najnizszas3):
            najnizszas3 = wartosc
    najnizszas1 = dec_to_bin(str(-najnizszas1))
    najnizszas2 = dec_to_bin(str(-najnizszas2))
    najnizszas3 = dec_to_bin(str(-najnizszas3))


    wynik.write("58.1\n-"+str(najnizszas1)+"\n"+"-"+str(najnizszas2)+"\n"+"-"+str(najnizszas3)+"\n")
    wynik.close()

zad_58_1(s1,s2,s3)

def zad_58_2(s1,s2,s3):
    wynik = open("wyniki_systemy.txt","a")
    harmongram = 12
    s1_aktualna = 12
    s2_aktualna = 12
    s3_aktualna = 12

    liczba_pomiarow = 0

    for a in range(1, len(s1)):
        harmongram += 24
        s1_aktualna = int(s1[a][0], 2)
        s2_aktualna = int(s2[a][0], 4)
        s3_aktualna = int(s3[a][0], 8)
        if s1_aktualna != harmongram and s2_aktualna != harmongram and s3_aktualna != harmongram:
            liczba_pomiarow += 1
    wynik.write("\n58.2\n"+str(liczba_pomiarow)+"\n")
    wynik.close()

zad_58_2(s1,s2,s3)

def zad_58_3(s1,s2,s3):
    wynik = open("wyniki_systemy.txt","a")
    s1max = int(s1[0][1], 2)
    s2max = int(s2[0][1], 4)
    s3max = int(s3[0][1], 8)

    liczba_dni_rekordowych = 1


    for a in range(1, len(s1)):
        czy_rekord = False
        s1_aktualna = int(s1[a][1], 2)
        s2_aktualna = int(s2[a][1], 4)
        s3_aktualna = int(s3[a][1], 8)

        if s1_aktualna > s1max:

            s1max = s1_aktualna

            czy_rekord = True


        if s2_aktualna > s2max:
            s2max = s2_aktualna
            czy_rekord = True

        if s3_aktualna > s3max:
            s3max = s3_aktualna
            czy_rekord = True

        if czy_rekord:
            liczba_dni_rekordowych +=1


    wynik.write("\n58.3\n"+str(liczba_dni_rekordowych)+"\n")
    wynik.close()

zad_58_3(s1,s2,s3)

def zad_58_4(s1):
    wynik = open("wyniki_systemy.txt","a")
    najwiekszy_skok = 0
    for a in range(len(s1)):
        ti = int(s1[a][1],2)
        for b in range(1, len(s1)):
            tj = int(s1[b][1], 2)
            r = (ti - tj) * (ti - tj)
            if a-b == 0:
                continue
            skok = (r/ (abs(a-b) ) )
            if skok > najwiekszy_skok:

                najwiekszy_skok = skok
    najwiekszy_skok = math.ceil(najwiekszy_skok)
    wynik.write("\n58.4\n"+str(najwiekszy_skok)+"\n")



zad_58_4(s1)

