class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2 = len(s1),len(s2)
       
        dict1 = Counter(s1)
        dict2 = Counter()
        for i in range(l2):
            dict2[s2[i]] +=1
            if i >=l1:
                dict2[s2[i-l1]] -=1
                if dict2[s2[i-l1]] ==0:
                    del dict2[s2[i-l1]]
            if dict1 == dict2:
                return True
        return False                
        