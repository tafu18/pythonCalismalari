#fibonacci
sayi1 = 1
sayi2 = 1
index = 1
print(sayi1)
print(sayi2)
while index < 33:
    temp = sayi1 + sayi2
    sayi2 = sayi1
    sayi1 = temp
    index = index + 1
    print(temp)    