
f = open('test.txt','rt',encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('---',text,'---')


# postion 단위는 byte
pos = f.tell()
print(pos)

# (offset, from_What)
#        , 0 (맨 앞에서)
# 1st param : offset
# 2nd param : from_what (0:시작, 1:현재위치, 2: 끝)
# text mode 에서는 from_what 은 0(파일 시작) 만 허용
f.seek(16,0)
text = f.read()
print(text)


# (offset, from_What)
#        , 2 (맨 끝에서)

# f.seek(10,1)
# text = f.read()
# print(text)


# line 단위로 읽기
linenum = 0
f2 = open('fileio2.py','rt',encoding='utf-8')

while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break
    linenum += 1
    print('{0},{1}'.format(linenum,line),end='')
    # print(line,end='')

f3 = open('fileio2.py','rt',encoding='utf-8')
lines = f3.readlines()
f3.close()
print(type(lines))

for linenum, line in enumerate(lines):
    print('{0},{1}'.format(linenum, line), end='')










