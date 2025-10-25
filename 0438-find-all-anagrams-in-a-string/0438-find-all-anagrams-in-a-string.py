class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        target = Counter(p)
        window = Counter(s[:length])
        left, right = 0, length
        answer = []
        while right < len(s):
            if window == target:
                answer.append(left)
            window[s[right]] += 1
            window[s[left]] -= 1
            left += 1
            right += 1
        if window == target:
            answer.append(left)

        return answer         

                                
        