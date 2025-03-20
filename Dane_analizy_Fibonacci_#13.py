# wypisywanie ciągu Fibonacciego
# kod ten generuje i wypisuje pierwsze 'n' liczbciągu Fibonacciego
# gdzie n w tym przypadku wynosi 10.
# Jeste toprosta implementacja, która wykorzystuje iterację do obliczenia kolejnych
# wartości ciągu. Może być przydatny w edukacji do nauki podstaw programowania oraz zrozumienia rekurencji i algorytmów.

a, b = 0,1
for i in range(0,10):
        print(a)
        a, b = b, a+b 
#fibonacci(10



