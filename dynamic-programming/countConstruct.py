"""
Count in how many ways we can construct the target string by using words from the wordBank array.

                  |   Brute Force    |    Memoized
---------------------------------------------------------
Time Complexity   |   O(n^m * m)     |    O(n * m^2)
Space Complexity  |   O(m^2)         |    O(m^2)

"""

def countConstruct(target: str, wordBank: List[str]) -> int:
    memo = {}
    
    def check(target):
        if target in memo: return memo[target]
        if target == "": return 1
        
        totalCount = 0
        
        for word in wordBank:
            if target.find(word) == 0:
                suffix = target[len(word):]
                numberOfWays = check(suffix)
                totalCount += numberOfWays
        
        memo[target] = totalCount
        return totalCount
    
    return check(target)

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
    
