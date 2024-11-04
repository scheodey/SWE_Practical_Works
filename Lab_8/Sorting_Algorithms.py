import matplotlib.pyplot as plt
import numpy as np
import time

#Exercise 2. Modified Bubble Sort with Early Stopping
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to track if any swapping happens
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        # If no two elements were swapped, the list is already sorted
        if not swapped:
            break
    return arr

# Test the modified bubble sort function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result with Early Stopping:", sorted_arr)



#Step 2: Implement Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)


#Step 3: Implement Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)


#Step 4: Compare Performance
import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)


#Exercise 
#1. In-Place Quick Sort Implementation
def quick_sort_in_place(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Taking the last element as pivot
    i = low - 1        # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
    return i + 1

# Test the in-place quick sort function
test_arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort_in_place(test_arr, 0, len(test_arr) - 1)
print("In-Place Quick Sort Result:", test_arr)


import matplotlib.pyplot as plt

# Modified Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test variables
test_arr_bubble = [64, 34, 25, 12, 22, 11, 90]
test_arr_merge = [64, 34, 25, 12, 22, 11, 90]
test_arr_quick = [64, 34, 25, 12, 22, 11, 90]

# Visualize sorting results
def visualize_sorting(sorting_algorithm, arr, title):
    sorted_arr = sorting_algorithm(arr.copy())  # Sort the array
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(sorted_arr)), sorted_arr, color='blue')
    plt.title(title)
    plt.xlabel('Array Index')
    plt.ylabel('Value')
    plt.xticks(range(len(sorted_arr)))  # Set x-ticks to match the array indices
    plt.show()

# Visualize Bubble Sort
visualize_sorting(bubble_sort, test_arr_bubble, "Bubble Sort Result")

# Visualize Merge Sort
visualize_sorting(merge_sort, test_arr_merge, "Merge Sort Result")

# Visualize Quick Sort
visualize_sorting(quick_sort, test_arr_quick, "Quick Sort Result")