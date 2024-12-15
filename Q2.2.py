with open('Day_2.txt','r') as file:
    content = file.read()

final_list = []
bad_list = []
reports = content.splitlines()
safe_report_cnt = 0
unsafe_report_cnt = 0

def is_safe(list_of_lvs):
    condition_one_met = True
    condition_two_met = True
    deltas = []
    for index, value in enumerate(list_of_lvs):
        if index < (len(list_of_lvs) - 1):
            value=int(value)
            adj = int(list_of_lvs[index + 1])
            delta = adj - value
            absolute = abs(delta)
            if absolute < 1 or absolute > 3:
                condition_one_met = False
                return index
            else:
                deltas.append(delta)
    if condition_one_met:
        for index, value in enumerate(deltas):
            is_neg = value < 0
            if index < (len(deltas) - 1):
                is_adj_neg = deltas[index + 1] < 0
                if is_adj_neg != is_neg:
                    condition_two_met = False
                    return index
        if condition_two_met:
            return -999
        
for i in reports:
    levels = i.split()
    current_index = is_safe(levels)
    prev_index = 0
    next_index = 0
    report_wout_next_index = levels[:current_index + 1] + levels[current_index + 2:]
    if current_index == -999:
        safe_report_cnt += 1
    else:
        report_wout_current_index = levels[:current_index] + levels[current_index + 1:]
        report_wout_prev_index = levels[:current_index-1] + levels[current_index:]
        report_wout_next_index = levels[:current_index + 1] + levels[current_index + 2:]
        eport_wout_next2_index = levels[:current_index + 2] + levels[current_index + 3:]
        if is_safe(report_wout_current_index) == -999:
            safe_report_cnt += 1
        elif is_safe(report_wout_prev_index) == -999:
            safe_report_cnt += 1
        elif is_safe(report_wout_next_index) == -999:
            safe_report_cnt += 1
        elif is_safe(eport_wout_next2_index) == -999:
            safe_report_cnt += 1
        else:
            unsafe_report_cnt +=1
            bad_list.append(current_index)

print(f"Safe:{safe_report_cnt} Unsafe:{unsafe_report_cnt} Total:{safe_report_cnt + unsafe_report_cnt}")










































#[END 12.14.24]

#for i in line_items:    
#    report = []
#    test = []
#    test2 = []
#    report = i.split()
#    test = i.split()
#    test2 = i.split()
#    index_of_bad_lv = is_safe(report)
#    if index_of_bad_lv == -1:
#        report_safe_count += 1
#    else:
#        del report[index_of_bad_lv]
#        index_of_bad2_lv = is_safe(report)
#        if index_of_bad2_lv == -1:
#            report_safe_count += 1
#        else:
#            del test[index_of_bad_lv - 1]
#            index_of_bad3_lv = is_safe(test)
#            if index_of_bad3_lv == -1:
#                report_safe_count += 1
#            else:
#                del test[-1]
#                index_of_bad3_lv = is_safe(test)
#                if index_of_bad3_lv == -1:
#                    report_safe_count += 1
#                else:
#                    unreport_safe_1count += 1
#                    print(f"{unreport_safe_1count}  {i}")
    #        del test[index_of_bad_lv - 1]
    #        index_of_bad3_lv = is_safe(test)
    #        if index_of_bad3_lv == -1:
    #            report_safe_count += 1
    #        else:
    #            del test2[-1]
    #            index_of_bad4_lv = is_safe(test2)
    #            if index_of_bad4_lv == -1:
    #                report_safe_count += 1
    #            else:
    #                unreport_safe_1count += 1
    #print(f"{report_safe_count}, {i}, {report}, {test}")
        #print(report)
        #index_of_bad2_lv = is_safe(report)
        #if index_of_bad2_lv == -1:
        #    report_safe_count += 1
#print(f"{unreport_safe_1count}  {i}")