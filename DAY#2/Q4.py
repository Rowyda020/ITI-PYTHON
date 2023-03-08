#Write a program which repeatedly reads numbers until the user enters “done”.
cnt = 0
sum = 0
number = int(input())
for i in range (number):
    inp = input()
    if inp == "done":
        break
    if inp.isdigit():
        sum += int(inp)
        cnt+=1
        avg = sum/cnt
print(cnt)
print(sum)
print(avg)