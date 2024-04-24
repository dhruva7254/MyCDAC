

# Fibonacci Series.
#     1,1,2,3,5,8,13,21,34,...

def fibonacci(n):
    fib_series = [1, 1]  
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

num_terms = 10
print("Fibonacci series up to", num_terms, "terms:")
print(fibonacci(num_terms))
