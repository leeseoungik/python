#문자열 검사 메소드

########################################################################
#문자열이 숫자와 문자일 때만 True를 반환한다.
ret = '123abc'.isalnum()
#True

ret = '123abc#'.isalnum()
#False

########################################################################
#문자일때만 True를 반환한다. 숫자나 기호가 포함되어 있으면 Fasle를 반환한다.
ret = 'abcd'.isalpha()
#True

ret = '가나다라'.isalpha()
#True

ret = 'abcd123'.isalpha()
#False

ret = 'abcd!@#'.isalpha()
#Fasle

########################################################################
#문자열(영문자만해당)이 모두 대문자이면 True를 반환한다.
ret = 'ABCD'.isupper()
#True

ret = 'ABcd'.isupper()
#Fasle

ret = '가나다abc'.isupper()
#False

ret = '가나다ABC'.isupper()
#True

ret = '가나다ABC!@#'.isupper()
#True

########################################################################
#문자열(영문자만해당) 이 모두 소문자이면 True를 반환한다.
ret = 'abcd'.islower()
#True

ret = 'ABcd'.islower()
#False

ret = '가나다abc'.islower()
#True

ret = 'abc가나다'.islower()
#True

ret = 'abc가나다!@#'.islower()
#True

########################################################################
#맨 처음이 대문자이고 뒤는 소문자이면 True를 반환한다.
ret = 'Title String'.istitle()
#True

ret = 'TItle String'.istitle()
#Fasle

########################################################################
#문자열이 십진수 숫자를 나타내면 True를 반환한다.
ret = '123'.isdecimal()
#True

ret = '1 2 3'.isdecimal()
#False

ret = '1 2 3 a b'.isdecimal()
#False

ret = '일이삼'.isdecimal()
#False

ret = '하나둘셋'.isdecimal()
#False

ret = '⑴'.isdecimal()
#False

ret = 'ⅶ'.isdecimal()
#False

ret = '①'.isdecimal()
#False

########################################################################
#문자열이 숫자를 나타내는 문자로만 이루어졌으면 True를 반환한다.
ret = '123'.isdigit()
#True

ret = '1 2 3'.isdigit()
#False

ret = '1 2 3 a b'.isdigit()
#False

ret = '일이삼'.isdigit()
#False

ret = '하나둘셋'.isdigit()
#False

ret = '⑴'.isdigit()
#True

ret = 'ⅶ'.isdigit()
#False

ret = '①'.isdigit()
#True


########################################################################
#수를 나타내는 문자열이면 True를 반환한다. 한자 숫자도 포함
ret = '123'.isnumeric()
#True

ret = '1 2 3'.isnumeric()
#False

ret = '1 2 3 a b'.isnumeric()
#False

ret = '일이삼'.isnumeric()
#False

ret = '하나둘셋'.isnumeric()
#False

ret = '⑴'.isnumeric()
#True

ret = 'ⅶ'.isnumeric()
#True

ret = '①'.isnumeric()
#True

ret = '一二三'.isnumeric()
#True

########################################################################
#스페이스, 탭등의 공백 문자면 True를 반환한다.
ret = ' '.isspace()
#True

ret = 'a b'.isspace()
#False

ret = '글자'.isspace()
#False

ret = '글 자'.isspace()
#False

########################################################################
#프린트 가능한 문자열이면 True를 반환한다.
ret = 'ㄱㄴㄷ'.isprintable()
#True

########################################################################
#프린트 가능한 문자열이면 True를 반환한다.
ret = 'ㄱㄴㄷ'.isidentifier()
#True

ㄱㄴㄷ='abd'
print(ㄱㄴㄷ)


print('end')