#정규식을 이용한 문자열 검색 메소드
import re

########################################################################
#문자열의 맨 앞글자부터 정규식과 일치하는지 조사
p = re.match('a.c', 'abc')
#<re.Match object; span=(0, 3), match='abc'>

p = re.match('b', 'abc')
#None

########################################################################
#문자열 전체를 검색하여 정규식과 일치하는지 조사
p = re.search('a.c', 'abc')
#<re.Match object; span=(0, 3), match='abc'>

p = re.search('b', 'abc')
#<re.Match object; span=(1, 2), match='b'>

########################################################################
#re모듈 상수(플래그) 이용하기
p = re.search('\w', '가나다라마ABC')
#<re.Match object; span=(0, 1), match='가'>

#일치 확인시에 ASCII 문자만 사용. (re.A 와 re.ASCII 는 같은 표현)
p = re.search('\w', '가나다라마ABC', flags=re.ASCII)
#<re.Match object; span=(5, 6), match='A'>

#일치 확인시에 대소문자 무시. (re.I 와 re.IGNORECASE 는 같은 표현)
p = re.search('[abc]+', 'ABC', flags=re.I)
#<re.Match object; span=(0, 3), match='ABC'>

p = re.search('[abc]+', 'ABC')
#None

#(.)점을 줄바꿈 문자까지 포함. (re.S or re.DOTALL)
p = re.search('a.c', 'A\nC', re.I | re.S)
#<re.Match object; span=(0, 3), match='A\nC'>

########################################################################
#정규 표현 객체 작성

#a-n 까지 영어 소문자 지정
regex = re.compile('[a-n]+')
print(type(regex))
#<class 're.Pattern'>

#지정한 문자열이 정규표현에 일치하는지 반환
p = regex.search('python')
#<re.Match object; span=(3, 4), match='h'>

#지정한 문자열 맨앞글자부터 정규표현에 일치하는지 반환
p = regex.match('python')
#None

#지정한 문자열 전체가 정규표현에 일치하는지 반환
p = regex.fullmatch('eggs')
#None

p = regex.fullmatch('egg')
#<re.Match object; span=(0, 3), match='egg'>

#전화번호에 사용되는 기호 패턴을 지정
regex2 = re.compile('[-+()]')

#지정한 문자열을 정규 표현 패턴에 일치하는 문자열로 분할. 반환은 list
l = regex2.split('080-1234-5678')
#<class 'list'>: ['080', '1234', '5678']

l = regex2.split('(080)1234-5678')
#<class 'list'>: ['', '080', '1234', '5678']

l = regex2.split('+80-80-1234-5678')
#<class 'list'>: ['', '80', '80', '1234', '5678']

#패턴과 일치하는 문자열을 repl로 치환.
str = regex2.sub('', '+80-80-1234-5678')
#'808012345678'

str = regex2.sub('#', '+80-80-1234-5678')
#'#80#80#1234#5678'

#숫자가 1문자 이상을 지정
regex3 = re.compile('\d+')

#지정한 문자열 안의 정규 표현에 일치한 문자열을 리스트로 반환
l = regex3.findall('080-1234-5678')
#<class 'list'>: ['080', '1234', '5678']

#정규 표현에 일치한 문자열을 반복자(iterator)로 반환
it = regex3.finditer('+80-80-1234-5678')
#<callable_iterator object at 0x000001D2271F74A8>
for n in it:
    print(n)
#<re.Match object; span=(1, 3), match='80'>
#<re.Match object; span=(4, 6), match='80'>
#<re.Match object; span=(7, 11), match='1234'>
#<re.Match object; span=(12, 16), match='5678'>

########################################################################
#매치 객체 - re.match() 나 re.search() 등에서 일치한 문자열 정보 객체

#전환번호 정규 표현 정의
regex = re.compile('(\d+)-(\d+)-(\d+)')

m = regex.match('080-1234-5678')

#매칭된 문자열 전체 반환
print(m.group())
#080-1234-5678

#매칭된 첫번째, 두번째, 세번째 문자열을 반환
print(m.group(1), m.group(2), m.group(3))
#080 1234 5678

#매칭된 첫번째, 두번째, 세번째 문자열을 튜플로 반환
print(m.group(1,2,3))
#('080', '1234', '5678')

#매칭된 문자열 전체 반환
print(m.group(0))
#080-1234-5678

#매칭되는 문자열에 서브그룹명을 부여
regex2 = re.compile(r'(?P<country>\w+):(?P<capital>\w+)')
m = regex2.match('korea:seoul good city!')

#서브그룹명으로 지정
print(m.group('country'), m.group('capital'))
#korea seoul

#일치한 문자열을 튜플 형식으로 모두 얻음
print(m.groups())
#('korea', 'seoul')

#일치한 문자열을 사전 형식으로 얻음
print(m.groupdict())
#{'country': 'korea', 'capital': 'seoul'}

#\n 형식으로 문자열 치환
print(m.expand(r'captial: \2, country: \1'))
#captial: seoul, country: korea

#\g<서브네임> 형식으로 문자열 치환
print(m.expand(r'capital: \g<capital>, country: \g<country>'))
#captial: seoul, country: korea

