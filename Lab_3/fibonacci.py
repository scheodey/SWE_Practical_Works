# Implement a Recursive Fibonacci Generator
print("Recursive Fibonacci Sequence")
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

print()
print("Iterative Fibonacci Sequence")
# Implement an Iterative Fibonacci Generator
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")


# Compare Performance
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")
print()

# Implement a Generator Function for Fibonacci Sequence
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")


# Implement Memoization for Recursive Fibonacci
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

print()

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

# Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number.
#to return a list of Fibonacci numbers up to n
print()
def fibonacci_iterative_list(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    fib_sequence = [0, 1]
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        fib_sequence.append(b)
    return fib_sequence

n = 10
print(f"Fibonacci sequence up to F({n}): {fibonacci_iterative_list(n)}")

print()
# Implement a function that finds the index of the first Fibonacci number that exceeds a given value.
#index of the first Fibonacci number
def fibonacci_index(index_value):
    if index_value < 0:
        return 0  

    a, b = 0, 1
    index = 1 
    
    while b <= index_value:
        a, b = b, a + b
        index += 1
    
    return index

value = 5
print(f"The first Fibonacci number that exceeds {value} is index: {fibonacci_index(value)}.")

print()

# Create a function that determines if a given number is a Fibonacci number.
# checks if a given number is a Fibonacci number
import math

def is_fib_num(x):
    def is_perfect_sqr(n):
        s = int(math.sqrt(n))
        return s * s == n

    
    return is_perfect_sqr(5 * x * x + 4) or is_perfect_sqr(5 * x * x - 4)


number = 38
print(f"The number {number} is {'fibonacci number' if is_fib_num(number) else 'not fibonacci number'}")

print()
# Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.
# calculating the ratio between consecutive Fibonacci numbers.
def fibonacci_ratios(terms):
    a, b = 0, 1
    golden_ratio = (1 + 5 ** 0.5) / 2
    print("Fibonacci Ratios Approaching the Golden Ratio:")

    for i in range(2, terms + 1):
        if a != 0:
            ratio = b / a
            print(f"Ratio F({i})/F({i-1}) = {ratio}")
        a, b = b, a + b

    print(f"\nApproximate Golden Ratio: {golden_ratio}")

fibonacci_ratios(10)