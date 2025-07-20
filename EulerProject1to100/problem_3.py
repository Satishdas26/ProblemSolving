'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?'''

def primeFactor(n):
    factors=[]
    while n%2==0:
        factors.append(2)
        n//=2
    i = 3
    while i*i<=n:
        while n%i==0:
            factors.append(i)
            n//=i
        i+=2
    if n>2:
        factors.append(n)
    return factors
                
num = int(input("Enter a number: "))
factors = primeFactor(num)
largest = max(factors) if factors else None

print(f"\nAll Prime Factors of {num}: {factors}")
print(f"Largest Prime Factor of {num}: {largest}")
                