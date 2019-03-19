#Written by <Akif>
#Bir turnuva düzenleyerek, turnuvaya katılım şartlarını kişilere sorarak turnuvaya katılıp katılamayacaklarını yazdıran program
print('''Birazdan sizden voleybol turnuvasına
katılım şartları için kişisel bilgileriniz istenecek
daha sonra şartlar ve bilgileriniz karşılaştırılarak
katılım durumunuz ekrana yazılacak
Voleybol turnuvasına katılabilmeniz için,
9. sınıf öğrencisi ve
en az 180 cm boyunda olmanız gerekmektedir''')
sinif=int(input("Sınıfınızı sayı olarak giriniz: "))
boy=int(input("Boyunuzu cm cinsinden sayı olarak giriniz: "))
          
if sinif==9 and boy>=180:
    print("Voleybol turnuvasına katılabilirsiniz.")
elif sinif!=9 and boy<180:
    print('''Voleybol turnuvasına katılamazsınız.
Çünkü hem 9. sınıf öğrencisi değilsiniz,
hem de boyunuz 180 cm'den kısa!''')
elif sinif!=9:
    print('''Voleybol turnuvasına katılamazsınız.
Çünkü 9. sınıf öğrencisi değilsiniz!''')
elif boy<180:
    print('''Voleybol turnuvasına katılamazsınız.
Çünkü boyunuz 180 cm'den kısa!''')
    
    

        
    
