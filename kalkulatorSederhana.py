# Kalkulator sederhana
print(20*"=")
print(f"Kalkulator Sederhana")
print(20*"=")

angka_1 = float(input(f"Masukkan angka 1: "))
operator = str(input(f"Masukkan operasi matematika (+, -, /, *): "))
angka_2 = float(input(f"Masukkan angka 2: "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasil operasi: {hasil:,}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasil operasi: {hasil:,}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasil operasi: {hasil:,}")
elif operator== "*":
    hasil = angka_1 * angka_2
    print(f"Hasil operasi: {hasil:,}")
else:
    print(f"Salah input woy")
    
print(f"Kamu mendapatkan jawaban yang kamu inginkan!!")