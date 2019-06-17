
f = open('123.txt','wb')
f.write(b'0123456789')
f.close()

# f = open('123.txt','rb',encoding='utf-8')
# f.seek(-5,1)
# data = f.read(3)
# print(data)
#
# f.seek(0,2)

# with ~ as
linenum = 0
with open('fileio2.py','rt',encoding='utf-8') as f2:
    for linenum, line in enumerate(f2.readlines()):
        line = f2.readline()
        if line == '':
            f2.close()
            break
        linenum += 1
        print('{0},{1}'.format(linenum,line),end='')

