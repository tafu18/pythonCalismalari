import random
import time

print("\nAdam Asmaca Oyununa Hoşgeldiniz\n")
name = input("İsminizi Girin: ")
print("Merhaba " + name + "! Bol Şanslar!")
time.sleep(2)
print("Oyun Hazırlanıyor\nHaydi Başlayalım!")
time.sleep(3)


def Oyun():
    global sayac
    global harfSayisi
    global kelime
    global dogruTahminler
    global uzunlugu
    global play_game
    tahminEdilecekKelimeler = ["İsmetÖzel","AbdurrahimKarakoç","SezaiKarakoç","CahitZarifoğlu","NazımHikmetRan","CemalSüreyya","ÖzdemirAsaf","AdilErdemBayazıt","MehmetAkifİnan","NurullahGenç","SerdarTuncer"]
    kelime = random.choice(tahminEdilecekKelimeler)
    uzunlugu = len(kelime)
    sayac = 0
    harfSayisi = '_' * uzunlugu
    dogruTahminler = []
    play_game = ""
    

def OyunTekrarı():
    global play_game
    play_game = input("Tekrar Oynamak İster misin? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Tekrar Oynamak İster misin? y = yes, n = no \n")
    if play_game == "y":
        Oyun()
        AdamAsmaca()
    elif play_game == "n":
        print("Oynadığın için Teşekkür Ederiz! Tekrar Bekleriz!")
        

def AdamAsmaca():
    global sayac 
    global harfSayisi
    global kelime
    global dogruTahminler
    global play_game
    limit = 5
    tahmin = input("Kelime: " + harfSayisi + " Tahmininizi Girin: ")
    tahmin = tahmin.strip()
    if len(tahmin.strip()) >= 2 or tahmin <= "9":
        print("Geçersiz Giriş, Bir harf deneyin\n")
        AdamAsmaca()
        
    elif tahmin in kelime:
        dogruTahminler.extend([tahmin])
        index = kelime.find(tahmin)
        kelime = kelime[:index] + "_" + kelime[index + 1:]
        harfSayisi = harfSayisi[:index] + tahmin + harfSayisi[index + 1:]
        print(harfSayisi + "\n")
    elif tahmin in dogruTahminler:
        print("Başka Bir Harf Deneyin.\n")
    else:
        sayac += 1
        if sayac == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Hatalı Tahmin. " + str(limit - sayac) + " tahmin hakkın kaldı\n")
        elif sayac == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Hatalı Tahmin. " + str(limit - sayac) + " tahmin hakkın kaldı\n")
        elif sayac == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Hatalı Tahmin. " + str(limit - sayac) + " tahmin hakkın kaldı\n")
        elif sayac == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Hatalı Tahmin. " + "Son tahmin hakkın \n")
        elif sayac == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Hatalı Tahmin. Adam Asıldı!!!\n")
            print("Doğru kelime:",dogruTahminler,kelime)
            OyunTekrarı()
    if kelime == '_' * uzunlugu:
        print("Tebrikler! Doğru Kelimeyi Tahmin Ettin!")
        OyunTekrarı()
    elif sayac != limit:
        AdamAsmaca()
Oyun()
AdamAsmaca()