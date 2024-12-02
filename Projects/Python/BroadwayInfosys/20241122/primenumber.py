num = int(input("Enter a number: "))

if num <= 1:  # Numbers less than or equal to 1 are not prime
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to √num
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")