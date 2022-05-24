class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("------학생목록------")
        print("이름", "총점", "평균", sep="\t")
        for student in Student.students:
            print(str(student))
        print("-------------------")

    def __init__(self, name=0, Korean=0, math=0, English=0, Science=0):
        self.name = name
        self.Korean = Korean
        self.Math = math
        self.English = English
        self.Science = Science
        Student.count += 1
        print("현재 생성된 총 학생 수는 {}명 입니다.".format(Student.count))
        Student.students.append(self)

    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))

    def get_sum(self):
        return self.Korean + self.Math + self.English + self.Science

    def get_average(self):
        return self.get_sum()/4

    def study(self):
        print("공부를 합니다.")

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

    def __eq__(self, other):
        return self.get_sum() == other.get_sum()

    def __ne__(self, other):
        return self.get_sum() != other.get_sum()

    def __gt__(self, other):
        return self.get_sum() > other.get_sum()

    def __ge__(self, other):
        return self.get_sum() >= other.get_sum()

    def __lt__(self, other):
        return self.get_sum() < other.get_sum()

    def __le__(self, other):
        return self.get_sum() <= other.get_sum()


class Teacher:
    def teach(self):
        print("가르칩니다.")


Student("용인성", 87, 80, 89, 91),
Student("나선희", 90, 91, 94, 95),
Student("연하진", 86, 88, 99, 95),
Student("김선민", 99, 86, 98, 90)
Student.print()

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__ 매서드가 호출 되었습니다.")

    def test(self):
        print("Parent 클래스의 test() 매서드입니다.")


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init__ 매서드가 호출 되었습니다.")

A = Child()