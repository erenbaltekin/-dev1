# Veri Tipleri:-----------------------------------------------------------------------------------------------------------------------------

# String => Metinsel türdeki veri tipidir. "kodlama" şeklinde tanımlanır ve üzerinde herhangi bir matematiksel işlem yapılamaz. 
# Toplama ve çarpma operatörleri ile ancak str ifadeyi toplama ile yanyana yazma, çarpma ile çarpılan sayı kadar yanyana yazma yapılabilir.

isim = "Eren"
print(isim) #Eren
print(isim+isim) #ErenEren
print(isim*5) #ErenErenErenErenEren
print(type(isim))

# İnteger => Tam sayı türündeki veri tipidir. Üzerinde aritmetik işlemler uygulanabilir. Sayının kendisi tırnaksız yazılarak tanımlanır.

fiyat = 544
print(fiyat)
print(type(fiyat))
# Not: Tırnak içinde tanımlandığından str ifade olmuş oldu. Çıktı olarak 413 versede str olduğundan üzerinde aritmetik işlem yapılamaz. 
fiyat2 = "413"
print(fiyat2)
print(type(fiyat2))

# Float => Ondalıklı sayı türündenki veri tipidir. Tanımlama yolu integer ile benzerdir. 

boy = 1.78
print(1.78)
print(type(boy))

# Not: Bölme işlemlerinin sonucu her daim float tipindedir. Tam sayılarla tam bir bölme işlemi yapılsa dahi.

toplamMaliyet = 500
birim = 10
birimMaliyet = toplamMaliyet / birim
print(birimMaliyet)
print(type(birimMaliyet))

# boolean => True veya False değerinde olabilen veri tipidir. Şart bloklarında, döngülerde kullanılır.

havaGunesliMi = False
print(havaGunesliMi)

print(type(2==2))

# Şart bloklarında şarta bağlı olarak True veya False elde edilir. Elde edilenlere göre ise o şart bloğu çalışır.
if 2 == 2:
    print(True)
else:
    print(False)

print(type(2==2))


# List => [] ile tanımlanır. İçindeki bilgiler indexlenebilir, güncellenebilir.

derslerim = ["matematik","fizik","kimya"]
print(derslerim[0]) # indexleme soldan sağa 0 ile başlar. Sağdan sola ise -1 ile
print(derslerim[-1])
derslerim[0] = "algoritma"
print(derslerim[0])

# Tuple => Tanımlamalar normal parantezle yapılabilir. Tuple da sonradan eleman değiştirme, atama işlemi yapılamaz. Indexleme yapılabilir.

kurslar = ("python","excel","AutoCad")
print(kurslar[0])

# Sets => sets'te tanımlamalar süslü parantezle yapılır. Indexlenemezler. Eklemeler yapılabilir.

fruits = {'orange', 'apple', 'banana'}
fruits.add('cherry')
fruits.update(['mango'], ['grape'])
print(fruits)

# Dictionary => key,value düzeni ile çalışan veri tipidir. Key bilgisi ile value ye ulaşmayı sağlar. 41 => kocaeli 34 => istanbul
şehirler = ['kocaeli', 'istanbul']
plakalar = [41, 34]

# Eleman ekleme;

plakalar['ankara'] = 6
print(plakalar)

# Eklediğimiz şekilde güncelleme de yapılabilir.

plakalar['kocaeli'] = 57
print(plakalar)



# Kodlama.io'daki Veri Tipi Örnekleri:-----------------------------------------------------------------------------------------------------------------------------

# Ders programı, Ödev1 gibi ifadeler string tipindedir.

# Ödev sayfasındaki yorum sayısı örneğin 30 integer tipindedir.

# Kursların ve eğitmetlerin sıralaması ise list tipindedir.

# Kursun tamamlanma oranını gösteren ve ilerlemeyi kaydeden kısımda ise şart blokları ve boolean tipinde veriler vardır.

tamamlandıMi = input("Ders tamamlandı mı? (E/H)")

if tamamlandıMi == "E":
    print("Ders tamamlandı.")
else:
    print("Ders tamamlanmadı.")

# Buradaki tamamlandıMi == "E" ifadesi bool tipinde veri vericektir. Bu gelen veriye göre şart bloğu çalışacaktır.


# Şart Blokları:-----------------------------------------------------------------------------------------------------------------------------
# Sitede giriş ekranında e-posta ve şifre soruluyor. Kullanıcıya ait kayıt olan bu bilgiler şart blokları girilen bilgilerle kıyas edilir eğer şartları sağlıyorsa
# giriş onaylanır, sağlanmıyorsa hangi bilginin yanlış girildiğini kullanıcıya belirtir.

kullaniciEposta = "istanbul34@gmail.com"
kullaniciSifre = "12345"

e_posta = input("E-posta giriniz: ")
sifre = input("Şifre giriniz: ")

if e_posta == kullaniciEposta and sifre == kullaniciSifre:
    print("Giriş yapıldı.")
elif e_posta == kullaniciEposta and sifre != kullaniciSifre:
    print("Hatalı sifre girdiniz.")
else:
    print("Kullanıcı bulunamadı.")    












