def binSearch(nums,target):
    floor_index = -1
    ceiling_index = len(nums)

    while floor_index+1 < ceiling_index:
        distance = ceiling_index - floor_index
        half_index = distance // 2

        guess_index = half_index + floor_index

        guess_num = nums[guess_index]

        if target == guess_num:
            return True
        
        if guess_num > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index

    return False
def main():
    print("testing binary search = "+str(bool(binSearch([1,2,3,4,5,6,7],8))))
main()
