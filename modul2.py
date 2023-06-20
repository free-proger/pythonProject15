from random import uniform
import sys

if __name__ == '__main__':
    maxx = 0
    maxxi = 0
    poli = 0
    s = 0
    A = [round(uniform(-10, 10), 2) for i in range(10)]
    a = int(input())
    b = int(input())

    for i in range(len(A)):
        if abs(A[i]) > maxx:
            maxx = abs(A[i])
            maxi = i
        if A[i] > 0:
            poli = i
    for i in range(poli, len(A)):
        s += A[i]
    print('максимальное по модулю ', maxi, 'сумма после первого', s)
    print('массив', A)
    print('отсортированный массив: ', sorted(A, key=lambda x: int(x) not in range(a, b + 1)))