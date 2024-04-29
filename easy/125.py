import re;
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Sin liberias y con el uso de 2 variables como pointers
        al ir recorriendo un array (aunque no es la manera mas optima, las mas optima es la solucion final usando liberias externas)
        str1 = ""
        str2 = ""
        i = 0
        for i in range(len(s)):
            if(s[i].isalnum()):
                str1 += s[i].lower()
            if(s[len(s)-1-i].isalnum()): 
                str2 += s[len(s)-1-i].lower()
        print(str1)
        print(str2)
        return str1==str2"""
        pattern = re.compile('[\W_]+') 
        test = (pattern.sub('', s)).lower()
        return test == test[::-1]