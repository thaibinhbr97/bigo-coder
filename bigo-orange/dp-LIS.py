"""
Dynamic Programming - LIS
Longest Increasing Subsequence
"""


# bottom up
def LIS(a):
    global last, dp, path
    length = 0
    path = [-1] * len(a)
    dp = [1] * len(a)
    for i in range(1, len(a)):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                path[i] = j
    for i in range(len(a)):
        if length < dp[i]:
            last = i
            length = dp[i]

    return length


a = [2, 5, 12, 3, 10, 6, 8, 14, 4, 11, 7, 15]
print("Length of Longest Increasing Subsequence is: ", end="")
print(LIS(a))


# top down
def LISTopdown(a, i, dp):
    if i == 0:
        return 1
    if dp[i] != -1:
        return dp[i]
    length = 1
    for j in range(i - 1, -1, -1):
        if a[i] > a[j]:
            length = max(length, LISTopdown(a, j, dp) + 1)
            dp[i] = length
    return length


a = [2, 5, 12, 3, 10, 6, 8, 14, 4, 11, 7, 15]
n = len(a)
print("Length of Longest Increasing Subsequence is: ", end="")
dp = [-1 for i in range(n + 1)]
length = 1
for i in range(n):
    length = max(length, LISTopdown(a, i, dp))
print(length)


dp = []
path = []
last = -1


def printLIS(a):
    global last
    result = []
    i = last
    while i != -1:
        result.append(a[i])
        i = path[i]
    for i in range(len(result) - 1, -1, -1):
        print(result[i], end=" ")
    print()


a = [2, 5, 12, 3, 10, 6, 8, 14, 4, 11, 7, 15]
print("Length of Longest Increasing Subsequence is:", LIS(a))
printLIS(a)


# LIS using Binary Search
def lowerBound(a, sub, n, x):
    left = 0
    right = n
    pos = right
    while left < right:
        mid = left + (right - left) // 2
        index = sub[mid]
        if a[index] >= x:
            pos = mid
            right = mid
        else:
            left = mid + 1
    return pos


def LIS(a):
    global path
    length = 1
    path = [-1] * len(a)
    dp.append(0)
    for i in range(1, len(a)):
        if a[i] <= a[dp[0]]:
            dp[0] = i
        elif a[i] > a[dp[length - 1]]:
            path[i] = dp[length - 1]
            dp.append(i)
            length += 1
        else:
            pos = lowerBound(a, dp, length, a[i])
            path[i] = dp[pos - 1]
            dp[pos] = i
    return length


dp = []
path = []


def printLIS(a, length):
    result = []
    i = dp[length - 1]
    while i >= 0:
        result.append(a[i])
        i = path[i]
    for i in range(len(result) - 1, -1, -1):
        print(result[i], end=" ")
    print()


a = [2, 5, 12, 3, 10, 6, 8, 14, 4, 11, 7, 15]
length = LIS(a)
print("Length of Longest Increasing Subsequence is:", length)
printLIS(a, length)


"""
Testing the CATCHER

[389,207,155,300,299,170,158,65] -> 6
[23,34,21] -> 2

Input:
389
207
155
300
299
170
158
65
-1
23
34
21
-1
-1

Output:
Test #1:
  maximum possible interceptions: 6

Test #2:
  maximum possible interceptions: 2
"""


def testingCatch():
    # O(T*n^2) for time and O(n) for space
    tc = 0
    while True:
        a = []
        while True:
            x = int(input())
            if x == -1:
                break
            a.append(x)
        if len(a) == 0:
            break
        dp = [1] * len(a)
        ans = 1
        for i in range(len(a)):
            for j in range(i):
                if a[j] >= a[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        tc += 1
        print("Test #" + str(tc) + ":")
        print("  maximum possible interceptions: " + str(ans))


# testingCatch()


"""
Wavio Sequence

L = 2*n + 1 -> odd
first (n+1) integers makes a strictly increasing sequence
last (n+1) integers makes a strictly decreasing sequence
no two adjacent integers are same in Wavio sequence

Example:
1 2 3 2 1 2 3 4 3 2 1 5 4 1 2 3 2 2 1 -> 9 for LIS in wavio sequence

Input:
10
1 2 3 4 5 4 3 2 1 10
19
1 2 3 2 1 2 3 4 3 2 1 5 4 1 2 3 2 2 1
5
1 2 3 4 5

Output:
9
9
1
"""


def LIS(a):
    f = [1] * len(a)
    ans = 1
    for i in range(len(a)):
        for j in range(i):
            if a[i] > a[j]:
                f[i] = max(f[i], f[j] + 1)
        ans = max(ans, f[i])
    return (ans, f)


def LDS(a):
    b = [1] * len(a)
    ans = 1
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            if a[i] > a[j]:
                b[i] = max(b[i], b[j] + 1)
        ans = max(ans, b[i])
    b.reverse()
    return (ans, b)


def wavioSequence():
    while True:
        try:
            n = int(input())
        except Exception:
            break
        a = list(map(int, input().split()))
        x, f = LIS(a)
        y, b = LDS(a)
        temp = [1] * len(a)
        for i in range(n):
            temp[i] = min(f[i], b[i])
        idx = temp.index(max(temp))
        ans = min(f[idx], b[idx]) * 2 - 1
        print(ans)


# wavioSequence()


# LIS using Binary Search
def lengthOfLIS(a):
    n = len(a)
    ans = []
    ans.append(a[0])

    for i in range(1, n):
        if a[i] > ans[-1]:
            # if the current number is greater than the last element of the answer list,
            # it means that we have found a longer increasing subsequence.
            # Hence, we append the current number to the answer list.
            ans.append(a[i])
        else:
            # if the current number is not greater than the last element of the answer list,
            # we perform a binary search to find the smallest element in the answer list that is
            # greater than or equal to the current number
            low = 0
            high = len(ans) - 1
            while low < high:
                mid = low + (high - low) // 2
                if ans[mid] < a[i]:
                    low = mid + 1
                else:
                    high = mid
            # we update the element at the found position with the current number.
            # By doing this, we are maintaing a sorted order in the answer list.
            ans[low] = a[i]
    # the length of the answer list represents the length of the longest increasing subsequence.
    return len(ans)


def lengthOfLDS(a):
    n = len(a)
    ans = []
    a.reverse()
    ans.append(a[0])
    for i in range(1, n):
        if a[i] > ans[-1]:
            ans.append(a[i])
        else:
            low = 0
            high = len(ans) - 1
            mid = low + (high - low) // 2
            if ans[mid] < a[i]:
                low = mid + 1
            else:
                high = mid
            ans[low] = a[i]
    return len(ans)


import bisect


def optimized_lis(arr):
    lis = []
    dp = [0] * len(arr)

    for i, x in enumerate(arr):
        pos = bisect.bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)
        else:
            lis[pos] = x
        dp[i] = pos + 1

    return dp


def LISBinary(a):
    length = 1
    dp = []
    dp.append(0)
    for i in range(1, len(a)):
        if a[i] <= a[dp[0]]:
            dp[0] = i
        elif a[i] > a[dp[length - 1]]:
            dp.append(i)
            length += 1
        else:
            pos = bisect.bisect_left(dp, a[i])
            dp[pos] = i
    return dp


def wavio_sequence_length():
    while True:
        try:
            n = int(input())
        except Exception:
            break
        a = list(map(int, input().split()))

        # Calculate LIS and LDS for the array
        lis = optimized_lis(a)
        lds = optimized_lis(a[::-1])[::-1]

        # Find the maximum Wavio sequence length
        max_wavio_len = 0
        for i in range(len(a)):
            max_wavio_len = max(max_wavio_len, 2 * min(lis[i], lds[i]) - 1)

        print(max_wavio_len)


# wavio_sequence_length()

a = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 5, 4, 1, 2, 3, 2, 2, 1]
print(optimized_lis(a))
print(optimized_lis(a[::-1])[::-1])
print(LISBinary(a))
# print(LISBinary(a[::-1])[::-1])
# print(lengthOfLIS(a))
# print(lengthOfLDS(a))
# print(LIS(a))
# print(LDS(a))

a = [2, -1, 4, 3, 5, -1, 3, 2]
# print(a)
# print(LIS(a))
# print(LDS(a))

a = [1, 2, 3, 4, 5]
# print(a)
# print(LIS(a))
# print(LDS(a))

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10]
# print(a)
# print(LIS(a))
# print(LDS(a))


"""
Beautiful People
"""

class Member {
    s,b,id
}
def cmp(u,v):
    if u.s == v.s:
        return u.b > v.b
    return u.s < v.s

def lowerBound(a,f,n,x):
    l = 1, r=n
    pos = r
    while l<=r:
        mid = (l+r)//2
        index =f[mid]
        if a[index].b >=x:
            pos = mid
            r = mid - 1
        else:
            l = mid+1
    return pos
    

def LIS(a, res):
    f = [] 
    path = [-1] * len(a)
    length = 1
    f[1] = 0
    for i in range(len(a)):
        if a[i].b > a[f[length]].b:
            length += 1
            f[length] = i
            path[i] = f[length-1]
        else:
            pos = lowerBound(a, f, length, a[i].b)
            f[pos]=i
            path[i] = f[pos-1]
    x = f[length]
    while x != -1:
        res.append(x)
        x = path[x]
    return length

def beautifulPeople():
    N = int(input())
    a = []
    for i in range(N):
        read(a[i].s)
        read(a[i].b)
        a[i].id = i + 1
    sorted(a,cmp)
    res = []
    length = LIS(a,res)
    print(length, '/n')
    for i in range(length):
        print(res[i], ' ')

'''
Check Transcription

001
kokokokotlin
'''
