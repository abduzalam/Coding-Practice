'''
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
'''

#Bruteforce approach
'''
def average_subarray_ofsize_k(K,arr):
    result = []
    for i in range(len(arr)-K+1):
        _sum =0.0
        for j in range(i,i+K):
            _sum += arr[j]
        result.append(_sum/K)
    return result
'''
#using sliding window
def average_subarray_ofsize_k(K,arr):
    result=[]
    window_start , window_end = 0,0
    _sum = 0.0
    for window_end in range(len(arr)):
        _sum += arr[window_end]
        if window_end >= K - 1:
            result.append(_sum/K)
            _sum -= arr[window_start]
            window_start += 1
    return result

def main():
    print("Average of sub array of size K "+str(average_subarray_ofsize_k(5,[1, 3, 2, 6, -1, 4, 1, 8, 2])))


main()

