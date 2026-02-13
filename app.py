print("Hello world")
n=9
def poweroftwo(n):
    if n==0:
        return 1
    else:
        power = poweroftwo(n-1)
        return power*2
print(poweroftwo(n))

# Optimized iterative version (O(n) time, O(1) space)
def poweroftwo_optimized(n):
    result = 1
    for _ in range(n):
        result *= 2
    return result

print("Optimized result:", poweroftwo_optimized(n))