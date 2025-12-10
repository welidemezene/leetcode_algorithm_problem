class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []
        for s in nums:
            freq[s]+=1
        
        for key, value in freq.items():
            heapq.heappush(heap,(value,key))
        ans = nlargest(k,heap)    
        list1 = []
        for k,v in ans:
            list1.append(v)
        return list1    


        