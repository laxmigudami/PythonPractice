def compute_gcd(a,b):
    if b == 0:
        return a
    else:
        return compute_gcd(b, a % b)
print(compute_gcd(45,15))