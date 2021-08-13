class Day5:
    # O(n) time solution, where n is the number of seats. O(1) space
    # https://adventofcode.com/2020/day/5#part2
    def binary_search(self, l, r, directions, idx):
        if idx >= len(directions):
            return l
        mid = int((l+r)/2)
        if directions[idx] == 'F' or directions[idx] == 'L':
            return self.binary_search(l, mid, directions, idx+1)
        else:
            return self.binary_search(mid + 1, r, directions, idx+1)

    def find_seat(self, arr):
        highest_result = 0
        lowest_result = 1000
        curr_sum = 0

        for direction in arr:
            row = self.binary_search(0,127,direction[:-3],0)
            col = self.binary_search(0,7,direction[-3:],0)
            curr_id = row * 8 + col
            curr_sum += curr_id
            highest_result = max(highest_result, curr_id)
            lowest_result = min(lowest_result, curr_id)

        # Calculate sum of lowest to highest seat
        # sum from 1 to N (inclusive of 1 & N) = N(N+1)/2         
        ids_sum = (1/2) * highest_result * (highest_result + 1) - (1/2) * (lowest_result-1) * (lowest_result)
        return(ids_sum - curr_sum)

fo = open("../inputs/day5input.txt", "r+")
arr = fo.read().splitlines()    
day5 = Day5()

print(day5.find_seat(arr))






