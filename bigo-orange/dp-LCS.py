"""
Love Calculator

"""


def solve(s, t):
    n = len(s)
    m = len(t)
    minLen = [n + 1][m + 1](INF)
    numWays = [n + 1][m + 1](0)
    for i in range(n):
        minLen[i][0] = i
        numWays[i][0] = 1
    for j in range(m):
        minLen[0][j] = j
        numWays[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            if s[i - 1] == t[j - 1]:
                minLen[i][j] = minLen[i - 1][j - 1] + 1
                numWays[i][j] = numWays[i - 1][j - 1]
            else:
                minLen[i][j] = min(minLen[i - 1][j], minLen[i][j - 1]) + 1
                if minLen[i][j] == minLen[i - 1][j] + 1:
                    numWays[i][j] += numWays[i - 1][j]
                if minLen[i][j] == minLen[i][j - 1] + 1:
                    numWays[i][j] += numWays[i][j - 1]
    return (minLen[n][m], numWays[n][m])

    return


def loveCalculator():
    t = int(input())
    for tc in t:
        s = input()
        t = input()
        answer = solve(s, t)
        print("Case " + tc + ": " + answer[0] + " " + answer[1])
