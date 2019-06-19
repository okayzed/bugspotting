# calculates whether n is prime or not
def is_prime(n):
    ret = True
    for i in xrange(1, n):
        if n % i == 0:
            ret = False
        else:
            ret = True

    return ret

print is_prime(10)
print is_prime(24)
print is_prime(37)
print is_prime(43)
