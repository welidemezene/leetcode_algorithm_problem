class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        for n in nums:
            divisor = set()
            for i in range(1,int(math.sqrt(n))+1):
                if n % i == 0:
                    divisor.add(i)
                    divisor.add(n//i)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                total_sum += sum(divisor)
        return total_sum                    
        