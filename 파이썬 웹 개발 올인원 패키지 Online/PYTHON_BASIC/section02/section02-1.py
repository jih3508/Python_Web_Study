# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Pyhon!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcom To', end='')
print('the black parade', end='')
print('piano notes')

# format 사용 [], {}, ()
print('{} and {}'.format('Yuu', 'Me'))
print("{0} abd {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

print("%s's favorite number is %d" % ('Eunki', 7)) #%s: 문자, %d : 정수 , %f: 실수)

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a = 776, b=6534.123))


"""
참고: Escpe 코드

\n : 개행
\t : 탭
\\ : '\'문자
\' : '문자
\" : "문자
\r : 캐리지 리턴
\f :  폼 피드
\a :  벨 소리
\b : 백 스페이스
\000 : 널 문자
"""

print("'you'")
print('\'\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\t\t\ttest')
