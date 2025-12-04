class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: [x[0],x[1]])

        left,right = intervals[0]
        list1 = []
        max1 = right
        for l,r in intervals[1:]:
           
            if max1 >= l:
                max1 = max(r,max1)
            else:
                list1.append([left,max1])
                left = l
                max1= r
        list1.append([left,max1])        
        return list1        

        