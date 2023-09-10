def FPB(x, y):
    while y != 0:
        sisa = x % y
        x = y
        y = sisa
    return x

a = 3
b = 4

kpk = (a * b) // FPB(a, b)
print(kpk)
