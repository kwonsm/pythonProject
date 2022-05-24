
class Student:
    def __init__(self, name=0, Korean=0, math=0, English=0, Science=0):
        self.name = name
        self.Korean = Korean
        self.Math = math
        self.English = English
        self.Science = Science

    def get_sum(self):
        return self.Korean + self.Math + self.English + self.Science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t {}\t {}\t".format(self.name, self.get_sum(), self.get_average())


studentA = Student("unknown", 0, 0, 0, 0)

students = [
    Student("용인성", 87, 80, 89, 91),
    Student("나선희", 90, 91, 94, 95),
    Student("연하진", 86, 88, 99, 95)
]


print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())