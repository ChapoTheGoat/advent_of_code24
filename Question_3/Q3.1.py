import re

with open(r'C:\Users\ggama\OneDrive - Metro Nashville Gov\Documents\GITHUB\advent_of_code24\Question_3\Day_3.1.txt','r') as file:
    content = file.read()

int_list = re.findall(r"mul\((\d+){1,4},(\d+){1,4}\)",content)

product_total = 0

for i in int_list:
    int_one, int_two = i
    product = int(int_one)*int(int_two)
    product_total += product

print(product_total)

# Answer: 178794710