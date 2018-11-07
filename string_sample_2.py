####################################################################
#문자열 변환 메소드
####################################################################

text = 'HELLO world'

#문자열을 모두 대문자로 변환
print(text.upper())
#HELLO WORLD

#문자열을 모두 소문자로 변환
print(text.lower())
#hello world

#대문자는 소문자로, 소문자는 대문자로 변환
print(text.swapcase())
#hello WORLD

#맨첫문자만 대문자, 나머지는 소문자로 변환
print(text.capitalize())
#Hello world

#단어마다 첫문자대문자+나머지소문자 로 변환
print(text.title())
#Hello World

#old를 new로 문자 변환, count옵션 지정시 지정수만큼만 변환
print(text.replace('H','x'))
#xELLO world


####################################################################
#서식화 메소드
####################################################################

print('1 + 2 = {0}'.format(1+2))
#1 + 2 = 3

a = 2
b = 3
print('{0} * {1} = {2}'.format(a, b, a*b))
#2 * 3 = 6

print('My name is {name}'.format(name='return40'))
#My name is return40

#서식화 값을 map 형식으로 지정
person = {'name':'return40', 'country':'Korea'}
print('My country is {country}'.format_map(person))
#My country is Korea

print('My country is {person[country]}'.format(person=person))
#My country is Korea

#서식화 값을 list 형식으로 지정
words= ['spam', 'ham', 'eggs']
print('I like {0[2]}'.format(words))
#I like eggs

#지정된 인수의 속성을 지정
from datetime import datetime
now = datetime.now()
print('Today is {0.year}-{0.month}-{0.day}'.format(now))
#Today is 2018-11-8


#포맷 지정 방법
import math

#지정된 폭안에서 왼쪽 정렬
print('|{:<30}|'.format('left algin'))
#|left algin                    |

#지정된 폭안에서 오른쪽 정렬
print('|{:>30}|'.format('right algin'))
#|                   right algin|

#지정된 폭안에서 중앙 정렬
print('|{:^30}|'.format('center'))
#|            center            |

#2진수, 8진수, 10진수, 16진수(소문자), 16진수(대문자) 변환
print('{0:b} {0:o} {0:d} {0:x} {0:X}'.format(1000))
#1111101000 1750 1000 3e8 3E8

#백분율 표기 변환 (%)
print('{:%}'.format(0.045))
#4.500000%

#숫자에 세자리마다 쉼표(,) 삽입
print('{:,}'.format(10000000000))
#10,000,000,000

#표시할 자릿수 지정
print('{:2.2%}'.format(0.045))
#4.50%

#고정소수점 변환 (:4.2f)
print('{:4.2f}'.format(math.pi))
#3.14

#날짜,시각 변환 (:%Y-%m-%d %H:%M:%S)
print('now time is {:%Y-%m-%d %H:%M:%S}'.format(now))
#now time is 2018-11-08 02:20:07


####################################################################
#기타 문자열 변환 메소드
####################################################################

#문자열 sub가 존재하는 위치는 반환
print('python'.find('th'))
#2

#없으면 -1 반환
print('python'.find('aa'))
#-1

#문자열 분할, 리스트로 반환
print('aaa,bbb,ccc,ddd'.split(','))
#['aaa', 'bbb', 'ccc', 'ddd']

#지정된 문자로 문자열을 결합
words = ['aaa', 'bbb', 'ccc', 'ddd']
print('-'.join(words[:2]))
#aa-bbb

print('-'.join(words))
#aaa-bbb-ccc-ddd

#지정된 접두사를 문자열을 검색, 지정은 튜플로 가능, 옵션으로 조사 위치 지정도 가능 startswith(prefix, start, end)
print('python'.startswith('py'))
#True

#지정된 접미사의 문자열을 검색, 지정은 튜플로 가능, , 옵션으로 조사 위치 지정도 가능 endswith(suffix, start, end)
image_suffix = ('jpg', 'png', 'gif')
print('image.png'.endswith(image_suffix))
#True

print('text.txt'.endswith(image_suffix))
#False

#문자열을 지정한 인코딩 형식으로 변환
text = '가abc나'
#print(text.encode('ascii'))
#UnicodeEncodeError: 'ascii' codec can't encode character '\uac00' in position 0: ordinal not in range(128)
#응용 : ascii로 변환안되는 문자 찾기

#지정 인코딩으로 변환안되는것 무시
print(text.encode('ascii', 'ignore'))
#b'abc'

print(text.encode('euc-kr'))
#b'\xb0\xa1abc\xb3\xaa'

print(text.encode('utf-8'))
#b'\xea\xb0\x80abc\xeb\x82\x98'

#문자열을 지정한 디코딩 형식으로 변환
print(b'\xea\xb0\x80abc\xeb\x82\x98'.decode('utf-8'))
#가abc나


####################################################################
#문자열 상수 이용
####################################################################
import string

#영문 소문자
print(string.ascii_lowercase)
#abcdefghijklmnopqrstuvwxyz

#영문 대문자
print(string.ascii_uppercase)
#ABCDEFGHIJKLMNOPQRSTUVWXYZ

#영문 소문자와 대문자 합친것
print(string.ascii_letters)
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

#10진수 숫자
print(string.digits)
#0123456789

#8진수 숫자
print(string.octdigits)
#01234567

#기호 문자열
print(string.punctuation)
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#공백으로 취급되는 문자열
tmp = string.whitespace
#\t\n\r\x0b\x0c

#상기 모두 문자열 포함
tmp = string.printable
#'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~ 	'



