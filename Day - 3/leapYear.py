entered_year = int(input("Enter the Year : \n"))

if entered_year % 4 == 0 :
    if entered_year % 100 == 0:
        if entered_year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year as not devided by 400")
    else:
        print("Leap year as not deviced by 100")
else:
    print("Not Leap year you fucker")