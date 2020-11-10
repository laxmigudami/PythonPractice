list = [12, 5, 84, 6, 1, 79, 23, 0, 0, 7]
for i in range(len(list)-1):
    min_val = min(list[i:])
    min_ind = list.index(min_val, i)
    if list[i] != list[min_ind]:
        list[i], list[min_ind] = list[min_ind], list[i]
    print(list)


