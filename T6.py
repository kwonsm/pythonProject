info1 = {'name': '철수', 'age': '21', 'Score': '4.3'}
info2 = {'name': '영희', 'age': '16', 'Score': '3.1'}
info3 = {'name': '민수', 'age': '24', 'Score': '3.9'}
info4 = {'name': '길동', 'age': '29', 'Score': '4.1'}

data1 ={
    1: info1,
    2: info2,
    3: info3,
    4: info4
}

print("간단한 데이터베이스 검색 기능 구현")
print("[데이터 검색]")
name = input("검색할 데이터의 이름을 입력하세요 > ")
for k in data1:
    if data1[k]['name'] == name:
        print(data1[k])

