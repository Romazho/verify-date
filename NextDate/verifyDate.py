
print("Hello and welcome to The Date Verification App!")

dayIsCorrect = False

while (not dayIsCorrect):
    print("Please enter a day: ")
    day = int(input())
    if (day < 1 or day > 31):
        print("Attention! The day must be between 1 and 31.")
    else:
        dayIsCorrect = True


monthIsCorrect = False
oddMonths = [1, 3, 5, 7, 8, 10, 12]  # months that have 31 days
evenMonths = [4, 6, 9, 11]  # months that have 30 days
febuary = 2

while (not monthIsCorrect):
    print("Please enter a month: ")
    month = int(input())
    if (month < 1 or month > 12):
        print("Attention! The month must be between 1 and 12.")
    elif ((month in evenMonths) and day == 31):
        print("Attention! This month can't have 31 days")
    elif ((month == 2) and day > 29):
        print("Attention! Febuary can't have more than 29 days")
    else:
        monthIsCorrect = True

yearIsCorrect = False
