import os, time, datetime, argparse, re

powersOfI = {
    1 : "i",
    2 : "-1",
    3 : "-i"
}


parser = argparse.ArgumentParser(description="Calculate a given power of the imaginary unit i")
parser.add_argument('-l', '--login', type=int, help='Name of logfile', nargs=1)
args = parser.parse_args()

print("\nThe following is a program that calculates a given power of the imaginary unit i")

def main():
    if __name__ == '__main__':
        if args.login == None:
            logFileName = askToLogOrNot()
        elif args.login[0].lower() != 'no' or args.login[0].lower() != n:
            logFileName = args.login[0]
        else:
            logFileName = 'n'


def calculatePower():
    global checkIfMultiple, powerOfSecondI, powerOfFirstI, imaginaryUnit, expandingFirstPower
    checkIfMultiple = multipleOfFour()
    powerOfSecondI = exponent % 4
    powerOfFirstI = exponent - powerOfSecondI

    if exponent < 4:
        imaginaryUnit = powersOfI[powerOfSecondI]
        print("\ni**" + str(exponent) + " = " + str(imaginaryUnit) + "\n")

    elif checkIfMultiple == True:
        imaginaryUnit = 1
        expandingFirstPower = powerOfFirstI // 4
        print("\ni**" + str(exponent) + " = (i**4)**" + str(expandingFirstPower))
        print("i**" + str(exponent) + " = (1)**" + str(expandingFirstPower))
        print("i**" + str(exponent) + " = 1" + "\n")

    else:
        imaginaryUnit = powersOfI[powerOfSecondI]
        expandingFirstPower = powerOfFirstI // 4
        print("\ni**" + str(exponent) + " = i**" + str(powerOfFirstI) + " x i**" + str(powerOfSecondI))
        print("i**" + str(exponent) + " = (i**4)**" + str(expandingFirstPower) + " x i**" + str(powerOfSecondI))
        print("i**" + str(exponent) + " = (1)**" + str(expandingFirstPower) + " x i**" + str(powerOfSecondI))
        print("i**" + str(exponent) + " = 1 " + "x " + imaginaryUnit)
        print("i**" + str(exponent) + " = " + imaginaryUnit + "\n")

def outputLogFile():
	if logFileName.lower() != "n":
		logfile = open(os.getcwd()+'/'+logFileName, 'w')

		logfile.write("\ni**" + str(exponent) + " = " + str(imaginaryUnit) + "\n")


        logfile.write("\ni**" + str(exponent) + " = (i**4)**" + str(expandingFirstPower) + "\n")
        logfile.write("i**" + str(exponent) + " = (1)**" + str(expandingFirstPower) + "\n")
        logfile.write("i**" + str(exponent) + " = 1" + "\n")

 
        logfile.write("\ni**" + str(exponent) + " = i**" + str(powerOfFirstI) + " x i**" + str(powerOfSecondI) + "\n")
        logfile.write("i**" + str(exponent) + " = (i**4)**" + str(expandingFirstPower) + " x i**" + str(powerOfSecondI) + "\n")
        logfile.write("i**" + str(exponent) + " = (1)**" + str(expandingFirstPower) + " x i**" + str(powerOfSecondI) + "\n")
        logfile.write("i**" + str(exponent) + " = 1 " + "x " + imaginaryUnit + "\n")
        logfile.write("i**" + str(exponent) + " = " + imaginaryUnit + "\n")

		logfile.close()
		print("A logfile was published to ", os.getcwd()+'/'+logFileName)
	else:
		print("No log created.")

        
def askToLogOrNot():
    logFileYesOrNo = input("Would you like to save a logfile? ")
    if re.search("y(yes)?", logFileYesOrNo, re.IGNORECASE):
        logFileName = input("Logfile filename: ")
    else:
        logFileName = 'n'
    return logFileName


def powerOfImaginaryUnit():
    imaginaryUnitPower = int(input("Enter the value of the exponent of you which the imaginary unit is raised to: "))
    return imaginaryUnitPower


def multipleOfFour():
    global exponent
    exponent = powerOfImaginaryUnit()
    if (exponent % 4) == 0:
        return True
    else: 
        return False


main()
calculatePower()

