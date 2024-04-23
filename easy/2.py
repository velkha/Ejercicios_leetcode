def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    x = 121
    x //= 10
    print(121 / 10)
    print(x)
    print(121 % 10)
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_number = 0
    while x > reverted_number:
        #add the last number
        reverted_number = reverted_number * 10 + x % 10
        #we remove the number we added
        x //= 10
    
    return x == reverted_number or x == reverted_number // 10