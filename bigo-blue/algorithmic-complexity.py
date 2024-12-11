def maxRead(n, t, minutes):
    # O(n) for time, O(1) for space
    max_book = 0
    left = 0
    time = 0
    for right in range(n):
        time += minutes[right]
        while time > t:
            time -= minutes[left]
            left += 1
        max_book = max(max_book, right - left + 1)
    print(max_book)
    return None


first_input = list(map(int, input().split()))
n = first_input[0]
t = first_input[1]
minutes = list(map(int, input().split()))
maxRead(n, t, minutes)

n = 4
t = 5
minutes = [3, 1, 2, 1]
maxRead(n, t, minutes)  # 3

n = 3
t = 3
minutes = [2, 2, 3]
maxRead(n, t, minutes)  # 1


n = 2
t = 10
minutes = [6, 4]
maxRead(n, t, minutes)  # 2


def array(n, k, nums):
    count = [0] * 100001
    unique = 0
    for right in range(n):
        if unique < k:
            if count[nums[right]] == 0:
                unique += 1
            count[nums[right]] += 1
        if unique == k:
            left = 0
            while True:
                if count[nums[left]] > 1:
                    count[nums[left]] -= 1
                    left += 1
                else:
                    print(left + 1, right + 1)
                    return None
    print("-1 -1")
    return None


first_input = list(map(int, input().split()))
n = first_input[0]
k = first_input[1]
second_input = list(map(int, input().split()))
nums = second_input
array(n, k, nums)

n = 4
k = 2
nums = [1, 2, 2, 3]
array(n, k, nums)  # 1 2

n = 8
k = 3
nums = [1, 1, 2, 2, 3, 3, 4, 5]
array(n, k, nums)  # 2 5

n = 7
k = 4
nums = [4, 7, 7, 4, 7, 4, 7]
array(n, k, nums)  # -1 -1


def serejaAndDima(n, nums):
    left = 0
    right = n - 1
    player1_score = 0  # Seraja's score
    player2_score = 0  # Dima's score
    player1_turn = True
    player2_turn = False
    while left <= right:
        if nums[left] > nums[right]:
            num = nums[left]
            left += 1
        else:
            num = nums[right]
            right -= 1
        if player1_turn and not player2_turn:
            player1_score += num
            player1_turn = False
            player2_turn = True
        else:
            player2_score += num
            player1_turn = True
            player2_turn = False

    print(player1_score, player2_score)
    return None


n = int(input())
nums = list(map(int, input().split()))
serejaAndDima(n, nums)

n = 4
nums = [4, 1, 2, 10]
serejaAndDima(n, nums)  # 12 5

n = 7
nums = [1, 2, 3, 4, 5, 6, 7]
serejaAndDima(n, nums)  # 16 12


def aliceAndBob(n, nums):
    # O(n) for time, O(1) for space
    count_a = 0
    count_b = 0
    left = 0
    right = n - 1
    a_finish = False
    b_finish = False
    while left <= right:
        if left == right:
            if a_finish == True and b_finish == False:
                count_b += 1
            elif b_finish == True and a_finish == False:
                count_a += 1
            else:
                count_a += 1
            break
        if nums[left] > nums[right]:
            count_b += 1
            nums[left] = nums[left] - nums[right]
            right -= 1
            b_finish = True
            a_finish = False
        elif nums[left] < nums[right]:
            count_a += 1
            nums[right] = nums[right] - nums[left]
            left += 1
            a_finish = True
            b_finish = False
        else:
            count_a += 1
            count_b += 1
            left += 1
            right -= 1
            a_finish = True
            b_finish = True
    print(count_a, count_b)
    return None


n = int(input())
nums = list(map(int, input().split()))
aliceAndBob(n, nums)

n = 5
nums = [2, 9, 8, 2, 7]
aliceAndBob(n, nums)  # 2 3

n = 1
nums = [1]
aliceAndBob(n, nums)  # 1 0


def george_and_round(n, m, A, B):
    # O(n+m) for time, O(1) for space
    sum = n
    i = 0
    j = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            sum -= 1
            i += 1
            j += 1
        else:
            j += 1
    print(sum)
    return None


first_input = list(map(int, input().split()))
n = first_input[0]  # number of problems in a good round
m = first_input[1]  # number of problems George prepared
second_input = list(map(int, input().split()))
A = second_input
third_input = list(map(int, input().split()))
B = third_input
george_and_round(n, m, A, B)


n = 3
m = 5
A = [1, 2, 3]
B = [1, 2, 2, 3, 3]
george_and_round(n, m, A, B)  # 0

n = 3
m = 5
A = [1, 2, 3]
B = [1, 1, 1, 1, 1]
george_and_round(n, m, A, B)  # 2

n = 3
m = 1
A = [2, 3, 4]
B = [1]
george_and_round(n, m, A, B)  # 3


n = 20
m = 25
A = [30, 32, 34, 39, 42, 43, 45, 46, 47, 48, 52, 55, 56, 57, 58, 59, 60, 65, 67, 69]
B = [
    2,
    3,
    4,
    5,
    8,
    9,
    14,
    16,
    18,
    20,
    24,
    27,
    29,
    30,
    34,
    35,
    36,
    37,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
]
george_and_round(n, m, A, B)  # 12


# n: number of guilty people
# claws: length of the i-th person's claw
# print the total number of alive people after the bell rings
def wrath(n, claws):
    # alive = n
    # left = n - 2
    # right = n - 1
    # while left >= 0:
    #     if left < right and left >= right - claws[right]:
    #         alive -= 1
    #     left -= 1
    # print(alive)
    # return None

    ans = 0
    right = n
    for left in range(n - 1, -1, -1):
        if left < right:
            ans += 1
        x = left - claws[left]
        if x < 0:
            x = 1
        if right > x:
            right = x
    print(ans)
    return None


n = int(input())
claws = list(map(int, input().split()))
wrath(n, claws)


n = 4
claws = [0, 1, 0, 10]
wrath(n, claws)  # 1

n = 2
claws = [0, 0]
wrath(n, claws)  # 2

n = 10
claws = [1, 1, 3, 0, 0, 0, 2, 1, 0, 3]
wrath(n, claws)  # 3


def approximate_constant_range(n, nums):
    # O(n) for time, O(1) for space
    right = 0
    best = 0
    count = 0
    freq = [0] * 100001
    for left in range(n):
        while right < n:
            if freq[nums[right]] == 0:
                if count == 2:
                    break
                count += 1
            freq[nums[right]] += 1
            right += 1
        best = max(best, right - left)
        if freq[nums[left]] == 1:
            count -= 1
        freq[nums[left]] -= 1
    print(best)
    return None


n = int(input())
nums = list(map(int, input().split()))
approximate_constant_range(n, nums)

n = 5
nums = [1, 2, 3, 3, 2]
approximate_constant_range(n, nums)  # 4

n = 11
nums = [5, 4, 5, 5, 6, 7, 8, 8, 8, 7, 6]
approximate_constant_range(n, nums)  # 5
