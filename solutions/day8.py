from collections import defaultdict
class Day8:
    # https://adventofcode.com/2020/day/8#part2
    def detect_loop(self, arr):
        visited = set()
        i = 0
        acc = 0
        while i < len(arr):
            if i in visited:
                return acc
            visited.add(i)
            if arr[i][0] == 'acc':
                acc += arr[i][1]
            elif arr[i][0] == 'jmp':
                i += arr[i][1]            
                continue
            i += 1
        return acc

    # Happy nodes are nodes that can reach the end
    def find_happy_nodes(self, arr):
        # Populate reversed edges, key is the node and value are immediate nodes that points to key.
        accessible_from = defaultdict(lambda: [])
        for i in range(len(arr)):
            if i > 0 and arr[i-1][0] != 'jmp':
                accessible_from[i].append(i-1)
            if arr[i][0] == 'jmp':                
                accessible_from[i + arr[i][1]].append(i)
        
        # Using transitive closure / DFS, we find all nodes that can access the last node
        happy_nodes = set()
        def dfs(idx):
            for i in accessible_from[idx]:
                if not i in happy_nodes:
                    happy_nodes.add(i)
                    dfs(i)
        dfs(len(arr)-1)
        return happy_nodes       
                    
    # Traverse from the start, when reach a 'jmp' or 'nop' instruction, try to replace with the other. If the next node it points to after the swap is a happy node, then its the correct swap.
    # When traversing, also keep track of the ACC sum, when the correct swap is found, update flag to True and just continue down the happy path.
    def traverse_part2(self, arr):
        happy_nodes = self.find_happy_nodes(arr)
        visited = set()        
        i, acc, flag= 0, 0, False
        
        while i < len(arr):
            # This is just for debugging purposes & make sure that there are no loops. 
            if i in visited:
                print('loop', flag, i)
                break
            visited.add(i)
            if flag: 
                if arr[i][0] == 'acc':
                    acc += arr[i][1]
                elif arr[i][0] == 'jmp':
                    i += arr[i][1]
                    continue
                i += 1
            else:
                if arr[i][0] == 'nop':
                    if i + arr[i][1] in happy_nodes:
                        flag = True
                        i += arr[i][1]                        
                    else:
                        i += 1
                elif arr[i][0] == 'jmp':
                    if i + 1 in happy_nodes:
                        flag = True
                        i += 1
                    else:
                        i += arr[i][1] 
                else:
                    acc += arr[i][1]
                    i += 1      
        return acc
                


lines = open("../inputs/day8input.txt", "r+")
arr = lines.read().splitlines()

def transform(s):
    instruction, arg = s.split(" ")
    sign = arg[0]
    val = int(arg[1:])
    if sign == '-':
        val *= -1
    return (instruction, val)
    
arr = list(map(lambda x: transform(x), arr))

day8 = Day8()

### Part 1
print(day8.detect_loop(arr))

### Part2 -> work backwards to find & label the 'happy' nodes that can lead to the end
# After that, we traverse from the start again, changing each nop -> jmp and each jmp -> nop. 
# If the next node from this change is a happy node, then is the solution. else, change back and continue trying.

print(day8.traverse_part2(arr))