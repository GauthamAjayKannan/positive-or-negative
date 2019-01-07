#test
leu=['a','e','i','o','u']
num=input()
if num in leu:
	print("Vowel")
elif num.isalpha():
	print("Consonant")
else:
	print("invalid")
