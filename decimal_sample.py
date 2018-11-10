##############################
#고정소수점형 계산
##############################
from decimal import Decimal

##############################
#Decimal 객체 생성
Decimal('1')
Decimal('3.14')

#3.14  부호(0:+, 1:-)
print(Decimal((0, (3, 1, 4), -2)))

#-3.14  부호(0:+, 1:-)
print(Decimal((1, (3, 1, 4), -2)))

#-1.414
print(Decimal((1, (1, 4, 1, 4), -3)))

##############################
#Decimal 계산

x  = Decimal('1.1')
y = Decimal('0.1')
z = x - y
print(z)

#TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
#z = x + 1.0

##############################
#유효 자릿수 지정

from decimal import getcontext

#기본 자릿수는 28자리
x = Decimal('10')
y = Decimal('3')
z = x / y
print(z)
#3.333333333333333333333333333

#자릿수 5 지정
getcontext().prec = 5

print(x / y)
#3.3333

##############################
#숫자 반올림 방법 지정 (rounding)

from decimal import ROUND_UP
from decimal import ROUND_DOWN
from decimal import ROUND_CEILING
from decimal import ROUND_FLOOR
from decimal import ROUND_HALF_UP
from decimal import ROUND_HALF_DOWN
from decimal import ROUND_HALF_EVEN
from decimal import ROUND_05UP


#소수 첫째 자리
exp = Decimal((0, (1,0), -1))

#ROUND_UP 올림
print(Decimal('1.04').quantize(exp, rounding=ROUND_UP))
print(Decimal('1.05').quantize(exp, rounding=ROUND_UP))
print(Decimal('-1.05').quantize(exp, rounding=ROUND_UP))
#1.1 , 1.1 , -1.1

#ROUND_DOWN 내림
print(Decimal('1.04').quantize(exp, rounding=ROUND_DOWN))
print(Decimal('1.05').quantize(exp, rounding=ROUND_DOWN))
print(Decimal('-1.05').quantize(exp, rounding=ROUND_DOWN))
#1.0 , 1.0 , -1.0

#ROUND_CEILING 양의 무한대 방향으로 올림
print(Decimal('1.04').quantize(exp, rounding=ROUND_CEILING))
print(Decimal('1.05').quantize(exp, rounding=ROUND_CEILING))
print(Decimal('-1.05').quantize(exp, rounding=ROUND_CEILING))
#1.1 , 1.1 , -1.0

#ROUND_FLOOR 음의 무한대 방향으로 올림
print(Decimal('1.04').quantize(exp, rounding=ROUND_FLOOR))
print(Decimal('1.05').quantize(exp, rounding=ROUND_FLOOR))
print(Decimal('-1.05').quantize(exp, rounding=ROUND_FLOOR))
#1.0 , 1.0 , -1.1

#ROUND_HALF_UP 사사오입(반올림)
print(Decimal('1.04').quantize(exp, rounding=ROUND_HALF_UP))
print(Decimal('1.05').quantize(exp, rounding=ROUND_HALF_UP))
print(Decimal('-1.05').quantize(exp, rounding=ROUND_HALF_UP))
#1.0 , 1.1, -1.1

#ROUND_HALF_DOWN 오사육입
print(Decimal('1.04').quantize(exp, rounding=ROUND_HALF_DOWN))
print(Decimal('1.05').quantize(exp, rounding=ROUND_HALF_DOWN))
print(Decimal('-1.05').quantize(exp, rounding=ROUND_HALF_DOWN))
#1.0 , 1.0 , -1.0

#ROUND_HALF_EVEN 바로 앞 자릿수가 홀수면 사사오입, 짝수면 오사육입
print(Decimal('1.04').quantize(exp, rounding=ROUND_HALF_EVEN))
print(Decimal('1.05').quantize(exp, rounding=ROUND_HALF_EVEN))
print(Decimal('-1.05').quantize(exp, rounding=ROUND_HALF_EVEN))
#1.0 , 1.0 , -1.0

#ROUND_05UP 바로 앞 자릿수가 0 or 5 이면 반올림, 그렇지 않으면 버림
print(Decimal('1.04').quantize(exp, rounding=ROUND_05UP))
print(Decimal('1.05').quantize(exp, rounding=ROUND_05UP))
print(Decimal('-1.05').quantize(exp, rounding=ROUND_05UP))
#1.1 , 1.1 ,  -1.1
