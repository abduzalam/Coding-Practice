'''
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

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

def fruits_into_basket(fruits):
    window_start = 0
    fruit_freq = {}
    max_length = 0

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if(right_fruit not in fruit_freq):
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1
        #using while loop to eliminate all characters which comes only once
        #between the first window....
        while(len(fruit_freq) > 2):
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -= 1
            if(fruit_freq[left_fruit] == 0):
                del fruit_freq[left_fruit]
            window_start += 1
        max_length = max(max_length,window_end-window_start + 1)
    return max_length

def main():
    print("maximum num of fruits "+str(fruits_into_basket(['A','B','C','A','C'])))
    print("maximum num of fruits "+str(fruits_into_basket(['A','B','C','B','B','C'])))

main()
