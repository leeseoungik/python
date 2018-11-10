##############################
#unicode 정규화
##############################
import unicodedata

##############################
#지정된 이름에 대응하는 문자 반환
print(unicodedata.lookup('LATIN SMALL LETTER A'))
#a

print(unicodedata.lookup('SNOWMAN'))
#☃

##############################
#문자 chr에 대응하는 이름 반환
print(unicodedata.name('A'))
#LATIN CAPITAL LETTER A

print(unicodedata.name('★'))
#BLACK STAR

print(unicodedata.name('※'))
#REFERENCE MARK

print(unicodedata.name('가'))
#HANGUL SYLLABLE GA

print(unicodedata.name('갏'))
#HHANGUL SYLLABLE GALH

##############################
#unicode문자열 정규화

#완성형으로 정규화
#정준 분해한 뒤에 다시 정준 결합
unicodedata.normalize('NFC', '한글')
#호환 분해한 뒤에 다시 정준 결합
unicodedata.normalize('NFKC', '한글')

#N조합형 정규화
#정준 분해
unicodedata.normalize('NFD', '한글')
#호환 분해
unicodedata.normalize('NFKD', '한글')

#한중일 호환용 한자 유니코드(樂)
print( unicodedata.normalize('NFC', '\uF914'))
print( unicodedata.normalize('NFC', '\uF95C'))
print( unicodedata.normalize('NFC', '\uF9BF'))
#樂

#한중일 통합 한자 유니코드(樂)
print( unicodedata.normalize('NFC', '\u6A02'))
#樂

print( unicodedata.normalize('NFC', '樂'))
#樂

str = u'樂'
#유니코드 값 반환
print(format(ord(str), 'X'))
#6A02

