import re

with open(r'C:\Users\ggama\OneDrive - Metro Nashville Gov\Documents\GITHUB\advent_of_code24\Question_3\Day_3.2.txt','r') as file:
    content = file.read()

def mul(input):
    int_list = re.findall(r"mul\((\d+){1,4},(\d+){1,4}\)",input)
    product_total = 0

    for i in int_list:
        int_one, int_two = i
        product = int(int_one)*int(int_two)
        product_total += product
    return product_total

# do() and don't()

# Logic - Detect when do() run mul, when don't() ignore until do() detected. Detect first set of mul(,)

# print(do_str)
dont_list = re.split(r"don\'t\(\)", content)
products = 0
for dont_str in dont_list:
    if dont_str == dont_list[0]:
        products = mul(dont_str)
    else:
        do_list = re.split(r"do\(\)+", dont_str)
        for do_str in do_list:
            if do_str != do_list[0]:
              mul_prod = mul(do_str)
              products += mul_prod
print(products)
# Answer: 76,729,637