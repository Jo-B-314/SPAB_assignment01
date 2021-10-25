from itertools import product
from math import factorial
from collections import Counter

def ntuples(n,k) :
    return n**k

def npermutations(n,k) :
    a = factorial(n)
    b = factorial (n-k)
    return int(a/b)

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

print(ntuples(n,k))
print(npermutations(n,k))
print(ncombinations(n,k))
print(nmultisets(n,k))