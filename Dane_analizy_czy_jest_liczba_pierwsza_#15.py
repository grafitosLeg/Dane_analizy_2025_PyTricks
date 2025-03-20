# wypisywanie liczb pierwszych 
# kod definiuje funkcję, która sprawdza, czy liczba jest pierwsza. 
# następnie w pętli wypisuje wszystkie liczby pierwsze w przedziale od 2 do 19
# Może byc przydatny w matematyce grach losowych lub algorytmach wymagających analizy liczb pierwszych

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


        

