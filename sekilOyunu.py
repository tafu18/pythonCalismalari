tekrar = int(input("Şimdi bir oyun oynayalım. Kaç kere oynamak istiyorsun? "))

for i in range (1,tekrar+1,1):
  print("dik üçgen, eşkenar üçgen, kare, dikdörtgen ya da daire seç.")
  print()
  tur = input("Hangi şekli istiyorsun ")

  if tur == "dik üçgen":
    satir = int(input("üçgen satır sayısını giriniz"))
    for sayi in range(1,satir+1,1):
      print(sayi*"*")

  elif tur == "eşkenar üçgen":
    satir = int(input("üçgen satır sayısını giriniz"))
    sayac = satir
    for sayi in range(1,satir+1):
      print(sayac*" ",(2*sayi-1)*"*")
      sayac-=1
      
  elif tur == "kare":
    satir = int(input("kare satır sayısını giriniz"))
    for dis in range(1,satir+1):
      for ic in range(1,satir+1):
          print("*", end=" ")
      print()

  elif tur =="dikdörtgen":
    satir = int(input("dikdörtgen satır sayısını giriniz"))
    sutun = int(input("dikdörtgen sütun sayısını giriniz"))
    for satir in range(1,satir+1):
      for sutun in range(1,sutun+1):
          print("*", end=" ")
      print()
      
  elif tur =="daire":
    satir = int(input("daire satır sayısını giriniz"))
    for sayi in range(satir):
      if sayi > satir/2:
        for k in range(satir-sayi):
          print(" ",end="")
        for m in range((sayi+2)*2-1):
          print("*",end="")
        print()

    for sayi in range(satir,0,-1):
      if sayi > satir/2:
        for k in range(satir-sayi):
          print(" ",end="")
        for m in range((sayi+2)*2-1):
          print("*",end="")
        print()
        
  else:
    print("dik üçgen, eşkenar üçgen, kare, dikdörtgen ya da daire seçebilirsiniz.")
    print()