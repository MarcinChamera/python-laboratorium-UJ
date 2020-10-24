from random import sample
L = sample(range(1, 1000), 10)
L_zero_filled = [number.zfill(3) for number in map(str, L)]
print(L_zero_filled)