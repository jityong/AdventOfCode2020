class Day3:
    # O(n+m) solution, where n is the num of rows and m is the number of columns
    def __init__(self, arr): 
        self.num_rows = len(arr)
        self.num_cols = len(arr[0])
        self.arr = arr

    def numOfTrees(self):
        c = 0
        result = 0
        for r in range(self.num_rows):
            if self.arr[r][c] == '#':
                result += 1
            c = (c + 3) % self.num_cols
        return result

    def numOfTreesPart2(self, right, down):        
        c = 0
        result = 0
        for r in range(0, self.num_rows, down):
            if self.arr[r][c] == '#':
                result += 1
            c = (c + right) % self.num_cols
        return result

fo = open("../inputs/day3input.txt", "r+")
arr = fo.read().splitlines()    
day3 = Day3(arr)

### Part 1
print(day3.numOfTrees())

### Part2 
traversals = [(1,1), (3,1), (5,1), (7,1), (1,2)]
result = 1
for right,down in traversals:
    result *= day3.numOfTreesPart2(right,down)
print(result)