class Day12:
    # Assumption -> degrees are always a factor of 90. Ie. degree % 90 = 0

    def enum_direction(self, s):
        if s == 'N':
            return 3
        if s == 'W':
            return 2
        if s == 'S':
            return 1
        if s == 'E':
            return 0   

    def part_1(self, instructions): 
        # east, south, west, north 
        directions = [0,0,0,0]
        curr_dir = 0

        for inst, val in instructions:
            if inst == 'F':
                directions[curr_dir] += val
            elif inst == 'R':
                curr_dir += int(val / 90)
                curr_dir %= 4
            elif inst == 'L':
                curr_dir -= int(val / 90)
                curr_dir %= 4
            else:
                directions[self.enum_direction(inst)] += val
        return abs(directions[0] - directions[2]) + abs(directions[1] - directions[3])

    def part_2(self, instructions): 
        def update_directions(val, pos):
            for i in range(4):
                directions[i] += way_point[pos] * val       
                pos = (pos + 1) % 4

        # east, south, west, north
        directions = [0,0,0,0]
        # bearings are relative to east_pos, in the order east -> south -> west -> north
        way_point = [10,0,0,1]
        east_pos = 0

        for inst, val in instructions:
            if inst == 'F':
                update_directions(val, east_pos)
            elif inst == 'R':
                east_pos -= int(val / 90)
                east_pos %= 4
            elif inst == 'L':
                east_pos += int(val / 90)
                east_pos %= 4
            else:
                pos = self.enum_direction(inst)
                pos = (pos + east_pos) % 4                
                way_point[pos] += val

        return abs(directions[0] - directions[2]) + abs(directions[1] - directions[3])

lines = open("../inputs/day12input.txt", "r+")
arr = lines.read().splitlines()
arr = list(map(lambda x: (x[:1], int(x[1:])), arr))

day12 = Day12()
print(day12.part_1(arr))

print(day12.part_2(arr))