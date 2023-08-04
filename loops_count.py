# user input 받아 갯수 만큼  fruits list 만큼 출력 반복하는 python code 작성
# - fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# - 출력은 index와 fruit name
# - Q 입력 시 while문 종료

bools = True
fruits = []
cnt = 0

while (bools):
    myfruit = input("과일 이름을 입력하세요 : ")
    if myfruit == "Q":
        print("종료합니다.")
        bools = False
    else: 
        fruits.append(myfruit)
        enumerate_fruits = enumerate(fruits) 
        cnt += 1
        print("Loops count : {}".format(cnt))
        for (index, value) in enumerate_fruits:
            print("{} : \"{}\"".format(index+1, value))


# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Loops count : 2
# 1 : "apple"
# 2 : "banana"
# Loops count : 3
# 1 : "apple"
# 2 : "banana"
# 3 : "cherry"
# Loops count : Q  # 종료

