"""
Palindromic Series
"""


def sumDigit(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res


# print(sumDigit(61))  # 7
# print(sumDigit(10101))  # 3
# print(sumDigit(1998))  # 27
# print(sumDigit(1234567))  # 28


def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False


# print(isPalindrome("gbgbgbg"))
# print(isPalindrome("abc"))


def palindromicSeries():
    T = int(input())
    dic = {}
    for i in range(10):
        dic[i] = chr(ord("a") + i)
    for tc in range(T):
        N = int(input())
        s = ""
        for ch in str(N):
            s += dic[int(ch)]
        S = s * (sumDigit(N) // len(s)) + s[: sumDigit(N) % len(s)]
        print("YES" if isPalindrome(S) else "NO")


# palindromicSeries()


"""
Examination Papers
"""


def totalMoves(n):
    return 2**n - 1


def examinationPapers():
    T = int(input())
    for tc in range(T):
        N = int(input())
        print(totalMoves(N))


examinationPapers()
