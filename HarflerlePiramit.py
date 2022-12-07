num = int(input("Satır Sayısını Girin: "))

for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,1+i):
        print(chr(64+i),end=" ")
    print()