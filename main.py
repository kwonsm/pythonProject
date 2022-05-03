# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import datetime
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        os.mkdir("current_time")
    except:
        print("이미 생성됨.")
    with open("d:/project/pythonProject/current_time/now.txt", "w") as file:
        fileList = os.listdir()
        file.write("현재 폴더의 목록: {}\n".format(fileList))
        file.write("그 중에 하나를 랜덤하게 선택: {}\n".format(fileList[random.randrange(0, len(fileList))]))
        now = datetime.datetime.now()
        file.write("{}년 {}월 {}일 {}시 {}분 {}초\n".format(now.year, now.month, now.day, now.hour, now.minute, now.second))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
