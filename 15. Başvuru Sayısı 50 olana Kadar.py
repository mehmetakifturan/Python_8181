#Written by <Akif>
#50 kişinin yukarıda ki turnuvaya katılması için toplam ne kadar başvuru olduğunu ekrana yazdıran program
print('''Birazdan voleybol turnuvasına
katılım şartları için kişisel bilgiler istenecek
daha sonra şartlar ve bilgiler karşılaştırılarak
turnuvaya katılabilecek 50 kişi olana kadar yapılan toplam başvuru sayısı ekrana yazılacak
Voleybol turnuvasına katılabilmeniz için,
9. sınıf öğrencisi ve
en az 180 cm boyunda olmanız gerekmektedir.''')
katilan=0
toplam=0
while katilan<50:
    toplam+=1
    sinif=int(input("Sınıfınızı sayı olarak giriniz: "))
    boy=int(input("Boyunuzu cm cinsinden sayı olarak giriniz: "))
              
    if sinif==9 and boy>=180:
        print("Voleybol turnuvasına uygun.")
        katilan+=1
    else:
        print("Voleybol turnuvasına uygun değil!")
        
print("Voleybol turnuvasına 50 uygun başvuru yapılana kadar toplam {} kişi başvuru yapıldı.".format(toplam))
    

        
    
