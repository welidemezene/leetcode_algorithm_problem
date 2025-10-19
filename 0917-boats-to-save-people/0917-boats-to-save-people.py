class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people) - 1
        people.sort()
        count1 = 0
        while left <= right:
            if people[left] + people[right] > limit:
                count1 +=1
                right -=1
               
            else:
                count1 +=1
                left+=1
                right-=1
               
        return count1        
       