import re

file = open('regex_sum_432963.txt')
numlist = list()
for line in file:
    line = line.rstrip()
    findnum = re.findall('[0-9]+',line)
    results = list(map(int, findnum))
    results = sum(results)
    numlist.append(results)

print(sum(numlist))
   
