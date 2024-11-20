from math import sqrt

# Important notes for prime number program
# 1. On checking the list of values below the numbers sqrt root we test against the values on division has any reminders.
# 2. As long as the reminder is not zero, the number is considered to be prime. but if the number is divisible any thing other than 1
# and itself, the number is a consonant number.
# By gaining the members within the square root list, we identify potential divisors of the number. This way,
# We get to choose a lower data set to check if the member is prime or not


def check_prime_number(n):
    is_prime_number = False
    if (n > 1):
        for number in range(2, int(sqrt(n))+1):  # []
            if (n % number == 0):
                is_prime_number = True
                break
        if (is_prime_number == False):
            return True
        else:
            return False
    else:
        return False


output = check_prime_number(1)
print(output)
