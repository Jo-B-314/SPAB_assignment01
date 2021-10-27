from itertools import product
from math import factorial
from fractions import Fraction as frac

def ntuples(n,k) :
    return n**k

def npermutations(n,k) :
    a = factorial(n)
    b = factorial (n-k)
    # a / b leads to 'OverflowError: integer division result too large for a float'
    c = frac(a,b)
    return c

def ncombinations(n,k) :
    a = factorial(n)
    b = factorial(n-k)
    c = factorial (k)
    return int(a / (b * c))

def nmultisets(n,k) :
    a = factorial(n+k-1)
    b = factorial(n-1)
    c = factorial(k)
    return int(a / (b * c))

print("Enter n:")
n = int(input())
print("Enter k:")
k = int(input())

print(f"\nn = {n}, k = {k}\n")
print(f"ntuples:\n{ntuples(n,k)}\n")
print(f"npermutations:\n{npermutations(n,k)}\n")
print(f"ncombinations:\n{ncombinations(n,k)}\n")
print(f"nmultisets:\n{nmultisets(n,k)}\n")