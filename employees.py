firma = {'IT':['Kacper Nowak','Blazej Wojcik','Aneta Kowalska'],
'Kadry':['Krzysztof Kaminski','Anna Wisniewska','Danuta Zielinska','Daria Szymanska'],
'Ksiegowosc':['Mirek Wozniak','Lukasz Dabrowski','Katarzyna Jankowska'],
'Sprzedaz':['Leszek Wojciechowski','Danuta Mazur','Kacper Kowalski','Anna Piotrowska','Katarzyna Grabowska']}


class pracownik:
    def __init__(self, imie, nazwisko, dzial, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dzial = dzial
        self.pensja = pensja

        if pensja < 3000:
            return 'Minimalna pensja dla pracownika wynosi 3000'

    def podwyzka(self, nowa_pensja):
        if self.nowa_pensja < pensja or self.nowa_pensja > 10000:
            return 'Nowa pensja jest nizsza od minimalnej lub przekracza maksymalne wynagrodzenie'
        else:
            self.nowa_pensja = pensja
            print('Nowa pensja wynosi', pensja)

    def nowy_dzial(self, nowy_dzial):
        if self.dzial == self.nowy_dzial:
            return 'Pracownik juz pracuje w dziale', self.nowy_dzial
        else:
            self.nowy_dzial = self.dzial
            return 'Pracownik zostal przeniesionydo dzialu', self.nowy_dzial

    def pracownik_dane(self):
        return self.imie, self.nazwisko, self.dzial, self.pensja

firma_old = firma
baza_firmy = []

def transferuj():
    for dzial, pracownicy_old in firma_old.items():
        for pracownicy_new in pracownicy_old:
            imie, nazwisko = pracownicy_new.split(" ")
            pracownik_new = pracownik(imie, nazwisko, dzial, pensja = 3000)
            baza_firmy.append(pracownik_new)
    firma_old.clear()

transferuj()

def firma_new():
    for pracownicy in baza_firmy:
        print(pracownicy.pracownik_dane())

firma_new()

def find_empl(podaj_nazwisko):
    for pracownik in baza_firmy:
        if podaj_nazwisko == pracownik.nazwisko:
            print('Jestem', pracownik.imie, pracownik.nazwisko, 'pracuje w dziale', pracownik.dzial, 'i zarabiam', pracownik.pensja, 'EUR')
            break
    else:
        print('Pracownik o takim nazwisku nie pracuje w tej firmie')


find_empl('Wozniak')


def daj_podwyzki(baza, dzial, kwota):
    print("Podwyzki o", kwota, "zł dla wszystkich z działu", dzial)
    try:
        for pracownik in baza:
            try:
                if pracownik.dzial == dzial:
                    try:
                        pracownik.podwyzka(kwota)
                    except TypeError:
                        print("Kwota musi byc wyrożona liczbowo")
                        break
            except AttributeError:
                print("pracownik {} nie ma właściwości dział! Sprawdź bazę danych: {}".format(pracownik, baza))
    except TypeError:
        print("Nieprawidłowa baza danych!", baza)


nowa_baza = transferuj()
szukaj_pracownika(nowa_baza, "Anna", "Wisniewska")

daj_podwyzki(baza_firmy, "IT", "500")
daj_podwyzki(5, "IT", 500)
daj_podwyzki([5 ,6 ,7], "IT", 500)
daj_podwyzki(baza_firmy, "IT", 500)