#Hasil konversi suhu

print('=== Celcius ke Fahrenheit ===')
celcius = float(input('Masukkan suhu: '))
fahrenheit = (9/5)*celcius + 32
print('Suhu dalam fahrenheit: ', fahrenheit, "fahrenheit")

print("=== Fahrenheit ke Kelvin ===")
fahrenheit = float(input('Masukkan suhu: '))
celcius = (9/5)*fahrenheit - 32
kelvin = celcius + 273
print('Suhu dalam kelvin: ', kelvin, 'Kelvin')

print("=== Kelvin ke Fahrenheit ===")
kelvin = float(input('Masukkan suhu: '))
celcius = kelvin - 273
fahrenheit = (9/5)*celcius + 32
print('Suhu dalam Fahrenheit: ', fahrenheit, "fahrenheit")