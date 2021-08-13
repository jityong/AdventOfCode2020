from collections import defaultdict
class Day1:
    # hashmap approach, O(n) time & space
    def find2Sum(self, target, arr, l):
        dic = defaultdict(lambda: 0)
        for i in range(l, len(arr)):
            dic[arr[i]] += 1  
        for num, freq in dic.items():
            other_num = target - num
            if num == other_num and freq >= 2 or other_num in dic:
                return [num, other_num]
    
    # O( n^(k-1) ) solution
    def findKSum(self, target, arr, idx, k):
        if target < 0:
            return []
        if k == 2: 
            return self.find2Sum(target, arr, idx)
        else: 
            for i in range(len(arr) - 2):
                curr_result = self.findKSum(target - arr[i], arr, i, k-1)
                if curr_result: 
                    curr_result.append(arr[i])
                    return curr_result
            return []

### Read input
fo = open("day1input.txt", "r+")
arr = fo.read().splitlines()        
arr = list(map(lambda x: int(x), arr))

### Part 1
day1 = Day1()
num1, num2 = day1.find2Sum(2020, arr, 0)
print("Part 1 result: ", num1+num2, num1 * num2)

### Part 2
nums = day1.findKSum(2020, arr, 0, 3)
nums_sum = 0
result = 1
for num in nums:
    nums_sum += num
    result *= num
print("Part 2 reult: ",nums_sum, result)


            