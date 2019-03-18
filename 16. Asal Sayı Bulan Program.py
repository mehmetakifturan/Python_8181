#Written by <Akif>
#Kullanıcının girdiği sayıya kadar olan asal sayıları yazdıran program
sayi=int(input("Pozitif bir sayı giriniz: "))
if sayi<2:
    print("2'den küçük hiçbir asal sayı yoktur.")

print(2)
for aralik in range(3,sayi+1):
    for bolen in range(2,aralik):
        if aralik%bolen==0:
            break
        if aralik-1>bolen:
            continue
        print(aralik)
        
    
