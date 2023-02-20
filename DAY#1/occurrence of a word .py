#Write a program that prints the number of times the string 'iti' occurs in anystring.
phrase=input()
word=input()
if word in phrase:    
    print(phrase.count(word))
else:
    print("There is no such a word")