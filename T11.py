file_name = "info141412.txt"
DB = []

try:############## 파일이 없을 때 -> 새로 만들기
    with open(file_name, "r") as file:
        for line in file:
            name, age, score = line.strip().split(", ")
except Exception as e:
    print(e)
    print("{}을 생성합니다.".format(file_name))
    with open(file_name, "w") as file:
        pass


def add():
    print("[데이터 추가]")
    while True:
        try:################데이터 타입이 안 맞을 때 -> 다시 입력 받기
            name = input("추가할 데이터의 이름을 입력하세요 > ")
            if name == "":################## name이 없을때 -> unknown으로 하기
                name = "unknown"
            age = int(input("추가할 데이터의 나이를 입력하세요 > "))
            Score = float(input("추가할 데이터의 성적을 입력하세요 > "))
            print(name, age, Score)
        except Exception as e:
            print(e)
        else:
            break

    new_info = {"name": name, "age": age, "Score": Score}
    DB.append(new_info)
    print("추가됨.")
    with open(file_name, "a") as file:
        file.write(str(new_info["name"]) + ", " + str(new_info["age"]) + ", " + str(new_info["Score"]) + "\n")


def search():
    for item in DB:
        file.write(str(item))

    print("[데이터 검색]")
    while True:
        try:##############입력 형식이 안 맞을 때 -> 맞을 때까지 다시 입력받음
            key, value = input("검색할 데이터의 key와 value를 입력하세요 > ").split(":")
        except Exception as e:
            print(type(e), e)
        else:
            break
    find = False
    for info in DB:
        if info[key] == value:
            print(info)
            find = True
    if not find:
        print("입력한 이름을 갖는 데이터가 존재하지 않습니다.")


def remove():
    find = False
    print("[데이터 삭제]")
    name = input("삭제할 데이터의 이름을 입력하세요 > ")
    for no, info in enumerate(DB):
        if info["name"] == name:
            del DB[no]
            find = True
    if find:############################이름을 찾지 못했을 때 -> 없다는 문구 출력
        print("삭제됨.")
    else:
        print("삭제 안됨. \n없는 이름입니다.")
    with open(file_name, "w") as file:
        for item in DB:
            file.write(str(item["name"]) + ", " + str(item["age"]) + ", " + str(item["Score"]) + "\n")


while True:
    print("""
    간단한 데이터베이스 만들기
    메뉴
    1. 데이터 추가
    2. 데이터 검색
    3. 데이터 삭제
    """)
    try:############메뉴를 이상하게(정수X) 입력했을 때 -> 다시 입력
        menu = int(input("메뉴를 선택하세요 > "))
        if menu == 1:
            add()
        elif menu == 2:
            search()
        elif menu == 3:
            remove()
        else:  #################메뉴를 이상하게(이상한 정수) 입력했을 때 -> 다시 입력
            print("메뉴를 잘못 입력하였습니다.")
    except Exception as e:
        print(type(e), e)

