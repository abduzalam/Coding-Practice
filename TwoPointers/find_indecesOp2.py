#First Option is preffered
def find_indices(arr,target):
    #pass
    start_index=0
    last_index = len(arr)  - 1    
    result =[]
    currSum=0
    while (start_index < last_index):
        currSum = arr[start_index] + arr[last_index]

        if currSum == target:
            result.append(start_index)
            result.append(last_index)
            return result
        elif currSum > target:
            last_index -= 1
        else:
            start_index +=1
       
def main():
    print("indices of target sum =" +str(find_indices([1,2,3,4,6],6)))
    print("indices of target sum =" +str(find_indices([2,5,9,11],11)))
main()
