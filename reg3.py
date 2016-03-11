string = raw_input("Input here:")
txt=string.split()
result=[]

for words in txt:
  if len(words) < 5:
     continue
  result.append(words)

print ','.join(result),"has characters more than five letters"
