#Write a program that remove all vowels from the input word and generate a brief version of it.
vows=['a','e','i','o','u']
phrase1 = input()
phrase2=""
for n in phrase1:
    if n not in vows:
        phrase2= phrase2+n
print(phrase2)