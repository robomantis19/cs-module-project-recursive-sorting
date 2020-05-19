# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    if arrA[-1] < arrB[0]: 
        merged_arr[len(arrA[:-1])] = arrA[-1]
        merge_sort(arrA)
    elif arrA[-1] > arrB[0]:
        merged_arr[len(arrB[0:])] = arrB[0] 
        merge_sort(arrB)
    # Your code here
    # if len(arrA) <= len(arrB): 
    #     lowest_length = arrA
    #     biggest_length = arrB
    # else: 
    #     lowest_length = arrB
    #     biggest_length = arrB
    # for i in range(0, len(lowest_length)):
    # if lowest_length[i] > biggest_length[i]:
        
    #     merged_arr.append(biggest_length[i])
    # else: 
    #     merged_arr.append(lowest_length[i])
        
    
    else: 


        return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    
    
    mid = (len(arr))//2
    chunk_1 = arr[mid:]
    chunk_2 = arr[:mid]
    # merged_arr = merge(chunk_1, chunk_2)
    if len(arr) == 2: 
        finalarray = []
        finalarray.append(chunk_1)
        finalarray.append(chunk_2)
        print('final', finalarray)
    else:
        merged_arr = merge(chunk_1, chunk_2)
        merge_sort(merged_arr)
    


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
