import random
import numpy as np

def Insertion_Sort(A):
    """
    Function sorts array via insertion sort. Time Complexity: Theta(n**2).
    Input: Unsorted array of integers.
    Output: Sorted array of integers.
    """
    if len(A) == 1:
        return A
    if len(A) <= 0:
        return None
    length = len(A)
    for i in range(0, length):
        temp = A[i]
        j = i - 1
        while j >= 0 and temp < A[j]:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = temp
    return A

print(Insertion_Sort(np.random.randint(1, 10001, 100))) ##Generates array of length 100 from 1 to 10000.