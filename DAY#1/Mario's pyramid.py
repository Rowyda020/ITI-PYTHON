#Write a program that build a Mario pyramid
number=int(input())
for m in range(number):
    for l in range(number-m-1):
        print(" ",end=" ")
    for l in range(m+1):
        print("*",end=" ")
    print()