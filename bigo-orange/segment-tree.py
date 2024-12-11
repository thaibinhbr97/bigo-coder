"""
sum of given range

brute force
O(Q*N)

segment tree
O(N+Q*logN)

1. height: h = logn
2. number of elements: 2^h+1 - 1
3. node left ith: 2*i + 1
4. node right ith: 2*i + 2
5. parent node of node ith: (i-1)/2
"""

from math import ceil, log2

INF = 10**9


def sumRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 0
    mid = (left + right) // 2
    return sumRange(segtree, left, mid, fr, to, 2 * index + 1) + sumRange(
        segtree, mid + 1, right, fr, to, 2 * index + 2
    )


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]


if __name__ == "__main__":
    a = [5, -7, 9, 0, -2, 8, 3, 6, 4, 1]
    n = len(a)
    h = ceil(log2(n))
    sizeTree = 2 * (2**h) - 1
    # sizeTree = 4*n
    segtree = [INF] * sizeTree
    lazy = [0] * sizeTree
    buildTree(a, segtree, 0, n - 1, 0)
    fromRange = 3
    toRange = 8
    res = sumRange(segtree, 0, n - 1, fromRange, toRange, 0)
    print("Sum of given range:", res)


def updateQuery(segtree, a, left, right, index, pos, value):
    # time: O(logN)
    if pos < left or right < pos:
        return
    if left == right:
        a[pos] = value
        segtree[index] = value
        return
    mid = (left + right) // 2
    if pos <= mid:
        updateQuery(segtree, a, left, mid, 2 * index + 1, pos, value)
    else:  # if pos > mid
        updateQuery(segtree, a, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]


def sumRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 0
    mid = (left + right) // 2
    return sumRange(segtree, left, mid, fr, to, 2 * index + 1) + sumRange(
        segtree, mid + 1, right, fr, to, 2 * index + 2
    )


""" 
Lazy Propagaton
Sum of Given Range

Time: O(logN)


"""


def updateQuery_sumQueryLazy(segtree, lazy, left, right, fr, to, delta, index):
    if left > right:
        return
    if lazy[index] != 0:
        segtree[index] += lazy[index] * (right - left + 1)
        if left != right:
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0
    # no overlap condition
    if fr > right or to < left:
        return
    # total overlap condition
    if fr <= left and right <= to:
        segtree[index] += delta * (right - left + 1)
        if left != right:
            lazy[2 * index + 1] += delta
            lazy[2 * index + 2] += delta
        return
    # otherwise partial overlap so look both left and right
    mid = (left + right) // 2
    updateQuery_sumQueryLazy(segtree, lazy, left, mid, fr, to, delta, 2 * index + 1)
    updateQuery_sumQueryLazy(
        segtree, lazy, mid + 1, right, fr, to, delta, 2 * index + 2
    )
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]


def sumQueryLazy(segtree, lazy, left, right, fr, to, index):
    if left > right:
        return INF
    if lazy[index] != 0:
        segtree[index] += lazy[index] * (right - left + 1)
        if left != right:  # not a leaf node
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0
    # no overlap
    if fr > right or to < left:
        return 0
    # total overlap
    if fr <= left and to >= right:
        return segtree[index]
    # partial overlap
    mid = (left + right) // 2
    return sumQueryLazy(segtree, lazy, left, mid, fr, to, 2 * index + 1) + sumQueryLazy(
        segtree, lazy, mid + 1, right, fr, to, 2 * index + 2
    )


"""
Curious Robin Hood

n sacks: 0 to n - 1
1. give all money from ith sack -> leaving the sack empty
2. add new amount in the ith sack
3. find the total amount of money from ith sack to jth sack

input:
T: T <= 5
n q
n integers
q lines:
1 i: give all money of the ith sack to the poor
2 i v: add money v to the ith sack
3 i j: find the total amount of money from ith sack to jth sack

example:
1
5 6
3 2 1 4 5
1 4
2 3 4
3 0 3
1 2
3 0 4
1 1

Case 1:
5
14
1
13
2
"""


def sumUp(nums, l, r):
    res = 0
    for i in range(l, r + 1):
        res += nums[i]
    return res


# brute force
def curiousRobinHood():
    T = int(input())
    for tc in range(1, T + 1):
        n, q = map(int, input().split())
        nums = list(map(int, input().split()))
        print("Case " + str(tc) + ":")
        for _ in range(q):
            query = list(map(int, input().split()))
            if len(query) == 2:
                i = query[1]
                print(nums[i])
                nums[i] = 0
            else:
                if query[0] == 2:
                    i = query[1]
                    v = query[2]
                    nums[i] = nums[i] + v
                elif query[0] == 3:
                    l = query[1]
                    r = query[2]
                    print(sumUp(nums, l, r))
    return


# curiousRobinHood()


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]


def sumRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 0
    mid = (left + right) // 2
    return sumRange(segtree, left, mid, fr, to, 2 * index + 1) + sumRange(
        segtree, mid + 1, right, fr, to, 2 * index + 2
    )


def updateQuery(segtree, a, left, right, index, pos, value):
    if pos < left or right < pos:
        return
    if left == right:
        a[pos] += value  # adding value to a[pos]
        segtree[index] += value  # adding value to segtree[index]
        return
    mid = (left + right) // 2
    if pos <= mid:
        updateQuery(segtree, a, left, mid, 2 * index + 1, pos, value)
    else:  # if pos > mid
        updateQuery(segtree, a, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]


INF = 10**9
from math import ceil, log2


def curiousRobinHoodSegmentTree():
    T = int(input())
    for tc in range(1, T + 1):
        n, q = map(int, input().split())
        nums = list(map(int, input().split()))
        h = ceil(log2(n))
        sizeTree = 2 * (2**h) - 1
        segtree = [INF] * sizeTree
        # segTree = [INF] * 4 * n
        buildTree(nums, segtree, 0, n - 1, 0)
        print("Case " + str(tc) + ":")
        for _ in range(q):
            query = list(map(int, input().split()))
            if query[0] == 1:
                i = query[1]
                print(nums[i])
                updateQuery(segtree, nums, 0, n - 1, 0, i, -nums[i])
            if query[0] == 2:
                i = query[1]
                v = query[2]
                updateQuery(segtree, nums, 0, n - 1, 0, i, v)
            if query[0] == 3:
                fr = query[1]
                to = query[2]
                print(sumRange(segtree, 0, n - 1, fr, to, 0))
    return


# curiousRobinHoodSegmentTree()


"""
Interval Product

N integers X1,...,Xn
K rounds

each round
a change command: change one value in the sequence
a product command: if product Xi,...Xj is positive, negative or 0

input:
N K
N integers
each K -> command C/P
C -> change command, P -> product command
C I V: Xi's value changes to V
P I J: product from Xi to Xj 

output:
P -> +/-/0
C -> no output

example:
4 6
-2 6 0 -1
C 1 10
P 1 4
C 3 7
P 2 2
C 4 -5
P 1 4
5 9
1 5 -2 4 3
P 1 2
P 1 5
C 4 -5
P 1 5
P 4 5
C 3 0
P 1 5
C 4 -5
C 4 -5

0+-
+-+-0
"""


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[2 * index + 1] * segtree[2 * index + 2]


def productRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 1
    mid = (left + right) // 2
    return productRange(segtree, left, mid, fr, to, 2 * index + 1) * productRange(
        segtree, mid + 1, right, fr, to, 2 * index + 2
    )


def updateQuery(a, segtree, left, right, index, pos, value):
    if pos < left or pos > right:
        return
    if left == right:
        a[pos] = value
        segtree[index] = value
        return
    mid = (left + right) // 2
    if pos <= mid:
        updateQuery(a, segtree, left, mid, 2 * index + 1, pos, value)
    else:  # if pos > mid
        updateQuery(a, segtree, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] * segtree[2 * index + 2]


INF = 10**9


def intervalProduct():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    segtree = [INF] * 4 * N
    buildTree(nums, segtree, 0, N - 1, 0)
    for _ in range(K):
        query = list(map(str, input().split()))
        command = query[0]
        if command == "C":
            i = int(query[1])
            v = int(query[2])
            updateQuery(nums, segtree, 0, N - 1, 0, i - 1, v)
        if command == "P":
            i = int(query[1])
            j = int(query[2])
            res = productRange(segtree, 0, N - 1, i - 1, j - 1, 0)
            if res > 0:
                print("+", end="")
            elif res < 0:
                print("-", end="")
            else:
                print("0", end="")
    print()
    return


def solveIntervalProduct():
    while True:
        try:
            intervalProduct()
        except EOFError:
            return


# solveIntervalProduct()

"""
Brackets

correct bracket expressions

every pair consists of opening bracket & closing braket
for every pair part of the word between the brackets of this pair
has equal number of opening and closing brackets

replacement - changes ith bracket into the opposite one
check - if the word is a correct bracket expression

a program which
reads -> bracket word and the sequence of operations performed
for every check operation -> checks if current bracket word is a correct
bracket expression
write out the outcome

input
n: length of bracket word
n brackets
m: number of operations
each m: k, k = 0 -> check, k > 0 -> replacement of kth bracket by the opposite

output
Test ith:
every check -> YES if correct bracket expression, NO otherwise
"""


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]


def updateQuery(a, segtree, left, right, index, pos, value):
    if pos < left or pos > right:
        return
    if left == right:
        a[pos] *= value
        segtree[index] *= value
        return
    mid = (left + right) // 2
    if pos <= mid:
        updateQuery(a, segtree, left, mid, 2 * index + 1, pos, value)
    else:
        updateQuery(a, segtree, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]


def check(segtree, minVal):
    if minVal < 0:
        return False
    if segtree[0] != 0:
        return False
    return True


def add(a):
    res = []
    temp = 0
    for i in range(len(a)):
        if a[i] == 1:
            temp += 1
        elif a[i] == -1:
            temp -= 1
        res.append(temp)
    return res


INF = 10**9


def brackets():
    tc = 1
    while True:
        try:
            n = int(input())
            print("Test " + str(tc) + ":")
            expression = input()
            nums = []
            segtree = [INF] * 4 * n
            for ch in expression:
                if ch == "(":
                    nums.append(1)
                elif ch == ")":
                    nums.append(-1)
            added = add(nums)
            segtree = [INF] * 4 * n
            buildTree(nums, segtree, 0, n - 1, 0)
            m = int(input())
            for _ in range(m):
                k = int(input())
                if k == 0:
                    minVal = min(added)
                    if check(segtree, minVal):
                        print("YES")
                    else:
                        print("NO")
                else:
                    updateQuery(nums, segtree, 0, n - 1, 0, k - 1, -1)
                    added = add(nums)
            tc += 1
        except EOFError:
            return


brackets()
