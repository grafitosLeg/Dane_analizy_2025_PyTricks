# wypisywanie słowników
# kod wypisuje klucze ze słownikai i odpowiadające im wartości. 
# Przydatny do prezentacji danych w czytelnej formie lub debugowania

slownik = {"imie": "Jan", "wiek": 30}
for klucz, wartosc in slownik.items():
    print(f"{klucz}: {wartosc}")

    
