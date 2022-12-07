A = [64, 2, 23, 25, 1, 18, 30, 44] 

for i in range(len(A)):  # A dizisi kadar for dönecek
    
    enKücük = i #rastgele hafızaya bir tane değer veriyoruz
    
    for j in range(i+1, len(A)): # i+1 yazdım çünkü zaten 0. index sıralandı for bir daha döndüğünde
                                 # 1. index sıralanmış olacak.
        
        if A[enKücük] > A[j]: # 1. fordaki i. indexteki değer 2. fordaki j. indexten büyükse değişkenlerin yeri değişecek.
            enKücük = j
        
    bosDegisken = A[i]
    A[i] = A[enKücük]         # Burada listede indexdeki değerlerin yerini değiştirmek için yaptım.
    A[enKücük] = bosDegisken
        
    
    # A[i], A[enKücük] = A[enKücük], A[i] # ------> Şu şekilde de yapabiliriz
        

print ("Sıralı Dizi") 
for i in A: 
	print(i) 
