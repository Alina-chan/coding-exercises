"""
Given an integer array nums, find out the shortest combination of numbers 
that sum up to target.

Brute force works for small targets, but for larger targets the code hangs.
We make use of memoization to speed up and optimize our code
"""

def bestSum(target: int, nums: List[int]) -> List[int]:
    memo = {}
    
    def calc(target, nums, shortest = None):
        if target in memo: return memo[target]
        if target == 0: return []
        if target < 0: return None

        for num in nums:
            remainder = target - num
            remainderCombo = calc(remainder, nums, shortest)
            
            if remainderCombo is not None:
                # Get a copy of remainderCombo and add num to the list
                combination = remainderCombo.copy() + [num]
                
                if not shortest or len(combination) < len(shortest):
                    shortest = combination
        
        memo[target] = shortest
        return shortest
    
    return calc(target, nums)
    
print(bestSum(10, [3, 4, 5, 7]))    
print(bestSum(505, [1, 2, 5, 25]))
