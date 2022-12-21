class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_done = set()
        courses_q = deque()
        prerequisites_set = [set() for i in range(numCourses)]
        enabler = [set() for i in range(numCourses)]
        output  = []
        for after, before in prerequisites:
            prerequisites_set[after].add(before)  # list where set of i gives courses that need to be done before course i can be done
            enabler[before].add(after)  # list where set of i can be enables with course i
            
        
        
        # add courses that can be done without doing any other course
        for i in range(numCourses):
            if len(prerequisites_set[i]) == 0:
                courses_q.append(i)
                
        while courses_q:
            n = len(courses_q)
            for i in range(n):
                current_course = courses_q.popleft()
                courses_done.add(current_course)
                output.append(current_course)
                for new_course in enabler[current_course]:
                    prerequisites_set[new_course].remove(current_course)
                    if len(prerequisites_set[new_course]) == 0 and new_course not in courses_done:
                        courses_q.append(new_course)
                
                           
        
            
            
        if len(courses_done) != numCourses:
            return []
        else:
            return output