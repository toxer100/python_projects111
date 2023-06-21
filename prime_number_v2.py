n = int(input("Введите верхнюю границу диапазона: "))
sieve = set(range(2, n+1))
lst = []

while sieve:
    prime = min(sieve)
    
    lst.append(prime)
    
    sieve -= set(range(prime, n+1, prime))

print(lst)