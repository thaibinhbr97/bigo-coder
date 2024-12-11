# v = [2, 3, 1, 5, 10, 11]

# # sorting
# Ascending
# v.sort()
# v = sorted(v)

# Descending
# v.sort(reverse=True)
# v = sorted(v, reverse=True)

# key lambda
# descending
# v.sort(key=lambda x: -x)
# v = sorted(v, key=lambda x: -x)
# print(v)

# sort sub list
# v[1:4] = sorted(v[1:4])
# print(v)


# Constructor
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num / self.denom)

    def __iter__(self):
        return self


v = []
v.append(Fraction(5, 4))
v.append(Fraction(7, 9))
v.append(Fraction(1, 8))
v.append(Fraction(9, 2))
v.append(Fraction(12, 8))
v.sort(key=lambda fraction: fraction.num / fraction.denom)
v.sort(key=lambda fraction: fraction.num / fraction.denom, reverse=True)
for value in v:
    print(value)


# Student constructor
class Student:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __str__(self):
        result = f"{self.id}: {self.score}"
        return result

    def __iter__(self):
        return self

    def __gt__(self, other):
        if self.score > other.score:
            return True
        elif self.score < other.score:
            return False
        else:
            if self.id < other.id:
                return True
            else:
                return False

    def __lt__(self, other):
        # First way
        if self.score < other.score:
            return True
        elif self.score > other.score:
            return False
        else:
            if self.id > other.id:
                return True
            else:
                return False

        # Second way
        # if (self.score < other.score) or (self.score == other.score and self.id > other.id):
        #     return True
        # return False


s = []
s.append(Student(100, 8.5))
s.append(Student(101, 7.5))
s.append(Student(102, 8.5))
s.append(Student(103, 10.0))
s.append(Student(104, 10.0))
s.append(Student(105, 4.5))
s.sort(reverse=True)
# s.sort(key=lambda k: (-k.score, k.id))
for student in s:
    print(student)


# Devu, the Dumb guy
def selfLearning(subjects, x):
    min_time = 0
    for subject in subjects:
        min_time += subject * x
        if x > 1:
            x -= 1
    return min_time


n, x = map(int, input().split())
subjects = list(map(int, input().split()))
result = selfLearning(subjects, x)
print(result)


# Leetcode 169
# Time: O(n) - Space(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for key, val in dic.items():
            if val > mid:
                return key


# Boyer-Moore algorithm
def majorityElement(nums):
    count = 0
    element = 0

    for num in nums:
        if count == 0:
            element = num
            count = 1
        elif num == element:
            count += 1
        else:
            count -= 1
    return element


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))


def isPalindrome(word):
    n = len(word)
    i = 0
    j = n - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


def firstPalindrome(words):
    # for word in words:
    #     if isPalindrome(word):
    #         return word
    # return ""

    for word in words:
        if word == word[::-1]:
            return word
        return ""


print(isPalindrome("abc"))  # False
print(isPalindrome("car"))  # False
print(isPalindrome("ada"))  # True
print(isPalindrome("racecar"))  # True
print(isPalindrome("cool"))  # False
print(isPalindrome("cqllrtyhw"))  # False
print(isPalindrome("swwisru"))  # False
print(isPalindrome("gpzmbders"))  # False
print(isPalindrome("wqibjuqvs"))  # False
print(isPalindrome("pp"))  # True
print(isPalindrome("usewxryy"))  # False
print(isPalindrome("ybqfuh"))  # False
print(isPalindrome("hqwwqftgyu"))  # False
print(isPalindrome("jggmatpk"))  # False
print(isPalindrome("aua"))  # True
print(isPalindrome("auua"))  # True
print(isPalindrome("auaa"))  # False
print(isPalindrome("auaua"))  # True


def missingNumber(nums):
    # # O(n^2) in time, O(n) in space
    # low = min(nums)
    # high = max(nums)
    # loi = list(range(len(nums) + 1))
    # print(loi)
    # for i in loi:
    #     if i not in nums:
    #         return i

    # O(nlogn) in time, O(n) in space
    # nums.sort()
    # for i in range(len(nums)):
    #     if i != nums[i]:
    #         return i
    #     return len(nums)

    # # O(n) in time, O(1) in space
    n = len(nums)
    total = int(n * (n + 1) / 2)  # calculate sum of n natural number
    subtotal = 0
    for num in nums:
        subtotal += num
    result = total - subtotal
    return result


nums1 = [3, 0, 1]
print(missingNumber(nums1))  # 2
nums2 = [0, 1]
print(missingNumber(nums2))  # 2
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]  # 8
print(missingNumber(nums3))


def intersect(nums1, nums2):
    # O(n) in space, O(nlogn) in time
    nums1.sort()
    nums2.sort()
    n1 = len(nums1)
    n2 = len(nums2)
    i, j = 0, 0
    result = []
    while i < n1 and j < n2:
        # print(nums1[i])
        # print(nums2[j])
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1
    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # [2,2]
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))  # [4,9]
nums1 = [1, 2, 2, 1]
nums2 = [2]
print(intersect(nums1, nums2))  # [2]
nums1 = [3, 1, 2]
nums2 = [1, 3]
print(intersect(nums1, nums2))  # [1,3]


def dumb_devu(n, x, times):
    # O(nlogn) for time, O(n) for space
    times.sort()
    ans = 0
    for time in times:
        ans += x * time
        if x > 1:
            x -= 1
    print(ans)
    return None


first_input = list(map(int, input().split()))
n = first_input[0]
x = first_input[1]
times = list(map(int, input().split()))
dumb_devu(n, x, times)

n = 2
x = 3
times = [4, 1]
dumb_devu(n, x, times)  # 11

n = 4
x = 2
times = [5, 1, 2, 1]
dumb_devu(n, x, times)  # 10

n = 3
x = 3
times = [1, 1, 1]
dumb_devu(n, x, times)  # 6


def gukiz_and_contest(n, ratings):
    # O(n) for time, O(n) for space
    best = max(ratings)
    rankings = [0] * (best + 1)
    for rating in ratings:
        rankings[rating] += 1
    # [0, 1, 0, 2]
    dic = {}  # dictionary for rank
    rank = 1
    for ranking in range(len(rankings) - 1, 0, -1):
        dic[ranking] = rank
        rank += rankings[ranking]
    # {"1": 3, "2": 3, "3": 1}
    for i, rating in enumerate(ratings):
        if i == len(ratings) - 1:
            print(dic[rating], end="\n")
        else:
            print(dic[rating], end=" ")
    return None


n = int(input())
ratings = list(map(int, input().split()))
gukiz_and_contest(n, ratings)

n = 3
ratings = [1, 3, 3]
gukiz_and_contest(n, ratings)  # 3 1 1

n = 1
ratings = [1]
gukiz_and_contest(n, ratings)  # 1

n = 5
ratings = [3, 5, 3, 4, 5]
gukiz_and_contest(n, ratings)  # 4 1 4 3 1


def business_trip(k, months):
    count = 0
    growth = 0
    months.sort(reverse=True)
    if k == 0:
        print(count)
        return None
    for month in months:
        growth += month
        count += 1
        if growth >= k:
            print(count)
            return None
    print("-1")
    return None


k = int(input())
months = list(map(int, input().split()))
business_trip(k, months)

k = 5
months = [1, 1, 1, 1, 2, 2, 3, 2, 2, 1, 1, 1]
business_trip(k, months)  # 2

k = 0
months = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 0]
business_trip(k, months)  # 0

k = 11
months = [1, 1, 4, 1, 1, 5, 1, 1, 4, 1, 1, 1]
business_trip(k, months)  # 3


def towers(N, lengths):
    heights = [0] * 1001
    for length in lengths:
        heights[length] += 1
    [0, 1, 1, 1]
    best = max(heights)
    count = len(set(lengths))
    print(best, count)
    return None


N = int(input())
lengths = list(map(int, input().split()))
towers(N, lengths)

N = 3
lengths = [1, 2, 3]
towers(N, lengths)  # 1 3

N = 4
lengths = [6, 5, 6, 7]
towers(N, lengths)  # 2 3


def homeChores(n, a, b, chores):
    chores.sort()
    # [1, 2, 3, 6, 100]
    low = chores[b - 1]  # minimum x
    high = chores[b]
    diff = high - low
    print(diff)
    return None


first_input = list(map(int, input().split()))
n = first_input[0]
a = first_input[1]
b = first_input[2]
chores = list(map(int, input().split()))
homeChores(n, a, b, chores)

n = 5
a = 2
b = 3
chores = [6, 2, 3, 100, 1]
homeChores(n, a, b, chores)  # 3

n = 7
a = 3
b = 4
chores = [1, 1, 9, 1, 1, 1, 1]
homeChores(n, a, b, chores)  # 0

n = 2
a = 1
b = 1
chores = [10, 2]
homeChores(n, a, b, chores)  # 8


def sort_the_array(n, arr):
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    if is_sorted(arr):
        print("yes")
        print(1, 1)
    else:
        start, end = -1, -1
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                start = i
                break

        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                end = i
                break

        arr[start : end + 1] = reversed(arr[start : end + 1])
        if is_sorted(arr):
            print("yes")
            print(start + 1, end + 1)
        else:
            print("no")
    return None


n = int(input())
arr = list(map(int, input().split()))
sort_the_array(n, arr)

n = 3
arr = [3, 2, 1]
sort_the_array(n, arr)  # yes 1 3

n = 4
arr = [2, 1, 3, 4]
sort_the_array(n, arr)  # yes 1 2

n = 4
arr = [3, 1, 2, 4]
sort_the_array(n, arr)  # no

n = 2
arr = [1, 2]
sort_the_array(n, arr)  # yes 1 1


def pash_and_tea(n, w, cups):
    # sort the tea cups in an increasing order
    cups.sort()

    # calculate the amount of water each girl will receive
    x = min(cups[0], cups[n] / 2)

    # calculate the maximum total amount of water
    max_water = x * n + 2 * x * n

    result = min(max_water, w)
    print(result)
    return None


n, w = map(int, input().split())
cups = list(map(int, input().split()))
pash_and_tea(n, w, cups)


n = 2
w = 4
cups = [1, 1, 1, 1]
pash_and_tea(n, w, cups)  # 3

n = 3
w = 18
cups = [4, 4, 4, 2, 2, 2]
pash_and_tea(n, w, cups)  # 18


n = 1
w = 5
cups = [2, 3]
pash_and_tea(n, w, cups)  # 4.5
