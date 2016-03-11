import re
f=open('/home/chowndarya/hello.txt','r')
s=f.read().lower()
words=re.findall(r'\w{5,}',s)
print len(words)
