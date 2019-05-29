ch=input()
ch.lower()
li=['a','e','i','o','u']
if(ord(ch)>=97 and ord(ch)<=122):
  if ch in li:
    print("Vowel")
  else:
	print("Consonant")
else:
  print("Invalid")
  
