##############################
#날짜와 시간 다루기
##############################

from datetime import date

##############################
#날짜 다루기 (datetime.date)

#지정한 날짜의 date 객체를 생성
newyearsday = date(2018, 11, 12)
print(newyearsday)
#2018-11-12

#년, 월, 일 반환
print(newyearsday.year, newyearsday.month, newyearsday.day)
#2018 11 12

#요일 반환 (0~6 : 월~일)
print(newyearsday.weekday())
#0

#요일 반환 (1~7 : 월~일)
print(newyearsday.isoweekday())
#1

#YYYY-MM-DD 형식의 날짜 문자열 반환
print(newyearsday.isoformat())
#2018-11-12

print(newyearsday.__str__())
#2018-11-12

print(str(newyearsday))
#2018-11-12

#지정한 포맷에 따라 문자열 반환
print(newyearsday.strftime('%Y/%m/%d'))
#2018/11/12

print(newyearsday.strftime('%Y %b %d (%a)'))
#2018 Nov 12 (Mon)

#현재 년-월-일 반환
print(newyearsday.today())

#날짜 계산
fu = date(2019, 1, 1)
bb = date(2018, 1, 1)
print(fu - bb)
#365 days, 0:00:00

##############################
#시각 다루기 (datetime.time)

from datetime import time

print(time(0, 0))
print(time())
#00:00:00

#지정한 시각의 time 객체 생성
print(time(16, 12, 15))
#16:12:15

#분 설정
print(time(0, 10))
print(time(minute=10))
#00:10:00

#초 설정
print(time(0, 0, 10))
print(time(second=10))
#00:00:10

#밀리초 설정
print(time(0, 0, 0, 10))
print(time(microsecond=10))
#00:00:00.000010

now = time(16, 12, 15)

#시, 분, 초 반환
print(now.hour, now.minute, now.second)
#16 12 15

#ISO 8601 형식(HH:MM:SS.mmmmmm) 반환, 마이크로초가 0일 떄는 HH:MM:SS 반환
print(now.isoformat())
#16:12:15

#지정한 포맷의 문자열 반환
print(now.strftime('%H:%M'))
#16:12

print(str(now))
#16:12:15

##############################
#일시 다루기 (datetime.datetime)

from datetime import datetime

#현재일시 얻음
today = datetime.today()
print(today)
#2018-11-11 15:00:06.500991

#date 객체 반환
print(today.date())
#2018-11-11

#time 객체 반환
print(today.time())
#15:00:57.116521

#ISO8601 형식의 문자열 얻음
print(today.isoformat())
#2018-11-11T15:03:23.082715

print(today.strftime('%Y/%m/%d'))
#2018/11/11

#일시 계산 (가능)
today2 = datetime.today()
print(today2 - today)

#UTC 구하기
print(datetime.utcnow())

##############################
#일시의 차 구하기 (datetime.timedelta)

from datetime import timedelta

td = date.today()
print(td)
#2018-11-11

#일주일의 timedelta 생성
#days, seconds, microseconds, milliseconds, minutes, hours, weeks 등 설정 가능
week = timedelta(days = 7)

#일주일 뒤의 날짜 얻음
print(td + week)
#2018-11-18

#2주일 뒤의 날짜 얻음
print(td + week * 2)
#2018-11-25

#일주일 전의 날짜 얻음
print(td - week)
#2018-11-04


