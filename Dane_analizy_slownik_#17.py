# wypisywanie elementów słownika
# kod ten wypisuje klucze i przypisane do nich wartościze słownika.
# Może być przydatny do prezentacji danych w łatwy do zrozumienia sposób, np w raportach 
# czy podczas debugowania

slownik = {"imie": "Jan", "wiek": 30}
for klucz in slownik:
    print(f"{klucz}: {slownik[klucz]}")

    


