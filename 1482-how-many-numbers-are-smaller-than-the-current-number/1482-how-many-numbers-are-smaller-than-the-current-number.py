class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = sorted(nums)
        freq = defaultdict(int)
        for i , n in enumerate(num):
            if n not in freq:
                freq[n]=i
        li = []        
        for i in range(len(nums)):
            li.append(freq[nums[i]])
        return li    

        