with open('Day_2.txt','r') as file:
    content = file.read()

line_items = content.splitlines()

final_list = []
first_list = []
sum = 0
for line in line_items:
    list = []
    report = line.split(" ")
    first_list.append(report)
for i in first_list:
    for index, value in enumerate(i):
        value = int(value)
        if index == i[-1]:
                print(index)
                a = int(i[index + 1])
                delta = value - a
                absolute=abs(delta)
                if absolute > 1 or absolute <=3:
                    list.append(delta)
                else:
                    break
        for index_r , value_r in enumerate(list):
            if index_r != list:
                value_r = int(value_r)
                a = int(list[1])
                value_c = value_r < 0
                a_c = a < 0
                if value_c == a_c:
                    pass
                else:
                    break
    final_list.append(i)
print(len(final_list))