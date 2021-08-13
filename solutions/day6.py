from collections import defaultdict
class Day6:
    def count_sum(self, arrs):
        result = 0
        for arr in arrs:
            curr_group = set()
            for ans in arr:
                curr_group.update(ans)
            result += len(curr_group)

        return result

    def count_sum_part2(self, arrs):
        result = 0
        for arr in arrs:
            result += self.helper(arr)
        return result

    def helper(self, arr):
        dic = defaultdict(lambda: 0)
        for ans in arr:
            for char in ans:
                dic[char] += 1
        result = 0 
        for key, freq in dic.items():
            if freq == len(arr):
                result += 1
        return result

fo = open("../inputs/day6input.txt", "r+")
arr = []
curr_arr = []
for line in fo: 
    if line == '\n':
        arr.append(curr_arr)
        curr_arr = []
    else:
        curr_arr.append(line.strip())        
arr.append(curr_arr)

day6 = Day6()
## Part 1
print(day6.count_sum(arr))

## Part 2
print(day6.count_sum_part2(arr))
