##############################
#전 세계 표준시간대 정보 다루기
#pip3 install pytz
##############################

import pytz
from datetime import datetime
from pprint import pprint

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

##############################
#표준시간대 정보 다루기

#서울 표준시간대 정보
seoul = pytz.timezone('Asia/Seoul')

#미국동부 표준시간대 정보
eastern = pytz.timezone('US/Eastern')

#서울의 현재 일시 얻기
seoul_dt = seoul.localize(datetime.now())
print(seoul_dt.strftime(fmt))
#2018-11-13 20:30:52 KST+0900

#서울의 시각을 미국동부 시각으로 변경
eastern_dt = seoul_dt.astimezone(eastern)
print(eastern_dt.strftime(fmt))
#2018-11-13 06:30:52 EST-0500

#
jan = datetime(2018, 1, 1)
jun = datetime(2018, 6, 1)

#서머타임 시간차 확인
print(eastern.utcoffset(jan))
#-1 day, 19:00:00
print(eastern.utcoffset(jun))
#-1 day, 20:00:00

#서머타임 시간차 반환
print(eastern.dst(jan))
#0:00:00
print(eastern.dst(jun))
#1:00:00

#표준시간대 이름 반환
print(eastern.tzname(jun))
#EDT
print(eastern.tzname(jan))
#EST

##############################
#표준시간대 리스트

#ISO3166 국가코드에 대해 표준시간대 반환
print(pytz.country_timezones['nz'])
#['Pacific/Auckland', 'Pacific/Chatham']

#ISO3166국가코드에 대해 영어 국가명을 반환
print(pytz.country_names['nz'])
#New Zealand

#pytz에서 사용가능한 전체 표준시간대 반환
print(len(pytz.all_timezones))
#591

#일반적인 표준시간대, 사용하지 않는 표준시간대 비포함
print(len(pytz.common_timezones))
#439

#일반적인 표준시간대 이름 집합
pprint(pytz.common_timezones_set)
# LazySet({'Africa/Abidjan',
#          'Africa/Accra',
#          'Africa/Addis_Ababa',
#          'Africa/Algiers',
#          'Africa/Asmara',
#           ..............................

#존재확인
print('Asia/Seoul' in pytz.common_timezones_set)
#True

