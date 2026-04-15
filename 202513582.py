# This function calculates the factorial of a given number n using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Example
print(factorial(5))  # 120

# This function calculates the nth Fibonacci number using iteration.
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
# Example
print(fibonacci_iter(10))  # 55