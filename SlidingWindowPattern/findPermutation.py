'''
Permutation in a String (hard) #

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

    abc
    acb
    bac
    bca
    cab
    cba

If a string has ‘n’ distinct characters it will have n!n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

'''

def permuation_string(the_string,pattern):

    freq_map = {}
    window_start = 0
    matched = 0
    for chr1 in pattern:
        if chr1 not in freq_map:
            freq_map[chr1] = 0
        freq_map[chr1] += 1

    for window_end in range(len(the_string)):
        right_char = the_string[window_end]
        if(right_char in freq_map):
            freq_map[right_char] -= 1
            if(freq_map[right_char] == 0):
                matched += 1
        if (len(pattern) == matched):
            return True

        if window_end >= len(pattern) - 1:
            left_char = the_string[window_start]
            window_start += 1
            if(left_char in freq_map):
                if freq_map[left_char] == 0:
                    freq_map[left_char] -= 1
                    matched -= 1
                freq_map[left_char] +=1
    return False
def main():
    print("perfumation exist in the string = "+ str(bool(permuation_string("oidbcaf","abc"))))

main()
