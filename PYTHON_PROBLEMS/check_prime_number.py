def is_prime(number):
    if number <= 1:  # Numbers less than 2 are not prime
        return False
    if number <= 3:  # 2 and 3 are prime numbers
        return True
    if number % 2 == 0 or number % 3 == 0:  # Eliminate multiples of 2 and 3
        return False

    # Check for factors from 5 to sqrt(number) skipping multiples of 2 and 3
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


# Example usage
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
