import nltk

f=open('1155109652.txt','r')
a=f.read()
tokens = nltk.word_tokenize(a)
tokensa = [token.lower() for token in tokens]

f=open('positive.txt','r')
b=f.read()
tokensb = nltk.word_tokenize(b)

f=open('negative.txt','r')
c=f.read()
tokensc = nltk.word_tokenize(c)

i=0
for x in tokensa:
  for y in tokensb:
    if x == y:
        i+=1
        print(x, y)
print(i)

j=0
for x in tokensa:
  for y in tokensc:
    if x == y:
        print(x, y)
        j+=1
print(j)

print("the overall sentiment score:",i-j)
