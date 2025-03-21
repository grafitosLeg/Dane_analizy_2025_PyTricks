# wypisywanie liczb pierwszych 
# kod definiuje funkcję, która sprawdza, czy liczba jest pierwsza. 
# następnie w pętli wypisuje wszystkie liczby pierwsze w przedziale od 2 do 19
# Może byc przydatny w matematyce grach losowych lub algorytmach wymagających analizy liczb pierwszych
# zmienna "i" jest argumentem "n" funkcji jest_pierwsza , "i" jest przepisywane do "n"

def jest_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, 20):
    if jest_pierwsza(i):
        print(i)
        
        
#wersja copilot z logami
# def jest_pierwsza(n):
#     print(f"Sprawdzam liczbę: {n}")
#     if n < 2:
#         print(f"{n} jest mniejsze niż 2, zwracam False")
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         print(f"Sprawdzam, czy {n} jest podzielne przez {i}")
#         if n % i == 0:
#             print(f"{n} jest podzielne przez {i}, zwracam False")
#             return False
#     print(f"{n} jest liczbą pierwszą, zwracam True")
#     return True

# for i in range(2, 20):
#     print(f"Sprawdzam liczbę w pętli głównej: {i}")
#     if jest_pierwsza(i):
#         print(f"Liczba pierwsza: {i}")
