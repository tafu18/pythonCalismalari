from abc import ABC, abstractmethod
class Virus(ABC):
    def __init__(self,bulasanUlke,bulasSayisi,olumOranı):
        self.bulasanUlke=bulasanUlke
        self.bulasSayisi=bulasSayisi
        self.__olumOranı=olumOranı
    @abstractmethod
    def belirtileri():
        print("Ates\nNefes Darligi")
    @abstractmethod
    def bulası():
        return "....'den bulaştı."
    
    def bilgiler():
        print(""""
Bulasan Ulke Sayisi: {}
Bulas Sayisi: {} 
Bulaşı:{}            
 """)
    
class Sars(Virus):
    def __init__(self,bulasanUlke,bulasSayisi,olumOranı):
        Virus.__init__(self,bulasanUlke,bulasSayisi,olumOranı)
        self.__olumOranı="%9,32"
 
    def getOlumOranı(self):
        return self.__olumOranı
        
    def belirtileri(self):
        print("~~~SARS'ın Belirtileri~~~\n-Ates\n-Nefes Darligi\n-Öksürük\n-Boğaz ağrısı ")

    def bulası(self):
        return "SARS Çin’de Misk Kedilerinden Bulaştı."

    def bilgiler(self,bulasanUlke,bulasSayisi):
        print("""
Sars Bulasan Ulke Sayisi: {}
Sars Bulas Sayisi: {}
Sars Olum Oranı: {}
Sars Bulaşı:{}
        """.format(self.bulasanUlke,self.bulasSayisi,s.getOlumOranı(),s.bulası()))
        
class Mers(Virus):
    def __init__(self,bulasanUlke,bulasSayisi,olumOranı):
        Virus.__init__(self,bulasanUlke,bulasSayisi,olumOranı)
        self.__olumOranı="%36,27"
 
    def getOlumOranı(self):
        return self.__olumOranı
        
    def belirtileri(self):
        print("~~~MERS'in Belirtileri~~~\n-Ateş\n-Titreme\n-Baş ağrısı\n-Baş dönmesi\n-Boğaz ağrısı\n-Kuru öksürük\n-Nefes darlığı\n-Kas ağrısı")

    def bulası(self):
        return "MERS Suudi Arabistan’da Develerden Bulaştı"

    def bilgiler(self,bulasanUlke,bulasSayisi):
        print("""
Mers Bulasan Ulke Sayisi: {}
Mers Bulas Sayisi: {}
Mers Olum Oranı: {}
Mers Bulaşı:{}
        """.format(self.bulasanUlke,self.bulasSayisi,m.getOlumOranı(),m.bulası()))
        
class Korona(Virus):
    def __init__(self,bulasanUlke,bulasSayisi,olumOranı):
        Virus.__init__(self,bulasanUlke,bulasSayisi,olumOranı)
        self.__olumOranı="%6,58"
 
    def getOlumOranı(self):
        return self.__olumOranı
        
    def belirtileri(self):
        print("~~~KORONA'nın Belirtileri~~~\n-Ateş\n-Baş ağrısı\n-Kuru öksürük\n-Nefes darlığı")

    def bulası(self):
        return "KORONA Çin'den Bulaştı ama Neyden Bulaştığı Şuan için Belirsiz."

    def bilgiler(self,bulasanUlke,bulasSayisi):
        print("""
Korona Bulasan Ulke Sayisi: {}
Korona Bulas Sayisi: {}
Korona Olum Oranı: {}
Korona Bulaşı:{}
        """.format(self.bulasanUlke,self.bulasSayisi,k.getOlumOranı(),k.bulası()))
       
s=Sars(15,8455,'')
s.bilgiler(15,8455)
s.belirtileri()

m=Mers(12,2494,'')
m.bilgiler(120,12100)
m.belirtileri()

k=Korona(74,4025890,'')
k.bilgiler(74,4025890)
k.belirtileri()