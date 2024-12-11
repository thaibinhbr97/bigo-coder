# def rearrangeArray(nums):
#     # # O(n) in time, O(n) in space
#     # positive = []
#     # negative = []
#     # result = []
#     # for num in nums:
#     #     if num > 0:
#     #         positive.append(num)
#     #     else:
#     #         negative.append(num)
#     # i = 0
#     # while i < len(positive):
#     #     result.append(positive[i])
#     #     result.append(negative[i])
#     #     i += 1
#     # return result

#     # n = len(nums)
#     # result = [0]*n

#     # # Initializing two pointers to track even and
#     # # odd indices for positive and negative integers respectively
#     # posIdx = 0
#     # negIdx = 1

#     # for i in range(n):
#     #     if nums[i] > 0:
#     #         # Placing the positive integer at the
#     #         # desired index in ans and incrementing posIdx by 2
#     #         result[posIdx] = nums[i]
#     #         posIdx += 2
#     #     else:
#     #         # Placing the negative integer at the
#     #         # desired index in ans and incrementing negIdx by 2
#     #         result[negIdx] = nums[i]
#     #         negIdx += 2
#     # return result

#     n = len(nums)
#     result = [0]*n

#     posIdx = 0
#     negIdx = 1

#     for i in range(n):
#         if nums[i] > 0:
#             result[posIdx] = nums[i]
#             posIdx += 2
#         else:
#             result[negIdx] = nums[i]
#             negIdx += 2
#     return result


# nums = [3, 1, -2, -5, 2, -4]
# print(rearrangeArray(nums))  # [3,-2,1,-5,2,-4]
# nums = [-1, 1]
# print(rearrangeArray(nums))  # [1,-1]


# def mergeAlternately(word1, word2):
#     # O(n) in time, O(n) in space
#     result = ''
#     n1 = len(word1)
#     n2 = len(word2)
#     i = 0
#     j = 0
#     while i < n1 and j < n2:
#         result += word1[i]
#         result += word2[j]
#         i += 1
#         j += 1
#     if n1 < n2:
#         result += word2[i:]
#     elif n1 > n2:
#         result += word1[j:]
#     return result


# word1 = "abc"
# word2 = "pqr"
# print(mergeAlternately(word1, word2))  # "apbqcr"
# word1 = "ab"
# word2 = "pqrs"
# print(mergeAlternately(word1, word2))  # "apbqrs"
# word1 = "abcd"
# word2 = "pq"
# print(mergeAlternately(word1, word2))  # "apbqcd"


# import math

# def isGcd(str, base):
#     if len(str) % len(base) != 0:
#         return False
#     else:
#         k = len(str) // len(base)
#         if base * k == str:
#             return True
#     return False


# def gcdOfStrings(str1, str2):
#     # # Brute Force solution
#     # # O(min(m,n)) for space, O(min(m,n)*(m+n)) for time

#     # n1 = len(str1)
#     # n2 = len(str2)
#     # n = min(n1, n2)
#     # base = str1 if n == n1 else str2

#     # while len(base) != 0:
#     #     if isGcd(str1, base) and isGcd(str2, base):
#     #         return base
#     #     else:
#     #         base = base[:-1]
#     # return ""

#     # Greatest Common Divisor
#     # O(m+n) for time, O(m+n) for space
#     if str1 + str2 != str2 + str1:
#         return ""
#     max_len = math.gcd(len(str1), len(str2))
#     return str1[:max_len]


# str1 = "ABCABC"
# str2 = "ABC"
# print(gcdOfStrings(str1, str2))  # "ABC"

# str1 = "ABABAB"
# str2 = "ABAB"
# print(gcdOfStrings(str1, str2))  # "AB"

# str1 = "LEET"
# str2 = "CODE"
# print(gcdOfStrings(str1, str2))  # ""


# def kidsWithCandies(candies, extraCandies):
#     # O(n) for space, O(n) for time
#     highest = max(candies)
#     minForGreatest = highest - extraCandies
#     result = []
#     for candy in candies:
#         if candy >= minForGreatest:
#             result.append(True)
#         else:
#             result.append(False)
#     return result


# candies = [2, 3, 5, 1, 3]
# extraCandies = 3
# print(kidsWithCandies(candies, extraCandies))  # [true,true,true,false,true]

# candies = [4, 2, 1, 1, 2]
# extraCandies = 1
# print(kidsWithCandies(candies, extraCandies))  # [true,false,false,false,false]

# candies = [12, 1, 12]
# extraCandies = 10
# print(kidsWithCandies(candies, extraCandies))  # [true,false,true]


# def canPlaceFlower(flowerbed, n):
#     # O(n) for time, O(1) for space
#     for i in range(len(flowerbed)):
#         # check if current slot is empty
#         if flowerbed[i] == 0:
#             # check if left and right slots are empty
#             empty_left_slot = (i == 0) or (flowerbed[i-1] == 0)
#             empty_right_slot = (i == len(flowerbed) -
#                                 1) or (flowerbed[i+1] == 0)
#             # if both left and right slots are empty, a flower can be planted
#             if empty_left_slot and empty_right_slot:
#                 flowerbed[i] = 1
#                 n -= 1
#                 if n <= 0:
#                     return True
#     return n <= 0

#     # # O(n) for time, O(n) for space
#     # newFlowerBed = [0] + flowerbed + [0]
#     # for i in range(1, len(newFlowerBed)-1):  # skip first and last
#     #     if newFlowerBed[i-1] == 0 and newFlowerBed[i+1] == 0 and newFlowerBed[i] == 0:
#     #         newFlowerBed[i] = 1
#     #         n -= 1
#     #     if n <= 0:
#     #         return True
#     # return n <= 0


# flowerbed = [1, 0, 0, 0, 1]
# n = 1
# print(canPlaceFlower(flowerbed, n))  # true

# flowerbed = [1, 0, 0, 0, 1]
# n = 2
# print(canPlaceFlower(flowerbed, n))  # false

# flowerbed = [1, 0, 1, 0, 1, 0, 1]
# n = 0
# print(canPlaceFlower(flowerbed, n))  # true

# flowerbed = [1, 0, 0, 0, 0, 1]
# n = 2
# print(canPlaceFlower(flowerbed, n))  # false

# flowerbed = [0, 0, 1, 0, 1]
# n = 1
# print(canPlaceFlower(flowerbed, n))  # true
