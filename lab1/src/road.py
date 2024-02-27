def route(our_list):
    m = len(our_list)
    finished_list = []
    for i in range(m):
        if i % 2 == 0:
            finished_list.extend(our_list[i])
        else:
            our_list[i].reverse()
            finished_list.extend(our_list[i])
    return finished_list


our_list = [[1,5,7], [6,8,3], [4,2,1], [2,2,4]]

print(route(our_list))
