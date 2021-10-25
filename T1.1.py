from itertools import product
from collections import Counter

k1 = 4; k2 = 6; k3 = 20
counts = Counter()
total = k1 * k2 * k3

for oneresult in product(range(1,k1+1), range(1, k2+1),range(1, 3+1)):
    value = max(0, sum(oneresult))
    counts[value] += 1
outcomes = sorted(counts.keys())
for outcome in outcomes:
    print(f"{outcome}: {counts[outcome]/total:.4f}")
