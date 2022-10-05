# 시험 chapter 4 조건문과 반복문 5슬라이드 처럼 출제

a = int(input('1에서 100 사이의 정수를 입력하세요 : '))
if(a<100) : 
    print('입력한 저수가 100보다 작음')
    print('a = %d' % a)
print('프로그램 종료')
print()

a = int(input('1에서 100 사이의 정수를 입력하세요 : '))
if(a==100) : 
    print('입력한 정수는 100입니다')
elif(a<100) : 
    print('입력한 정수가 100보다 작음')
    print('a = %d' % a)
else : 
    print('입력한 값은 %d이고 100보다 크다' % a)
if(a % 2 == 0) : 
    print('입력한 정수는 %d이고 짝수임' % a)
else:
    print('입력한 정수는 %d이고 홀수임' % a)
print('프로그램 종료')
print()

age = int(input('나이를 입력하세요 : '))
if(age >= 18):
    score = int(input('점수를 입력하세요: '))
    if(score >= 80):
        print('%d점으로 합격입니다.'%score)
    else:
        print('%d점으로 불합격입니다.'%score)
else:
    print('나이가 %d세로 18살 미만으로 불합격입니다.'%age)
print()

money = int(input('지갑에 얼마 있습니까? '))
if(money >= 10000):
    print('축제에서 사먹자')
elif(money >= 5000):
    print('학식을 먹자')
else:
    print('집에가서 라면먹자')
print()

pocket = []
pocket.append(input('주머니에 있는 것은? (money, card, ...): '))
if 'monney' in pocket:
    print('택시 타고 가자')
elif 'card'in pocket:
    print('모범택시 타고 가자')
else:
    print('버스 타고 가자')
print()

score = int(input('점수를 입력하세요: '))
if(score > 100 or score < 0):
    print('점수는 0점부터 100점 까지만 입력 가능합니다.')
else:
    if(score >= 95):
        grade = 'A+'
    elif(score >= 90):
        grade = 'A'
    elif(score >= 85):
        grade = 'B+'
    elif(score >= 80):
        grade = 'B'
    elif(score >= 75):
        grade = 'C+'
    elif(score >= 70):
        grade = 'C'
    elif(score >= 65):
        grade = 'D+'
    elif(score >= 60):
        grade = 'D'
    else:
        grade = 'F'
    print('{0}점은 "{1}" 학점 입니다.'.format(score, grade))
print()

year = int(input('연도를 입력하세요: '))
if(((year%4==0) and(year%100))or(year%400==0)):
    print('%d 년은 윤년입니다.'%year)
else:
    print('%d 년은 평년입니다.'%year)
print()

a = int(input('a 값을 입력하시오: '))
b = int(input('b 값을 입력하시오: '))
print('\n입력된 a 값은 = {0}\n입력된 b 값은 = {1}\n' .format(a,b))
if(a>b):
    temp = a
    a = b
    b = temp
    print('변경된 a 값은 = {0}\n변경된 b 값은 = {1}\n' .format(a, b))
else:
    print('a, b 값은 변경되지 않았다.')
    print('a = {0}, b = {1}' .format(a, b))
# 작은 수를 a 큰 수를 b에 저장하는 예제를 제시하였으나, a와 b 값 교환으로 문제를 풀었다.
# *****.format(a,b)와 (% (a,b))의 차이가 무엇인가?*****
print()
for i in range(5):
    print('Hello, World!')
print()

sum = 0
for n in range(1, 11) :
    print(n)
    sum += n
    print("sum = ", sum)
print()

sum_even = 0
sum_odd = 0
for n in range(1, 101):
    if(n % 2 == 0):
        sum_even += n
    else:
        sum_odd += n
print('짝수의 합 = ', sum_even)
print('홀수의 합 = ', sum_odd)
print()

for i in range(10):
    print(i, end = ' ')
print()
for i in range(1, 15):
    print(i, end = ' ')
print()
for i in range(1, 15, 2):
    print(i, end = ' ')
print()
for i in range(15, -1, -1):
    print(i, end = ' ')
print()
#python은 신기하다 print 구문 안에 정의와 입력이 겂나 짧게 가능하다

L1 = list(range(10))
L2 = list(range(1, 15))
L3 = list(range(1, 15, 2))
L4 = list(range(15, -1, -1))
print(L1);print(L2);print(L3);print(L4)
print()

for i in range(1, 10):
    guguLine = ''
    for k in range(2, 10):
        guguLine += str("%dX%d=%2d, " % (k, i, k*i))
    print(guguLine)
print()