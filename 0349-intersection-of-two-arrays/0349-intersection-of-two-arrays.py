class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      freq = defaultdict(int)
      for num in nums1:
        freq[num]+=1
      li = []
      for num in nums2:
        if num in freq:
            li.append(num)
            del freq[num]
      return li      

          

