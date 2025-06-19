def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # gcd, u, v
    else:
        g, u1, v1 = extended_gcd(b, a % b)
        u = v1
        v = u1 - (a // b) * v1
        return g, u, v

gcd_val, u, v = extended_gcd(26513, 32321)
print(f"gcd = {gcd_val}, u = {u}, v = {v}")