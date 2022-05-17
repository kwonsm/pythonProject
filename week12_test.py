PI = 3.141592


def number_input():
    output = input("숫자입력> ")
    return float(output)

def get_circumference(R):
    return 2*PI*R

def get_circle_area(r):
    return r**2*PI

def printHi(name):
    print("Hi~ {}".format(name))


if __name__ == "__main__":
    radius = number_input()
    print("원지름: ", get_circumference(radius))
    print("넓이: ", get_circle_area(radius))