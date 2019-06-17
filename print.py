import sys

print(1)
print('hello','','hgello')

# sep 파라미터
x = 0.2
s = 'Hello'
print(str(x)+' '+s)
print(x, s, sep=' ')

# 기본적인 print() 함수 호출
print(sep=' ',end='\n')

# file 파라미터를 지정
print('hello World',file=sys.stdout)
print('error;hello World',file=sys.stderr)

# file 출력
f = open('hello.txt','w')
print(type(f))
print('Hello World',file=f)
f.close()
