##############################
#시각 다루기
##############################

import time

##############################
#시각 구하기

#UTC의 현재시각 반환
print(time.gmtime())
#time.struct_time(tm_year=2018, tm_mon=11, tm_mday=12, tm_hour=5, tm_min=39, tm_sec=14, tm_wday=0, tm_yday=316, tm_isdst=0)

#UTC로 부터 경과 시간으로 표현된 시각을 반환 (인수:초)
print(time.gmtime(1000000000))
#time.struct_time(tm_year=2001, tm_mon=9, tm_mday=9, tm_hour=1, tm_min=46, tm_sec=40, tm_wday=6, tm_yday=252, tm_isdst=0)

#지역(local)의 현재 시각 반환
print(time.localtime())
#time.struct_time(tm_year=2018, tm_mon=11, tm_mday=12, tm_hour=14, tm_min=56, tm_sec=41, tm_wday=0, tm_yday=316, tm_isdst=0)

#지역(local)로 부터 경과 시간으로 표현된 시각을 반환 (인수:초)
print(time.localtime(1542002676))
#time.struct_time(tm_year=2018, tm_mon=11, tm_mday=12, tm_hour=15, tm_min=4, tm_sec=36, tm_wday=0, tm_yday=316, tm_isdst=0)

#지정된 포맷으로 반환
print(time.strftime('%Y-%m_%d', time.localtime()))
#2018-11_12

#UTC의 현재시각 반환 (
print(time.time())
#1542002676.601546

print(time.gmtime(1542002676))
#time.struct_time(tm_year=2018, tm_mon=11, tm_mday=12, tm_hour=6, tm_min=4, tm_sec=36, tm_wday=0, tm_yday=316, tm_isdst=0)

##############################
#시각 객체

local = time.localtime()

#년
print(local.tm_year)
#2018

#월
print(local.tm_mon)
#11

#일
print(local.tm_mday)
#12

#시
print(local.tm_hour)
#15

#분
print(local.tm_min)
#32

#초
print(local.tm_sec)
#51

#요일 (0~6:월~일)
print(local.tm_wday)
#0

#연중일수 반환 (오늘까지의 연중일수)
print(local.tm_yday)
#316

#서머타임 적용여부 (0:서머타임 아님)
print(local.tm_isdst)
#0

#UTC와 지역(local)의 차이를 초로 반환
print(local.tm_gmtoff)
#32400

##############################
#스레드 일시 정지

for i in range(5):
    print(time.time())
    time.sleep(0.5)  #0.5초 대기




