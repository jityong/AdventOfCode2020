from collections import defaultdict
from collections import deque

class Day7:
    # Both DFS algo, O(V+E) time 
    def __init__(self, arr):
        self.contained_by = defaultdict(lambda: set())
        self.contains = defaultdict(lambda: [])
        self.populate_edges(arr)

    def populate_edges(self, arr):
        for key, values in arr:
            for val in values:
                if val[1]:
                    self.contained_by[val[1]].add(key)
                self.contains[key].append(val)
        
    def transitive_closure_part1(self, bag):        
        visited = set()
        def dfs(bag):
            result = 0            
            for val in self.contained_by[bag]:
                if not val in visited:
                    result += 1 + dfs(val) 
                    visited.add(val)
            return result 
        
        return dfs(bag)
    
    def transitive_closure_part2(self, bag):         
        result = 0
        for val in self.contains[bag]:
            dfs_val = self.transitive_closure_part2(val[1])
            result += int(val[0]) + int(val[0]) * dfs_val            
        return result
                

lines = open("../inputs/day7input.txt", "r+")
arr = []
for line in lines:
    key, values = line.split("contain")
    key = key.split(" ")
    key = key[0] + " " + key[1]

    if values.strip() == "no other bags.":
        arr.append((key, [(0, "")]))
        continue

    values = values.split(",")
    result_values = []
    for val in values:
        val = val.strip()        
        val = val.split(" ")        
        result_values.append((val[0], val[1] + " " + val[2]))
    
    arr.append((key, result_values))

day7 = Day7(arr)
### Part 1
print(day7.transitive_closure_part1("shiny gold"))

### Part 2
print(day7.transitive_closure_part2("shiny gold"))