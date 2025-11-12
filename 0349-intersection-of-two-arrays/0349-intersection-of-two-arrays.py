class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        le = len(nums1)
        s = set(nums1)
        li = []
        for i in range(le):
            if nums1[i] in nums2 and nums1[i] not in li:
                li.append(nums1[i])
        return li        

        