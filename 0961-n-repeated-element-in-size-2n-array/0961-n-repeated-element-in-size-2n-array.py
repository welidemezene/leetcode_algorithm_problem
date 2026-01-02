class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        le = len(nums)
        for i in range(le):
            freq[nums[i]] +=1
        for n in freq:
            if freq[n] > 1:
                return n    
        