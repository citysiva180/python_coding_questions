def calcGCD(n: int, m: int) -> int:
    # Write your code here
    while m != 0:
        n, m = m, n % m
    return n


output = calcGCD(9, 3)
print(output)
