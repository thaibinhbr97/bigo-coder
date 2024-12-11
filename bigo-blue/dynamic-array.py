# declare list
# l = []

# l.append()

# l.insert(pos, obj)

# len(l)

# l[i]

# remove element at the end
# l.pop()

# remove element at a position
# l.pop(pos)

# clear all values
# l.clear()

# increase the size
# l.extend(2*[0])

# decrease the size
# l = l[0:2]

# check if empty
# if len(l) == 0: do something

# loop forward
# for i in range(len(l)):
#   print(l[i], end=', ')

# loop reverse
# for i in range(len(l)-1, -1, -1):
#   print(l[i], end=', ')

# declare string
# s = ""

# add multiple strings
# string0 = string0[:position] + string1 + string0[position:]

# remove substring
# string = string[:start_pos] + string[end_pos:]

# find substring in string -> -1 if not exist, index of substring in string if exist
# s.find(string)

# get substring
# string[start_pos:end_pos]

# combine strings
# string1 + string2

# check if digit using ASCII
# s = "123abc"
# for c in s:
#     if (ord(c)) >= 48 and ord(c) <= 57:
#         print(c, "is digit")
#     else:
#         print(c, "is not digit")

# isalpha/isLetter
# isdigit/isDigit
# islower/isLowerCase
# isupper/isUpperCase

# casting
# int(string)
# float(string)
# str(number)

# covert to lower or uppercases
# s.upper()
# s.lower()

# covert to lower or uppercases using ASCII
# s = "algorithm"
# c = chr(ord(s[2]) - 32)
# print(c)

# break string to words
# line = "nothing is impossible"
# line = line.split()
# s0 = line[0]
# print(s0)


# fashion in berland
# input - n: int, v: list
# special case: if n = 1, then "YES", else "NO"
# if number of 0 in v = 1, then "YES", else "NO"
def checkJacket(n, v):
    if n == 1:
        if v[0] == 1:
            print("NO")
        else:
            print("YES")
    else:
        count0 = 0
        for element in v:
            if element == 0:
                count0 += 1
        if count0 == 1:
            print("YES")
        else:
            print("NO")
    return None


n = int(input())
v = list(map(int, input().split()))

checkJacket(3, [1, 0, 1])
checkJacket(3, [1, 0, 0])
checkJacket(n, v)


def foo(n):
    if n == 0:
        return 1.0
    else:
        sum = 0
        count = 0
        for i in range(n):
            sum += foo(i)
            count += 1
        return sum


def correctFasten(n, nums):
    if n == 1:
        if nums[0] == 1:
            print("YES")
        else:
            print("NO")
        return None

    count_zero = 0
    for num in nums:
        if num == 0:
            count_zero += 1
    if count_zero == 1:
        print("YES")
    else:
        print("NO")
    return None


n = int(input())
nums = list(map(int, input().split()))
correctFasten(n, nums)


def minRotation(exhibit):
    start = ord("a")
    count = 0
    for letter in exhibit:
        count += min(abs(ord(letter) - start), 26 - abs(ord(letter) - start))
        start = ord(letter)
    print(count)
    return None


exihibit = "ares"
print(minRotation(exihibit))

exihibit = "zeus"
print(minRotation(exihibit))

exihibit = "map"
print(minRotation(exihibit))

exhibit = input()
minRotation(exhibit)


def bearAndGame(n, nums):
    start = 0
    boring_interval = 15
    end = 90
    for num in nums:
        if start + boring_interval < num:
            print(start + boring_interval)
            return None
        else:
            start = num
    if start + boring_interval <= end:
        print(start + boring_interval)
    else:
        print(end)
    return None


n = 3
nums = [7, 20, 88]
bearAndGame(n, nums)  # 35

n = 9
nums = [16, 20, 30, 40, 50, 60, 70, 80, 90]
bearAndGame(n, nums)  # 15

n = 9
nums = [15, 20, 30, 40, 50, 60, 70, 80, 90]
bearAndGame(n, nums)  # 90

n = 5
nums = [14, 29, 44, 59, 73]  # 88
bearAndGame(n, nums)

n = input()
nums = list(map(int, input().split()))
bearAndGame(n, nums)


def findLexiString(s, t):
    if s >= t:
        print("No such string")
        return None
    ans = ""
    end = len(s) - 1
    isConvert = False
    while end >= 0:
        while s[end] == "z" and isConvert == False:
            end -= 1
            ans += "a"
        if isConvert == False:
            ans += chr(ord(s[end]) + 1)
            isConvert = True
        else:
            ans += s[end]
        end -= 1
    ans = ans[::-1]
    if ans < t:
        print(ans)
    else:
        print("No such string")
    return None


s = "k"
t = "m"
# findLexiString(s, t)  # l

s = "klmnopq"
t = "klmpopq"
findLexiString(s, t)  # klmnopr

s = "abcde"
t = "abcdf"
findLexiString(s, t)  # No such string

s = "abaa"
t = "acaa"
findLexiString(s, t)  # abab

s = "xxxxxxxxxxxxxxxxxyyyyyyyyyyybbbbbbbccccccccddddddddddeeeeeeellllllllllzzzzzzzz"
t = "xxxxxxxxxxxxxxxxxyyyyyyyyyyybbbbbbbccccccccddddddddddeeeeeeelllllllllmzzzzzzzz"
findLexiString(s, t)
# xxxxxxxxxxxxxxxxxyyyyyyyyyyybbbbbbbccccccccddddddddddeeeeeeelllllllllmaaaaaaaa

s = "aaaaaaaaaaaaaamnzdl"
t = "aaaaaaaaaaaaaamnzeg"
findLexiString(s, t)  # aaaaaaaaaaaaaamnzdm

s = input()
t = input()
findLexiString(s, t)


def smartChosen(n, nums, A, B):
    # # O(n^2) for time, O(1) for space
    # len1 = n[0]
    # len2 = n[1]
    # num1 = nums[0]
    # num2 = nums[1]
    # count = 0
    # total = 0

    # for left in range(num1):
    #     for right in range(len2 - num2, len2):
    #         if count >= num2:
    #             break
    #         if A[left] >= B[right]:
    #             break
    #         else:
    #             count += 1
    #     if total >= num1:
    #         break
    #     if count >= num2:
    #         total += 1
    #     count = 0
    # if total >= num1:
    #     print("YES")
    # else:
    #     print("NO")
    # return None

    # O(1) for time, O(1) for space
    len1 = n[0]
    len2 = n[1]
    num1 = nums[0]
    num2 = nums[1]
    last_a = A[num1 - 1]
    first_b = B[len2 - num2]
    if last_a < first_b:
        print("YES")
    else:
        print("NO")
    return None


n = [3, 3]
nums = [2, 1]
A = [1, 2, 3]
B = [3, 4, 5]
smartChosen(n, nums, A, B)  # YES

n = [3, 3]
nums = [3, 3]
A = [1, 2, 3]
B = [3, 4, 5]
smartChosen(n, nums, A, B)  # NO

n = [5, 2]
nums = [3, 1]
A = [1, 1, 1, 1, 1]
B = [2, 2]
smartChosen(n, nums, A, B)  # YES

n = [4, 4]
nums = [2, 2]
A = [3, 4, 5, 6]
B = [3, 4, 5, 6]
smartChosen(n, nums, A, B)  # YES

n = list(map(int, input().split()))  # size of A & B
nums = list(map(int, input().split()))  # chosen number k from A and m from B
A = list(map(int, input().split()))  # array A
B = list(map(int, input().split()))  # array B
smartChosen(n, nums, A, B)


# find the segment that covers all other segments
# print its number if exist, -1 otherwise
# [a,b] covers [c,d] if a <= c <= d <= b
def bigSegment():
    # O(n) for time, O(n) for space
    n = int(input())
    i = 0
    segments = []
    cur_min = 10**9 + 1
    cur_max = 0
    while i < n:
        segment = list(map(int, input().split()))
        cur_min = min(cur_min, segment[0])
        cur_max = max(cur_max, segment[1])
        segments.append(segment)
        i += 1
    for j in range(len(segments)):
        if segments[j][0] == cur_min and segments[j][1] == cur_max:
            print(j + 1)
            return None
    print(-1)
    return None


bigSegment()


import copy


def passwords():
    first_input = list(map(int, input().split()))
    n = first_input[0]
    k = first_input[1]
    i = 0
    passwords = []

    while i < n:
        password = input()
        passwords.append(password)
        i += 1
    passwords = sorted(passwords, key=len)

    correct_password = input()
    password_length = len(correct_password)

    for password in passwords:
        if password == correct_password:
            passwords.remove(password)

    passwords_worst = copy.deepcopy(passwords)
    i = 0
    while i < n:
        if i >= n - 1:
            passwords_worst.append(correct_password)
            break
        else:
            if len(passwords_worst[i]) > password_length:
                passwords_worst.insert(i, correct_password)
                break
        i += 1

    passwords_best = copy.deepcopy(passwords)
    i = 0
    while i < n:
        if i >= n - 1:
            passwords_best.append(correct_password)
            break
        else:
            if len(passwords_best[i]) >= password_length:
                passwords_best.insert(i, correct_password)
                break
        i += 1

    worst_time = 0
    best_time = 0
    time_out = 5
    time_enter = 1

    trials = copy.deepcopy(k)
    # best_time
    for password in passwords_best:
        if trials == 0:
            trials = copy.deepcopy(k)
            best_time += time_out
        if password == correct_password:
            best_time += time_enter
            break
        best_time += time_enter
        trials -= 1

    trials = copy.deepcopy(k)
    # worst_time
    for password in passwords_worst:
        if trials == 0:
            trials = copy.deepcopy(k)
            worst_time += time_out
        if password == correct_password:
            worst_time += time_enter
            break
        worst_time += time_enter
        trials -= 1

    print(f"{best_time} {worst_time}")
    return None


# SOLUTION 2
def passwords():
    # O(n) for time, O(n) for space
    first_input = list(map(int, input().split()))
    n = first_input[0]
    k = first_input[1]
    arr = []
    smaller = 0
    same = 0
    for i in range(0, n):
        trial = input()
        arr.append(trial)
    password = input()
    for trial in arr:
        if len(trial) < len(password):
            smaller += 1
        if len(trial) == len(password) and trial != password:
            same += 1
    WA_best = smaller  # wrong attempt best
    WA_worst = smaller + same  # wrong attempt worst
    delay_best = WA_best // k
    delay_worst = WA_worst // k
    best_case = WA_best + delay_best * 5 + 1
    worst_case = WA_worst + delay_worst * 5 + 1
    print(best_case, worst_case)


passwords()


# SOLUTION 1
from collections import defaultdict


# suffix array: swap any two chars
# suffix automaton: remove any char
def suffixStructure(s, t):
    # Time O(n)
    dic_s = defaultdict(int)
    dic_t = defaultdict(int)
    for e in s:
        dic_s[e] += 1
    for e in t:
        dic_t[e] += 1
    for e in dic_t:
        if dic_s[e] < dic_t[e]:
            print("need tree")
            return None
    # now either automaton or array or both
    if len(s) == len(t):
        print("array")
        return None

    j = 0
    for i in range(len(s)):
        if s[i] == t[j]:
            j += 1
        if j == len(t):
            print("automaton")
            return None
    print("both")
    return None


s = "automaton"
t = "tomat"
suffixStructure(s, t)  # automaton

s = "array"
t = "arary"
suffixStructure(s, t)  # array

s = "both"
t = "hot"
suffixStructure(s, t)  # both

s = "need"
t = "tree"
suffixStructure(s, t)  # need tree

s = "ifaligpnhjdgfcbonmljpjjbbjlgbnocplnbjfkbggnhhmmdlmmecchpfiomdjabphmdikekjjdfcoaogfdpifhfpcadbcpkpp"
t = "ipkqpcyiqftcltctttzcrxzocjidqpvzjbnleapkshytzuatmyexbunmesajmkfeysvbselpsqtrv"
suffixStructure(s, t)  # need tree

s = "abacaba"
t = "aaaa"
suffixStructure(s, t)  # automaton

s = "nbjigpsbammkuuqrxfnmhtimwpflrflehffykbylmnxgadldchdbqklqbremcmzlpxieozgpfgrhegmdcxxfyehzzelcwgkierrj"
t = "bjbakuqrnhimwhffykylmngadhbqkqbrcziefredxxezcgkerj"
suffixStructure(s, t)  # automaton

s = input()
t = input()
suffixStructure(s, t)


# SOLUTION 2
def che(s, t):
    j = 0
    for i in s:
        if t[j] == i:
            j += 1
        if j == len(t):
            return True


s = input()
t = input()
sa = sorted(s)
st = sorted(t)
if sa == st:
    print("array")
elif che(s, t):
    print("automaton")
elif che(sa, st):
    print("both")
else:
    print("need tree")


# SOLUTION 3
def suffixStructure(s, t):
    cnt_s = [0] * 26
    cnt_t = [0] * 26
    for char in s:
        x = ord(char) - ord("a")  # s[i] - 'a'
        cnt_s[x] += 1
    for char in t:
        x = ord(char) - ord("a")
        cnt_t[x] += 1

    need_tree = False
    automaton = False
    array = False

    for i in range(26):
        if cnt_s[i] < cnt_t[i]:
            need_tree = True
            break
        elif cnt_s[i] > cnt_t[i]:
            automaton = True
            break

    # now frequency of every elements in cnt_s equals frequency of every elements in cnt_t
    match = -1
    for e in t:
        match = s.find(e, match + 1)
        if match == -1:
            array = True
            break

    if need_tree:
        print("need tree")
    else:
        if automaton and array:
            print("both")
        elif automaton:
            print("automation")
        elif array:
            print("array")
    return None


# s = "automaton"
# t = "tomat"
# suffixStructure(s, t)  # automaton

# s = "array"
# t = "arary"
# suffixStructure(s, t)  # array

# s = "both"
# t = "hot"
# suffixStructure(s, t)  # both

s = "need"
t = "tree"
suffixStructure(s, t)  # need tree

s = "ifaligpnhjdgfcbonmljpjjbbjlgbnocplnbjfkbggnhhmmdlmmecchpfiomdjabphmdikekjjdfcoaogfdpifhfpcadbcpkpp"
t = "ipkqpcyiqftcltctttzcrxzocjidqpvzjbnleapkshytzuatmyexbunmesajmkfeysvbselpsqtrv"
suffixStructure(s, t)  # need tree

s = "abacaba"
t = "aaaa"
suffixStructure(s, t)  # automaton

s = "nbjigpsbammkuuqrxfnmhtimwpflrflehffykbylmnxgadldchdbqklqbremcmzlpxieozgpfgrhegmdcxxfyehzzelcwgkierrj"
t = "bjbakuqrnhimwhffykylmngadhbqkqbrcziefredxxezcgkerj"
suffixStructure(s, t)  # automaton
