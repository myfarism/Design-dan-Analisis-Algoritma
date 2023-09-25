# Summation
arr = [3, 7, 5, 2, 1, 8, 9]
total = 0
for i in range(len(arr)):
  total = total + arr[i]

print(total)

# Inversi
def countInversion(arr):
  result = 0
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] > arr[j]:
        result += 1
  return result

arr = [21, 70, 36, 14, 25]
print(countInversion(arr))

# MinMaks (divide-conquer)
def divideAndConquer_Max(arr, ind, len):
  maximum = -1

  if (ind >= len - 2):
    if (arr[ind] > arr[ind + 1]):
      return arr[ind]
    else:
      return arr[ind + 1]

  maximum = divideAndConquer_Max(arr, ind + 1, len)

  if (arr[ind] > maximum):
    return arr[ind]
  else:
    return maximum

def divideAndConquer_Min(arr, ind, len):
  minimum = 0

  if (ind >= len - 2):
    if (arr[ind] < arr[ind + 1]):
      return arr[ind]
    else:
      return arr[ind + 1]

  minimum = divideAndConquer_Min(arr, ind + 1, len)

  if (arr[ind] < minimum):
    return arr[ind]
  else:
    return minimum



minmum, maximum = 0, -1

arr = [4, 12, 23, 9, 21, 1, 35, 2, 24]

maximum = divideAndConquer_Max(arr, 0, 9)
minimum = divideAndConquer_Min(arr, 0, 9)

print("The minimum number in the array is: ", minimum)
print("The maximum number in the array is: ", maximum)

# Merge Sort
def mergeSort(array):
  if len(array) > 1:
    r = len(array) // 2
    L = array[:r]
    M = array[r:]

    mergeSort(L)
    mergeSort(M)

    i = j = k = 0

    while i < len(L) and j < len(M):
      if L[i] < M[j]:
        array[k] = L[i]
        i += 1
      else:
        array[k] = M[j]
        j += 1
      k += 1

    while i < len(L):
      array[k] = L[i]
      i += 1
      k += 1

    while j < len(M):
      array[k] = M[j]
      j += 1
      k += 1

def printList(array):
  for i in range(len(array)):
    print(array[i], end=" ")
  print()

array = [4, 12, 23, 9, 21, 1, 35, 2, 24]

mergeSort(array)

print("Sorted array is: ")
printList(array)

# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

data = [4, 12, 23, 9, 21, 1, 35, 2, 24]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print("Sorted array in Ascending Order:")
print(data)

# Maximum Subarray Sum

def maxSubSum(arr):
  max_so_far = 0
  max_ending_here= 0
  for i in range(len(arr)):
    max_ending_here += arr[i]
    if max_ending_here > max_so_far:
      max_so_far = max_ending_here
    if max_ending_here < 0:
      max_ending_here = 0
  return max_so_far

arr = [-2, -5, 6, -2, -3, 1, 5, -6]

result = maxSubSum(arr)
print(result)

# Max Crossing Sum
def maxCrossingSum(arr, low, mid, high):
    result = 0
    leftSum = float('-infinity')

    for i in range(mid, low - 1, -1):
        result += arr[i]
        if result > leftSum:
            leftSum = result

    result = 0
    rightSum = float('-infinity')

    for i in range(mid + 1, high + 1):
        result += arr[i]
        if result > rightSum:
            rightSum = result

    return leftSum + rightSum

def maxSum(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    return max(maxSum(arr, low, mid),
               maxSum(arr, mid + 1, high),
               maxCrossingSum(arr, low, mid, high))

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
result = maxSum(arr, 0, len(arr) - 1)
print(result)

# Longest Common Prefix
def longestCommonPrefix(a):
  size = len(a)

  if (size == 0):
    return ""

  if (size == 1):
    return a[0]

  a.sort()

  end = min(len(a[0]), len(a[size - 1]))

  i = 0
  while (i < end and a[0][i] == a[size - 1][i]):
    i += 1

  pre = a[0][0:i]
  return pre

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
result = longestCommonPrefix(arr)
print(result)

arr = ["apple", "ape", "april"]
result = longestCommonPrefix(arr)
print(result)

# Median Array
def medianOfArray( arr1, arr2, n):
  m1 = -1
  m2 = -1
  count = 0
  i=j=0
  while count < n+1:
    count += 1
    if i ==n:
      m1 = m2
      m2 = arr2[0]
      break
    if j == n:
      m1 = m2
      m2 = arr1[0]
      break
    if arr1[i] < arr2[j]:
      m1 = m2
      m2 = arr1[i]
      i += 1
    else:
      m1 = m2
      m2 = arr2[j]
      j += 1
  return (m1 + m2) // 2

arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]

result = medianOfArray(arr1, arr2, len(arr1))

print(result)

def solution(arr):
  n = len(arr)

  if n % 2 == 0:
    z = n // 2
    e = arr[z]
    q = arr[z - 1]
    ans = (e + q) / 2
    return ans
  else:
    z = n // 2
    ans = arr[z]
    return ans

arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]

arr3 = arr1 + arr2

arr3.sort()
print("Median = ", solution(arr3))

# Floor in sorted array
def floorSorted (arr,low, high,x) :
  if low > high:
    return -1
  if arr[low] > x:
    return -1
  if arr[high] <= x:
    return arr[high]

  mid=(low+high)//2

  if arr[mid]==x:
    return arr[mid]
  if mid > 0 and x >= arr[mid-1] and arr[mid] > x:
    return arr[mid-1]
  if mid < high and x < arr[mid+1] and x >= arr[mid]:
    return arr[mid]
  if x > arr[mid]:
    return floorSorted (arr, mid+1, high, x)
  else:
    return floorSorted (arr, low, mid-1,x)

arr = [1, 2, 8, 10, 12, 14, 19]
x = 5
print(floorSorted(arr, 0, len(arr) - 1, x))

# Mencari nilai terdekat dengan metode divide dan conquer
def closestNumber (arr, low, high, x):
  if low > high:
    return -1
  if arr[high] <= x:
    return arr[high]
  if arr[low] >= x:
    return arr[low]
  mid=(low+high)//2
  if arr[mid]==x:
    return arr[mid]
  abs_mid = abs(arr[mid]-x)
  if mid > 0:
    abs_left = abs(arr [mid-1]-x)
    if abs_left < abs_mid:
      return closestNumber (arr, low, mid-1,x)
  if mid < high:
    abs_right = abs(arr[mid+1]-x)
    if abs_right < abs_mid:
      return closestNumber (arr, mid+1, high, x)
  #print ('after')
  return arr[mid]

arr = [2, 5, 6, 7, 8, 8, 9]
x = 9
print(closestNumber(arr, 0, len(arr) - 1, x))

def find_closest(lst, k):
  lst.sort()
  closest_num = lst[0]
  for num in lst:
    if abs(num - k) < abs(closest_num - k):
      closest_num = num
    if num > k:
      break
  return closest_num

lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
k = 9.1
print(find_closest(lst, k))

lst = [2, 5, 5, 7, 8, 8, 9]
k = 6
print(find_closest(lst, k))

# Mencari fixed point dengan metode divide dan conquer
def fixedPoint(arr, low, high):
  if low > high:
    return -1
  if arr[high] == high:
    return arr[high]
  if arr[low] == low:
    return arr[low]
  mid = (low + high) // 2
  if arr[mid] == mid:
    return arr[mid]
  if mid > arr[mid]:
    return fixedPoint(arr, mid + 1, high)
  else:
    return fixedPoint(arr, low, mid - 1)

arr = [9, 1, 4, 5, 2]
print(fixedPoint(arr, 0 , len(arr) - 1))
