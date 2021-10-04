'''Problem Statement #

Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

'''

def remove_dup(arr):
    
    dup_cntr = 1
    count = 0
    i = 1
    while i < len(arr):
        if arr[dup_cntr - 1] != arr[i]:
            arr[dup_cntr] = arr[i]
            dup_cntr += 1
        i +=1
    return dup_cntr


def main():
    print("After dup removal="+str(remove_dup([2, 3, 3, 3, 6, 9, 9])))
    print("After dup removal="+str(remove_dup([2, 2, 2, 11])))
main()
