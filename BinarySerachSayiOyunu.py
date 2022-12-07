import random

sayi = random.randint(0,100)

sayac = True
while sayac:

    tahmin = int(input("Tahmini Girin: "))
    
    if tahmin < sayi:
        print("Daha büyük sayı girin.")
        
    elif tahmin > sayi:
        print("Daha kücük sayı girin.")
        
    elif tahmin == sayi:
        print("Tebrikler doğru bildiniz.")
    
        sayac = False