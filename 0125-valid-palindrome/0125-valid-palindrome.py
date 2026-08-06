class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        i,j = 0,n-1
        
        while i<j:
            if not s[i].isalnum():
                i+=1
                continue

            if not s[j].isalnum():
                j-=1
                continue

            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False

        return True