##############################
#datetime 의 확장 모듈
#pip3 install python-dateutil
##############################

from dateutil.parser import parse

##############################
#날짜 구문 해석

#날짜 구문 해석, 반환값:datetime.datetime
print(parse('2018/11/12 16:30:22'))
#2018-11-12 16:30:22

print(parse('2018-11-12'))
#2018-11-12 00:00:00

print(parse('20181112'))
#2018-11-12 00:00:00

print(parse('20181112163022'))
#2018-11-12 16:30:22

print(parse('Tue, 13 Nov 2018 12:34:56'))
#2018-11-13 12:34:56

##############################
#default 를 지정한 해석
#지정하지 않은 값은 default의 값이 사용됨

from datetime import datetime

default = datetime(2018, 12, 25)

print(parse('2018/11/12 12:34:56', default=default))
#2018-11-12 12:34:56

#시분초만 설정하면..
print(parse('12:34:56', default=default))
#2018-12-25 12:34:56

#시분만 설정하면..
print(parse('12:34', default=default))
#2018-12-25 12:34:00

##############################
#dayfirst, yearfirst 를 지정한 해석

#월일년 으로 해석
print(parse('1/2/3'))
#2003-01-02 00:00:00

#일월년 으로 해석
print(parse('15/2/3'))
#2003-02-15 00:00:00

#일월년 으로 해석
print(parse('1/2/3', dayfirst=True))
#2003-02-01 00:00:00

#년월일 으로 해석
print(parse('1/2/3', yearfirst=True))
#2001-02-03 00:00:00

#년월일 으로 해석
print(parse('15/2/3', yearfirst=True))
#2015-02-03 00:00:00

##############################
#날짜의 차 계산 - relativedelta

from dateutil.relativedelta import  relativedelta
from datetime import datetime, date

now = datetime.now()
print(now)
#2018-11-12 17:36:17.427483

today = date.today()
print(today)
#2018-11-12

#인수명에 s가 있고 없고 차이에 주의
#s가 있으면 +- 계산, 없으면 절대값 지정
#한 달 후
print(now + relativedelta(months=+1))
#2018-12-12 17:36:17.427483

#한 달 전의 일후일 후
print(now + relativedelta(months=-1, weeks=+1))
#2018-10-19 17:36:17.427483

#한 달 후 10시
print(now + relativedelta(months=+1, hour=10))
#2018-12-12 10:36:17.427483

##############################
#요일 지정

from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU

print(today)
#2018-11-12

#다음 금요일
print(today + relativedelta(weekday=FR))
#2018-11-16

#이번달 마지막 금요일
print(today + relativedelta(day=31, weekday=FR(-1)))
#2018-11-30

#다음 월요일
print(today + relativedelta(weekday=MO(+1)))
#2018-11-12

#오늘을 제외한 다음 월요일
print(today + relativedelta(days=+1, weekday=MO(+1)))
#2018-11-19

##############################
#그 해 몇번째 날 계산

#2018년의 100일째 (입력 날짜와 상관없이 그 해 처음부터 셈)
print(date(2018, 1, 1) + relativedelta(yearday=100))
#2018-04-10

#2012년의 윤일을 포함한 100일째
print(date(2012, 1, 1) + relativedelta(yearday=100))
#2012-04-09

#2012년의 윤일을 제외한 100일째
print(date(2012, 1, 1) + relativedelta(nlyearday=100))
#2012-04-10

##############################
#일 수 차 계산

#두 일시의 차
print(relativedelta(date(2018,1 ,1), today))
#relativedelta(months=-10, days=-11)

print(relativedelta(date(2019,1 ,1), today))
#relativedelta(months=+1, days=+20)

##############################
#반복 규칙

from dateutil.rrule import rrule
from dateutil.rrule import DAILY, WEEKLY, MONTHLY
#

start = datetime(2018, 1, 1)

#지정일로부터 3일간
print(list(rrule(DAILY, count=3, dtstart=start)))
#[datetime.datetime(2018, 1, 1, 0, 0), datetime.datetime(2018, 1, 2, 0, 0), datetime.datetime(2018, 1, 3, 0, 0)]

#시작일에서 지정일까지 매일
print(list(rrule(DAILY, dtstart=start, until=datetime(2018, 1, 3))))
#[datetime.datetime(2018, 1, 1, 0, 0), datetime.datetime(2018, 1, 2, 0, 0), datetime.datetime(2018, 1, 3, 0, 0)]

#지정일까지 매주 화,목  (wkst:주의 처음 요일 지정)
print(list(rrule(WEEKLY, count=4, wkst=SU, byweekday=(TU, TH), dtstart=start)))
#[datetime.datetime(2018, 1, 2, 0, 0), datetime.datetime(2018, 1, 4, 0, 0), datetime.datetime(2018, 1, 9, 0, 0), datetime.datetime(2018, 1, 11, 0, 0)]

#매월 마지막 금요일
print(list(rrule(MONTHLY, count=4, byweekday=FR(-1), dtstart=start)))
#[datetime.datetime(2018, 1, 26, 0, 0), datetime.datetime(2018, 2, 23, 0, 0), datetime.datetime(2018, 3, 30, 0, 0), datetime.datetime(2018, 4, 27, 0, 0)]

#격주
print(list(rrule(WEEKLY, interval=2,  count=3, dtstart=start)))
#[datetime.datetime(2018, 1, 1, 0, 0), datetime.datetime(2018, 1, 15, 0, 0), datetime.datetime(2018, 1, 29, 0, 0)]
