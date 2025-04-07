class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=0
        while len(students)>count:
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count=0
            else:
                students.append(students[0])
                count+=1
                students.pop(0)
        return len(students)
        

            



        