# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0
    b = 0 
    for i in range(0, elements): 
        if a >= len(arrA): 
            merged_arr[i] = arrB[b]
            b+= 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a+= 1
        elif arrA[a] < arrB[b]: 
            merged_arr
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else: 
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    
    if(len(arr) <= 1):
        return arr
    else:
        mid = (len(arr))//2
        chunk_1 = arr[mid:]
        chunk_2 = arr[:mid]
        merge_sort(chunk_1)
        merge_sort(chunk_2)
    # merged_arr = merge(chunk_1, chunk_2)
        return merge(chunk_1, chunk_2)
    


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
