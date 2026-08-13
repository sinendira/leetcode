class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bull = dict()

        in_secret = dict()
        in_guess = dict()
        bulls = 0
        for i in range(len(secret)):
            in_secret[secret[i]] = in_secret.get(secret[i],0) + 1
            in_guess[guess[i]] = in_guess.get(guess[i], 0) + 1

            if secret[i] == guess[i]:
                bulls += 1
                bull[secret[i]] = bull.get(secret[i],0) + 1
        
        cows = 0
        for x in set(secret):
            if x in in_guess:
                cows += max(min(in_guess[x],in_secret[x]) - bull.get(x,0),0)
        return(f"{bulls}A{cows}B")

            