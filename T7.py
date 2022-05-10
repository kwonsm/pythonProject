info1 = {'name': '철수', 'age': '21', 'Score': '4.3'}
info2 = {'name': '영희', 'age': '16', 'Score': '3.1'}
info3 = {'name': '민수', 'age': '24', 'Score': '3.9'}
info4 = {'name': '길동', 'age': '29', 'Score': '4.1'}

data = [info1, info2, info3, info4]

while True:
    print("""
    메뉴
    1. 데이터 추가
    2. 데이터 검색
    3. 데이터 삭제""")
    menu = int(input("메뉴를 선택하세요 > "))
    if menu == 1:
        print("[데이터 추가]")
        name = input("추가할 데이터의 이름을 입력하세요 > ")
        age = input("추가할 데이터의 나이를 입력하세요 > ")
        Score = input("추가할 데이터의 성적을 입력하세요 > ")
        new_info = {"name": name, "age": age, "Score": Score}
        data.append(new_info)
        print("추가됨.")

    elif menu == 2:
        print("[데이터 검색]")
        key, value = input("검색할 데이터의 key와 value를 입력하세요 > ").split(":")
        find = False
        for info in data:
            if info[key] == value:
                print(info)
                find = True
        if find == False:
            print("입력한 이름을 갖는 데이터가 존재하지 않습니다.")

    elif menu == 3:
        print("[데이터 삭제]")
        name = input("삭제할 데이터의 이름을 입력하세요 > ")
        for no, info in enumerate(data):
            if info["name"] == name:
                del data[no]
        print("삭제됨.")
