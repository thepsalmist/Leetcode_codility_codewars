# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# Aproach 1
# The smallest positive integer n=1, worst case, missing positive integer len(A)+1
# Therefor n belongs between (n=1, to n=(len(A)+1))


def solution(A):
    for i in range(len(A)):
        if A[i] < 0:
            A[i] = 0

    for i in range(len(A)):
        val = abs(A[i])
        if 1 <= val <= len(A):
            if A[val - 1] > 0:
                A[val - 1] *= -1
            elif A[val - 1] == 0:
                A[val - 1] = -1 * (len(A) + 1)

    for i in range(1, len(A) + 1):
        if A[i - 1] >= 0:
            return i
    return len(A) + 1
