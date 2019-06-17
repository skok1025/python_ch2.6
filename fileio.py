
# textmode 가 default : t
f = open('test.txt','wt',encoding='utf-8')
writesize = f.write('안녕하세요.\npython입니다.')
f.close()

print(writesize)

# binary mode : b
f = open('test2.txt','wb')
writesize = f.write(bytes('안녕하세요.\npython입니다.',encoding='utf-8'))
f.close()
print(writesize)

# read test
f = open('test.txt','rt',encoding='utf-8')
text= f.read()
print(text)

# binary read : copy file
fsrc = open('dog.jpeg','rb')
data = fsrc.read()
fsrc.close()

print(type(data))
fdest = open('dog2.jpeg','wb')
fdest.write(data)
fdest.close()


