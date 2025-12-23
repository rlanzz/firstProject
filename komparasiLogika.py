# Latihan soal
# 1. --- 0 +++ 5 --- 8 +++
# 2. +++ 0 --- 5 +++ 8 ---

# NOMOR 1
inputUser = float(input('Masukkan angka antara 0 hingga 5 atau lebih 8: '))
# Lebih dari 0
isLebihDari = inputUser > 0 
print('Angka yang kamu masukkin:', isLebihDari)
# Kurang dari 5
isKurangDari = inputUser < 5
print('Angka yang kamu masukkin:', isKurangDari)
# Lebih dari 8
isLebihDari2 = inputUser > 8
print('Angka yang kamu masukkin:', isLebihDari2)
# Hasil akhir
isCorrect = isLebihDari and isKurangDari or isLebihDari2
print('Angka hasil yang kamu masukkin:', isCorrect)

# NOMOR 2
inputUser = float(input('Masukkan angka kurang dari 0 atau antara 5 dengan 8: '))
# Kurang dari 0
inputAnjay = inputUser < 0
print('Angka yang kamu masukkin:', inputAnjay)
# Antara 5 dan 8
inputAnjir = 5 < inputUser < 8
print('Angka yang kamu masukkin:', inputAnjir)
# Hasil akhir 
isBenar = inputAnjay or inputAnjir
print('Angka hasil akhir kamu:', isBenar)
