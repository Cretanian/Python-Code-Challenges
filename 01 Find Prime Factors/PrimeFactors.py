def isprime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def primefactors(num):
    primefactor = []
    primehelper = 2

    while num != 1:
        if num % primehelper == 0 & primehelper != 1:
            primefactor.append(primehelper)
            num = num / primehelper
        else:
            primehelper += 1

    print(primefactor)


if __name__ == '__main__':
    print('Enter your number:')
    inputNumber = int(input())

    if isprime(inputNumber):
        print(inputNumber)
    else:
        primefactors(inputNumber)
