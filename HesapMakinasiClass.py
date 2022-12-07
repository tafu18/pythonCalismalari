class HesapMakinesi:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def toplama(self):
        return self.sayi1 + self.sayi2
    def cikarma(self):
        return self.sayi1 - self.sayi2
    def carpma(self):
        return self.sayi1 * self.sayi2
    def bolme(self):
        return self.sayi1 / self.sayi2
    
print("""
 İşlem Kodu | İşlem Adı
---------------------------------   
    1)      Toplama İşlemi\n
    2)      Çıkarma İşlemi\n
    3)      Çarpma İşlemi\n
    4)      Bölme İşlemi\n
      """)
İşlemKodu=int(input("LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİN KODUNU GİRİN ---> "))

def İşlem(num1,num2):
    hesapmakinesi=HesapMakinesi(num1,num2)
    if İşlemKodu==1:
        print("Sonuç= ",hesapmakinesi.toplama())
    elif İşlemKodu==2:
        print("Sonuç= ",hesapmakinesi.cikarma())
    elif İşlemKodu==3:        
        print("Sonuç= ",hesapmakinesi.carpma())
    elif İşlemKodu==4:        
        print("Sonuç= ",hesapmakinesi.bolme())   
    else: 
        print("\n              SYSTEM FAİL\nLÜTFEN BELİRTİLEN İŞLEM KODLARINDAN BİRİNİ SEÇİN")        

İşlem(18,2)