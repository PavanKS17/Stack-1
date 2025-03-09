# This approach is based on the idea of using the information from the answer array to find the next warmer day.
# We traverse the array from right to left, keeping track of the hottest temperature seen so far.
# We can also try Monotonic Stack approach to solve this problem.
# TC: O(n)
# But this approach gives SC: O(1)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer