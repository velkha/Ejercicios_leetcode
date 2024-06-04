class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        length_of_longest_palindrome = 0
        odd_count_found = False
        for count in char_count.values():
            if count % 2 == 0:
                length_of_longest_palindrome += count
            else:
                length_of_longest_palindrome += count - 1
                odd_count_found = True
        if odd_count_found:
            length_of_longest_palindrome += 1
        
        return length_of_longest_palindrome