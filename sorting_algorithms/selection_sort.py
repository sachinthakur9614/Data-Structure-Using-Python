

def selection_sort(nlist):
    for item in range(len(nlist)-1,0,-1):
        max_pos = 0
        for location in range(1,item+1):
            if nlist[location]>nlist[max_pos]:
                max_pos = location
        
        temp =  nlist[item]
        nlist[item] = nlist[max_pos]
        nlist[max_pos] = temp

nlist = [14,46,43,27,57,41,45,21,70]
selection_sort(nlist)
print(nlist)