# # 문자열 자료형
str1 = "작은 따옴표의 모양은 '이다"
str2 = '큰 따옴표의 모양은 " 이다'
print(str1)
print(str2)
str3 = "큰 따옴표의 모양은 \" 이다"
print(str3)
str4 = '작은 따옴표의 모양은 \'이다'
print(str4)

str5 = "보안의 \n3요소"
str6 = '''기밀성
무결성
가용성'''
str7 = """Confidentiality
Intergrity
Availability"""
print(str5)
print(str6)
print(str7)
print()
# escape 문자처리
print('hello, \nworld!')
print('hello, \tworld!')
print('hello, \\world!')
print('hello, /world!')
print('welcome to, my\'world!')
print('\"안녕하세요\"')
print('hello, \rworld!')
print('12345 \r678')
print('hello, \fworld!')
print('hello, \aworld!')
print('hello, \bworld!')
print('hello, \vworld!')
print('8진수 -> \141')
print('16진수 -. \x61')
print('유니코드 :  \N{LINE FEED}')
print('16비트 16진수로 유니코드 표현: \u0061')
print('32비트 16진수로 유니코드 표현: \U00000061')
print(R'벨소리를 듣고 싶으면 \a 를 사용하세요')
print()
#문자열 포맷
print('전공은 %s이다' % '컴퓨터공학')
print('현재 학년은 %i학년이다.' % 1)
print('전공은 %s이고 현재 학년은 %d학년이다.' % ('영어영문학과', 4))
major = '영어영문학과'
grade = 4
print('전공은 %s이고 현재 학년은 %d학년이다.' % (major, grade))
print('컴퓨터공학과의 취업률은 %d%%이다.' % 100)
print('컴퓨터공학과의 춰업률은 %5.2f%%이다.' % 89.1746)
print('컴퓨터공학과의 취업률은 %5.2f%%이다.' % 89.1766)
print('이번달은 %02d월이다.' % 9)

print('|%10s|' % '컴퓨터공학')
print('|%-10s|' % '컴퓨터공학')
print('원주율 값은 |%10.5f|입니다.' % 3.141592653589)
print('원주율 값은 |%-10.5f|입니다.' % 3.141592653589)
print('원주율 값은 |%0.5f|입니다.' % 3.141592653589)
print('원주율 값은 |%0.5f|입니다.' % 3.141592653589)
print()
# 문자열 연결과 반복
s1 = '컴퓨터'
s2= '공학'
print(s1 + s2)
s3 = (s1+s2+'!! ') * 3
print(s3)
_name = '김형원'
print(_name)
print()
# 문자열 인덱싱
str9 = 'Computer security'
print(str9[0], str9[1], str9[2], str9[3], str9[4])
print(str9[-17], str9[-16], str9[-15], str9[-14], str9[-13])
print(str9[0]+str9[1]+str9[2]+str9[3]+str9[4])
print(str9[0:8])
print(str9[:8])
print(str9[9:])
print(str9[:])
print(str9[0:16])
print(str9[9:-5])

print(str9.capitalize())
print(str9.count('t'))
print(str9.find('s'))
print(str9.rfind('t'))
print(str9.index('s'))
print(str9.find('S'))
# print(str9.index('S'))
print(str9.upper())
print(str9.lower())

