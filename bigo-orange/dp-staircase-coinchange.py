"""
Dynamic Programming

Use a list to keep track of the result

Example:
Fibonacci problem

Solution:
Recursion => O(2^n)

Top-Down Approach (Memoization)
Bottom-Up Approach (Tabulation)
=> O(n) for time complexity



"""


# Top-down
def fibonacci(n):
    if n == 0:
        return dp[0]
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]


n = 6
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1
print(fibonacci(n))


# Bottom-up
def fibonacci(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


n = 6
dp = [0] * (n + 1)
print(fibonacci(n))


# Staircase Problem
# Top-Down
def staircase(n):
    if n < 0:
        return 0
    if dp[n] != 0:
        return dp[n]
    dp[n] = staircase(n - 1) + staircase(n - 2)
    return dp[n]


n = 7
dp = [0] * (n + 1)
dp[0] = 1
print(staircase(n))


# Bottom-up
def staircase(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


n = 7
print(staircase(n))


# Coin change problem
def coinChangeProblem(total, coins, n):
    dp = [0] * (total + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], total + 1):
            dp[j] += dp[j - coins[i]]
    return dp[total]


def printSolution(result, total, coins, n, pos):
    if total == 0:
        for r in result:
            print(r, end=" ")
        print()
    for i in range(pos, n):
        if total >= coins[i]:
            result.append(coins[i])
            printSolution(result, total - coins[i], coins, n, i)
            result.pop()


if __name__ == "__main__":
    total = 10
    coins = [1, 2, 5, 10]
    n = 4
    # print("Number of Solutions:", coinChangeProblem(total, coins, n))
    result = []
    # printSolution(result, total, coins, n, 0)


"""
Bytelandian Gold Coins

exchange 1 coin -> 1/2, 1/3, 1/4 (all round down) or exchange to USD with rate of 1:1
"""
maxN = 10**6 + 1
dp = [-1] * maxN


def solve(n):
    if n < 3:
        return n
    if n < maxN and dp[n] != -1:
        return dp[n]
    result = max(solve(n // 2) + solve(n // 3) + solve(n // 4), n)
    if n < maxN:
        dp[n] = result
    return result


def byteGoldCoin():
    while True:
        try:
            data = int(input())
            print(solve(data))
        except EOFError:
            break


# byteGoldCoin()


"""
K-based Numbers
"""


def count_numbers(k, n, flag):
    # O(n^2) for time & space
    # base case
    if n == 1:
        # if 0 wasn't chosen previously
        if flag:
            return k - 1
        else:
            return 1
    # if 0 wasn't chosen previously
    if flag:
        return (k - 1) * (
            count_numbers(k, n - 1, False) + count_numbers(k, n - 1, True)
        )
    else:
        return count_numbers(k, n - 1, 1)


def kBasedNumbers():
    n = int(input())
    k = int(input())
    print(count_numbers(k, n, True))


# kBasedNumbers()

k = 10
n = 2
# print(count_numbers(k, n, True))  # 90

k = 10
n = 3
# print(count_numbers(k, n, True))  # 891

"""
Grid Traveler
"""


def gridTraveler(h, w):
    # Time: O(2^n+m), Space: O(n+m)
    if h == 1 and w == 1:
        return 1
    if h == 0 or w == 0:
        return 0
    return gridTraveler(h - 1, w) + gridTraveler(h, w - 1)


# print(gridTraveler(1, 1))  # 1
# print(gridTraveler(2, 3))  # 3
# print(gridTraveler(3, 2))  # 3
# print(gridTraveler(3, 3))  # 6
# print(gridTraveler(18, 18))  # 2333606220


def gridTravelerMemoize(h, w, memo={}):
    # Time: O(n*m), Space: O(n+m)
    key = str(h) + "," + str(w)
    if key in memo:
        return memo[key]
    if h == 0 or w == 0:
        return 0
    if h == 1 and w == 1:
        return 1
    memo[key] = gridTravelerMemoize(h - 1, w, memo) + gridTravelerMemoize(
        h, w - 1, memo
    )
    return memo[key]


# print(gridTravelerMemoize(1, 1))  # 1
# print(gridTravelerMemoize(2, 3))  # 3
# print(gridTravelerMemoize(3, 2))  # 3
# print(gridTravelerMemoize(3, 3))  # 6
# print(gridTravelerMemoize(18, 18))  # 2333606220

"""
Memoization Recipe

1. Make it work
- visualize the problem as a tree
- implement the tree using recursion
- test it

2. Make it efficient
- add a memo object
- add a base case to return memo values
- store return values into the memo
"""


def canSum(targetSum, numbers):
    # m: height
    # n: array length
    # O(n^m) for time, O(m) for space
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for number in numbers:
        remainder = targetSum - number
        if canSum(remainder, numbers):
            return True
    return False


# print(canSum(7, [2, 3]))  # True
# print(canSum(7, [5, 3, 4, 7]))  # True
# print(canSum(7, [2, 4]))  # False
# print(canSum(8, [2, 3, 5]))  # True
# print(canSum(300, [7, 14]))  # False


def canSumMemoize(targetSum, numbers, memo):
    # m: height/targetSum
    # n: array length
    # O(m*n) for time, O(m) for space
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for number in numbers:
        remainder = targetSum - number
        if canSumMemoize(remainder, numbers, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


print(canSumMemoize(7, [2, 3], {}))  # True
print(canSumMemoize(7, [5, 3, 4, 7], {}))  # True
print(canSumMemoize(7, [2, 4], {}))  # False
print(canSumMemoize(8, [2, 3, 5], {}))  # True
print(canSumMemoize(300, [7, 14], {}))  # False


def howSum(targetSum, numbers):
    # Time: O(n^m * m), Space: O(m)
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for number in numbers:
        remainder = targetSum - number
        remainderResult = howSum(remainder, numbers)
        if remainderResult != None:
            return remainderResult + [number]

    return None


print(howSum(7, [2, 3]))  # [3,2,2]
print(howSum(7, [5, 3, 4, 7]))  # [4,3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2,2,2,2]
# print(howSum(300, [7, 14]))  # None


def howSumMemoize(targetSum, numbers, memo):
    # Time: O(n*m*m), Space: O(m^2)
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for number in numbers:
        remainder = targetSum - number
        remainderResult = howSumMemoize(remainder, numbers, memo)
        if remainderResult != None:
            memo[targetSum] = remainderResult + [number]
            return memo[targetSum]

    memo[targetSum] = None
    return None


print(howSumMemoize(7, [2, 3], {}))  # [3,2,2]
print(howSumMemoize(7, [5, 3, 4, 7], {}))  # [4,3]
print(howSumMemoize(7, [2, 4], {}))  # None
print(howSumMemoize(8, [2, 3, 5], {}))  # [2,2,2,2]
print(howSumMemoize(300, [7, 14], {}))  # None


"""
Alphacode

BEAN -> 25114
25114 -> BEAN, BEAAD, YAAD, YAN, YKD, BEKD

OUTPUT:
how many ways to decode this string to words based on the above method

TC:
25114 -> ... above example
1111111111 -> AAA, KA, AK
3333333333 -> CCCCCCCCCC

when check a character -> use that character OR use the combination of that character and the previous
character to a word

f[i]: # of ways
f[0]: 1
f[i] = a + b
a = f[s]
b = f[s-1] + f[s]
"""

maxN = 5005
while True:
    s = input()
    if s == "0":
        break

    f = [0] * maxN
    n = len(s)
    f[0] = 1
    f[1] = 1

    for i in range(2, n + 1):
        if s[i - 1] != "0":
            f[i] += f[i - 1]
        # 14 -> 1 * 10 + 4
        val = (s[i - 2] - "0") * 10 + s[i - 1] - "0"
        if val >= 10 and val <= 26:
            f[i] += f[i - 2]

    print(f[n])

"""
Ingenuous Cubrency

21 coins -> coin ith: i**3

18 = 8 + 8 + 1 + 1 = 2**3 + 2**3 + 1**3 + 1**3

example:
10 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 1 + 1 + 2**3 -> 2

21 = 21 1 = 13 1 + 1 8 = 5 1 + 2 8 -> 3

dp[0] = 1
dp[i] = dp[i] + dp[i-j**3] (i>= j**3)

1. cal dp[i] from 1 to 9999
2. each tc -> input n and print dp[n]

O(21 * 9999)
"""
maxN = 10000
dp = [0] * maxN
dp[0] = 1
for j in range(1, 21):
    for i in range(j**3, 9999):  # i >= j^3
        dp[i] = dp[i] + dp[i - j**3]
while True:
    if n == "0":
        break
    print(dp[n], "/n")
