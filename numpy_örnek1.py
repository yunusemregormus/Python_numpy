import numpy as np
# kahvaltı listesi oluşturalım
kahvalti_listesi = np.array(["Yumurta","Peynir","Bal(hayatımın anlam bütünlüğü)","Zeytin","Domates","Çay","Çemen","Sucuk"])

# listenin 3. elemanı nedir
print("listenin 3. elemanı = " + kahvalti_listesi[2])

# listenin sondan ikinci eleman nedir
print("listenin sondan ikinci elemanı = " + kahvalti_listesi[-2])

# listedeki 1.,2.,3. elemanlarını listele
print("listedeki 1., 2., 3. elemanların listesi = " + kahvalti_listesi[:3])

# aralıkta ilk indexi belirtmezsen nolur
print("aralıkta ilk indexi belirtmezsen nolur = " + kahvalti_listesi[6:])

# aralıkta son indexi belirtmezsen nolur
print("aralıkta son indexi belirtmezsen nolur = " + kahvalti_listesi[1:])

# listenin tüm elemanları göster
for e in kahvalti_listesi:
    print("listenin tüm elemanları = " + e)

# listede kaç eleman var
print(len(kahvalti_listesi))

# listede kaşar var mı?
if "kaşar" in kahvalti_listesi:
    print("listede kaşar var")
else:
    print("listede kaşar yok")

# listenin sonuna kaşar ekleyelim
kahvalti_listesi = np.append(kahvalti_listesi, "kaşar")
print(kahvalti_listesi)

# salatalığı 3. sıraya ekleyelim
kahvalti_listesi = np.insert(kahvalti_listesi,2,"salatalık")
print(kahvalti_listesi)