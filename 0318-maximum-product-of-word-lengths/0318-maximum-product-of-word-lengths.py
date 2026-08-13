class Solution:
    def maxProduct(self, words: List[str]) -> int:
        self.map = {}
        self.max = 0
        for idx in range(len(words)):
            self.map[idx] = set()
            for ch in words[idx]:
                self.map[idx].add(ch)
                if(len(self.map[idx])==26): 
                    break
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                self.max = max(self.max,(self.checker(self.map[i],self.map[j],i,j,words))) 
        return self.max
    def checker(self,set1:set,set2:set,i:int,j:int,words:List[str]) -> int:
        for ch in set1:
            if ch in set2:
                return 0
        return len(words[i])*len(words[j])