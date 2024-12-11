"""
18	 00010010
invert
     11101101

add 1 ->
     11101110 -> -18

0	10000000


123 01111011
invert 
    10000100

add 1 ->
    10000101 -> -123
    
    
leftshift 123:  01111011 -> 11110110
leftshit: multiply by 2 -> 246

rightshift 123: 01111011 -> 00111101
rightshift: divide by 2 -> 61

arithmetic shift: meaning carry the sign over to the result after the shift

arithmetic leftshift -23:  11101001 -> 11010010
-> multiply by 2 -> -46

arithmetic rightshift -23: 11101001 -> 11110100
-> divive by 2 -> -12

&: AND
1 & 1 => 1
0 & 0 => 0
0 & 1 => 0
1 & 0 => 0

|: OR
1 | 1 => 1
1 | 0 => 1
0 | 1 => 1
0 | 0 => 0

^: XOR
1 ^ 1 => 0
0 ^ 0 => 0
1 ^ 0 => 1
0 ^ 1 => 1

~: NOT

shiftleft: <<

shiftright: >>

get ith bit:
x & (1 << i) != 0
my sol: (x >> i) & 1

set ith bit:
x | (1 << i) 
my sol: (x >> i) | 1

clear ith bit:
x & ~(1 << i)

switch ith bit:
x ^ (1 << i)


examples:
get bit at 2th of 5
(5 >> 2) & 1
5 & (1 << 2)

clear bit at 2th pos of 5
00000101 => 5
00000001 => 1
00000100 => 1 << 2
11111011 => ~(1 << 2)
00000100 => 5 & (~(1 << 2))

set bit at 3th pos of 5
00000101 => 5
00000001 => 1
00001000 => 1 << 3
00001101 => 5 | (1 << 3)

switch bit at 3th pos of 5
00000101 => 5
00000001 => 1
00001000 => 1<<3
00001101 => 5 ^ (1<<3)

switch bit at 2th pos of 5
00000101 => 5
00000001 => 1
00000100 => 1<<2
00000001 => 5 ^ (1<<2)
"""

# find a missing number (FMN)
# given a list from 1 to n, there is one number missing. Find the missing number
a = [1, 2, 3, 4, 6, 7, 8, 9]

# way 1: using sum formula
# O(n) for time
total = sum(a)
total_sum = 9 * 10 / 2  # n(n+1)/2 a sum formula
res = total_sum - total  # res is the missing number
print(int(res))

# way 2: using XOR ^
# O(n) for time
XOR_sum = 0
XOR_total = 0
for num in range(1, 10):
    XOR_sum ^= num
for num in a:
    XOR_total ^= num
res = XOR_sum ^ XOR_total
print(res)


# source code for finding the missing number
def getMissingNumber(a, n):
    # Time: O(n)
    xor = 1
    xor_array = a[0]
    for i in range(2, n + 2):
        xor ^= i
    for i in range(1, n):
        xor_array ^= a[i]
    return xor ^ xor_array


if __name__ == "__main__":
    a = [1, 2, 3, 4, 6, 7, 8, 9]
    result = getMissingNumber(a, 8)
    print(result)


# source code for fiding the missing number (optimized)
def computeXOR(n):
    # if n is a multiple of 4
    if n % 4 == 0:
        return n
    # if n % 4 gives remainder of 1
    if n % 4 == 1:
        return 1
    # if n % 4 gives remainder of 2
    if n % 4 == 2:
        return n + 1
    # if n % 4 gives remainder of 3
    return 0


def optimizedGetMissingNumber(a, n):
    xor_array = a[0]
    xor = computeXOR(n + 1)
    for i in range(1, n):
        xor_array ^= a[i]
    return xor ^ xor_array


if __name__ == "__main__":
    a = [1, 2, 3, 4, 6, 7, 8, 9]
    result = optimizedGetMissingNumber(a, 8)
    print(result)


# reverse bits of the given number
def bit_reversal(n):
    s = 8
    rev = 0
    while n != 0:
        # shift left
        rev <<= 1
        # if current bit is 1
        if n & 1 == 1:
            rev ^= 1  # XOR 1
        # shift right
        n >>= 1
        s -= 1
    if s > 0:
        rev <<= s
    return s


def bit_reversal(n):
    s = 0


if __name__ == "__main__":
    n = 38
    rev = bit_reversal(n)
    print(n, " (", bin(n), ")", sep="")
    print(rev, " (", bin(rev), ")", sep="")


"""
Samu and her Birthday Party

A[i] -> list of favorites in decimal

each W, W & A[i] != 0
"""


def bit2Int(s, k):
    ret = 0
    for i in range(k):
        if s[i] == "1":
            ret += 1 << i
    return ret


def bitCount1(W):
    count = 0
    while W > 0:
        if W & 1:
            count += 1
        W >>= 1


t = int(input())
for tc in t:
    n, k = map(int, input().split())
    A = []
    for i in range(n):
        s = int(input())
        A.append(bit2Int(s, k))

        ans = k
        for W in range(1 << (k - 1)):
            flag = True
            for i in range(n):
                if (W & A[i]) == 0:
                    flag = False
                    break
            if flag == True:
                ans = min(ans, bitCount1(W))

        print(ans)


"""
Sansa and XOR
"""
ans = 0
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(n):
        read(arr[i])
    ans = 0
    for i in range(n):
        if ((i+1) * (n-i)) % 2 == 1:
            ans ^-= arr[i]
    print(ans)
    
