numbers=(1,2,3,4,5,6,7,8,9)
count1=0
count2=0
for i in numbers:
    if i%2==0:
        count1=count1+1
    else:
        count2=count2+1
print("Number of even numbers: ",count1)
print("Number of odd numbers: ",count2)