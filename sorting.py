def bubble(list):
    while True:
        total_changes=0
        for i in range(len(list)):
            if i == len(list)-1:
                break
            elif list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                total_changes+=1
            else:
                continue
        if total_changes != 0:
            continue
        else:
            break
    return list
def insertion(list):
    for i in range(1, len(list)):
        x,n = i,1
        while x-n>0 and list[x-n]>list[x]:
            print(list)
            n+=1
        if list[x-n]>list[x]:
            list.insert(x-n,list.pop(i))
        else:
            list.insert(x-(n-1),list.pop(i))
    return list
def selection(list):
    main = []
    for i in range(len(list)):
        main.append(min(list))
        list.remove(min(list))
    return main