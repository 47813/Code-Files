def selectionSort(A):
    for i in range(len(A) - 1):
        least = i  # i's index
        for j in range(i + 1, len(A)):  # from the least variable's next number to the end of the list
            if A[j] < A[least]:
                least = j  # if least variable's number is smaller than j, set j as the least variable

        A[i], A[least] = A[least], A[i]  # switch the smallest number (least) with i's index


def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]  # save A[i]'s data
        j = i - 1
        while j >= 0 and key < A[j]:  # from A[i]'s previous card to the beginning of the list
            # until you meet a smaller number than key
            A[j + 1] = A[j]  # move the numbers, which are bigger than key, by 1 to the right
            j -= 1  # check the last number
        A[j + 1] = key  # put key at the empty index


def bubbleSort(A):
    for i in range(len(A) - 1, 0, -1):
        change = False  # check if the list was changed
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]  # swap number if left number is bigger than right number
                change = True  # list changed
        if not change: break  # if no change, which means the list is sorted, break


def printStep(A, idx):
    print(A)


if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    L = list(data)
    print("Before : ", L)
    selectionSort(L)
    print("Selection : ", L)
    print()

    L = list(data)
    print("Before : ", L)
    insertionSort(L)
    print("Insertion : ", L)
    print()

    L = list(data)
    print("Before : ", L)
    bubbleSort(L)
    print("Bubble : ", L)
