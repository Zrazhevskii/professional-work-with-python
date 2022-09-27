import numpy as np

def get_employees():
    print('В нашей организации работает 150 человек')

def sieve_of_Eratosthenes():
    N = int(input('Введите число для вычесления простых чисел '))
    a = np.array(range(3,N,2))
    for j in range(0, int(round(np.sqrt(N),0))):
        a[(a!=a[j]) & (a%a[j] == 0)] = 0
        a = a[a!=0]
    a = [2]+list(a)
    print(a)

