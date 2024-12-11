"""
printer queue
"""


def printer_queue():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        nums = list(map(int, input().split()))
        q = []

        for i in range(n):
            q.append((nums[i], i))
        time = 0
        while q:
            mx = max(q)
            if q[0][0] == mx[0]:
                time += 1
                if q[0][1] == m:
                    print(time)
                    break
                q.pop(0)
            else:
                q.append(q.pop(0))


printer_queue()


"""
pangram
"""


def pangram():
    n = int(input())
    word = input()
    word = word.lower()
    dic = {}
    for letter in word:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    if len(dic) != 26:
        print("NO")
        return
    print("YES")
    return


pangram()

"""
Soldier and Bananas
"""


def soldier_and_bananas():
    k, n, w = map(int, input().split())
    total = 0
    for i in range(1, w + 1):
        total += k * i
    owned = n - total
    if owned < 0:
        print(-owned)
    else:
        print(0)
    return


soldier_and_bananas()

"""
Find The Median
"""


def find_the_median():
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    length = len(ar)
    print(ar[length // 2])
    return


find_the_median()


import queue

"""
Bombs! NO they are Mines!!
"""
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def is_valid(r, c, rows, cols):
    return r >= 0 and r < rows and c >= 0 and c < cols


def bom(R, C):
    rows = int(input())
    matrix = [[0 for _ in range(R)] for _ in range(C)]
    count = [[0 for _ in range(R)] for _ in range(C)]
    for i in range(rows):
        line = list(map(int, input().split()))
        row = line[0]
        total = line[1]
        for j in range(total):
            col = line[j + 2]
            matrix[row][col] = 1

    sr, sc = map(int, input().split())  # start row, start col
    er, ec = map(int, input().split())  # end row, end col
    q = queue.Queue()
    q.put((sr, sc))
    matrix[sr][sc] = 1

    while not q.empty():
        cr, cc = q.get()  # cur row, cur col

        for i in range(4):  # up, down, left, right
            r = cr + dr[i]
            c = cc + dc[i]

            if is_valid(r, c, R, C) and matrix[r][c] != 1:
                matrix[r][c] = 1
                q.put((r, c))
                count[r][c] = count[cr][cc] + 1
            if r == er and c == ec:
                print(count[er][ec])
                return


while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break
    bom(R, C)
