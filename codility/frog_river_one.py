# A small frog wants to get to the other side of a river. The frog is currently located at position 0, and wants to get to position X. Leaves fall from a tree onto
# the surface of the river.You are given a non-empty zero-indexed array A consisting of N integers representing the falling leaves.
# A[K] represents the position where one leaf falls at time K, measured in minutes.

# The goal is to find the earliest time when the frog can jump to the other side of the river.
# The frog can cross only when leaves appear at every position across the river from 1 to X.

# For example, you are given integer X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# In minute 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

# Approach 1: Brute Solution
# For each time value. Check if all the positions are filled

# Approach 2:


def solution(X, A):
    B = [-1] * X
    for i in range(0, len(A)):
        if A[i] < X and B[A[i] - 1] == -1:
            B[A[i] - 1] = i
    m = 0
    for i in range(0, len(B)):
        if B[i] == -1:
            return -1
        m = max(m, B[i])

    return m


# Approach 3
def solution(X, A):
    B = [0] * X
    s = 0
    for i in range(0, len(A)):
        if B[A[i] - 1] == 0 and A[i] <= X:
            s += 1
            B[A[i] - 1] = 1
        if s == X:
            return i
        return -1
