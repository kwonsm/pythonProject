#사용자 정의 함수 고급


[a, b] = [10, 20]
(c, d) = (10, 20)
print(type((1, 2)))

tuple_test = 10, 20, 30, 40
a1, b1, c1, d1 = 10, 20, 30, 40
print(tuple_test, type(tuple_test))


def test():
    return 10, 20, 40


print(test())

file1 = open("basic.txt", "w")
file1.write("Hello python programming...")
file1.close()

with open("basix.txt","w") as file2:
    file2.write("aaaaaaaaa")

with open("basic.txt","r") as file3:
    contents = file3.read()
    print(contents)

import random

hanguls = list("가나다라마바사아자차카파타하")

with open("info.txt", "w") as file4:
    for i in range(10):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 199)

        file4.write("{}, {}, {}\n".format(name, weight, height))

with open("info.txt", "r") as file5:
    for line in file5:
        name, weight, height = line.strip().split(", ")

        if(not name) or (not weight) or (not height):
            continue

        bmi = int(weight/(int(height))*int(height))
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]))

