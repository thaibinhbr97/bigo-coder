"""
Lecture Note
"""


# using for loop
def binarySearch(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        if x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# using recursion
def binarySearchRecursion(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binarySearchRecursion(a, left, mid - 1, x)
        return binarySearchRecursion(a, left + 1, right, x)
    return -1


# binary search first (recursion)
def binary_search_first(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if (mid == left or x != a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return binary_search_first(a, mid + 1, right, x)
        else:
            return binary_search_first(a, left, mid - 1, x)
    return -1


# binary search last (recursion)
def binary_search_last(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if (mid == right or x != a[mid + 1]) and a[mid] == x:
            return mid
        elif x < a[mid]:
            return binary_search_last(a, left, mid - 1, x)
        else:
            return binary_search_last(a, mid + 1, right, x)
    return -1


import bisect

# # bisect_left
# # lower bound -> return a first pos >= x in [first,last)
# # >=
a = [1, 1, 2, 2, 2, 3, 4, 5, 7]
# n, x = 9, 1
n, x = 9, 10
pos = bisect.bisect_left(a, x, 0, n)
pos = bisect.bisect_left(a, x)
print(pos)

# # bisect_right
# # upper bound -> return a first pos > x in [first,last)
# # >
pos = bisect.bisect_right(a, x, 0, n)
pos = bisect.bisect_right(a, x)
print(pos)


if __name__ == "__main__":
    # n, x = map(int, input().split())
    # a = list(map(int, input().split()))
    a = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
    n = len(a)
    x = 0
    result = binarySearch(a, 0, n - 1, x)  # 4
    # result = binarySearchRecursion(a, 0, n - 1, x)  # 4
    print(result)


"""
Where is The Marble
"""


def binary_search(marbles, x):
    left = 0
    right = len(marbles) - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == left or x != marbles[mid - 1]) and marbles[mid] == x:
            return mid
        elif x > marbles[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


T = 0
while True:
    T += 1
    N, Q = map(int, input().split())
    if N == 0 and Q == 0:
        break
    marbles = []
    for _ in range(N):
        marble = int(input())
        marbles.append(marble)
    marbles.sort()
    queries = []
    for _ in range(Q):
        query = int(input())
        queries.append(query)
    print("CASE# " + str(T) + ":")
    for query in queries:
        pos = binary_search(marbles, query)
        if pos == -1:
            print(str(query) + " not found")
        else:
            print(str(query) + " found at " + str(pos + 1))


"""
Pizzamania
"""


def two_pointer(nums, M):
    # two pointers
    # O(n) for time, O(1) for space
    count = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        x = nums[left] + nums[right]
        if x == M:
            count += 1
            left += 1
            right -= 1
        elif x < M:
            left += 1
        else:
            right -= 1
    return count


def binary_search(x, nums):
    # binary search
    # O(nlogn) for time, O(1) for space
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == x:
            return True
        if nums[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return False


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()  # sorted nums

    # res = two_pointer(nums, M)
    # print(res)

    res = 0
    for num in nums:
        if binary_search(M - num, nums):
            res += 1
    print(res // 2)

"""
Eko

20,15,10,17 with H = 15 => 15,15,10,15 and 5 + 2 = 7 is removed

N: # of trees
M: required woods
trees: trees 
"""
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
large = trees[-1]


def naive_solution(trees, M):
    for height in range(large, -1, -1):
        total = 0
        for tree in trees:
            if height < tree:
                total += abs(height - tree)
        if total >= M:
            return height
    return -1


print(naive_solution(trees, M))


def binary_search(trees, M):
    left = 0
    right = trees[-1]
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for tree in trees:
            if mid < tree:
                total += abs(mid - tree)
        if total >= M:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    print(ans)


binary_search(trees, M)

import bisect

"""
The playboy chimp

N: # of heights for female chimp
heights: height for each female chimp in a list
Q: # of queries for Luchu heights
queries: each query representing Luchu height
"""

N = int(input())
heights = list(map(int, input().split()))
Q = int(input())
queries = list(map(int, input().split()))


def is_valid(i, N):
    return i in range(N)


def playboy_chimp(N, heights, Q, queries):
    for query in queries:
        ans = ""
        left = bisect.bisect_left(heights, query)
        left -= 1
        right = bisect.bisect_right(heights, query)
        if is_valid(left, N):
            num_left = str(heights[left])
        else:
            num_left = "X"
        if is_valid(right, N):
            num_right = str(heights[right])
        else:
            num_right = "X"
        ans = num_left + " " + num_right
        print(ans)
    return


playboy_chimp(N, heights, Q, queries)


"""
Money and the Oiled Bamboo

T: tests
n: # of stairs
heights: height of start from ground
"""


def binary_search(n, heights):
    # # Space: O(1), Time: O(logn)
    # low = heights[0]
    # high = heights[-1]
    # while low <= high:
    #     mid = (low + high) // 2
    #     temp_mid = mid
    #     for i in range(len(heights)):
    #         if i == 0:
    #             if temp_mid == heights[0]:
    #                 temp_mid -= 1
    #             elif temp_mid < heights[0]:
    #                 temp_mid = -1
    #                 break
    #         else:
    #             diff = heights[i] - heights[i - 1]
    #             if temp_mid == diff:
    #                 temp_mid -= 1
    #             elif temp_mid < diff:
    #                 temp_mid = -1
    #                 break
    #     if temp_mid >= 0:
    #         ans = mid
    #         high = mid - 1
    #     else:
    #         low = mid + 1

    # return ans

    # Space: O(n), Time: O(logn)
    low = heights[0]
    high = heights[-1]
    steps = [heights[0]]
    for i in range(1, len(heights)):
        steps.append(heights[i] - heights[i - 1])
    while low <= high:
        mid = (low + high) // 2
        temp = mid
        for step in steps:
            if mid < step:
                temp = -1
                break
            elif mid == step:
                temp -= 1
        if temp >= 0:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    heights = list(map(int, input().split()))
    ans = binary_search(n, heights)
    print("Case " + str(t) + ":" + " " + str(ans))


"""
Energy Exchange

i -> a[i]
when x transfered, k% is lost
x - xk/100

n,k: # of bateries, % energy lost via transfer
batteries: as a list

output:
maximum energy in each battery
epsilon <= 10^-6
"""

n, k = map(int, input().split())
batteries = list(map(int, input().split()))
sumEnergy = 0
for i in range(n):
    sumEnergy += batteries[i]
left = 0
right = 1000
eps = 10**-7
while right - left > eps:
    mid = (left + right) / 2
    sumTransfer = 0
    for i in range(n):
        if batteries[i] > mid:
            sumTransfer += batteries[i] - mid
    sumLost = k / 100 * sumTransfer
    if mid * n < sumEnergy - sumLost:
        left = mid
    else:
        right = mid
print(mid)


"""
Hacking the random number generator

n,k: # of numbers, a value k
nums: distinct numbers


ex: 
5 2
1 5 3 4 2

1 3 -> 2
5 3 -> 2
4 2 -> 2

output:
3

1 2 3 4 5

"""

n, k = map(int, input().split())
nums = list(map(int, input().split()))


def binary_search(low, high, num):
    while low <= high:
        mid = (low + high) // 2
        mid_val = nums[mid]
        if mid_val == num:
            return 1
        elif mid_val > num:
            high = mid - 1
        else:
            low = mid + 1
    return 0


def hack_random_generator(nums, n, k):
    # # naive solution
    # # O(n^2) for time, O(1) for space
    # res = 0
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if abs(nums[i] - nums[j]) == k:
    #             res += 1
    # print(res)

    # binary search
    # O(nlogn), O(1) for space
    res = 0
    nums.sort()
    for i in range(n):
        if binary_search(0, n - 1, nums[i] + k):
            res += 1
    print(res)


hack_random_generator(nums, n, k)


"""
Solve It
"""

import math


def f(x):
    return (
        p * (math.e ** (-x))
        + q * math.sin(x)
        + r * math.cos(x)
        + s * math.tan(x)
        + t * (x**2)
        + u
    )


eps = 10**-8


def solve():
    low = 0
    high = 1
    while high - low > eps:
        x = (high + low) / 2
        if f(low) * f(x) <= 0:
            high = x
        else:
            low = x
    return (low + high) / 2


while True:
    try:
        line = input()
        p, q, r, s, t, u = map(float, line.split())
        if f(0) * f(1) > 0:
            print("No solution")
        else:
            ans = solve()
            print("%.4f" % ans)
    except EOFError:
        break
