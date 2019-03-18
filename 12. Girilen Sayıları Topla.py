#Written by <Akif>
#Bir turnuva düzenleyerek, turnuvaya katılım şartlarını kişilere sorarak turnuvaya katılıp katılamayacaklarını yazdıran program
print('''Birazdan sizden sürekli sayı girmeniz istenecek
0'dan küçük ya da 100'den büyük bir sayı girerseniz
o zamana kadar girdiğiniz tüm sayıların toplamı ekrana yazılacak''')
toplam=0
sayac=-1
sayi=0
while sayi>=0 and sayi<=100:
    toplam+=sayi
    sayac+=1
    sayi=int(input("Sayı giriniz: "))
    
    
print("Girdiğiniz {} adet sayının toplamı: {} eder.".format(sayac,toplam))
    

        
    
