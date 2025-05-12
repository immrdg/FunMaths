# Co-primes (or Relative Primes): Two numbers whose H.C.F. is 1 are called co-prime numbers,
#  Ex. (2, 3), (8, 9) are pairs of co-primes


def coPrimes(a: int, b: int) -> bool:
    """
    Checks if two numbers are co-primes or not

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number

    Returns
    -------
    bool
    """
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


if __name__ == '__main__':
    # Not co-primes
    print(coPrimes(4, 6))
    print(coPrimes(9, 12))

    # Co-primes
    print(coPrimes(3, 2))
    print(coPrimes(9, 8))
