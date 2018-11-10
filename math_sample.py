##############################
#기본적인 수치 계산
#https://docs.python.org/3.7/library/functions.html
#https://docs.python.org/3.7/library/math.html
##############################

##############################
#수치계산(내장함수)

#절대값
print(abs(-5.0))
#5.0

#최대값
print(max([1, -2, 5]))
#5

print(max(1, -2, 5))
#5

#최소값
print(min([1, -2, 5]))
#-2

print(min(1, -2, 5))
#-2

#덧셈
print(sum([1, 2, 3]))
#6

#iterator값에 start값을 더함
print(sum([1, 2, 3], 2))
#8

#x의 y승을 구함
print(pow(2, 3))
#8

#x의 y승의 %z 계산
print(pow(2,3,6))
#2

##############################
#수치계산(math)
import math

#x의 자연로그를 구함
print(math.log(100))
#4.605170185988092

#밑을 10으로 하는 로그 구함
print(math.log(100, 10))
#2.0

#밑을 10으로 하는 로그 구함
print(math.log10(100))
#2.0

#x의 y승 구함
print(math.pow(2, 3))
#8

#x의 제곱근 구함
print(math.sqrt(16))
#4.0

radian = math.radians(90)

#라디안x의 사인을 구함
print(math.sin(radian))
#1.0

#라디안x의 코사인을 구함
print(math.cos(radian))
#6.123233995736766e-17

#라디안x의 탄젠트를 구함
print(math.tan(radian))
#1.633123935319537e+16

#부동소수점형 값 x 이상의 최소 정숫값 구함
print(math.ceil(3.14))
#4

#부동소수점형 값 x 이하의 최소 정숫값 구함
print(math.floor(3.14))
#3

print(math.floor(-3.14))
#-4

#부동소수점형 값 x 의 소수점 아래를 버림
print(math.trunc(3.14))
#3

print(math.trunc(-3.14))
#-3

#x의 절대값을 구함
print(math.fabs(-3.14))
#3.14

#원주율 상수
print(math.pi)
#3.141592653589793

#자연로그 밑의 상수
print(math.e)
#2.718281828459045



