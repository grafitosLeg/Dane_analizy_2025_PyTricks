
# Kod sprawdza, czy dany klucz znajduje się w słowniku. Może być przydatny do weryfikacji dostępnosci 
# danych przed ich wykorzystaniem w dalszej czesci programu.Co zapobiega błędom w trakcie działania programu.

# slownik = {"klucz1": "wartość1", "klucz2": "wartość2"}
# W tym przypadku slownik to zmienna, która przechowuje obiekt typu dict (słownik). 
# Słowniki w Pythonie to struktury danych, które przechowują pary klucz-wartość. 
# Klucze muszą być unikalne i niemutowalne (np. stringi, liczby), a wartości mogą być dowolnego typu

slownik = {"nazwisko":"Kowolski", "wiek": 25}
print("imie" in slownik) # True
print("nazwisko" in slownik) # False

 
