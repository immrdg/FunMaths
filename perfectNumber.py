# Perfect Numbers: A number, the sum of whose factors (except the number itself), is equal to the number, is called
# a perfect number, e.g. 6, 28, 496
#  The factors of 6 are 1, 2, 3 and 6. And, 1 + 2 + 3 = 6.
#  The factors of 28 are 1, 2, 4, 7, 14 and 28. And, 1 + 2 + 4 + 7 + 14 = 28


def isPerfectNumber(number: int) -> bool:
    """
    Checks whether a given number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper positive divisors,
    excluding the number itself.

    Parameters
    ----------
    number : int
        The number to check.

    Returns
    -------
    bool
        Whether the number is a perfect number or not.
    """
    factors = set()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)

    factors.remove(number)
    return sum(factors) == number


if __name__ == '__main__':
    print(isPerfectNumber(6))
    print(isPerfectNumber(28))
    print(isPerfectNumber(496))
    print(isPerfectNumber(8128))

    # Not perfect numbers
    print(isPerfectNumber(9))
    print(isPerfectNumber(12))
    print(isPerfectNumber(24))
    print(isPerfectNumber(27))
