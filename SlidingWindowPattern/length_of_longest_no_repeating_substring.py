'''
Given a string, find the length of the longest substring which has no repeating characters
Ex:1

Input String : "aabccbb"
Output :3
Explanation : The longest substring without any repeating char is "abc"
'''

def lengthof_longest_substring_with_no_repeat(instr):
    char_index_map = {}
    window_start = 0
    max_length = 0

    for window_end in range(len(instr)):
        right_char = instr[window_end]
        if right_char in char_index_map:
            window_start = max(window_start,char_index_map[right_char]+1)
        char_index_map[right_char] = window_end
        max_length = max(max_length,window_end-window_start + 1)
    return max_length
        

            
def main():
    print("length of longest substring with no repeat = "+str(lengthof_longest_substring_with_no_repeat("aabccbb")))
    print("length of longest substring with no repeat = "+str(lengthof_longest_substring_with_no_repeat("abbbb")))
    print("length of longest substring with no repeat = "+str(lengthof_longest_substring_with_no_repeat("abccde")))
main()
