'''
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

def fruit_in_basket(the_fruites):
    window_start = 0
    fruits_map = {}
    max_fruits = 0

    for window_end in range(len(the_fruites)):
        right_char = the_fruites[window_end]
        if (right_char not in fruits_map):
            fruits_map[right_char] = 0
        fruits_map[right_char] += 1

        while (len(fruits_map) > 2):
            left_char = the_fruites[window_start]
            fruits_map[left_char] -= 1
            if (fruits_map[left_char] == 0):
                del fruits_map[left_char]           
            window_start += 1
        max_fruits = max(max_fruits,window_end - window_start + 1)
    return max_fruits

def main():
    print("the max num of fruites = " + str(fruit_in_basket(['A','B','C','A','C'])))
main()
