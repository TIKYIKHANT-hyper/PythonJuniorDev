instructionCounter = 0
memory = []
for i in range(0, 40):
    memory.append(" +0000")


def memoryview():
    print("20 space memory view")
    for x in range(0, 20):
        justifiedstr = str(memory[x]).rjust(10)
        print(justifiedstr, end="  ")
        if x % 10 == 9:
            print()


def drawlines():
    for z in range(140):
        print("-", end="")
        if z == 139:
            print()


operand = int()
operationCode = int()
instructionRegister = str()
accumulator = int()
while True:
    drawlines()
    print(f"accumulator : {accumulator}".rjust(20))
    print(f"instruction register: {instructionRegister}".rjust(20))
    print(f"instruction counter: {instructionCounter}".rjust(20))
    memoryview()
    usrin = int(input("Enter for instruction: "))

    if usrin >= 1000:
        instructionRegister = int(usrin)
        operationCode = instructionRegister // 100
        operand = instructionRegister % 100
        if operand >= 20:
            print("Out of space")
            break
        if operationCode == 10:
            valuein = int(input("Enter your value: "))
            memory[operand] = int(valuein)
            accumulator = instructionRegister
            instructionCounter += 1

        elif operationCode == 11:
            print(f"The value at location {operand} is {memory[operand]} ")
            instructionCounter += 1

        elif operationCode == 20:
            accumulator = memory[operand]
            instructionCounter += 1

        elif operationCode == 21:
            memory[operand] = "+" + str(accumulator)
            instructionCounter += 1

        elif operationCode == 30:
            accumulator += memory[operand]
            instructionCounter += 1

        elif operationCode == 31:
            accumulator -= memory[operand]
            instructionCounter += 1

        elif operationCode == 32:
            accumulator /= memory[operand]
            instructionCounter += 1

        elif operationCode == 33:
            accumulator *= memory[operand]
            instructionCounter += 1

        elif operationCode == 40:
            memory[operand] = accumulator
            instructionCounter += 1

        elif operationCode == 41:
            if accumulator < 0:
                memory[operand] = accumulator
                instructionCounter += 1

        elif operationCode == 42:
            if accumulator == 0:
                memory[operand] = accumulator
                instructionCounter += 1

        elif operationCode == 43:
            print("Virtual machine eliminated")
            break

    else:
        print("Please enter valid instruction")

