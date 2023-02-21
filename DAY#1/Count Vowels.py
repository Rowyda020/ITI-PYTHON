#Write a program that counts up the number of vowels [a, e, i, o,u] contained in the string.
vows=['a','o','i','e','u']
cnt=0
phrase = input()
for i in phrase:
    if i in vows:
        cnt+=1
print(cnt)
        
    
