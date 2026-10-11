def nieparzysty_skrot(n):
    w = 0
    tura = 1
    while n >= 1:
        if (n % 10) % 2 == 0:
            n //= 10
        else:
            w += n % 10 * tura
            n //= 10
            tura *= 10

    return w


def czy_istnieje_nieparzysty_skrot(n):
    if nieparzysty_skrot(n) != 0:
        return True
    return False

def wczytaj_dane(plik):
    odczyt = open(plik, 'r')
    dane = odczyt.readlines()
    for a in range(len(dane)):
        dane[a] = int(dane[a].strip())
    odczyt.close()
    return dane
dane = wczytaj_dane("skrot_przyklad.txt")


def zad_3_2(dane):
    wynik = open("wyniki3_2.txt", "w")
    nie_ist_nieparzysty = []
    for a in range(len(dane)):
        if czy_istnieje_nieparzysty_skrot(dane[a]) == False:
            nie_ist_nieparzysty.append(dane[a])
            #print(dane[a])

zad_3_2(dane)


def nwd(x, y):
    w = 1
    for c in range(2, x+1):
        if x % c == 0 and y % c == 0:

            w = c
    return w
dane = wczytaj_dane("skrot2_przyklad.txt")
def zad_3_3(dane):
    w= []
    for a in range(len(dane)):
        ns = nieparzysty_skrot(dane[a])
        if nwd(dane[a], ns) == 7:
            w.append(dane[a])
    #print(w)
zad_3_3(dane)
h=int("1100",2)

x = 10000
y = hex(1000848)[2:].upper()



bin = "1001"
dec = 0
for cyfra in bin:
    dec = dec * 2 + int(cyfra)
print(dec)
b = ""
while dec>0:
    r = str(dec % 2)
    b = r + b
    dec//=2
print(b)


def dec_na_hex(n):
    if n == 0: return "0"

    znaki = "0123456789ABCDEF"
    wynik_hex = ""

    while n > 0:
        reszta = n % 16
        wynik_hex = znaki[reszta] + wynik_hex  # Bierzemy literę/cyfrę pod indeksem reszty
        n //= 16

    return wynik_hex


# Przykład: 255 -> "FF", 31 -> "1F"
print(dec_na_hex(255))
print(dec_na_hex(31))


