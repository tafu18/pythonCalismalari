from tkinter import *
import random

pencere = Tk()




pencere.title("TAS-KAGIT-MAKAS")
      
kullanıcı1 = Label(pencere,text="1. Kullanıcının Adı:",bg="lightblue",font=("calibri italic",14))
kullanıcı1.place(x=20,y=0)

kullanıcı2 = Label(pencere,text="2. Kullanıcının Adı:",bg="lightblue",font=("calibri italic",14))
kullanıcı2.place(x=280,y=0)

kullanıcıEntry1 = Entry()
kullanıcıEntry1.place(x=30,y=35)

kullanıcıEntry2 = Entry()
kullanıcıEntry2.place(x=290,y=35)

oyuncuTercih1 = None




def Baslat():

    
    kullan1 = kullanıcıEntry1.get()
    kullan2 = kullanıcıEntry2.get()
    
    kullanıcıEntry1.destroy()
    kullanıcıEntry2.destroy()
    
    kullanıcıLabel1 = Label(pencere,text=kullan1,bg="lightblue",font=("calibri italic",14))
    kullanıcıLabel1.place(x=45,y=28)
    kullanıcıLabel2 = Label(pencere,text=kullan2,bg="lightblue",font=("calibri italic",14))
    kullanıcıLabel2.place(x=305,y=28)
    
    baslatButonu.destroy()

    
    global oyuncuSkor1
    global oyuncuSkor2
    oyuncuSkor1 = 0
    oyuncuSkor2 = 0
  
    def tercihTas():
        oyuncuTercih2 = random.randint(1,3)        
        oyuncuTercih1 = 1
        if oyuncuTercih1 == 1 and oyuncuTercih2 == 1 :
                   print(
           """
           {0} ---> Taş      
           {1} ---> Taş      
           """.format(kullan1,kullan2))
          
                   print("""       Berbare
             ---------""")   
          
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 2 :
                   print(
           """
           {0} ---> Kağıt   
           {1} ---> Kağıt      
           """.format(kullan1,kullan2))
                   print("""       Berbare
             ---------""")   
              
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 3 :
                   print(
           """
           {0} ---> Makas      
           {1} ---> Makas    
           """.format(kullan1,kullan2))
                   print("""       Berbare
             ---------""")   
                
                     
        elif oyuncuTercih1 == 1 and oyuncuTercih2 == 2 :

                   print(
           """
           {0} ---> Taş      
           {1} ---> Kağıt      
           """.format(kullan1,kullan2))
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
              
        elif oyuncuTercih1 == 1 and oyuncuTercih2 == 3 :

                   print(
           """
           {0} ---> Taş      
           {1} ---> Makas      
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
                  
                    
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 1 :

          
                   print(
           """
           {0} ---> Kağıt      
           {1} ---> Taş      
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
                  
              
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 3 :

                  
                   print(
           """
           {0} ---> Kağıt      
           {1} ---> Makas    
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
                  
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 1 :

                  
                   print(
           """
           {0} ---> Makas      
           {1} ---> Taş      
           """.format(kullan1,kullan2))
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
              
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 2 :

                  
                   print(
           """
           {0} ---> Makas      
           {1} ---> Kağıt    
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
        
    def tercihKagit():
        oyuncuTercih2 = random.randint(1,3)         
        oyuncuTercih1 = 2
        if oyuncuTercih1 == 1 and oyuncuTercih2 == 1 :
                   print(
           """
           {0} ---> Taş      
           {1} ---> Taş      
           """.format(kullan1,kullan2))
          
                   print("""       Berbare
             ---------""")   
          
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 2 :
                   print(
           """
           {0} ---> Kağıt   
           {1} ---> Kağıt      
           """.format(kullan1,kullan2))
                   print("""       Berbare
             ---------""")   
              
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 3 :
                   print(
           """
           {0} ---> Makas      
           {1} ---> Makas    
           """.format(kullan1,kullan2))
                   print("""       Berbare
             ---------""")   
                
                     
        elif oyuncuTercih1 == 1 and oyuncuTercih2 == 2 :

                   print(
           """
           {0} ---> Taş      
           {1} ---> Kağıt      
           """.format(kullan1,kullan2))
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
              
        elif oyuncuTercih1 == 1 and oyuncuTercih2 == 3 :

                   print(
           """
           {0} ---> Taş      
           {1} ---> Makas      
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
                  
                    
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 1 :

          
                   print(
           """
           {0} ---> Kağıt      
           {1} ---> Taş      
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
                  
              
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 3 :

                  
                   print(
           """
           {0} ---> Kağıt      
           {1} ---> Makas    
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
                  
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 1 :

                  
                   print(
           """
           {0} ---> Makas      
           {1} ---> Taş      
           """.format(kullan1,kullan2))
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
              
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 2 :

                  
                   print(
           """
           {0} ---> Makas      
           {1} ---> Kağıt    
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
    
    def tercihMakas():
        oyuncuTercih2 = random.randint(1,3) 
        oyuncuTercih1 = 3
        if oyuncuTercih1 == 1 and oyuncuTercih2 == 1 :
                   print(
           """
           {0} ---> Taş      
           {1} ---> Taş      
           """.format(kullan1,kullan2))
          
                   print("""       Berbare
             ---------""")   
          
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 2 :
                   print(
           """
           {0} ---> Kağıt   
           {1} ---> Kağıt      
           """.format(kullan1,kullan2))
                   print("""       Berbare
             ---------""")   
              
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 3 :
                   print(
           """
           {0} ---> Makas      
           {1} ---> Makas    
           """.format(kullan1,kullan2))
                   print("""       Berbare
             ---------""")   
                
                     
        elif oyuncuTercih1 == 1 and oyuncuTercih2 == 2 :

                   print(
           """
           {0} ---> Taş      
           {1} ---> Kağıt      
           """.format(kullan1,kullan2))
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
              
        elif oyuncuTercih1 == 1 and oyuncuTercih2 == 3 :

                   print(
           """
           {0} ---> Taş      
           {1} ---> Makas      
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
                  
                    
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 1 :

          
                   print(
           """
           {0} ---> Kağıt      
           {1} ---> Taş      
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
                  
              
        elif oyuncuTercih1 == 2 and oyuncuTercih2 == 3 :

                  
                   print(
           """
           {0} ---> Kağıt      
           {1} ---> Makas    
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
                  
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 1 :

                  
                   print(
           """
           {0} ---> Makas      
           {1} ---> Taş      
           """.format(kullan1,kullan2))
                   print("""       {0} Kazandı
           ------------------------""".format(kullan2))
                  
              
        elif oyuncuTercih1 == 3 and oyuncuTercih2 == 2 :

                  
                   print(
           """
           {0} ---> Makas      
           {1} ---> Kağıt    
           """.format(kullan1,kullan2))        
                   print("""       {0} Kazandı
           ------------------------""".format(kullan1))
           
    
    TercihBilgi=Label(pencere,text="Tercihinizi Seçin:",bg="lightblue",font=("calibri italic",14))
    TercihBilgi.place(x=10,y=55)
    
    tercihTasButonu = Button(pencere,text=" Taş ",bg="lightblue",command=tercihTas)
    tercihTasButonu.place(x=20,y=90)
    tercihKagitButonu = Button(pencere,text="Kağıt",bg="lightblue",command=tercihKagit)
    tercihKagitButonu.place(x=20,y=120)
    tercihMakasButonu = Button(pencere,text="Makas",bg="lightblue",command=tercihMakas)
    tercihMakasButonu.place(x=20,y=150)
        
    oyuncuTercih2 = random.randint(1,3)
    
        
    # tercihSec = Button(pencere,text="  Tercih  ",bg="lightblue",font=("calibri italic",10),command=tercihKontrol)
    # tercihSec.place(x=30,y=190)



    


baslatButonu = Button(pencere,text="Başla",bg="lightblue",command=Baslat)
baslatButonu.place(x=170,y=100)

pencere.geometry("450x550+250+250")
pencere.resizable(0,0)  
pencere.config(bg="lightblue")
pencere.mainloop()









#     oyuncuTercih1=StringVar()   # Radiobuttondaki verileri alabilmek için değişken atadım.

# # Radiobuton şeklinde tercih ekledim ekledim.
    

    
#     tercih1=Radiobutton(pencere,text="Taş",bg="lightblue",fg="black",value="1",variable=oyuncuTercih1,font=("calibri italic",14))
#     tercih1.place(x=20,y=90)
    
#     tercih2=Radiobutton(pencere,text="Kağıt",bg="lightblue",fg="black",value="2",variable=oyuncuTercih1,font=("calibri italic",14))
#     tercih2.place(x=20,y=120)        
    
#     tercih3=Radiobutton(pencere,text="Makas",bg="lightblue",fg="black",value="3",variable=oyuncuTercih1,font=("calibri italic",14))
#     tercih3.place(x=20,y=150)









   # if oyuncuTercih1 == 1 and oyuncuTercih2 == 1 :
   #           print(
   #   """
   #   {0} ---> Taş      
   #   {1} ---> Taş      
   #   """.format(kullan1,kullan2))
    
   #           print("""       Berbare
   #     ---------""")   
    
   #       elif oyuncuTercih1 == 2 and oyuncuTercih2 == 2 :
   #           print(
   #   """
   #   {0} ---> Kağıt   
   #   {1} ---> Kağıt      
   #   """.format(kullan1,kullan2))
   #           print("""       Berbare
   #     ---------""")   
        
   #       elif oyuncuTercih1 == 3 and oyuncuTercih2 == 3 :
   #           print(
   #   """
   #   {0} ---> Makas      
   #   {1} ---> Makas    
   #   """.format(kullan1,kullan2))
   #           print("""       Berbare
   #     ---------""")   
          
               
   #       elif oyuncuTercih1 == 1 and oyuncuTercih2 == 2 :
   #           oyuncuSkor2 = oyuncuSkor2 + 1
   #           print(
   #   """
   #   {0} ---> Taş      
   #   {1} ---> Kağıt      
   #   """.format(kullan1,kullan2))
   #           print("""       {0} Kazandı
   #   ------------------------""".format(kullan2))
            
        
   #       elif oyuncuTercih1 == 1 and oyuncuTercih2 == 3 :
   #           oyuncuSkor1 = oyuncuSkor1 + 1
   #           print(
   #   """
   #   {0} ---> Taş      
   #   {1} ---> Makas      
   #   """.format(kullan1,kullan2))        
   #           print("""       {0} Kazandı
   #   ------------------------""".format(kullan1))
            
              
   #       elif oyuncuTercih1 == 2 and oyuncuTercih2 == 1 :
   #           oyuncuSkor1 = oyuncuSkor1 + 1
    
   #           print(
   #   """
   #   {0} ---> Kağıt      
   #   {1} ---> Taş      
   #   """.format(kullan1,kullan2))        
   #           print("""       {0} Kazandı
   #   ------------------------""".format(kullan1))
            
        
   #       elif oyuncuTercih1 == 2 and oyuncuTercih2 == 3 :
   #           oyuncuSkor2 = oyuncuSkor2 + 1
            
   #           print(
   #   """
   #   {0} ---> Kağıt      
   #   {1} ---> Makas    
   #   """.format(kullan1,kullan2))        
   #           print("""       {0} Kazandı
   #   ------------------------""".format(kullan2))
            
            
   #       elif oyuncuTercih1 == 3 and oyuncuTercih2 == 1 :
   #           oyuncuSkor2 = oyuncuSkor2 + 1
            
   #           print(
   #   """
   #   {0} ---> Makas      
   #   {1} ---> Taş      
   #   """.format(kullan1,kullan2))
   #           print("""       {0} Kazandı
   #   ------------------------""".format(kullan2))
            
        
   #       elif oyuncuTercih1 == 3 and oyuncuTercih2 == 2 :
   #           oyuncuSkor1 = oyuncuSkor1 + 1
            
   #           print(
   #   """
   #   {0} ---> Makas      
   #   {1} ---> Kağıt    
   #   """.format(kullan1,kullan2))        
   #           print("""       {0} Kazandı
   #   ------------------------""".format(kullan1))
            
        
  #       turSayısı = turSayısı - 1
    
  #   if oyuncuSkor1 > oyuncuSkor2:
  #       print("Oyunu {} Kazandı".format(kullan1))
    
  #   elif oyuncuSkor2 > oyuncuSkor1:
  #       print("Oyunu {} Kazandı".format(kullan2))
    
    
  #   elif oyuncuSkor1 == oyuncuSkor2:
  #       secim = input("""Beraberlik.
  #   Oyunu berabere bitirmek için [Y/y]
  #   Tekrar Oynamak için [N/n] yazın.
  #   >>>> """)
  #       if secim == "N" or secim == "n":
  #           Baslat()
        
  #       elif secim == "Y" or secim == "y":
  #           print("Kardeşlik Kazandı...")




