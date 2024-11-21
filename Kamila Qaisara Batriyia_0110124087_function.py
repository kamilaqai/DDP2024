# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit 

#cetak 0 celcius ke 32 fahrenheit dan cetak 100 celcius ke 212 fahrenheit
suhu_celcius1 = 0
suhu_celcius2 = 100
suhu_fahrenheit1 = celcius_ke_fahrenheit (suhu_celcius1)
suhu_fahrenheit2 = celcius_ke_fahrenheit (suhu_celcius2)
print('Suhu Celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)
print('Suhu Celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)

# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
print()
print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung= bilangan % 2 == 0 #Menentukan bilangan ganjil atau genap
    return hitung #Mengembalikan nilai hitung 

angka = 4
hasil = genap_ganjil(angka)
print(f'Bilangan {angka} bernilai {hasil}')
angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f'Bilangan {angka2} bernilai {hasil2}')

#  Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus 
print()
print('## Nomor 3 ##')
def cek_kelulusan(nilai):
    if nilai > 60:
        return 'Lulus'
    else:
        return 'Gagal'
nilai_kamu = 80
status =cek_kelulusan(nilai_kamu)
print(f'Nilai: {nilai_kamu}, Status: {status}')
nilai_kamu2 = 60
status2 =cek_kelulusan(nilai_kamu2)
print(f'Nilai: {nilai_kamu2}, Status: {status2}')

# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
print()
print('## Nomor 4 ##')
def bilangan_ganjil(number):
    for a in range(1, number, 2):
        print(a, end=" ")

bilangan_ganjil(20)