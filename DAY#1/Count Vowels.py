vows=['a','o','i','e','u']
cnt=0
phrase = input()
for i in phrase:
    if i in vows:
        cnt+=1
print(cnt)
        
    