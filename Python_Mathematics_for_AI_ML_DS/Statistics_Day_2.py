#   Calculating the mode in Python

'''from collections import defaultdict 
sample = [1, 3, 2, 5, 7, 0, 2, 3] 
def mode(values): 
    counts = defaultdict(lambda: 0) 
    for s in values: 
        counts[s] += 1 
    max_count = max(counts.values()) 
    modes = [v for v in set(values) if counts[v] == max_count] 
    return modes 
print(mode(sample))

# OUTPUT: [2, 3]


# 2. . Calculating variance in Python

data = [0, 1, 5, 7, 9, 10, 14] 
def variance(values): 
    mean = sum(values) / len(values) 
    _variance = sum((v - mean) ** 2 for v in values) / len(values) 
    return _variance 
print(variance(data)) '''

# OUTPUT: 21.387755102040813