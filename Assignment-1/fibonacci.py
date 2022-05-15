num1=1
num2=1
print("Fibonacci series between 0 to 50: ")
print(num1,num2,end=" ")
for i in range(50):
    num3=num1+num2
    if num3>=50:
        break
    else:
        print(num3,end=" ")
    num1=num2
    num2=num3  