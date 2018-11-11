##############################
#간단한 통계 계산
##############################

import statistics

data = [1, 2, 2, 3, 4, 5, 6]

##############################
#데이터의 평균값 구하기
print(statistics.mean(data))
#3.2857142857142856

#데이터의 중앙값 구하기
print(statistics.median(data))
#3

#데이터의 최빈값 구하기
print(statistics.mode(data))
#2


#데이터의 모표준편차 구하기
print(statistics.pstdev(data))
#1.6659862556700857

#데이터의 표본표준편차 구하기
print(statistics.stdev(data))
#1.7994708216848747

#데이터의 모분산 구하기
print(statistics.pvariance(data))
#2.7755102040816326

#데이터의 표본분산 구하기
print(statistics.variance(data))
#3.238095238095238