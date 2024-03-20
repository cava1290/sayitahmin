from random import randint

oyun_modu = input("Oyun modunu seçin (kolay - zor): ")

if oyun_modu == "zor":
    max_hak = 5
else:
    max_hak = 10

rand = randint(1, 100)
sayac = 0

while sayac < max_hak:
    sayac += 1
    sayi = int(input("1 ile 100 arasında değer girin (0 çıkış): "))
    if sayi == 0:
        print("Oyunu iptal ettin")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
    elif sayi > rand:
        print("Daha Düşük Bir sAyı girin.")
    else:
        print("Rastgele seçilen sayı {0}!".format(rand))
        print("Tahmin hakın {0}".format(sayac))
        break
else:
    print("Hakkınız bitti. Doğru sayı {0}.".format(rand))