
import pandas
from collections import Counter

with open('Day_1.txt','r') as file:
    content = file.read()

line_items = content.splitlines()
l_list = []
r_list = []
sum = 0
for line in line_items:
    a=line[5:]
    a=a.strip()
    b=line[:-5]
    b=b.strip()
    l_list.append(a)
    r_list.append(b)
r_list.sort()
l_list.sort()
for i in range(len(r_list)):
    r_list[i]=int(r_list[i])
    l_list[i]=int(l_list[i])
    difference = abs(r_list[i] - l_list[i])
    sum = sum + difference

# 1 Answer = 2,164,381

dup = list(filter(lambda x: x in r_list, l_list))
dup_dict = dict(Counter(dup))
output = 0 
for label,val in dup_dict.items():
    test = label * val
    output = output + test
print(output)
# 2 Answer = 20,719,933