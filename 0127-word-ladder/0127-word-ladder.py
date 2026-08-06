class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        s = set(wordList)
        if endWord not in s:
            return 0
        if beginWord == endWord:
            return 1
        frontBegin, frontEnd = {beginWord}, {endWord}
        visited = {beginWord, endWord}
        d = 1
        while frontBegin and frontEnd:
            if len(frontBegin) > len(frontEnd):
                frontBegin, frontEnd = frontEnd, frontBegin
            nxt = set()
            d += 1
            for w in frontBegin:
                wlst = list(w)
                for i in range(len(wlst)):
                    orig = wlst[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == orig:
                            continue
                        wlst[i] = c
                        t = ''.join(wlst)
                        if t in frontEnd:
                            return d
                        if t in s and t not in visited:
                            visited.add(t)
                            nxt.add(t)
                    wlst[i] = orig
            frontBegin = nxt
        return 0