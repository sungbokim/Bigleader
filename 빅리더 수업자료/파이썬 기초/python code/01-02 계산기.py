## 함수
def add_func(n1, n2) :
    return n1 + n2

def rem_func(n1, n2) :
    return n1 % n2
## 변수
num1, num2 = 0 , 0
result = 0
## 메인
# 두 숫자의 더하기/빼기 등등을 계산하기
num1 = int(input("숫자1 :"))
num2 = int(input("숫자2 :"))

result = add_func(num1, num2)
print(num1, '+', num2 , '=', result)

result = rem_func(num1, num2)
print(num1, '%', num2 , '=', result)

# 퀴즈 : 빼기, 곱하기, 나누기, 나머지, 제곱...
#빼기 :-, 곱하기:* , 나누기:\, 나머지:%, 제곱:**