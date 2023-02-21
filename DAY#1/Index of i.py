#Write a program that prints the locations of "i" character in any string you added.
string= input()
i=input()
if i in string:
    print(string.index(i))
else:
    print("location not found")