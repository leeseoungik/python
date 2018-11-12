##############################
#시각 다루기
##############################

import time

#UTC의 현재시각 반환
print(time.gmtime())
#time.struct_time(tm_year=2018, tm_mon=11, tm_mday=12, tm_hour=5, tm_min=39, tm_sec=14, tm_wday=0, tm_yday=316, tm_isdst=0)

#UTC로 부터 경과 시간으로 표현된 시각을 반환 (인수:초)
print(time.gmtime(1000000000))
#time.struct_time(tm_year=2001, tm_mon=9, tm_mday=9, tm_hour=1, tm_min=46, tm_sec=40, tm_wday=6, tm_yday=252, tm_isdst=0)

#