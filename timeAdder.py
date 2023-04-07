"""
def timeAdd(start,end,date):
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    newlist = start.split(":")
    res_period = ""
    if int(newlist[0]) > 12:
        if "AM" in start:
            res_period += "PM"
        elif "am" in start:
            res_period += "pm"
        elif "PM" in start:
            res_period += "AM"
        elif "pm" in start:
            res_period += "pm"
        else:
            int(end) - int(newlist[0])
"""

def timeAdd(start,end,day=None):
    if "AM" not in start.upper() and "PM" not in start.upper():
        time1 = start.strip()
        time2 = end.strip()
        newtime1 = time1.split(":")
        newtime2 = time2.split(":")
        res_hr = int(newtime1[0]) + int(newtime2[0])
        res_min = int(newtime1[1]) + int(newtime2[1])
        if res_min >= 60:
            res_hr += 1
            res_min -= 60
        if res_hr > 12:
            res_hr -= 12
        print(f"{res_hr}:{res_min}\n")
    elif "AM" in start.upper() or "PM" in start.upper():
        new_list = (start.strip()).split(" ")
        new_str = new_list[0].split(":")
        period = new_list[1]
        end_str = (end.strip()).split(":")
        res_min = int(new_str[1]) + int(end_str[1])
        res_hr = int(new_str[0]) + int(end_str[0])
        if res_min >= 60:
            res_hr += 1
            res_min -= 60
        if res_hr > 12:
            res_hr -= 12
            if period == "pm":
                print(f"{res_hr}:{res_min} am\n")
            elif period == "PM":
                print(f"{res_hr}:{res_min} AM\n")
            elif period == "am":
                print(f"{res_hr}:{res_min} pm\n")
            elif period == "AM":
                print(f"{res_hr}:{res_min} PM\n")
        else:
            print(f"{res_hr}:{res_min} {period}\n")

timeAdd("10:30 PM","2:20")