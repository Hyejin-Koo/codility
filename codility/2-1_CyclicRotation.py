# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import copy
import random


def solution(A, K):
    # write your code in Python 3.6
    M = copy.deepcopy(A) # deepcopy A
    for i in range(len(A)):
        if A[i] >0:
            A[i] = A[i] + random.random()
        else:
            A[i] = A[i] - random.random() # in case of negative elements

    for j in A:
        M[int((A.index(j)+K)) %len(A)] = int(j)
    

    return M
