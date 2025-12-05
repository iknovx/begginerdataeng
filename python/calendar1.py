import calendar

# Simple calendar display for a given year

def display_calendar():
    # Calendar header
    year = int(input("Enter year: "))
    print(f"Calendar for the year {year}\n")

    cal = calendar.TextCalendar()
    

    for month in range(1, 13):
        for month_name in calendar.month_name[1:]:
            if month_name == calendar.month_name[month]:
                if month == 12:
                    print("New Year is coming!")
                print(f"The month is: {month_name} is {month}\n")             
                print(f"{cal.formatmonth(year, month)}")

