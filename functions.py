NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]
UNKNOWN = "?"


def findMissing(isbn: str) -> str:
    if len(isbn) != 10:
        raise Exception("Invalid input, Length is not 10")
    sumNumbers = 0
    unknownIndex = -1
    for i, letter in enumerate(isbn):
        if letter == UNKNOWN:
            if unknownIndex != -1:
                raise Exception(f"Invalid input, found two {UNKNOWN}s")
            unknownIndex = i + 1
        else:
            if letter.upper() not in NUMBERS:
                raise Exception(f"Invalid input, {letter} is not allowed")
            if letter.upper() == "X" and i + 1 != 10:
                raise Exception(f"Invalid input, found X at index {i + 1}")
            sumNumbers += (i + 1) * NUMBERS.index(letter.upper())
    if unknownIndex == -1:
        raise Exception(f"Invalid input, found no {UNKNOWN}")
    # inverse = findInverse(unknownIndex, 11)  # find inverse
    inverse = gcdExtended(unknownIndex, 11)[1]
    unknownValue = -sumNumbers * inverse % 11  # solving linear congruence
    if unknownValue == 10 and unknownIndex != 10:
        raise Exception("NO Solution possible")
    # print(f"{unknownIndex}{unknown} + {sumNumbers} ≡ 0 mod 11")
    # print(f"{unknownIndex}{unknown} ≡ {-sumNumbers} mod 11")
    # print(f"{unknownIndex}{unknown} ≡ {-sumNumbers % 11} mod 11")
    # print(f"{unknown} ≡ {-sumNumbers % 11 * inverse} mod 11")
    # print(f"{unknown} ≡ {unknownValue} mod 11")
    # print(f"{unknown} = {unknownValue}")
    return isbn.replace(UNKNOWN, NUMBERS[unknownValue]).upper()


def findInverse(a: int, b: int):
    for i in range(1, b):
        if a * i % b == 1:
            if i < abs(i - b):
                return i
            return i - b
    raise Exception  # gcd != 1


def gcdExtended(a, b):  # code from https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
    if a == 0:
        return b, 0, 1
    gcd, x, y = gcdExtended(b % a, a)
    return gcd, y - (b // a) * x, x
