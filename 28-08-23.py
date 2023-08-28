"""Algoritma:

1. Jika n = 0, return nilai m sebagai hasil dan stop. Jika tidak, kembali ke Step 2
2. Bagi nilai m dengan n, masukan nilai sisanya ke r
3. Masukan nilai n ke m dan nilai r ke n. kembali ke Step 1


pseudocode:

While n =! 0 do
r <--- m mod n
m <--- n
n <--- r
return m




Bilangan Prima
-----------------

Algoritma:



Psuedocode:

Fungsi adalahPrima(angka):
    Jika angka <= 1 maka
        Kembalikan False
    Jika angka <= 3 maka
        Kembalikan True
    Jika angka habis dibagi 2 atau angka habis dibagi 3 maka
        Kembalikan False
    i = 5
    Selama i * i <= angka maka
        Jika angka habis dibagi i atau angka habis dibagi (i + 2) maka
            Kembalikan False
        i = i + 6
    Kembalikan True

Fungsi tampilkanBilanganPrima(batas_atas):
    list_prima = []  # Inisialisasi list untuk bilangan prima
    Untuk setiap angka dari 2 hingga batas_atas lakukan:
        Jika adalahPrima(angka) maka
            Tambahkan angka ke list_prima
    Tampilkan list_prima

"""
#Code:

#Fungsi
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def display_primes(upper_limit):
    prime_list = []
    for number in range(2, upper_limit + 1):
        if is_prime(number):
            prime_list.append(number)
    return prime_list

# Menggunakan fungsi untuk menampilkan bilangan prima hingga batas atas tertentu (contoh: 50)
upper_limit = 50
primes = display_primes(upper_limit)
print("Bilangan prima hingga", upper_limit, "adalah:")
print(primes)
