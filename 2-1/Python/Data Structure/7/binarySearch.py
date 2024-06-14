import random
from selection_insertion_bubbleSort import selectionSort

def rBinarySearch(A, key, low, high):  # time regulation O(n)/2
    if (low > high):
        return -1  # list must be sorted
    mid = (low + high) // 2  # get median value of list

    if key == A[mid]: return mid  # find median
    elif key < A[mid]: return rBinarySearch(A, key, low, mid - 1)  # if number is bigger than median, get new median by dividing the list to upper half
    else: return rBinarySearch(A, key, mid + 1, high)  # if number is smaller than median, get new median by dividing the list to lower half


if __name__ == '__main__':
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))
    selectionSort(A)  # sorted
    print(A)

    key = int(input('Input Search Key: '))
    print(f"rBinarySearch(A, {key}) = {rBinarySearch(A, key, 0, 14)}")
