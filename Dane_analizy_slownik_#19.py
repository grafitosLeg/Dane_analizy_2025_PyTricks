# usuwanie elementów ze słownika
# Kod demonstruje usuwanie elemenu ze slownika w Pythonie.
# po usunięciu klucza "wiek, pozostały tylko klucz "imie".
# Moze być przydatny do zarządzania danymi, gdy potrzebujemy modyfikować zawartość słownika

slownik = {"imie": "Jan", "wiek": 30}
del slownik["wiek"]
print(slownik)

