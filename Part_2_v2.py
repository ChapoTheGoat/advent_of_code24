with open('Day_2.txt','r') as file:
    content = file.read()

final_list = []

line_items = content.splitlines()
print(line_items[0])
for i in line_items:    
    list = []
    list = i.split()
    for index, value in enumerate(list):
        deltas = []
        final_list.append(list)
        if index < (len(list) - 1):
            index=int(index)
            value=int(value)
            adj = int(list[index + 1])
            delta = adj - value
            absolute = abs(delta)
            if absolute > 1 or absolute <=3:
                    deltas.append(delta)
        print(deltas)
 