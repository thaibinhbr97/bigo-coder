"""
Backtracking

for N-Queen problem, time complexity is O(n!) = O(n^n)

"""

# N = 4
# board = [[0] * N for i in range(N)]


# def printSolution():
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j], end=" ")
#         print()
#     print()


# def check(board, row, col):
#     # check vertical
#     for i in range(row):
#         if board[i][col]:
#             return False
#     # check main diagonal
#     i = row
#     j = col
#     while i >= 0 and j >= 0:
#         if board[i][j]:
#             return False
#         i -= 1
#         j -= 1
#     # check secondary diagonal
#     i = row
#     j = col
#     while j < N and i >= 0:
#         if board[i][j]:
#             return False
#         i -= 1
#         j += 1
#     return True


# def NQueen(board, row):
#     if row == N:
#         printSolution()
#         return True
#     for j in range(N):
#         if check(board, row, j) == True:
#             board[row][j] = 1
#             NQueen(board, row + 1)
#             board[row][j] = 0
#     return False


# if __name__ == "__main__":
#     NQueen(board, 0)


# """
# Permutations of string
# """


# def permutations(s, l, r):
#     """
#     Time complexity: O(N*N!) => O(N^N+1)
#     """
#     if l == r:
#         print("".join(s))
#     else:
#         for i in range(l, r):
#             s[l], s[i] = s[i], s[l]
#             permutations(s, l + 1, r)
#             s[l], s[i] = s[i], s[l]


# if __name__ == "__main__":
#     s = list("ABCD")
#     permutations(s, 0, len(s))


# """
# Distinct permutations of string
# """


# def shouldSwap(s, start, end):
#     for i in range(start, end):
#         if s[i] == s[end]:
#             return False
#     return True


# def distinctPermutations(s, l, r):
#     """
#     Time comlexity: O(N*N*N!)
#     """
#     if l >= r:
#         print("".join(s))
#         return
#     for i in range(l, r):
#         if shouldSwap(s, l, i) == True:
#             s[l], s[i] = s[i], s[l]
#             distinctPermutations(s, l + 1, r)
#             s[l], s[i] = s[i], s[l]


# if __name__ == "__main__":
#     s = list("AABB")
#     distinctPermutations(s, 0, len(s))


# print()

# """
# Combination

# Time complexity: O(K^N)
# """


# def printAns(a):
#     for i in range(len(a)):
#         print(a[i], end=" ")


# def combination(a, n, left, k):
#     if k == 0:
#         printAns(a)
#         print()
#         return
#     for i in range(left, n + 1):
#         a.append(i)
#         combination(a, n, i + 1, k - 1)
#         a.pop()


# if __name__ == "__main__":
#     n = 6
#     k = 4
#     a = []
#     combination(a, n, 1, k)

"""
function backtracking(curState, ...otherParams):
    if curState is a Solution:
        processSolution(curState)
    if curState is invalid:
        exit
    for nextStep can move from curState:
        apply nextStep to curState
        backtracking(curState, ...otherParams)
        remove nextStep from curState
"""


"""
Lotto

input:
n list of n
0 to end

output:
combination in ascending order

"""


def printAns(a):
    for i in range(len(a)):
        print(a[i], end=" ")


def combination(S, a, n, left, k):
    if k == 0:
        printAns(a)
        print()
        return
    for i in range(left, n):
        a.append(S[i])
        combination(S, a, n, i + 1, k - 1)
        a.pop()


# Time complexity: O(T*(6^N)), T: # of test cases, 6: # of chosen elements in the array, N: # of distinct numbers of the set (49)
# => O(T*(6^49))
while True:
    raw_data = list(map(int, input().split()))
    if raw_data[0] == 0:
        break
    k = 6
    S = raw_data[1:]
    n = len(S)
    a = []
    combination(S, a, n, 0, k)
    print()

"""
The Hamming Distance Problem

input:
# of dataset

"""


"""
Minimize Absolute Difference

5 numbers of positive numbers
find subset 4 numbers such that |a/b - c/d| is minimal

output:
a b c d
in lexiclogical order
"""


"""
Digger Octaves

'X': crystal
'.': empty

input:
T

each T:
N 
each N: connections

output:
each T => gives # of distinct ways to get 8 crystals
"""
