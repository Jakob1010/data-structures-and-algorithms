class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        managers = {}
        num_of_minutes = 0
        for i,m in enumerate(manager):
            if m in managers:
                managers[m].append(i)
            elif m != -1:
                managers[m] = [i]
         
        def find_max_num_of_minutes(emp):
            max_minutes = 0
            if informTime[emp] == 0:
                return max_minutes
            else:
                for sub_emp in managers[emp]:
                    emp_time = informTime[emp]
                    max_minutes = max(max_minutes,emp_time + find_max_num_of_minutes(sub_emp))
            return max_minutes
        
        return find_max_num_of_minutes(headID)