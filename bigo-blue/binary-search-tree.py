"""
Lecture Node

maximum 2 children on each parent node
each node is distinct
for each node, val of each node on the left < parent node and val of each node on the right > parent node
order 2 since there are 2 maximum children on each node
"""


class Node:
    # declare a class in BST
    # Time: O(1)
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None


# create a new node
# Time: O(1)
def createNode(x):
    newNode = Node()
    newNode.key = x
    return newNode


# add a new value to BST
# Time: O(h), h is the height of tree. Worst case: O(n)
def insertNode(root, x):
    if root == None:
        return createNode(x)
    if x > root.key:
        root.right = insertNode(root, x)
    elif x < root.key:
        root.left = insertNode(root, x)
    return root


# create a binary search tree (BST)
# Time: O(N*h), h is the height of tree
def createTree(a, n):
    root = None
    for i in range(n):
        root = insertNode(root, a[i])
    return root


# find a value in BST
# Time: O(h), h is the height of tree. Worst case: O(n)
def searchNode(root, x):
    if root == None or root.key == x:
        return root
    if root.key < x:
        return searchNode(root.right, x)
    return searchNode(root.left, x)


# delete a value in BST
# case 1: delete a left node
# traverse from root node to leaft node and delete it
# case 2: delete a node that has one or two leaf nodes
# bring a correct leaf node to replace the deleted node and delete the old node
# case 3: delete a root node/ delete the node that has multiple child nodes
# find a node that has a min value from the right branch or a max value from the left branch to replace the
# root node, then delete that node
# Time: O(h), h is height of tree. Worst case: O(n)
def deleteNode(root, x):
    if root == None:
        return root
    if x < root.key:
        root.left = deleteNode(root.left, x)
    elif x > root.key:
        root.right = deleteNode(root.right, x)
    else:
        if root.left == None:
            temp = root.right
            del root
            return temp
        elif root.right == None:
            temp = root.left
            del root
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current


# Traverse BST
# Inorder Traversal (Left -> Root -> Right) (1)
# Preorder Traversal (Root -> Left -> Right) (2)
# Postorder Traversal (Left -> Right -> Root) (3)


# Inorder Traversal (Left -> Root -> Right)
# 15 20 25 30 37 40 45
def inorderTraversal(root):
    if root != None:
        inorderTraversal(root.left)
        print(root.key, end=" ")
        inorderTraversal(root.right)


# Preorder Traversal (Root -> Left -> Right)
# 30 20 15 25 40 37 45
def preorderTraversal(root):
    if root != None:
        print(root.key, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)


# Postorder Traversal (Left -> Right -> Root)
# 15 25 20 37 45 40 30
def postorderTraversal(root):
    if root != None:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.key, end=" ")


# calculate size of BST
# Time: O(n)
def size(root):
    if root == None:
        return 0
    return size(root.left) + 1 + size(root.right)


# delete BST
# Time: O(n)
def deleteTree(root):
    if root == None:
        return
    deleteTree(root.left)
    deleteTree(root.right)
    del root


# Since Python has no built-in BST class, so we use Set set up by Hash


"""
Distinct Count

T: test cases
N,X: # of numbs, X: # of distinct numbs
A: arrays

Good: X distint numbers
Bad: < X ditinct numbers
Average: > distinct numbers
"""


def distinct_count():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        s = set()
        for i in range(N):
            s.add(A[i])
        n_distincts = len(s)
        if n_distincts == X:
            print("Good")
        elif n_distincts < X:
            print("Bad")
        else:
            print("Average")
    return


distinct_count()


"""
Isenbaev's Number

n: # of teams
each row: 3 members

A B C
B C D
D E A

A: [B,C,D,E], B:[A,C,D], C:[A,B,D], D:[E,A]
create a dictionary(key: set())
sort the dictionary by key in alphabetical order
"""


def champion_number():
    n = int(input())
    dic = dict()

    return


champion_number()


"""
Megacity

n,s: # of locations, population
each location has xi, yi coordinate values of ith location and number ki people

output:
-1 if it cannot become a megacy
min radius of the circle that city needs to expand to become a megacity
"""

import math


class DistancePopulation:
    def __init__(self, distance, population):
        self.distance = distance
        self.population = population

    def __lt__(self, other):
        return self.distance < other.distance


def megacity():
    MILLION = 10**6
    n, s = map(int, input().split())

    if s >= MILLION:
        print(0)

    pairs = []
    for _ in range(n):
        x, y, k = map(int, input().split())
        dist = x * x + y * y
        pairs.append(DistancePopulation(dist, k))
    pairs.sort()

    for i in range(n):
        s += pairs[i].population
        if s >= MILLION:
            distance = pairs[i].distance
            print(math.sqrt(distance))
            return
    print(-1)
    return


megacity()

"""
Monk and his friends

N: students
A: candies
M: students coming to sit with others that have the same # number of candies

T: test cases
"""


def monk_and_friends():
    N, M = map(int, input().split())
    candies = list(map(int, input().split()))
    A = set(candies[:N])
    B = candies[N:]
    for candy in B:
        if candy in A:
            print("YES")
        else:
            A.add(candy)
            print("NO")


T = int(input())
for _ in range(T):
    monk_and_friends()

1
7 4
3 5 5 5 5 5 1 4 1 2 2


"""
Penguins

Emperor Penguins - singing
Little Penguins - dancing
Macaroni Penguins - surfing

Output:
the kind of penguin that has a maximum number of appearances
"""


def penguins():
    n = int(input())
    freq = dict()
    for i in range(n):
        penguin = input()
        if penguin not in freq:
            freq[penguin] = 1
        else:
            freq[penguin] += 1

    ans = ""
    max_count = 0
    for penguin, count in freq.items():
        if count >= max_count:
            max_count = count
            ans = penguin
    print(ans)
    return


penguins()

"""
Minimum Loss

price prediction for a house in n years ahead from now
pi: price of the house in ith year
want min loss based on these requirements:
- cannot sell the house at the price >= the bought price
- cannot sell the house in the same bought year

Output:
find and print a min loss if bought the house and would sell it in
n years ahead
"""

n = int(input())
prices = list(map(int, input().split()))


def min_loss(n, prices):
    # # Time: O(n^2), Space: O(n)
    # loss = []
    # INF = float("inf")
    # for i in range(n):
    #     for j in range(i, n):
    #         diff = prices[j] - prices[i]
    #         if diff < 0:
    #             loss.append(diff)

    # print(-max(loss))
    # return

    # Time: O(nlogn), Space: O(n)
    min_cost = 10**16
    order = {}
    for i in range(n):
        order[prices[i]] = i
    prices.sort()
    for i in range(1, n):
        pre = prices[i - 1]
        post = prices[i]
        if post - pre < min_cost and order[post] < order[pre]:
            min_cost = post - pre
    print(min_cost)
    return


min_loss(n, prices)
