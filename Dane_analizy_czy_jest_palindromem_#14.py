# sprawdzanie czy cią jest palindronem
# kod definiuje funkcję is_palindrome, która sprawdza czy podany ciąg znaków jest palindronem
# czyli czy czyta się tak samo od przodu i od tyłu.
# Może byc przydatny w aplikacjach zajmujących się analizą tekstu lub przy tworzeniu gier słownych.

def jest_palindromem(ciag):
    return ciag == ciag[::-1]

print(jest_palindromem("kajak")) # True
print(jest_palindromem("kajak")) # False




