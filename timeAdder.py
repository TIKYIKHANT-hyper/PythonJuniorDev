def add_time(start,duration,day=None):
    new_time = ""
    date_count = 0
    day_passed = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    twentyfourhour_division_check = (duration.strip()).split(":")
    hour_check = int(twentyfourhour_division_check[0])
    minute_check = int(twentyfourhour_division_check[1])
    start_str = (start.strip()).split(":")

    start_min_section = (start_str[1]).split(" ")
    start_min_check = int(start_min_section[0])
    if (hour_check % 24) == 0 and (minute_check + start_min_check) < 60:
        day_pass_by_hour_check = hour_check // 24
        day_passed += day_pass_by_hour_check
    if day != "" and day != None:

        for date in days:
            if date.lower() == day.lower():
                break
            else:
                date_count += 1

    if "AM" not in start.upper() and "PM" not in start.upper():
        time1 = start.strip()
        time2 = duration.strip()
        newtime1 = time1.split(":")
        newtime2 = time2.split(":")
        res_hr = int(newtime1[0]) + int(newtime2[0])
        res_min = int(newtime1[1]) + int(newtime2[1])
        while res_min >= 60:
            res_hr += 1
            res_min -= 60
        while res_hr > 12:
            res_hr -= 12
            # res_hr_len = len(str(res_hr))
        res_min_len = len(str(res_min))
        """
        if res_hr_len == 1:
            res_hr = f"0{res_hr}"
        """
        if res_min_len == 1:
            res_min = f"0{res_min}"
        new_time = f"{res_hr}:{res_min}"
    elif "AM" in start.upper() or "PM" in start.upper():
        new_list = (start.strip()).split(" ")
        new_str = new_list[0].split(":")
        period = new_list[1]
        end_str = (duration.strip()).split(":")
        res_min = int(new_str[1]) + int(end_str[1])
        res_hr = int(new_str[0]) + int(end_str[0])

        while res_min >= 60:
            res_hr += 1
            res_min -= 60

        while res_hr > 12:
            res_hr -= 12

            if period == "pm":
                period = "am"

                if date_count == len(days):
                    date_count = 0
                    if (hour_check % 24) == 0 and (minute_check + start_min_check) < 60:
                        continue
                    else:
                        day_passed += 1
                elif date_count < len(days):
                    date_count += 1
                    if (hour_check % 24) == 0 and (minute_check + start_min_check) < 60:
                        continue
                    else:
                        day_passed += 1
                    if date_count == len(days):
                        date_count = 0
            elif period == "am":
                period = "pm"
            elif period == "PM":
                period = "AM"
                if date_count == len(days):
                    date_count = 0
                    if (hour_check % 24) == 0 and (minute_check + start_min_check) < 60:
                        continue
                    else:
                        day_passed += 1
                elif date_count < len(days):
                    date_count += 1
                    if (hour_check % 24) == 0 and (minute_check + start_min_check) < 60:
                        continue
                    else:
                        day_passed += 1
                    if date_count == len(days):
                        date_count = 0
            elif period == "AM":
                period = "PM"
        if res_hr == 12 and period.upper() == "AM":
            period = "PM"

        elif res_hr == 12 and period.upper() == "PM":
            period = "AM"
            if date_count == len(days):
                date_count = 0
                day_passed += 1
            elif date_count < len(days):
                date_count += 1
                day_passed += 1
                if date_count == len(days):
                    date_count = 0
        #res_hr_len = len(str(res_hr))
        res_min_len = len(str(res_min))
        """
        if res_hr_len == 1:
            res_hr = f"0{res_hr}"
        """
        if res_min_len == 1:
            res_min = f"0{res_min}"
        if day != None and day != "":
            if day_passed == 0:
                new_time = f"{res_hr}:{res_min} {period}, {days[date_count]}"
            elif day_passed == 1:
                new_time = f"{res_hr}:{res_min} {period}, {days[date_count]} (next day)"
            else:
                new_time = f"{res_hr}:{res_min} {period}, {days[date_count]} ({day_passed} days later)"
        elif (day == None or day == "") and day_passed > 0:
            if day_passed == 1:
                new_time = f"{res_hr}:{res_min} {period} (next day)"
            else:
                new_time = f"{res_hr}:{res_min} {period} ({day_passed} days later)"
        else:
            new_time = f"{res_hr}:{res_min} {period}"
    return new_time

test1 = add_time("11:40 AM", "0:25")
print(test1)