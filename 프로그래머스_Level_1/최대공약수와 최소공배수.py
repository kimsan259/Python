def gcdlcm(a, b):
    big, small = max(a,b),min(a,b)
    while small > 0:
        big, small = small, big % small
    return [big, int((a*b)/big)]

print(gcdlcm(2,5))

# from fractions import gcd
# def gcdlcm(a,b):
#   return [gcd(a,b), a*b/gcd(a,b)]
# print(gcdlcm(3,12))