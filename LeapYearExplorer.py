#Question 3 Task 1: Leap Year Explorer
what_year_is_it = input("What year is it?")
num_year=int(what_year_is_it)


if num_year%4 == 0:
    if num_year%100==0:
        if num_year%400==0:
            print("This is a leap year!")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year!")
else:
    print("This is not a leap year. ")