# wypisywanie elementów słownika  - wypisywanie pary klucz-wartość
# dla zmiennej klucz w słownik:
#     wypisz klucz i wartość

slownik = {"imie":"Kowolski", "wiek": 25}

for klucz in slownik:
    print(f"{klucz}: {slownik[klucz]}")

    