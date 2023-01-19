def isprime(n):
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n > 1:
        for r in range(2,n):
            if n % r == 0:
                return False
            else:
                return True