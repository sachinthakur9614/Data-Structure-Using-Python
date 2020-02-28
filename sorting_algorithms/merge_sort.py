
def merge_sort(unlist):
    if len(unlist) <= 1:
        return unlist
    mid = len(unlist) // 2
    left_lst = unlist[:mid]
    right_lst = unlist[mid:]
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)
    return list(merge(left_lst,right_lst))


def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
        
    if len(left_half) ==0:
        res = res+ right_half
    else:
        res= res +left_half
    return res

unlst = [64,34,25,12,22,90,80]
print(merge_sort(unlst))