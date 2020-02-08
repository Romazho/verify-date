
def verifyDate():
    print("Hello and welcome to The Date Verification App!")

    dayIsCorrect = False

    while (not dayIsCorrect):
        print("Please enter a day: ")
        day = int(input())
        if (day < 1 or day > 31):
            print("Attention! The day must be between 1 and 31.")
        else:
            dayIsCorrect = True

    oddMonths = [1, 3, 5, 7, 8, 10, 12]  # months that have 31 days
    evenMonths = [4, 6, 9, 11]  # months that have 30 days
    february = 2

    monthIsCorrect = False

    while (not monthIsCorrect):
        print("Please enter a month: ")
        month = int(input())
        if (month < 1 or month > 12):
            print("Attention! The month must be between 1 and 12.")
        elif ((month in evenMonths) and day == 31):
            print("Attention! This month can't have 31 days")
        elif ((month == 2) and day > 29):
            print("Attention! February can't have more than 29 days")
        else:
            monthIsCorrect = True

    yearIsCorrect = False

    while (not yearIsCorrect):
        print("Please enter a year: ")
        year = int(input())
        if (year < 0):
            print("Attention! A year cannot be negative.")
        elif(year % 1000 == 0 and month == february):
            yearIsCorrect = True
        elif(year % 100 == 0 and month == february and day > 28):
            print("Attention! The day " + str(day) + " cannot exist on the month of February on the year " +
                  str(year) + ". Because a 'hundred' year isn't actually a leap year!")
        elif(year % 4 != 0 and month == february and day > 28):
            print("Attention! The day " + str(day) + " cannot exist on the month of February on the year " +
                  str(year) + ". Because it's not a leap year!")
        else:
            yearIsCorrect = True

    print("Congratulations! You have chosen a correct date! Your date is: " +
          str(day) + "/" + str(month) + "/" + str(year))


verifyDate()
