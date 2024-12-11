"""
Lecture Note

Trie
"""


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


# Time: O(string_length) for add, find, and delete


# adding word to trie
# case 1: an adding word is not yet in trie
# case 2: an adding word is a prefix of other string in trie
# case 3: an adding word already has a prefix of other string in trie
def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
    temp.countWord += 1


# find a word in trie
# case 1: a word does not exist in trie
# case 2: a word exists, but it is not a word in trie (as a prefix of other word in trie)
# case 3: a word can be found in trie
def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return False
        temp = temp.child[ch]
    return temp.countWord > 0


# delete a word in trie

# case 1: a word is independent, once deleted it does not affect
# other words in trie
# step 1: go through from first char to last char of a word to
# determine if it exists in trie or not
# step 2: check each node to see if it can be deleted or not
# conditions to delete:
# - is the node the end of a word
# - is the node the prefix of other node

# case 2: a word is a prefix of other word
# step 1: go through from start to last char of a word that needs to be deleted to determine if it exists in trie or not
# step 2: check each node to see if it can be deleted or not
# conditions to delete:
# - is the node the end of a word
# - is the node a prefix of other word

# case 3: a word that needs to be deleted contains other word
# step 1: go through from the start to last char of a word that needs to be deleted
# step 2: check each node to see if it satisfies deleting conditions
# conditions for deleting:
# - is the node the end of a word
# - is the node a prefix of other word


def isWord(node):
    return node.countWord != 0


def isEmpty(node):
    return len(node.child) == 0


def removeWord(root, s, level, len):
    if root == None:
        return False
    if level == len:
        if root.countWord > 0:
            root.countWord -= 1
            return True
        return False
    ch = s[level]
    if ch not in root.child:
        return False
    flag = removeWord(root.child[ch], s, level + 1, len)
    if (
        flag == True
        and isWord(root.child[ch]) == False
        and isEmpty(root.child[ch]) == True
    ):
        del root.child[ch]
    return flag


def printWord(root, s):
    if isWord(root):
        print(s)
    for ch in root.child:
        printWord(root.child[ch], s + ch)


if __name__ == "__main__":
    root = Node()
    addWord(root, "bigo")
    addWord(root, "the")
    addWord(root, "then")
    print(findWord(root, "there"))
    print(findWord(root, "th"))
    print(findWord(root, "the"))
    printWord(root, "")
    removeWord(root, "bigo", 0, 4)
    removeWord(root, "the", 0, 3)
    removeWord(root, "then", 0, 4)


"""
Search Engine

n,q: # of data, # of queries

next n lines
s, weight: data, priority

next q lines
query: query for output

output:
print q lines, each line is a max priority for each query if found, otherwise -1
"""


class Node:
    def __init__(self):
        self.weight = 0
        self.child = dict()


def addWord(root, s, weight):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.weight = max(temp.weight, weight)


def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return -1
        temp = temp.child[ch]
    return temp.weight


n, q = map(int, input().split())
root = Node()
for _ in range(n):
    line = list(map(str, input().split()))
    word = line[0]
    weight = int(line[1])
    addWord(root, word, weight)
for _ in range(q):
    word = input()
    print(findWord(root, word))

# 2 1
# hackerearth 10
# hackerrank 9
# hacker


"""
DNA Prefix

n: # of DNA sets
each set contains {A,C,G,T}
Find a subset that has common longest prefix * the number of samples in the set that is maximum

Input:
T: test cases
n: # of DNA sets
next n lines: DNA
"""


class Node:
    def __init__(self):
        self.level = 0
        self.count = 0
        self.child = dict()


def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        tempLevel = temp.level
        temp = temp.child[ch]
        temp.level = tempLevel + 1
        temp.count += 1


def solve(root, s):
    temp = root
    res = 0
    for ch in s:
        if ch not in temp.child:
            return -1
        temp = temp.child[ch]
        res = max(res, temp.count * temp.level)
    return res


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    root = Node()
    strings = []
    for _ in range(n):
        s = input()
        strings.append(s)
        addWord(root, s)
    ans = []
    for s in strings:
        ans.append(solve(root, s))
    print("Case " + str(t) + ": " + str(max(ans)))


# 1
# 4
# ACGT
# ACGTGCGT
# ACCGTGC
# ACGCCGT

"""
Consistency Checker

Given a set of numbers, find if these number are consistent with each other or not

Input:
T: test cases
n: # of data for each test case
data: n data for each test case

Output:
"YES" for consistent
"NO" otherwise
"""

My solution (does not work)


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


def addWordAndCheckConsistent(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.countWord != 0:
            return True  # prefix of current words in trie
    temp.countWord += 1
    if temp.child:
        return True  # prefix of current words in trie
    return False  # not prefix of current words in trie


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    root = Node()
    printed = False
    for _ in range(n):
        s = input()
        ans = addWordAndCheckConsistent(root, s)
        if ans == True:
            print("Case " + str(t) + ": NO")
            printed = True
            break
    if not printed:
        print("Case " + str(t) + ": YES")


# Solution
class TrieNode:
    def __init__(self):
        self.wordCount = 0
        self.child = dict()


def addWord(root, s):
    n = len(s)
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = TrieNode()
        temp = temp.child[ch]
    temp.wordCount += 1


def isConsistent(root, s):
    temp = root
    for ch in s:
        if temp.wordCount != 0:
            return False
        if ch not in temp.child:
            return True
        temp = temp.child[ch]
    return len(temp.child) == 0


def consistency_checker(strings):
    root = TrieNode()
    for s in strings:
        addWord(root, s)
    for s in strings:
        if not isConsistent(root, s):
            return "NO"
    return "YES"


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    strings = []
    for _ in range(n):
        s = input()
        strings.append(s)
    ans = consistency_checker(strings)
    print(f"Case {tc}: {ans}")


# 1
# 10
# 579379
# 524492
# 696009
# 696
# 92476
# 5315058
# 788469082
# 32529
# 25
# 65545


"""
Contacts

add: add name
find: find partial

Input:
n: # of commands
each command: add/find word

Output:
for each find, print a number that starts with prefix existed in trie
"""


class Node:
    def __init__(self):
        self.count = 0
        self.child = dict()


def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.count += 1


def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return 0
        temp = temp.child[ch]
    return temp.count


n = int(input())
root = Node()
for _ in range(n):
    command, word = map(str, input().split())
    if command == "add":
        addWord(root, word)
    else:
        print(findWord(root, word))

# Input:
# 4
# add hack
# add hackerrank
# find hac
# find hak

# Output:
# 2
# 0

"""
Bank and Vulnerable Passwords

Input:
N: # of passwords
for N rows, each row contains a password

Output:
vulnerable if it exists a prefix of other word in trie
and non vulnerable otherwise
"""


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


def isVulnerable(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        # In case words added before are shorter in length than a current word:
        # go through each character, if countWord at that character is not 0 meaning that this prefix already exists in other words -> vulnerable
        if temp.countWord != 0:
            return True
    temp.countWord += 1
    # In case words added before are longer in length than a current word:
    # go one child further and check if child is empty or not
    # if child is not empty -> it is a prefix of other word in trie -> vulnerable
    # else -> not vulnerable
    if temp.child:
        return True
    return False


N = int(input())
root = Node()
for _ in range(N):
    s = input()
    printed = False
    if isVulnerable(root, s) and not printed:
        printed = True
        print("vulnerable")
        break
if not printed:
    print("non vulnerable")


# 2
# likemeifyoucan
# likeme

"""
No Prefix Set

N: # of strings, each string contains a - j (inclusive)
GOOD SET: if no string is a prefix of other strings. 
Otherwise, BAD SET. In case that if 2 strings are identical -> they are prefix of each other -> BAD SET.

Output:
GOOD SET if no prefix in a set of strings
BAD SET if at least one prefix exists in a set of strings
"""


class Node:
    def __init__(self):
        self.wordCount = 0
        self.child = dict()


def addWordAndCheckValid(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.wordCount != 0:
            return False
    temp.wordCount += 1
    if temp.child:
        return False
    return True


N = int(input())
root = Node()
for _ in range(N):
    s = input()
    ans = addWordAndCheckValid(root, s)
    printed = False
    if not ans:
        print("BAD SET")
        print(s)
        printed = True
        break
if not printed:
    print("GOOD SET")


"""
Old Berland Language

N: # of words in ancient Berland language

Input:
N
nums are length of each word

Output:
YES 
print these words on each line

NO
"""


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = 0
        self.word = 0


def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
    temp.countWord += 1


N = int(input())
nums = list(map(str, input().split()))
