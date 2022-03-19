


content = ""
with open(".dat","r") as file:
  content = file.read()
with open(".dat","w") as file:
  file.write(content)

wordlist=content.split()

worddict={'aaa':0, 'bbb':0,'ccc':0,'ddd':0}
for i in wordlist:
  if i in worddict:
    worddict[i]=worddict[i]+1
  
    
 
print(worddict)

print(len(wordlist))
