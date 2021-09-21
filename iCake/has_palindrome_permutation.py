'''
Write an efficient function that checks_whetherany permutation of an input string is a palindrome.
Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False

Idea here is simple: loop each char in the input string

and add the each char to a dictionary or a Set if the set not having the char
else remove from the set 

finally the length set is even number, then its not a palidrome and if the length is lesss than or equal to 1 , its a palindrom and permutation also

'''


import unittest
def has_palindrome_permutation(the_string):
     unpaired_characters = set()
     
     for char in the_string:
         if char in unpaired_characters:
             unpaired_characters.remove(char)
         else:
             unpaired_characters.add(char)
             
     return len(unpaired_characters) <= 1
# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
