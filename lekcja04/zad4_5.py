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


Lr = list(range(10))
odwracanie_rekurencja(Lr, 0, 9)
print(Lr)

Li = list(range(10))
odwracanie_iteracja(Lr, 0, 9)
print(Li)