import re
class Day4:
    # https://adventofcode.com/2020/day/4 
    # Regex & parsing input
    def __init__(self):
        self.fields = {
            'byr':lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
            'iyr':lambda x: len(x) == 4 and int(x) >= 2010 and int(x) <= 2020,
            'eyr':lambda x: len(x) == 4 and int(x) >= 2020 and int(x) <= 2030, 
            'hgt':lambda x: self.validateHgt(x),
            'hcl':lambda x: re.fullmatch(r'#[0-9a-f]{6}', x) != None, 
            'ecl':lambda x: x in {'amb','blu','brn','gry','grn','hzl','oth'},
            'pid':lambda x: re.fullmatch(r'[0-9]{9}', x) != None,
            # 'cid':lambda x: True
        }
    
    def validateHgt(self, s):
        if len(s) <= 2:
            return False
        unit = s[len(s)-2:]
        num = s[:len(s)-2]
        if not num.isnumeric() or not (unit == 'cm' or unit == 'in'):
            print(s, num, unit)
            return False
        if unit == 'cm':
            return int(num) >= 150 and int(num) <= 193
        else: 
            return int(num) >= 59 and int(num) <= 76      

    def isValid(self, s):
        s_fields = {}
        for field in s:
            key, val = field.split(":")
            s_fields[key] = val.strip()
        for field, validate in self.fields.items():
            if not field in s_fields:
                return False 
            if not validate(s_fields[field]):
                return False
        return True
    

fo = open("../inputs/day4input.txt", "r+")
arr = []
curr_arr = []
### Parse input
for line in fo:
    if line == '\n':
        arr.append(curr_arr)
        curr_arr = []
    else:
        curr_arr += line.split(" ")
if curr_arr:
    arr.append(curr_arr)

day4 = Day4()
result = 0 
for passport in arr:
    if day4.isValid(passport):
        result += 1 

print(result)
