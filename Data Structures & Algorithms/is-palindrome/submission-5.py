class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = s[::-1]
        b1= re.sub(r'[^a-zA-Z0-9]', '', b).lower()
        s1 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(b1)
        if s1 == b1 : 
            return True 
        else : 
            return False