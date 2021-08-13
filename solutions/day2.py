from collections import defaultdict

class Day2:
    def parseInput(self, s): 
        rule, password = s.split(":")
        password = password.strip()
        freq, char = rule.split(" ")
        char = char.strip()
        first_num, second_num = freq.split("-")
        return (int(first_num), int(second_num), char, password)
    
    def isValid(self, s):
        parsedInput = self.parseInput(s)
        min_freq, max_freq, char, password = parsedInput
        
        dic = defaultdict(lambda: 0)
        for letter in password:
            dic[letter] +=  1
        
        return dic[char] >= min_freq and dic[char] <= max_freq

    def isValidPart2(self,s):
        parsedInput = self.parseInput(s)
        first_pos, second_pos, char, password = parsedInput

        isFirstPosValid = first_pos < len(password) + 1 and password[first_pos-1] == char
        isSecondPosValid = second_pos < len(password) + 1 and password[second_pos-1] == char
        return isFirstPosValid ^ isSecondPosValid

fo = open("../inputs/day2input.txt", "r+")
arr = fo.read().splitlines()    
day2 = Day2()

### Part 1
result = 0
for s in arr:
    if day2.isValid(s):
        result += 1
print(result)

### Part 2
result = 0
for s in arr:
    if day2.isValidPart2(s):
        result += 1
print(result)
