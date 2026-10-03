def wczytaj_dane(plik):
    odczyt = open(plik, 'r')
    dane = odczyt.readlines()
    for a in range(len(dane)):
        dane[a] = dane[a].split(" ")
        dane[a][0] = int(dane[a][0].strip())
        dane[a][1]= int(dane[a][1].strip())
    return dane

dane = wczytaj_dane("dron.txt")

def nwd(a, b):
    nwd = 1

    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:
            nwd = i
    return nwd

def zad_3_1(dane):
    wynik = open("wyniki3.txt", "w")
    w = 0
    for a in range(len(dane)):
        if nwd(abs(dane[a][0]), abs(dane[a][1])) > 1:
            w += 1
    wynik.write("3.1\n"+str(w) + "\n")
    wynik.close()
zad_3_1(dane)

def zad_3_2(dane):
    wynik = open("wyniki3.txt", "a")
    w = 0
    lok = [0,0]
    pkt = []
    for a in range(len(dane)):
        lok[0] += dane[a][0]
        lok[1] += dane[a][1]
        if lok[0] > 0 and lok[1] > 0 and lok[0] < 5000 and lok[1] < 5000:
            w += 1
        pkt.append([lok[0], lok[1]])
    for b in range(len(pkt)):
        srodek = pkt[b]
        for c in range(len(pkt)):

            lewo = pkt[c]
            for d in range(len(pkt)):

                prawo = pkt[d]

                if (srodek[0] == (lewo[0] + prawo[0])/2) and (srodek[1] == (lewo[1] + prawo[1])/2) and b!=c and d!=b and d!=c:
                    wynik.write("3.2\n(" + str(lewo[0]) + ") (" + str(lewo[1]) + ")\n")
                    wynik.write("("+str(srodek[0]) + ") (" + str(srodek[1]) + ")\n")
                    wynik.write("(" + str(prawo[0]) + ") (" + str(prawo[1]) + ")\n")
                    wynik.close()
                    return





zad_3_2(dane)
