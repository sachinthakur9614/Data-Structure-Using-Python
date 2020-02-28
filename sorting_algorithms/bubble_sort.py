


def bubblesort(lst):
    for item_num in range(len(lst)-1,0,-1):
        for idx in range(item_num):
            if lst[idx]>lst[idx+1]:
                temp = lst[idx]
                lst[idx] = lst[idx+1]
                lst[idx+1] = temp


lst = [10,12,9,15,16,70,80,42,34,90]
bubblesort(lst)

