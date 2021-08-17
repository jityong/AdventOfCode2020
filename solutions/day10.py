class Day10:
    def __init__(self,arr):
        arr.insert(0,0)
        arr.append(max(arr)+3)
        arr.sort()
        self.arr = arr

    def part_1(self):
        num_one_diff = 0
        num_three_diff = 0        
        for i in range(1, len(self.arr)):
            if self.arr[i] - self.arr[i-1] == 1:
                num_one_diff += 1
            elif self.arr[i] - self.arr[i-1] == 3:
                num_three_diff += 1
        return num_one_diff * num_three_diff 
    
    def part_2(self):
        dp = [0] * len(self.arr)
        dp[0] = 1
        i = 0
        for i in range(len(self.arr)):            
            j = i
            val = self.arr[j]
            result = 0
            j -= 1
            while j >= 0 and val - self.arr[j] <= 3:
                dp[i] += dp[j]
                j -= 1            
        return dp[len(self.arr)-1]

lines = open("../inputs/day10input.txt", "r+")
arr = lines.read().splitlines()

arr = list(map(lambda x: int(x), arr))

day10 = Day10(arr)
print(day10.part_1())

print(day10.part_2())