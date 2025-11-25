word=input("enter a word ")
nword=""
for i in range(len(word) - 1, -1, -1):
  word=word.lower()
  if word[i]==" ":
    word=word.replace(" ","")
    continue
  nword=nword+word[i]
if nword==word.strip(" "):
  print("Its a palindrome!!",nword)
else:
  print(word,"Not a palindrome")
