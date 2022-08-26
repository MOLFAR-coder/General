import sorting
names = []
def read():
    file = open("names.txt")
    for name in file.readlines():
        names.append(name[:-1])
    file.close()
def linear(name):
    for element in names:
        if element==name:
            print("Name Found at Index",names.index(element))
            break
        else:
            continue
def binary(name):
    low,high = 0,len(names)-1
    while True:
        mid = (low+high)//2
        print(names[mid])
        if names[mid]==name:
            print("Name found at index",mid)
            break
        elif names[mid]<name:
            low = mid+1
        else:
            high = mid-1
        if mid==(low+high)//2:
            print("Name Not present")
            break
        else:
            continue
read()
sorting.bubble(names)
print(names)
ask  = input("Enter the name you want to search for: ")
binary(ask)