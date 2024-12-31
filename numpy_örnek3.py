# 5x5 boyutunda, 0 ile 100 arasında rastgele tamsayılarla dolu bir matris oluştur.
# Matristeki maksimum ve minimum değerleri bul.
# Matriste 50'den küçük olan değerleri 0 yap.


import numpy as np
# 1. Rastgele 5x5 matris oluştur
np.random.seed(42) # Sonuçların tekrarlanabilir olması için random seed komutu kullanıldı.
matris = np.random.randint(0,101,(5,5))
print("orijinal matis: \n", matris)

# 2. Maksimum ve minimum değerleri bul
maks_deger = np.max(matris)
min_deger =  np.min(matris)
print("maksimum değer : ", maks_deger)
print("minimum değer :", min_deger)

# 3. 50'den küçük olan değerleri 0 yap
matris[matris<50]=0
print("Düzenlenmiş matris : \n",matris)