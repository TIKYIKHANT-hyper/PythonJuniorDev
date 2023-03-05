def formatter(mylist, showans=False):
    if len(mylist) > 5:
        return "Error: Too many problems."
    myfirstline = ""
    mysecondline = ""
    myliner = ""
    myans = ""
    first_op = ""
    myoperator = ""
    second_op = ""
    formatted_str = ""
    for problems in mylist:
        problem = problems.split()
        first_op = problem[0]
        myoperator = problem[1]
        second_op = problem[2]
        ans = ""
        if myoperator == "+" or myoperator == "-":
            pass
        else:
            return "Error: Operator must be '+' or '-'."

        if first_op.isdigit() == False or second_op.isdigit() == False:
            return "Error: Numbers must only contain digits."

        if len(first_op) > 4 or len(second_op) > 4:
            return "Error: Numbers cannot be more than four digits."
        if myoperator == "+":
            ans = int(first_op) + int(second_op)
        elif myoperator == "-":
            ans = int(first_op) - int(second_op)
        stringlen = max(len(first_op), len(second_op)) + 2

        firstline = first_op.rjust(stringlen)
        secondline = myoperator + " " + (second_op.rjust(stringlen - 2))
        liner = "-" * stringlen
        myanswer = str(ans).rjust(stringlen)
        if len(mylist) > 1:
            myfirstline += firstline + "    "
            mysecondline += secondline + "    "
            myliner += liner + "    "
            myans += myanswer + "    "
        else:
            myfirstline += firstline
            mysecondline += secondline
            myliner += liner
            myans += myanswer

    if showans:
        formatted_str = myfirstline + "\n" + mysecondline + "\n" + myliner + "\n" + myans
    else:
        formatted_str = myfirstline + "\n" + mysecondline + "\n" + myliner

    return formatted_str


myfun = formatter(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)

print(myfun)