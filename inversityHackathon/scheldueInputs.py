def dayCalc(day):
    dayHours = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}

    while True:
        print("Please input from the hours of the day that you are busy from: (24HR Clocks) E.G 14 for 2PM")
        while True:
            dayStart = int(
                input("Please input from what hour you are busy from on " + day + ":"))  # Start time on {day}
            dayEnd = int(input("Please input from what hour you are free from on " + day + ":"))  # End time on {day}
            if dayStart > dayEnd:
                print("Invalid inputs")
            else:
                break

        hoursToRemove = set(range(dayStart, dayEnd+1))
        dayHours = dayHours - hoursToRemove
        dayHours = list(dayHours)

        print(dayHours)
        # dayHours.append(dayStart)  # Adds the starting hour to array
        # while dayStart != dayEnd:
        #     dayStart = dayStart + 1 # Increments day start variable
        #     dayHours.append(dayStart)






# ---------------------------------------------------------------------------------------

# Takes user inputs for each day's
monday = dayCalc("Monday")
tuesday = dayCalc("Tuesday")
wednesday = dayCalc("Wednesday")
thursday = dayCalc("Thursday")
friday = dayCalc("Friday")
saturday = dayCalc("Saturday")
sunday = dayCalc("Sunday")
