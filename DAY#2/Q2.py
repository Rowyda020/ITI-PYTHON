#write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"
def fbFunc(x):
         if x%3==0 and x%5==0:
            print("FizzBuzz")
         elif x%3==0:
            print("Fizz")
         elif x%5==0:
            print("Buzz")
         else:
            print(i)
x=int(input())


fbFunc(x)