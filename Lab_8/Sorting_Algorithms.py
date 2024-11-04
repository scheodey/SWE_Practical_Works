import matplotlib.pyplot as plt
import numpy as np
import time
import random

class Sorter:
    def __init__(self, data):
        self.data = data

    def bubble_sort(self):
        arr = self.data.copy()
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

    def merge_sort(self):
        return self._merge_sort_helper(self.data.copy())

    def _merge_sort_helper(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort_helper(arr[:mid])
        right = self._merge_sort_helper(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
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

    def quick_sort(self):
        return self._quick_sort_helper(self.data.copy())

    def _quick_sort_helper(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return self._quick_sort_helper(less) + [pivot] + self._quick_sort_helper(greater)

    def quick_sort_in_place(self):
        arr = self.data.copy()
        self._quick_sort_in_place_helper(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort_in_place_helper(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort_in_place_helper(arr, low, pi - 1)
            self._quick_sort_in_place_helper(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def compare_algorithms(self):
        algorithms = {
            "Bubble Sort": self.bubble_sort,
            "Merge Sort": self.merge_sort,
            "Quick Sort": self.quick_sort,
            "In-Place Quick Sort": self.quick_sort_in_place
        }

        for name, func in algorithms.items():
            start_time = time.time()
            func()
            end_time = time.time()
            print(f"{name} took {end_time - start_time:.6f} seconds")

    def visualize_sorting(self, title):
        sorted_data = self.bubble_sort()  # You can replace with any sorting method
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(sorted_data)), sorted_data, color='blue')
        plt.title(title)
        plt.xlabel('Array Index')
        plt.ylabel('Value')
        plt.xticks(range(len(sorted_data)))
        plt.show()


# Example Usage
if __name__ == "__main__":
    # Generate a random array for testing
    random_data = [random.randint(1, 1000) for _ in range(100)]

    sorter = Sorter(random_data)

    # Test sorting algorithms
    print("Testing sorting algorithms:")
    sorter.compare_algorithms()

    # Visualize sorting results
    sorter.visualize_sorting("Bubble Sort Result")
