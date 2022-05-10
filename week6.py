#딕셔너리

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

dict_a = {
    "name": "어벤져스 엔드게임",
    "type": "히어로 무비",
    "director": ["안소니 루소", "조 루소"],
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지"]
}
print(dict_a)
dict_a["name"]
dict_a["type"]
dict_a["cast"][0] == "아이언맨"

name = int(input())
dictionary = {
    name: 1000,
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕"],
    "origin": "필리핀"
}

print(dictionary)
print("name:", dictionary["name"])
dictionary["name"] = "8D 건조 망고"
print("name", dictionary["name"])

key = input()
if key in dictionary:
    print(dictionary[key])
else:
    print("no key")

value = dictionary.get("존재하지 않는 키")
print("값:", value)

if value == None:
    print("존재하지 않는 key에 접근하였습니다.")

for key in dict_a:
    print("{}: {}".format(key, dict_a[key]))


import time as t

list1 = [4, 1, 3, 4]
list2 = sum(list1)
print(list2)

list3 = list(range(1, 12, 2))
print(list3)
print((6//3))
a = 99
list4 = list(range(1, int(input()), a))
print(list4)

sec = 5
target_tick = t.time() + sec
number = 0

while t.time() < target_tick:
    number += 1
print("{}초동안 {}번 반복됨.".format(sec, number))

