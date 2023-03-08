def func(name,email):
    if len(name) > 0 and len (email) >0:
        return name,email
    else:
        print("name and email are required")

    
name = input()
email = input()
func(name,email)
print(name,email)
