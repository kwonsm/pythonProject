def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return factorial_recursive(n-1)*n

def factorial_loop(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans


print("팩토리얼 수행")

n = int(input("n > "))
print("재귀함수 이용: {}".format(factorial_recursive(n)))
print("반복문 이용: {}".format(factorial_loop(n)))