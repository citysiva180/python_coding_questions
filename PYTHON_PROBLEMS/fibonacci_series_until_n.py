def fibonacci_generator():
    a, b = 0, 1
    while True:  # Infinite Fibonacci generator
        yield a
        a, b = b, a + b

# Generate a list of the first `n` Fibonacci numbers
n = 10
gen = fibonacci_generator()
result = list(next(gen) for _ in range(n))
print(result)
