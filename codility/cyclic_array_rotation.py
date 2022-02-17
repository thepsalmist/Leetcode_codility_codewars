# A function that takes two parameters, K and an array A
# The function will push numbers in array from left to right and brings the last elemet to the begining for every cycle
# The number K determines the maximum cycles

## Solution approach
# The index of each element changes from its index to the final cyclic position e.g (A[i] + K)


def solution(A, K):
    # store length of A in a variable N
    N = len(A)
    # create an empy list same size a A
    # B = A.copy()
    B = [None] * N

    for i in range(0, N):
        B[(i + K) % N] = A[i]
    return B
