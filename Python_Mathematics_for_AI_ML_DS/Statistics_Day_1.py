# 1Calculating a mean in Python

sample = [1, 3, 2, 5, 7, 0, 2, 3] 
mean = sum(sample) / len(sample) 
print(mean)

# OUTPUT:  2.875

# 2 Calculating a weighted mean in Python

sample = [90, 80, 63, 87]
weights = [.20, .20, .20, .40] 
weighted_mean = sum(s * w for s,w in zip(sample, weights)) / sum(weights) 
print(weighted_mean)

#OUTPUT:  81.4

# 3 Calculating a weighted mean in Python

sample = [90, 80, 63, 87]
weights = [1.0, 1.0, 1.0, 2.0] 
weighted_mean = sum(s * w for s,w in zip(sample, weights)) / sum(weights) 
print(weighted_mean)

#OUTPUT:  81.4

# 4

sample = [0, 1, 5, 7, 9, 10, 14] 
def median(values): 
    ordered = sorted(values) 
    print(ordered) 
    n = len(ordered) 
    mid = int(n / 2) - 1 if n % 2 == 0 else int(n/2)
    
    if n % 2 == 0: 
        return (ordered[mid] + ordered[mid+1]) / 2.0 
    else: 
        return ordered[mid] 
print(median(sample)) 