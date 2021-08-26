# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import copy

def solution(A):
    # write your code in Python 3.6
    A.sort()
    B = copy.deepcopy(A) #deep copy A
    B = list(set(B)) #delete pair
    
    if len(B) == 1: # when all elements are equal
        return A[0]

    for i in range(len(A)-1): #exclude comparing the last elements
        if i%2 == 0:
            if A[i] != A[i+1]:
                return A[i]
    
    
    # if the last element is not pair
    return A[-1]
