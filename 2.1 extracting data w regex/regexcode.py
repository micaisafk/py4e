import re
handle = open("regex_sum_2090649.txt", "r")
file = handle.read()

numlist = re.findall('[0-9]+' , file)

numlist = [int(i) for i in numlist]
x = sum(numlist)

print(x)

#bonus: try to print in one line of code:
print(sum([int(i) for i in re.findall('[0-9]+', open("regex_sum_2090649.txt").read())]))