#with open('Day_2.txt','r') as file:
#    content = file.read()

#final_list = []

#line_items = content.splitlines()
#count = 0
#for i in line_items:    
#    list = []
#    list = i.split()
#    deltas = []
#    condition_one_met = True
#    con_count_one = 0
#    condition_two_met = True
#    con_count_two = 0
#    bad_report = 0
#    for index, level in enumerate(list):
#        if index < (len(list) - 1):
#            index=int(index)
#            level=int(level)
#            adj = int(list[index + 1])
#            delta = adj - level
#            absolute = abs(delta)
#            if absolute < 1 or absolute > 3:
#                   con_count_one += 1
#                   bad_report = level
#            deltas.append(delta)
#    if con_count_one > 1:
#        condition_one_met = False
#        #print(f"{bad_report} + {i} count.{con_count_one}")
#    if condition_one_met:
#        for index, diff in enumerate(deltas):
#            bad_report_2 = 0
#            neg = diff < 0
#            if index < (len(deltas) - 1):
#                adj_neg = deltas[index + 1 ] < 0
#                if adj_neg != neg:
#                     con_count_two += 1
#                     bad_report_2 = level
#                    # print(f"{bad_report_2} - {deltas} count.{con_count_one}")
#    if con_count_two > 1:
#            condition_two_met = False
#        # print(f"Count = {con_count_two} {bad_report_2}, Report Bad = {con_count_one} {bad_report}, {list}")
#    if condition_two_met and bad_report_2==bad_report:
#        final_list.append(i)
#        count += 1
#        print(f"Count = {con_count_two} {bad_report_2}, Report Bad = {con_count_one} {bad_report}, {list}")
#print(f"Count = {count}, List_Count = {len(final_list)}")

##899
##390 Wrong Answer


#Ian Fix

with open('Day_2_sample.txt','r') as file:
    content = file.read()

final_list = []

line_items = content.splitlines()
report_safe_count = 0
unreport_safe_1count = 0

def is_safe(list):
    condition_one_met = True
    condition_two_met = True
    deltas = []
    for index, value in enumerate(list):
        if index < (len(list) - 1):
            index=index
            value=int(value)
            adj = int(list[index + 1])
            delta = adj - value
            absolute = abs(delta)
            if absolute < 1 or absolute > 3:
                condition_one_met = False
                return index + 1
            else:
                deltas.append(delta)
    print(deltas)
    if condition_one_met:
        for index, value in enumerate(deltas):
            is_neg = value < 0
            if index < (len(deltas) - 1):
                is_adj_neg = deltas[index + 1] < 0
                if is_adj_neg != is_neg:
                    condition_two_met = False
                    return index + 1
        if condition_two_met:
            return -1



for i in line_items:    
    report = []
    report = i.split()
    index_of_bad_lv = is_safe(report)
    if index_of_bad_lv == -1:
        report_safe_count += 1
    else:
        unreport_safe_1count += 1
        del report[index_of_bad_lv]
        print(report)
        index_of_bad2_lv = is_safe(report)
        if index_of_bad2_lv == -1:
            report_safe_count += 1

print(f"{report_safe_count} {index_of_bad_lv}")