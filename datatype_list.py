fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

def initial_list(thislist):
    for i in range(0,len(thislist)):
        whatisit = thislist[i][0]
        print(whatisit)
print("변경전")
initial_list(fruitlist)

fruitlist[2]="수박"

print("변경후")
initial_list(fruitlist)

print("정렬후")
fruitlist.sort()
initial_list(fruitlist)

print(fruitlist[-4:])

fruitlist.sort(reverse=True)
initial_list(fruitlist
             )
