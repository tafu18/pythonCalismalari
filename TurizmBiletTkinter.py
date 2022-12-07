from tkinter import *  # Tkinter modülündeki tüm sınıfları import ettim.
from tkinter import messagebox  # Ekrana Mesaj Bildirimi Vermesi İçin İmport ettim.

pencere=Tk()  #Ana penceremizi oluşturuyoruz.
pencere.title("TAŞDEMİR TURİZM 18")  # Penceremize isim verdim.

class Yolculuk():
    Güzergah=""     # Güzergah bilgisini alabilmek için baoş string değişkeni tanımladım.
    x=StringVar()   # Radiobuttondaki verileri alabilmek için değişken atadım.

# Radiobuton şeklinde güzergahları ekledim.
    
    GüzergahBilgi=Label(pencere,text="Gideceğiniz Güzergahı Seçin:",bg="lightblue",font=("calibri italic",14))
    GüzergahBilgi.place(x=50,y=230)
    
    rota1=Radiobutton(pencere,text="1) Seydisehir - Konya",bg="lightblue",fg="black",value="1",variable=x,font=("calibri italic",14))
    rota1.place(x=70,y=260)
    
    rota2=Radiobutton(pencere,text="2) Seydisehir - Istanbul",bg="lightblue",fg="black",value="2",variable=x,font=("calibri italic",14))
    rota2.place(x=70,y=290)        
    
    rota3=Radiobutton(pencere,text="3) Seydisehir - Ankara",bg="lightblue",fg="black",value="3",variable=x,font=("calibri italic",14))
    rota3.place(x=70,y=320)

# Güzergahların ayrtısını almak için yukarıda tanımladığımız Güzergah ve x değişkenin koşul kullanarak kullanıcının seçtiği
# Güzergahın ayrıntısını değişkenimize aktarıyoruz.
    
    def RotaYaz():        
        if Yolculuk.x.get()=="1":
            Yolculuk.Güzergah="""|                                                |
|            Seydisehir - Konya                  |
|            1 Saat 30 Dakika                    |
|            103 KM                              |
|            50 TL                               |
|                                                |            """ 
            print(Yolculuk.Güzergah)
            
        elif Yolculuk.x.get()=="2":
            Yolculuk.Güzergah="""|                                                |
|            Seydisehir - Istanbul               |
|            11 Saat 30 Dakika                   |
|            818 KM                              |
|            250 TL                              |
|                                                |            """
            print(Yolculuk.Güzergah)
            
        elif Yolculuk.x.get()=="3":
            Yolculuk.Güzergah="""|                                                |
|            Seydisehir - Ankara                 |
|            5 Saat 45 Dakika                    |
|            351 KM                              |
|            150 TL                              |
|                                                |            """ 
            print(Yolculuk.Güzergah)
            
        else:
            print("|                                                |")
            print("|          Lütfen Bir Tane Rota Seçin            |")

class Yolcu():
    
#  Kullanıcıdan ad,soyad,TC ve tarih almak için hem Entry hemde Label tanımladım.

    Ad=Label(pencere,text="Adınız: ",bg="lightblue",font=("calibri italic",14))
    Ad.place(x=80,y=0)
    
    Ad_entry=Entry()
    Ad_entry.place(x=210,y=5)
    
    Soyad=Label(pencere,text="Soyadınız: ",bg="lightblue",font=("calibri italic",14))
    Soyad.place(x=80,y=35)
    
    Soyad_entry=Entry()
    Soyad_entry.place(x=210,y=40)
    
    TC=Label(pencere,text="TC Numaranız: ",bg="lightblue",font=("calibri italic",14))
    TC.place(x=80,y=70)
    
    TC_entry=Entry()
    TC_entry.place(x=210,y=75)
    
    Tarih=Label(pencere,text="Tarihi Giriniz:\n(GG.AA.YYYY) ",bg="lightblue",font=("calibri italic",14))
    Tarih.place(x=80,y=105)
    
    Tarih_entry=Entry()
    Tarih_entry.place(x=210,y=120)
                    
                
class Bilet(Yolculuk,Yolcu):
# Bilet classında global değişken olarak ekledim.
    ad="" 
    soyad="" 
    tc="" 
    tarih="" 
    def BiletYaz():

# Entry den aldığımız değerleri kendi belirlediğimiz değişkenlere almak için bu şekilde bir fonksiyon yazdım.

        Bilet.ad=Yolcu.Ad_entry.get()
        Bilet.soyad=Yolcu.Soyad_entry.get()
        Bilet.tc=Yolcu.TC_entry.get()
        Bilet.tarih=Yolcu.Tarih_entry.get()
        
        if Bilet.ad=="" or Bilet.soyad=="" or Bilet.tc=="" or Bilet.tarih=="":
            print( """--------------------------------------------------            
|             TAŞDEMİR  TURİZM  18               |
|         20 YILDIR SEKTORUN EN IYISI            |
|                                                |
|                                                |
|     Lütfen Bilgileriniz Eksiksiz Giriniz       |""") 
        
        else:
            print( """-------------------------------------------------- 
|                                                |                                      
|                                                |                       
|             TAŞDEMİR  TURİZM  18               |                        
|         20 YILDIR SEKTORUN EN IYISI            |            
|                                                |            
|                                                |                    
|            Yolcu Adı: {0}                                
|            Yolcu Soyadı: {1}                           
|            Yolcu TC No: {2}                           
|            Tarih: {3}                         
|                                                |""".format(Bilet.ad,Bilet.soyad,Bilet.tc,Bilet.tarih))


# Biletle ilgili bütün bilgilerin yazılması için tek bir fonkssiyon yazdım.

def TesekkurMetni():
    
    print("""|                                                |
|                                                |
|                                                |
|           Bizi Tercih Ettiğiniz İçin           |
|               Teşekkür Ederiz...               | 
|                                                |               
|               TAŞDEMİR TURİZM 18               |
|             İyi Yolculuklar Diler :)           |
|                                                |          
|                                                |
--------------------------------------------------          """)

# Satın alındı mesajı gelmesi ve biletini nasıl yazdıracağını göstermesi için yazdım.

def SatınAlındı():
    if Yolculuk.Güzergah == "" or Bilet.ad=="" or Bilet.soyad=="" or Bilet.tc=="" or Bilet.tarih=="":
        Mesaj1=messagebox.showinfo(title="Satın Alma Başarısız",message="Bilet Satın Alınamadı\nLütfen Bilgilerinizi ve\nGüzergahınızı Kontrol Edin" )
    
    else:
        Mesaj2=messagebox.showinfo(title="Satın Alındı",message="Bilet Satın Alındı\nYazdırmak İçin 'Yazdır'a Tıklayın" )
        

# Yolcunun isim, soyisim, TC, ve tarih bilgilerini alması için buton ve komut ekledim.

VeriButton=Button(pencere,text="Kayıt Ol",font=("calibri italic",14),command=Bilet.BiletYaz)
VeriButton.place(x=190,y=160)
          
#  Seçilen Güzergahı Ekrana yazması için buton ve komut ekledim.

buton=Button(pencere,text="   Seç   ",font=("calibri italic",12),command=Yolculuk.RotaYaz)
buton.place(x=190,y=365)

# Kullanıcıyı rehber olması amacıyla nereye tıklayacağını söylemek amacıyla yazdım.

SatınAl=Label(pencere,text="""
              Bileti Satın Almak İçin Tıklayın
                                          
              |
              |
              |
              V
                                          """,bg="lightblue")
SatınAl.place(x=100,y=400)

# Bileti yazdırmak için buton.

BiletYazdır=Button(pencere)
BiletYazdır.config(text="  ----> Yazdır <----  ",bg="lightblue",font=("calibri italic",12),command=TesekkurMetni)
BiletYazdır.pack(side=BOTTOM,fill=X)

# Satın alındı mesajı gelmesi için buton.


SatınAl=Button(pencere,text="----> Satın Al <----",bg="lightblue",font=("calibri italic",12),command=SatınAlındı)
SatınAl.pack(expand=1,anchor="se",fill=X)

# Penceremizin özellikleri belirlenmesi için yazdım.

pencere.geometry("450x600+550+250")
pencere.config(bg="lightblue")

# Pencerenin ekranda kalması için zorunlu.

pencere.mainloop()