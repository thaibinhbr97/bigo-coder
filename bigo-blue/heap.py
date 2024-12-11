"""
heap -> min-heap or max-heap
1. build help from list: O(n) for time
2. find min/max on heap: O(1) for time
3. add a new node to heap: O(logn) for time
4. delete a new node from heap: O(logn) for time

to find index of children node from ith node:
left = index*2 + 1
right = index*2 + 2
"""


def minHeapify(i):
    # i is the index of ith element in the list
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len(h) and h[left] < h[smallest]:
        smallest = left
    if right < len(h) and h[right] < h[smallest]:
        smallest = right
    if smallest != i:
        # swap
        h[i], h[smallest] = h[smallest], h[i]
        minHeapify(smallest)


def buildHeap(n):
    for i in range(n // 2 - 1, -1, -1):
        minHeapify(i)


# if __name__ == "__main__":
#     h = [7, 12, 6, 10, 17, 15, 2, 4]
#     buildHeap(len(h))
#     print(h)


# find min of min-heap
def top():
    return h[0]


# add a new node to heap
def push(value):
    h.append(value)
    i = len(h) - 1
    while i != 0 and h[(i - 1) // 2] > h[i]:
        h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]
        i = (i - 1) // 2


# delete a node from min-heap
def pop():
    length = len(h)
    if length == 0:
        return
    h[0] = h[length - 1]
    h.pop()
    minHeapify(0)


# priority queue
# 1: PriorityQueue using put(), get(), queue[0]
import queue

variable = queue.PriorityQueue()


# work with max heap using PriorityQueue
class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


a = [7, 12, 6, 10, 17, 15, 2, 4]
pq = queue.PriorityQueue()
for x in a:
    pq.put(PQEntry(x))
# work with min heap using PriorityQueue
pq = queue.PriorityQueue()
h = [7, 12, 6, 10, 17, 15, 2, 4]
for x in h:
    pq.put(x)
# size: len(pq.queue)
# empty: pq.empty()
# clear: pq=queue.PriorityQueue()

# 2: heapq
import heapq

variable = []


# work with max heap using heapq
class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


a = [7, 12, 6, 10, 17, 15, 2, 4]
h = []
for x in a:
    heapq.heappush(h, PQEntry(x))
# working with min heap using heapq
h = [7, 12, 6, 10, 17, 15, 2, 4]
heapq.heapify(h)
print(h)
size: len(h)
clear: h.clear()

import heapq


def three_largest_product(n, A):
    # using heap
    # O(nlogk) for time, O(n) for space
    max_heap = []
    for num in A:
        heapq.heappush(max_heap, -num)
        if len(max_heap) < 3:
            print(-1)
            continue
        first = heapq.heappop(max_heap)
        second = heapq.heappop(max_heap)
        third = heapq.heappop(max_heap)
        product = -1 * first * second * third
        print(product)
        heapq.heappush(max_heap, first)
        heapq.heappush(max_heap, second)
        heapq.heappush(max_heap, third)
    return

    # using comparison
    # O(n) for time, O(1) for space
    # first, second, third = 0, 0, 0
    # count = 0
    # for e in A:
    #     if e > first:
    #         third = second
    #         second = first
    #         first = e
    #     elif e > second:
    #         third = second
    #         second = e
    #     elif e > third:
    #         third = e
    #     if first == 0 or second == 0 or third == 0:
    #         count += 1
    #         if count < 3:
    #             print(-1)
    #         else:
    #             print(0)
    #     else:
    #         product = first * second * third
    #         print(product)
    # return


n = int(input())
A = list(map(int, input().split()))
three_largest_product(n, A)

n = 5
A = [1, 2, 3, 4, 5]
three_largest_product(n, A)  # -1 -1 6 24 60


"""
1: "1 v" add an element to heap
2: "2 v" delete an element from heap
3: "3" return a min element in heap
"""

import heapq


class Heap:
    unique = set()

    def __init__(self):
        self.min_heap = []

    def add(self, value):
        heapq.heappush(self.min_heap, value)

    def delete(self, value):
        self.unique.add(value)

    def pop(self):
        while self.min_heap[0] in self.unique:
            self.unique.discard(self.min_heap[0])
            heapq.heappop(self.min_heap)
        print(self.min_heap[0])


n = int(input())
h = Heap()
for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        h.add(query[1])
    elif query[0] == 2:
        h.delete(query[1])
    elif query[0] == 3:
        h.pop()

import heapq


def qheap1():
    # O(T*N*logN)
    while True:
        N = int(input())
        if N == 0:
            break
        nums = list(map(int, input().split()))
        heapq.heapify(nums)
        cost = 0
        while len(nums) != 1:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            addition = first + second
            cost += addition
            heapq.heappush(nums, addition)
        print(cost)


qheap1()


import heapq


def roy_and_trending_topic(k):
    """
    p: 50
    l: 5
    c: 10
    s: 20
    """
    N = int(input())
    max_change = []
    heapq.heapify(max_change)
    topics = {}
    for _ in range(N):
        id, z_score, p, l, c, s = list(map(int, input().split()))
        new_z_score = p * 50 + l * 5 + c * 10 + s * 20
        change = new_z_score - z_score
        topics[id] = new_z_score
        heapq.heappush(max_change, (change, id))
        if len(max_change) > k:
            heapq.heappop(max_change)
    res = []
    for _ in range(k):
        id = heapq.heappop(max_change)[1]
        res.append([id, topics[id]])
    for e in res[::-1]:
        print(e[0], e[1])
    return


roy_and_trending_topic(5)

import heapq


def promotion():
    n = int(input())
    prize = 0
    min_heap = []
    max_heap = []
    for _ in range(n):
        inputs = list(map(int, input().split()))
        k = inputs[0]
        receipts = inputs[1:]
        for receipt in receipts:
            heapq.heappush(min_heap, receipt)
            heapq.heappush(max_heap, -receipt)
            low = heapq.heappop(min_heap)
        high = -heapq.heappop(max_heap)
        prize += high - low
    print(prize)


promotion()


def a(n):
    freq = {}
    while n > 0:
        digit = n % 10
        if digit not in freq:
            freq[digit] = 1
        else:
            freq[digit] += 1
        n //= 10
    return freq


print(a(1003))


def create_staircase(nums):
    while len(nums) != 0:
        step = 1
        subsets = []
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets


def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets


nums = [1, 2, 3, 4, 5, 6]
print(create_staircase(nums))  # True

nums = [1, 2, 3, 4, 5, 6, 7]
print(create_staircase(nums))  # False

import fileinput
import os

# os.chdir(r"/Users/bradnguyen/github-repos/interview-preps/data-structures/python")
filename = "coding_qual_input.txt"


def decode(message_file):
    # create a dictionary to decode from number to message
    dic = {}
    # an answer string
    ans = ""
    # read line from the message_file
    for line in fileinput.input(files=message_file):
        # since line from file follows 'num word', we get it separately to key value into dic more easily
        num = int(line.split()[0])
        word = line.split()[1]
        # add value: word into dic every time we read a line
        dic[num] = word

    # a loop used to take an input from user
    while True:
        prompt = input()
        # a loop stops when there is no input or empty input
        if prompt == "":
            break
        # we only need the last element of the input and use it to decode the message
        value = int(prompt.split()[-1])
        # add each word to the message
        ans += dic[value] + " "
    # message is ans without the last whitespace
    ans = ans[: len(ans) - 1]
    # return message
    return ans


print(decode(filename))


import heapq


def restaurant_rating():
    # Time Limit Exceed
    # N = int(input())
    # max_heap = []
    # for _ in range(N):
    #     query = list(map(int, input().split()))
    #     command = query[0]  # 1, 2
    #     if command == 1:
    #         heapq.heappush(max_heap, -query[1])
    #     elif command == 2:
    #         temp = []
    #         k = len(max_heap) // 3
    #         if k == 0:
    #             print("No reviews yet")
    #         else:
    #             while k > 0:
    #                 value = heapq.heappop(max_heap)
    #                 temp.append(value)
    #                 k -= 1
    #             print(-value)
    #             for e in temp:
    #                 heapq.heappush(max_heap, e)

    N = int(input())
    ratings = []  # min heap
    display = []  # max heap
    total = 0
    for _ in range(N):
        query = list(map(int, input().split()))
        command = query[0]  # 1, 2
        if command == 1:
            total += 1
            heapq.heappush(ratings, query[1])
            if len(ratings) > total // 3:
                value = heapq.heappop(ratings)
                heapq.heappush(display, -value)
            elif -display[0] > ratings[0]:
                a = heapq.heappop(display)
                heapq.heappush(ratings, -a)
                b = heapq.heappop(ratings)
                heapq.heappush(display, -b)
        else:
            if total < 3:
                print("No reviews yet")
            else:
                print(ratings[0])


restaurant_rating()
