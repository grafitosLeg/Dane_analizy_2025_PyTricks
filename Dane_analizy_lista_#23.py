# wypisywanie elementów zagnieżdżonej listy
# kod wypisuje wszystkie elementy zagnieżdżonej listy, czyli listy zawierającej
# inne listy. 
# Może byc przydatny do przetwarzania i wyodrębniania danych z struktury wielowymiarowej

lista = [[1, 2], [3, 4], [5, 6]]
for podlista in lista:
    for element in podlista:
        print(element)
