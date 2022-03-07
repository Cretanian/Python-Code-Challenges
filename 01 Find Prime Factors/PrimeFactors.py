def isprime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def get_prime_factors(num):
    prime_factor = list()
    prime_helper = 2

    while num != 1:
        if num % prime_helper == 0 & prime_helper != 1:
            prime_factor.append(prime_helper)
            num = num // prime_helper
        else:
            prime_helper += 1

    return prime_factor


if __name__ == '__main__':
    print('Enter your number:')
    inputNumber = int(input())

    if isprime(inputNumber):
        print(inputNumber)
    else:
        get_prime_factors(inputNumber)
