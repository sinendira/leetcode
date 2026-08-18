class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s==t or not s:
            return True
        
        n1 = len(s)
        n2 = len(t)

        if n1>n2 or not(t):
            return False

        fast = 0
        res = ""

        for i in range(n2):
            if fast <n1 and s[fast] == t[i]:
                res+=s[fast]
                fast+=1
        if res != s:
            return False
        else:
            return True
        