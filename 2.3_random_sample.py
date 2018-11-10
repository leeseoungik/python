##############################
#의사 난수 다루기
##############################

import random

##############################
#난수 생성
print(random.random())

print(random.randint(1, 5))

print(random.uniform(1, 5))

##############################
#시드 고정
random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

print(random.random())

##############################
#특정 분포를 따라는 난수 생성

normal_variate = []
gamma = []

for i in range(10000):
    #평균 mu, 표준편차 sigma의 정규분포를 따르는 난수 생성
    normal_variate.append(random.lognormvariate(0, 1))
    #형상모수 k, 척도모수 theta의 감마분포를 따라는 난수 생성
    gamma.append((random.gammavariate(3, 1)))

##############################
#무작위 선택
seq = [1, 2, 3, 4, 5]

#시퀀스 요소중 무작위 선택
print(random.choice(seq))
print(random.choice(seq))
print(random.choice(seq))

#시퀀스 요소중 두번째 인수 개수의 리스트를 작성하여 반환
#같은 요소가 중복 추출 되지 않음
print(random.sample(seq, 3))
print(random.sample(seq, 3))
print(random.sample(seq, 3))

#ValueError: Sample larger than population or is negative
#print(random.sample(seq, 6))

#원래 시퀀스 요소 순서를 새로 변경
random.shuffle(seq)
print(seq)

