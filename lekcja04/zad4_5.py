def odwracanie_rekurencja(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    return odwracanie_rekurencja(L, left + 1, right - 1)


def odwracanie_iteracja(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


L1 = list(range(10))
L2 = list(range(10))
L3 = list(range(10))
L4 = list(range(10))
odwracanie_rekurencja(L1, 0, 9)
odwracanie_rekurencja(L2, 3, 7)
odwracanie_iteracja(L3, 0, 9)
odwracanie_iteracja(L4, 3, 7)
print(L1)
print(L2)
print(L3)
print(L4)