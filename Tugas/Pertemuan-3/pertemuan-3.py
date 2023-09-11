# -*- coding: utf-8 -*-
"""
Pertemuan 3
"""

aList = ["John", 33, "Toronto", True]
print(aList)

from datetime import date

x = date.today()
tanggal = x.strftime("%B %d, %Y")

mahasiswa = ["Faris", "2022071068", "Informatika", "Design dan Analisis Algoritma", tanggal, "Universitas Pembangunan Jaya"]

print("Mahasiswa = ", mahasiswa, "\n")

# Cetak NIM
print("# Cetak NIM")
print(mahasiswa[1], "\n")

# Cetak Nama Universitas
print("# Cetak Nama Universitas")
print(mahasiswa[-1], "\n")

# Slicing Nim dan Prodi
print("# Slicing NIM dan Prodi")
print(mahasiswa[1:3], "\n")

# Iterasi
print("# Iterasi")
for x in mahasiswa:
  print("UPJ " + x)

bin_colors = ['Red', 'Green', 'Blue', 'Yellow']
print("bin_colors = ", bin_colors, "\n")

print("# Print Index ke-1")
print(bin_colors[1], "\n")

# Slicing
print("# Slicing")
print(bin_colors[0:2],  "\n")

# Iterasi
print("# Iterasi")
for i in bin_colors:
  print(i + " Square")

# Tuple
bin_colors = ('Red', 'Green', 'Blue', 'Yellow')
print(bin_colors, "\n")

print(bin_colors[1])
print(bin_colors[2:], "\n")

# UPJ
UPJ = ('Universitas', 'Pembangunan', 'Jaya')
print(UPJ, "\n")

# Nested Tuple
print("# Nested Tuple")
hariAwal = ("Senin", "Selasa", "Rabu")
hariAkhir = ("Kamis", "Jumat", "Sabtu")

hari = (hariAwal, hariAkhir)
print(hari, "\n")

# Latihan Nested Tuple
print("# Latihan")
pertama = (100)
kedua = (200, 400, 600)
ketiga = (300)
keempat = (400, 800)
nested_tuple = (pertama, kedua, ketiga, keempat)
print(nested_tuple)

# Dictionary
print("# Dictionary")
bin_colors = {
    "manual_color": "Yellow",
    "approved_color": "Green",
    "refused_color": "Red"
}
print(bin_colors, "\n")

# Mengambil Nilai
print("# Mengambil Nilai")
print(bin_colors.get('approved_color'))
print(bin_colors['approved_color'], "\n")

# Memperbarui Nilai
print("# Memperbarui Nilai")
bin_colors['approved_color'] = "Purple"
print(bin_colors, "\n")

# Latihan Dictionary
print("# Latihan")
data_mahasiswa = {
    "Nama": "Faris",
    "NIM": 2022071068,
    "Prodi": "Informatika",
    "Universitas": "UPJ"
}
print(data_mahasiswa)

# Sets
green = {'grass', 'leaves'}
print(green, "\n")

# Inisiasi set dan merubah list menjadi set
# Inisiasi set
print("# Inisiasi set dan merubah list menjadi set")
set_01 = {4, 5, 6, 2}
print(set_01, "\n")

# Inisiasi merubah list menjadi set
print("# Inisiasi merubah list menjadi set")
set_02 = set()
set_03 = set([2, 1, 4, 3])
print(type(set_02))
print(set_03, "\n")

# Menambah anggota set
print("# Menambah anggota set")
set_04 = {2, 3, 4, 5, 6}
print(set_04)
set_04.add(1)
print(set_04, "\n")

# Menghapus nilai 4
print("# Menghapus nilai 4")
set_04.discard(4)
print(set_04, "\n")

# Menambahkan nilai 10
print("# Menambahkan nilai 10")
set_04.add(10)
print(set_04)

# Union Set
print("# Union Set")
set_A = {1, 2, 3, 4}
print("set_A = ", set_A)
set_B = {3, 4, 5, 6}
print("set_B = ",set_B)
print(set_A | set_B)
print(set_A.union(set_B), "\n")

# Intersection Set
print("# Intersection Set")
print(set_A & set_B)
print(set_A.intersection(set_B), "\n")

# Difference Set
print("# Difference Set")
print(set_A - set_B)
print(set_A.difference(set_B), "\n")

# Symmetric Difference Set
print("# Symmetric Difference Set")
print(set_A ^ set_B)
print(set_A.symmetric_difference(set_B), "\n")

# Latihan Union Set
print("# Latihan")
yellow = {'dandelions', 'leaves', 'fire hydrant'}
red = {'fire hydrant', 'blood', 'rose', 'leaves'}
print("yellow = ", yellow)
print("red = ", red)
print(yellow | red)
print(yellow & red)

# DataFrames
print("# DataFrames")
import pandas as pd
df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]
])
df.columns = ['id', 'name', 'age', 'decision']
print(df, "\n")

# Seleksi kolom
print("# Seleksi Kolom")
df[['name', 'age']]
print(df, "\n")

# Latihan DataFrames
print("# Latihan")
mhs = pd.DataFrame([
    ['1', 'Informatika', 50, 30, 20],
    ['2', 'Sistem Informasi', 55, 30, 25],
    ['3', 'Teknik Sipil', 40, 30, 10]
])
mhs.columns = ['No', 'Prodi', 'Mahasiswa', 'Lakilaki', 'Perempuan']
print(mhs)

import numpy as np

# Matrix
print("# Matrix")
myMatrix = np.array([[11, 12, 13], [21, 22 ,23], [31, 32, 33]])
print(myMatrix)
print(type(myMatrix), "\n")

# Transpose Matrix
print("# Transpose Matrix")
matrixC = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix C = ")
print(matrixC, "\n")
print("# Setelah ditranspose")
transpose_matrixC = np.transpose(matrixC)
print("Transpose Matrix C = ")
print(transpose_matrixC)

# Latihan Matrix
print("# Latihan")
matrixL = np.array([[100, 200, 300], [700, 600, 500], [900, 1000, 800]])
print("Matrix Latihan = ")
print(matrixL, "\n")
print("# Setelah ditranspose")
transpose_matrixL = np.transpose(matrixL)
print("Transpose Matrix Latihan = ")
print(transpose_matrixL)

import numpy as np

# Vektor
print("# Vektor \n")
# Menggunakan List
print("# Menggunakan List")
vector1 = [22,33,44,55]
print(vector1)
print(type(vector1))

# Menggunakan array
print("\n# Menggunakan array")
vector2 = np.array([22,33,44,55])
print(vector2)
print(type(vector2))

# Stack

# Membuat class stack
class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items)-1]
  def size(self):
    return len(self.items)

# Penggunaan class Stack
print("# Stack")
stack = Stack()
stack.push('Red')
stack.push('Green')
stack.push('Blue')
stack.push('Yellow')

print(stack.pop())
print(stack.isEmpty())

# Queue
print("# Queue")

# Membuat class queue
class Queue(object):
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def enqueue(self, item):
    self.items.insert(0, item)
  def dequeue(self):
    return self.items.pop()
  def size(self):
    return len(self.items)

# Penggunaan class queue
queue = Queue()
queue.enqueue('Red')
queue.enqueue('Green')
queue.enqueue('Blue')
queue.enqueue('Yellow')

print("\n# Melihat size dari queue")
print(queue.size())

print("\n# Mengeluarkan queue pertama")
print(queue.dequeue())

print("\n# Mengeluarkan queue Kedua")
print(queue.dequeue())

# Tree
print("# Tree\n")

# Membuat class tree
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.data),
        if self.right:
            self.right.print_tree()

# Penggunaan class tree
root = Node(2)#root
root.left = Node(3) #child kiri dari root
root.right = Node(5) #child kanan dari root
root.left.left = Node(7) #child kiri dari 3
root.left.right = Node(9) #child kanan dari 3
root.right.left = Node(11) #child kiri dari 5
root.right.right = Node(13) #child kanan dari 5
root.print_tree()
