A = [
    [2, 4],
    [3, 1]
]

B = [
    [7, 2],
    [5, 6]
]

n = 2

C = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  for j in range(n):
    for k in range(n):
      C[i][j] += A[i][k] * B[k][j]

for row in C:
  print(row)

#Perkalian matriks
mat1 = [
    [7, 0],
    [4, 6],
]

mat2 = [
    [3, 0],
    [5, 2],
]

mat3 = []

for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)

for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):
        print(mat3[x][y], end=' ')
    print()

n = int(input("Masukan nilai n: "))

for k in range(2, (n-1)):
  if n % k == 0:
    print(k)

# 1. Faktorial

def faktorial(n):
    if (n==1):
        return n
    return faktorial(n-1)*n

n = int(input("Masukkan nilai n: ")) #input nilai
print(f"Hasil dari {n}! adalah: ", faktorial(n)) #output nilai

# Mencari element terbesar

def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai

    return nilai_terbesar

a = [3, 20, 100, -35, 50]

print(a)
print('Nilai terbesar:', nilai_maksimal(a))

# Mencari element terkecil

def nilai_minimal(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai

    return nilai_terkecil

a = [3, 20, 100, -35, 50]

print(a)
print('Nilai terkecil:', nilai_minimal(a))

#Sequential Search

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 2))

def seqSearch(alist, item):
    k = 0
    found = False

    while k < len(alist) and not found:
        if alist[k] == x:
            found = True
        else:
            k = k + 1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 2))

#bubble Sort

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

def bubble_sort(L):
    for n in range(len(L)):
      for i in range(n):
          for k in range(n - 1, i, -1):
              if L[k] < L[k - 1]:
                  # Tukar elemen jika elemen sekarang lebih kecil dari elemen sebelumnya
                  temp = L[k]
                  L[k] = L[k - 1]
                  L[k - 1] = temp

# Contoh penggunaan:
list_angka = [5, 2, 9, 3, 8, 6]
bubble_sort(list_angka)
print(list_angka)

#Uji Keprimaan

x = int(input('Input Satu angka bulat: '))

angka_prima = True
if((x==0) or (x==1)):
    angka_prima = False
else:
    for i in range(2,(x//2)):
        if((x%i)== 0):
            angka_prima = False
            break

if(angka_prima):
    print(x,'Adalah Angka Prima')
else:
    print(x,'bukan angka prima')

# Polynomial
def polynomial_py(a,x):
    result = 0
    for n,a_n in enumerate(a):
        x_power_n = 1
        for i in range(n):
            x_power_n *= x
        result += a_n * x_power_n
    return result

a = [1,2,0,3]# coefficient
x = 1.5
print(polynomial_py(a,x))

#Get Matching substring in string
# Initializing string
test_str = "GFG is good website";

#initializing potential substrings
test_list = ["GFG","stie","Geeks","Tutorial"]

#printing original string
print("The orginal string is : "+ test_str)

#printing potential string list
print("The original list is: "+str(test_list))

#using list comprehension
#Get matching substrings in string
res = [sub for sub in test_list if sub in test_str]
#printing result
print("The list of foun subsrings : "+ str(res))

#Mencari pasangan titik jarak terdekat

from math import sqrt
from random import randint

titik = []
n = int(input('Masukkan jumlah titik yang ingin Anda cari jaraknya: '))
for i in range(0,n):
    titik.append([randint(0,100),randint(0,100)])
print('Titik:\n',titik)
def hitungjarak(lis):
    lisjarak = []
    for i in range (0,len(lis)-1):
        for j in range (i+1,len(lis)):
            jarak = sqrt((lis[i][0]-lis[j][0])**2 + (lis[i][1]-lis[j][1])**2)
            lisjarak.append(jarak)
            print('Titik: ',lis[i], 'Titik: ',lis[j],': ',jarak)
    return min(lisjarak)
print('Jarak terdekat:\n',hitungjarak(titik))

#Find Maximum Value in Linear Search

def find_maximum(lst):
    max = None
    for el in lst:
        if max == None or el > max:
            max = el
    return max
test_scores = [88,93,75,100,80,67,71,92,90,83]
print(find_maximum(test_scores)) #returns 100

def bubblesort(alist):
    for passnum in range (len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist = [54,26,93,17,77,31,44,55,20]
bubblesort(alist)
print(alist)

def Sequential_Search(dlist, item):

    pos = 0
    found = False

    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found, pos

print(Sequential_Search([11,23,58,31,56,77,43,12,65,19], 31))

#algoritma Brute Force: pangkat

bilangan = int(input('Masukkan bilangan: '))
pangkat = int(input('Masukkan pangkat: '))

def hitung_pangkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitung_pangkat(bilangan, pangkat - 1)

    return bilangan

hasil = hitung_pangkat(bilangan, pangkat)
print(f'Hasil = {hasil}')

#algoritma Brute Force: Faktorial

n = int(input('Masukkan nilai n: '))

def hitung_faktorial (n):
    if n > 2:
        return n * hitung_faktorial(n - 1)


    return 2

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')

#slide 75
#algoritma Brute Force: String matching

def string_match(string, sub_str):
    # Brute force string matching
    for i in range(len(string)-len(sub_str)+1):
        index = i # index Point to the 1 Three characters to be compared
        for j in range(len(sub_str)):
            if string[index] == sub_str[j]:
                index += 1
            else:
                break
            if index-i == len(sub_str):
                return i
    return -1

if __name__ == "__main__":
    print(string_match("adbcbdc","bdc"))

#Algoritma Brute Force

import random
from itertools import permutations
alltours = permutations

def distance_tour(aTour):
    return sum(distance_points(aTour[i - 1], aTour[i])
        for i in range(len(aTour)))

aCity = complex
def distance_points(first, second):
    return abs(first - second)

def generate_cities (number_of_cities):
    seed=111;width=500;height=300
    random.seed((number_of_cities, seed))
    return frozenset(aCity(random.randint(1, width), random.randint(1,height))
        for c in range(number_of_cities))

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

def visualize_tour(tour, style='bo-'):
    if len(tour) > 1000: plt.figure(figzice=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')
def visualize_segment (segment, style='bo-'):
        plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
        plt.axis('scaled')
        plt.axis('off')

def X(city): "X axis"; return city.real

def Y(city): "Y axis"; return city.imag

from time import process_time
from collections import Counter
def tsp(algorithm, cities):
    t0 = process_time()
    tour = algorithm(cities)
    t1 = process_time()
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}:{} cities => tour lenght {:.0f}(in {:.3f} sec)".format(name(algorithm), len(tour), distance_tour(tour), t1-t0))

def name(algorithm): return algorithm.__name__.replace('_tsp','')

#strategi algoritma brute force
def brute_force(cities):
    "Generate all possible tours of the cities and choose the shortest tour."
    return shortest_tour(alltours(cities))
def shortest_tour(tours): return min(tours, key=distance_tour)

tsp(brute_force, generate_cities(10))
