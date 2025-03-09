class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for index,value in enumerate(numbers):
            diff = target - value
            if diff  in dict:
                return [dict[diff],index+1]    
            dict[value] = index+1    