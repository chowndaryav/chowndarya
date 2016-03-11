import sys

string = raw_input("Input here:")
txt=string.split()
result=[]

num=len(sys.argv)-1
if num:
  for words in txt:
    if len(words)<5:
       result.append(words)
    else:
       result.append(sys.argv[1])

  print result
