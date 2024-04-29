## 메서드 (=함수) 부분
def add_func(n1, n2) :
    retVal = n1 + n2
    return retVal

def sub_func(n1, n2) :
    retVal = n1 - n2
    return retVal
## 전역 변수 (=클래스 변수)
num1, num2, res = 100, 200, 0
## 메인 함수 부분
res = add_func(num1, num2)
print(num1, "+", num2, "=", res)


res = sub_func(num1, num2)
print(num1, "-", num2, "=", res)
