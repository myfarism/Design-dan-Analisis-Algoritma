# Swap
var1 = 1
var2 = 2
var1, var2 = var2, var1

print(var1, var2)

# Latihan Swap
var1 = 1
var2 = 2
var3 = None

# Menukar Posisi
var3 = var1
var1 = var2
var2 = var3

print(var1, var2)

# Bubble Sort
list1 = [25, 21, 22, 24, 23, 27, 26]

def BubbleSort(myList):
  lastElementIndex = len(myList)-1
  print(0, myList)
  for passNo in range(lastElementIndex, 0, -1):
    for idx in range (passNo):
      if myList[idx] > myList[idx + 1]:
        myList[idx], myList[idx + 1] = myList[idx + 1], myList[idx]
      print(idx + 1, myList)
  return myList


BubbleSort(list1)

# Latihan Bubble Sort
list2 = [100, 20, 60, 90, 40, 30, 10]

def latihanBubbleSort(myList):
  lastElementIndex = len(myList)-1
  print(0, myList)
  for passNo in range(lastElementIndex, 0, -1):
    for idx in range (passNo):
      if myList[idx] > myList[idx + 1]:
        myList[idx], myList[idx + 1] = myList[idx + 1], myList[idx]
      print(idx + 1, myList)
  return myList


latihanBubbleSort(list2)

# Insertion Sort
def InsertionSort(myList):
  for i in range (1, len(myList)):
    j = i - 1
    next = myList[i]

    while (myList[j] > next) and (j >= 0):
      myList[j + 1] = myList [j]
      j = j - 1
      myList[j + 1] = next
  return myList

listInsert = [35, 31, 32, 34, 33 ,37, 36]
print(listInsert)
InsertionSort(listInsert)

# Latihan Insertion Sort
def latihanInsertionSort(myList):
  for i in range (1, len(myList)):
    j = i - 1
    next = myList[i]

    while (myList[j] > next) and (j >= 0):
      myList[j + 1] = myList [j]
      j = j - 1
      myList[j + 1] = next
  return myList

listLatihanInsertion = [89, 12, 57, 16,25, 11, 75]
print(listLatihanInsertion)
latihanInsertionSort(listLatihanInsertion)

# Selection Sort
def SelectionSort(myList):
  for fill_slot in range(len(myList) - 1, 0, -1):
    max_index = 0
    for location in range(1, fill_slot + 1):
      if myList[location] > myList[max_index]:
        max_index = location
    myList[fill_slot], myList[max_index] = myList[max_index], myList[fill_slot]
  return myList

listSelection = [70, 15, 25, 19, 34, 44]
print(listSelection)
SelectionSort(listSelection)

# Latihan Selection Sort
def SelectionSort(myList):
  for fill_slot in range(len(myList) - 1, 0, -1):
    max_index = 0
    for location in range(1, fill_slot + 1):
      if myList[location] > myList[max_index]:
        max_index = location
    myList[fill_slot], myList[max_index] = myList[max_index], myList[fill_slot]
  return myList

listLatihanSelection = [89, 12,57, 16, 25]
print(listLatihanSelection)
SelectionSort(listLatihanSelection)

# Linear Search
def LinearSearch(myList, item):
  index = 0
  found = False

  while index < len(myList) and found is False:
    if myList[index] == item:
      found = True
    else:
      index = index + 1
  return found

listLinear = [12, 33, 11, 99, 22, 55, 90]
print(listLinear)
print(LinearSearch(listLinear, 12))
print(LinearSearch(listLinear, 91))

# Latihan Linear Search
def latihanLinearSearch(myList, item):
  index = 0
  found = False

  while index < len(myList) and found is False:
    if myList[index] == item:
      found = True
    else:
      index = index + 1
  return found

latihanLinear = ['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p',]
print(latihanLinearSearch(latihanLinear, 'a'))

# Binary Search
def BinarySearch(myList, item):
  first = 0
  last = len(myList) - 1
  found = False

  while first <= last and not found:
    midpoint = (first + last) // 2
    if myList[midpoint] == item:
      found = True
    else:
      if item < myList[midpoint]:
        last = midpoint - 1
      else:
        first = midpoint + 1
  return found

listBinary = [12, 33, 11, 99, 22, 55, 90]
print(BinarySearch(listBinary, 12))
print(BinarySearch(listBinary, 91))

# Latihan Binary Search
def latihanBinarySearch(myList, item):
  first = 0
  last = len(myList) - 1
  found = False

  while first <= last and not found:
    midpoint = (first + last) // 2
    if myList[midpoint] == item:
      found = True
    else:
      if item < myList[midpoint]:
        last = midpoint - 1
      else:
        first = midpoint + 1
  return found

latihanBinary = ['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p',]
print(latihanBinarySearch(latihanBinary, 'a'))

# Interpolation Search
def IntPolSearch(myList, x):
  idx0 = 0
  idxn = (len(myList) - 1)
  found = False
  while idx0 <= idxn and x >= myList[idx0] and x <= myList[idxn]:

    mid = idx0 + int(((float(idxn - idx0) / (myList[idxn] - myList[idx0])) * (x - myList[idx0])))

    if myList[mid] == x:
      found = True
      return found

    if list[mid] < x:
      idx0 = mid + 1
  return found

listIntPol = [12, 33, 11, 99, 22, 55, 90]
print(IntPolSearch(listIntPol, 12))
print(IntPolSearch(listIntPol, 91))

# Latihan Interpolation Search
def latihanIntPolSearch(myList, x):
  idx0 = 0
  idxn = (len(myList) - 1)
  found = False
  while idx0 <= idxn and x >= myList[idx0] and x <= myList[idxn]:

    mid = idx0 + int(((float(idxn - idx0) / (myList[idxn] - myList[idx0])) * (x - myList[idx0])))

    if myList[mid] == x:
      found = True
      return found

    if list[mid] < x:
      idx0 = mid + 1
  return found

latihanIntPol = ['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p',]
print(latihanIntPolSearch(latihanIntPol, 'u'))
