#Written by <Akif>
#100 kişilik bir ekipten yukarıda ki hazırlanacak turnuvaya kaç kişinin katılıp kaç kişinin katılamayacak olduğunu yazdıran program
print('''Birazdan 100 kişinin voleybol turnuvasına
katılım şartları için kişisel bilgileri istenecek
daha sonra şartlar ve bilgiler karşılaştırılarak
turnuvaya kaç kişinin katılıp kaç kişinin katılamayacağı ekrana yazılacak
Voleybol turnuvasına katılabilmeniz için,
9. sınıf öğrencisi ve
en az 180 cm boyunda olmanız gerekmektedir.''')
katilan=0
katilamayan=0
for ali in range(100):
    sinif=int(input("Sınıfınızı sayı olarak giriniz: "))
    boy=int(input("Boyunuzu cm cinsinden sayı olarak giriniz: "))
              
    if sinif==9 and boy>=180:
        print("Voleybol turnuvasına uygun.")
        katilan+=1
    else:
        print("Voleybol turnuvasına uygun değil!")
        katilamayan+=1
print("Voleybol turnuvasına {} kişi katılabilir, {} kişi katılamaz.".format(katilan,katilamayan))
    

        
    
