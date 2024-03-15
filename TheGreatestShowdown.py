#Question 2 Task 1: Identify the Greatest

x= input("Pick a number ")
y= input("Pick a number ")
z= input("Pick a number ")

a=int(x)
b=int(y)
c=int(z)

if a>b>c:
    print("The largest number is: ", a)
elif b>a>c:
    print("The largest number is: ", b)
else:
    print("The largest number is ", c)

#Question 2 Task 2: Identify the Smallest
#Using the variables from task 1

if a<b<c:
    print("The smallest number is: ", a)
elif b<c<a:
    print("The smallest number is: ", b)
else:
    print("The smallest number is ", c)  

#Question 2 Task 3: Equality Check 5
#Using same variables as question 1

if a==b==c:
    print("All numbers are equal")
elif a==b:
    if a==b>c:
        print("Two numbers are equal and the largest")
    else:
        print("Two numbers are equal and they are the smallest")
elif a==c:
    if a==c>b:
        print("Two numbers are equal and the largest")
    else:
        print("Two numbers are equal and they are the smallest")   
elif b==c:
    if b==c>a:
        print("Two numbers are equal and the largest")
    else:
        print("Two numbers are equal and they are the smallest")
else:
    print("Please pick at least two of the same numbers.")          