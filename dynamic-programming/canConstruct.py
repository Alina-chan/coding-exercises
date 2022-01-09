"""
Given an array of strings, find out if we can construct the target string by concatenating elements from the wordBank.

target = "abcdef" 
wordBank = ["ab", "abc", "cd", "def", "abcd"]

              target = abcdef
              /      |      \
        [ab] /       | [abc]  \ [abcd]
            /        |         \
          cdef       def        ef          # remaining strings with no such prefix in wordBank 
           |         |                      # will return False to parent
      [cd] |         | [def]
           |         |
           ef        ""                     # empty string returns True to parent

                  |   Brute Force    |    Memoized
---------------------------------------------------------
Time Complexity   |   O(n^m * m)     |    O(n * m^2)
Space Complexity  |   O(m^2)         |    O(m^2)

"""

def canConstruct(target: int, wordBank: List[str]) -> bool:
    memo = {}
    
    def build(target):
        if target in memo: return memo[target]
        if target == "": return True

        for word in wordBank:
            # check if word is the prefix of target
            if target.find(word) == 0:
                suffix = target[len(word):]
                
                if build(suffix):
                    memo[target] = True
                    return True
                
        # target cannot be created     
        memo[target] = False
        return False
    
    return build(target)

print(canConstruct("abcdef", ["ab", "abc", "cd","def","abcd"])) # True
print(canConstruct("skateboard", ["bo", "rd", "ate","t","ska","sk","boar"])) # False
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee","eeee","eeeee","eeeeee"])) # False
