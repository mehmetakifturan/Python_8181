#Written by <Akif>
#kullanıcının girecek olduğu 10(on) sayının toplamını ve bu sayıların ortalamasını bularak ekrana yazdıran program
print('''Birazdan sizden on tane sayı istenecek
Daha sonra bu sayıların toplamı ve ortalaması ekrana yazılacak''')
toplam=0
for alirmak in range(10):
    sayi=int(input("{}. sayıyı giriniz: ".format(alirmak+1)))
    toplam+=sayi
print("Girdiğiniz on sayının toplamı: ",toplam)
print("Girdiğiniz on sayının ortalaması: ",toplam/10)
    

        
    
