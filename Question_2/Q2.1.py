with open('Day_2.txt','r') as file:
    content = file.read()

final_list = []

line_items = content.splitlines()
count = 0
for i in line_items:    
    list = []
    list = i.split()
    deltas = []
    condition_one_met = True
    condition_two_met = True
    for index, value in enumerate(list):
        if index < (len(list) - 1):
            index=int(index)
            value=int(value)
            adj = int(list[index + 1])
            delta = adj - value
            absolute = abs(delta)
            if absolute < 1 or absolute > 3:
                condition_one_met = False
                break
            else:
                deltas.append(delta)
    if condition_one_met:
        for index, value in enumerate(deltas):
            is_neg = value < 0
            if index < (len(deltas) - 1):
                is_adj_neg = deltas[index + 1] < 0
                if is_adj_neg != is_neg:
                    condition_two_met = False
                    break
        if condition_two_met:
            final_list.append(i)
            count += 1
print(count)
print(len(final_list))
#Answer 379