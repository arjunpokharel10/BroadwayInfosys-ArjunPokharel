def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
fibonacci = fib(0)
print(fibonacci)

