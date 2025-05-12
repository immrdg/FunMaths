# Test for a Number to be Prime:
#  Let p be a given number and let n be the smallest counting number such that n2 ≥ p.
#  Now, test whether p is divisible by any of the prime numbers less than or equal to n. If yes, then p is not
# prime otherwise, p is prime.

def isPrime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    print("2 is prime:", isPrime(2))
    print("3 is prime:", isPrime(3))
    print("4 is prime:", isPrime(4))
    print("5 is prime:", isPrime(5))
    print("6 is prime:", isPrime(6))
    print("7 is prime:", isPrime(7))
    print("8 is prime:", isPrime(8))
    print("9 is prime:", isPrime(9))
    print("10 is prime:", isPrime(10))
    print("11 is prime:", isPrime(11))
    print("12 is prime:", isPrime(12))

