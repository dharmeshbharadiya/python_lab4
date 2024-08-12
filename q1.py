def merge_sort(un_list):
    if len(un_list) <= 1:
        return un_list
        
    middle = len(un_list) // 2
    left_list = un_list[:middle]
    right_list = un_list[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res
un_list = [10, 2, 6, 7, 12, 22]
print(merge_sort(un_list))