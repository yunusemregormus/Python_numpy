# Bir matris veriliyor. Bu matrisin:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# Her bir sütunun toplamını hesapla.
# Her bir satırın ortalamasını bul.
# Matrisin transpozunu al.


import numpy as np

matris = np.array([

    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(matris)

# Her bir sütunun toplamını hesapla.
sutun_toplam = np.sum(matris,axis=0)
print("Sütun toplamı : ",sutun_toplam)

# Her bir satırın ortalamasını bul.
satir_ortalama = np.mean(matris,axis=1)
print("satır ortalamaları : ", satir_ortalama)

# Matrisin transpozunu al.
transpozu = np.transpose(matris)
print("transpozu : ", transpozu)