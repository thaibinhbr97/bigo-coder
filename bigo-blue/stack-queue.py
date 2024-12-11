def transform_the_expression(expression):
    s = []
    for symbol in expression:
        if symbol.isalpha():
            print(symbol, end="")
        elif symbol == ")":
            print(s.pop(), end="")
        # elif symbol in ["+", "-", "*", "/", "^"]:
        elif symbol != "(":
            s.append(symbol)
    print()
    return None


t = int(input())
for i in range(t):
    expression = input()
    transform_the_expression(expression)


def street_parade(n, mobiles):
    side_street = []
    expected = 1
    possible = True
    for mobile in mobiles:
        while side_street and side_street[-1] == expected:
            side_street.pop()
            expected += 1
        if mobile == expected:
            expected += 1
        elif side_street and side_street[-1] < mobile:
            possible = False
            break
        else:
            side_street.append(mobile)
    if possible:
        print("yes")
    else:
        print("no")
    return None


while True:
    n = int(input())
    if n == 0:
        break
    mobiles = list(map(int, input().split()))
    street_parade(n, mobiles)

from queue import Queue


def throw_card_away(q):
    discard_cards = []
    if q.qsize() == 1:
        print("Discarded cards:")
        print("Remaining card:", q.queue[0])
        return None
    while q.qsize() > 1:
        discard_card = q.get()
        discard_cards.append(discard_card)
        move_card = q.get()
        q.put(move_card)
    last_card = q.queue[0]
    print("Discarded cards:", ", ".join(list(map(str, discard_cards))))
    print("Remaining card:", last_card)
    return None


while True:
    n = int(input())
    if n == 0:
        break
    q = Queue()
    for i in range(1, n + 1):
        q.put(i)
    throw_card_away(q)

from queue import Queue


def patient_queue():
    count = 0
    while True:
        population, commands = map(int, input().split())
        if population == 0 and commands == 0:
            break
        count += 1

        hos_queue = Queue()
        for i in range(1, min(population, commands) + 1):
            hos_queue.put(i)

        print("Case " + str(count) + ":")
        for _ in range(commands):
            line = input().split()
            cmd = line[0]
            if cmd == "N":
                front = hos_queue.get()
                print(front)
                hos_queue.put(front)
            else:
                x = int(line[1])
                n = hos_queue.qsize()
                hos_queue.put(x)
                for i in range(n):
                    front = hos_queue.get()
                    if front != x:
                        hos_queue.put(front)
    return None


patient_queue()


def mass_of_molecule(string):
    s = []
    molecules = {"C": 12, "H": 1, "O": 16}
    for char in string:
        if char in molecules:
            s.append(molecules[char])
        elif char.isdigit():
            mol = s[-1] * int(char)
            s.pop()
            s.append(mol)
        elif char == "(":
            s.append("(")
        elif char == ")":
            total = 0
            while s[-1] != "(":
                total += s[-1]
                s.pop()
            s.pop()
            s.append(total)
    print(sum(s))
    return None


mass_of_molecule(input())

string = "COOH"
mass_of_molecule(string)  # 45

string = "CH(CO2H)3"
mass_of_molecule(string)  # 148

string = "((CH)2(OH2H)(C(H))O)3"
mass_of_molecule(string)  # 222


def compiler_and_parser(string):
    # # Using stack
    # # O(n) for time, O(n) for space
    # s = []
    # ans = 0
    # for i, char in enumerate(string):
    #     if char == "<":
    #         s.append(char)
    #     elif len(s) == 0:
    #         break
    #     else:
    #         s.pop()
    #         if len(s) == 0:
    #             ans = i + 1
    # print(ans)
    # return None

    # Using count to count the "<" element from the string
    # O(n) for time, O(1) for space
    count = 0
    ans = 0
    for i, char in enumerate(string):
        if char == "<":
            count += 1
        elif count == 0:
            break
        else:
            count -= 1
            if count == 0:
                ans = i + 1
    print(ans)
    return None


T = int(input())
for _ in range(T):
    string = input()
    compiler_and_parser(string)


string = "<<<>><>>>>><><><><><><>"
compiler_and_parser(string)  # 8

string = "<<>>"
compiler_and_parser(string)  # 4

string = "><"
compiler_and_parser(string)  # 0

string = "<>>>"
compiler_and_parser(string)  # 2

string = "<<<"
compiler_and_parser(string)  # 0


from collections import deque


# server free & query queue empty -> server process query
# server busy & < b queries in queue -> query added to queue
# server busy & >= b queries in queue -> new query rejected and never processed
def processing_queries(n, b, queries):
    ans = []
    q = deque()
    processing = 0
    for query in queries:
        t = query[0]
        d = query[1]
        while len(q) != 0 and t >= q[0]:
            q.popleft()
        if len(q) <= b:
            processing = max(t, processing) + d
            q.append(processing)
            ans.append(processing)
        else:
            ans.append(-1)
    for e in ans:
        print(e, end=" ")
    print()
    return None


n, b = map(int, input().split())
queries = []
for i in range(n):
    query = list(map(int, input().split()))
    queries.append(query)
processing_queries(n, b, queries)

n = 5
b = 1
queries = [[2, 9], [4, 8], [10, 9], [15, 2], [19, 1]]
processing_queries(n, b, queries)  # 11 19 -1 21 22

n = 4
b = 1
queries = [[2, 8], [4, 8], [10, 9], [15, 2]]
processing_queries(n, b, queries)  # 10 18 27 -1
