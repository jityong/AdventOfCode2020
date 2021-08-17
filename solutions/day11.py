import copy
class Day11: 
    def __init__(self, seats):
        self.num_row = len(seats)
        self.num_col = len(seats[0])

        self.arr = [[0] * self.num_col for i in range(self.num_row)]
        for i in range(self.num_row):
            for j in range(self.num_col):
                self.arr[i][j] = 1 if seats[i][j] == 'L' else -1
    
    def isValid(self, i, j):
        return i >= 0 and j >= 0 and i < self.num_row and j < self.num_col

    def find_num_adj_occupied_part1(self, arr_copy, r, c):
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        num_adj_occupied = 0
        for i,j in directions:
            if self.isValid(r+i, c+j) and arr_copy[r+i][c+j] == 1: 
                num_adj_occupied += 1
        return num_adj_occupied
 
    # O(nm * W), where W is the total number of iterations
    def part_1(self): 
        arr_copy = copy.deepcopy(self.arr)
        changes = True        
        while changes: 
            changes = False
            for r in range(self.num_row):
                for c in range(self.num_col):      
                    num_adj_occupied = self.find_num_adj_occupied_part1(arr_copy, r, c)              
                    if num_adj_occupied >= 4 and self.arr[r][c] == 1:                                                
                        changes = True
                        self.arr[r][c] = 0
                    elif num_adj_occupied == 0 and self.arr[r][c] == 0:
                        changes = True
                        self.arr[r][c] = 1                        
            arr_copy = copy.deepcopy(self.arr)
        
        result = 0         
        for r in range(self.num_row):
            for c in range(self.num_col):
                result += 1 if self.arr[r][c] == 1 else 0
        return result

    def find_num_adj_occupied_part2(self, arr_copy, r, c):
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        num_adj_occupied = 0
        for i,j in directions:
            curr_r = r + i
            curr_c = c + j
            while self.isValid(curr_r, curr_c) and arr_copy[curr_r][curr_c] == -1: 
                curr_r += i 
                curr_c += j
            if self.isValid(curr_r, curr_c) and arr_copy[curr_r][curr_c] == 1:
                num_adj_occupied += 1

        return num_adj_occupied  

    # O(nm * max(height, width, diagonal_len) * W), where n is num_row, m is num_col, W is the total number of iterations
    # Possible optimisation is to store the (i,j) of the next seat in the specified direction if the current node is floor. Then no need to loop through each time to find the next seat.
    # With above optimisation will be O(nm * W)
    def part_2(self): 
        arr_copy = copy.deepcopy(self.arr)
        changes = True        
        while changes: 
            changes = False
            for r in range(self.num_row):
                for c in range(self.num_col):      
                    num_adj_occupied = self.find_num_adj_occupied_part2(arr_copy, r, c)              
                    if num_adj_occupied >= 5 and self.arr[r][c] == 1:                                                
                        changes = True
                        self.arr[r][c] = 0
                    elif num_adj_occupied == 0 and self.arr[r][c] == 0:
                        changes = True
                        self.arr[r][c] = 1                        
            arr_copy = copy.deepcopy(self.arr)
        
        result = 0         
        for r in range(self.num_row):
            for c in range(self.num_col):
                result += 1 if self.arr[r][c] == 1 else 0
        return result

lines = open("../inputs/day11input.txt", "r+")
arr = lines.read().splitlines()

day11 = Day11(arr)
print(day11.part_1())

day11_part2 = Day11(arr)
print(day11_part2.part_2())