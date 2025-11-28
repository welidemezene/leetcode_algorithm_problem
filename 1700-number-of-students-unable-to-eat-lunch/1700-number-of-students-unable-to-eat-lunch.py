class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
       zero = students.count(0)
       one = len(students) - zero

       for l in sandwiches:
        if l == 0:
            if zero == 0:
                return one
            zero -=1
        else:
            if one == 0:
                return zero
            one -=1
       return 0                 

       

