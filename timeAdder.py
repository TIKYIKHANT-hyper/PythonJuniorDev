def timeAdd(start,end,day=""):
    date_count = 0
    day_passed = 0
    if day != "" and day != None:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for date in days:
            if date.lower() == day.lower():
                break
            else:
                date_count += 1

    if "AM" not in start.upper() and "PM" not in start.upper():
        time1 = start.strip()
        time2 = end.strip()
        newtime1 = time1.split(":")
        newtime2 = time2.split(":")
        res_hr = int(newtime1[0]) + int(newtime2[0])
        res_min = int(newtime1[1]) + int(newtime2[1])
        while res_min >= 60:
            res_hr += 1
            res_min -= 60
        while res_hr > 12:
            res_hr -= 12
        print(f"{res_hr}:{res_min}\n")
    elif "AM" in start.upper() or "PM" in start.upper():
        new_list = (start.strip()).split(" ")
        new_str = new_list[0].split(":")
        period = new_list[1]
        end_str = (end.strip()).split(":")
        res_min = int(new_str[1]) + int(end_str[1])
        res_hr = int(new_str[0]) + int(end_str[0])

        while res_min >= 60:
            res_hr += 1
            res_min -= 60
        while res_hr > 12:
            res_hr -= 12

            if period == "pm":
                period = "am"
                if day != "" and day != None:
                    if date_count == len(days):
                        date_count = 0
                        day_passed += 1
                    elif date_count < len(days):
                        date_count += 1
                        day_passed += 1
                        if date_count == len(days):
                            date_count = 0
            elif period == "am":
                period = "pm"
            elif period == "PM":
                period = "AM"
                if day != "" and day != None:
                    if date_count == len(days):
                        date_count = 0
                        day_passed += 1
                    elif date_count < len(days):
                        date_count += 1
                        day_passed += 1
                        if date_count == len(days):
                            date_count = 0
            elif period == "AM":
                period = "PM"

        if day != None and day != "":
            if day_passed == 0:
                print(f"{res_hr}:{res_min} {period} {days[date_count]}")
            elif day_passed == 1:
                print(f"{res_hr}:{res_min} {period} {days[date_count]} (next day)")
            else:
                print(f"{res_hr}:{res_min} {period} {days[date_count]} ({day_passed} days later)")
        else:
            print(f"{res_hr}:{res_min} {period}\n")

timeAdd("12:30 AM","2:40","SunDay")