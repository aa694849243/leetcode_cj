# 5621. 无法吃午餐的学生数量
from typing import List
import collections


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        sandwiches = collections.deque(sandwiches)
        cnt = 0
        while cnt < len(students) and sandwiches:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                cnt = 0
            else:
                a = students.popleft()
                students.append(a)
                cnt += 1
        return len(students)


Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])


# 5622. 平均等待时间
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers or len(customers[0]) == 0:
            return 0
        n = len(customers)
        total = customers[0][1]
        m = []
        m.append(customers[0][0] + customers[0][1])
        for i in range(1, n):
            if customers[i][0] <= m[-1]:
                total += customers[i][1] + m[-1] - customers[i][0]
                m.append(m[-1] + customers[i][1])
            else:
                total += (customers[i][1])
                m.append(customers[i][0] + customers[i][1])
        return total / n


# 5623. 修改后的最大二进制字符串
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        m = collections.Counter(binary)
        b = m['0']
        if b <= 1:
            return binary
        for i in range(len(binary)):
            if binary[i] == '0':
                break
        return binary[:i] + '1' * (b - 1) + '0' + '1' * (len(binary) - i - b)
