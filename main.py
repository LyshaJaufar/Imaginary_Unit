import os, time, datetime, argparse, re

powersOfI = {
    1 : "i",
    2 : "-1",
    3 : "-i"
}


parser = argparse.ArgumentParser(description="Calculate a given power of the imaginary unit i")
parser.add_argument('-l', '--login', help='Name of logfile', nargs=1)
parser.add_argument('-p', '--power',help='Value of the exponent of you which the imaginary unit is raised to')
args = parser.parse_args()

print("\nThe following is a program that calculates a given power of the imaginary unit i")

def main():
    global exponent, logFileName, starttime
    if __name__ == '__main__':
        if args.power == None:
            exponent = powerOfImaginaryUnit()
        else:
            exponent = int(args.power)

        if args.login == None:
            logFileName = askToLogOrNot()
        elif args.login[0].lower() != 'no' or args.login[0].lower() != n:
            logFileName = args.login[0]
        else:
            logFileName = 'n'
    starttime = time.time()

def calculatePower():
    global checkIfMultiple, powerOfSecondI, powerOfFirstI, imaginaryUnit, expandingFirstPower, elapsedtime
    checkIfMultiple = multipleOfFour()
    powerOfSecondI = exponent % 4
    powerOfFirstI = exponent - powerOfSecondI

    elapsedtime = str(datetime.timedelta(seconds=round(time.time()-starttime, 2)))
    elapsedtime = elapsedtime[:-4]

    print('\n\n')
    print("Total execution time:", elapsedtime)
    if exponent < 4:
        imaginaryUnit = powersOfI[powerOfSecondI]
        print("i**" + str(exponent) + " = " + str(imaginaryUnit) + "\n")

    elif checkIfMultiple == True:
        imaginaryUnit = 1
        expandingFirstPower = powerOfFirstI // 4
        print("i**" + str(exponent) + " = (i**4)**" + str(expandingFirstPower))
        print("i**" + str(exponent) + " = (1)**" + str(expandingFirstPower))
        print("i**" + str(exponent) + " = 1" + "\n")

    else:
        imaginaryUnit = powersOfI[powerOfSecondI]
        expandingFirstPower = powerOfFirstI // 4
        print("i**" + str(exponent) + " = i**" + str(powerOfFirstI) + " x i**" + str(powerOfSecondI))
        print("i**" + str(exponent) + " = (i**4)**" + str(expandingFirstPower) + " x i**" + str(powerOfSecondI))
        print("i**" + str(exponent) + " = (1)**" + str(expandingFirstPower) + " x i**" + str(powerOfSecondI))
        print("i**" + str(exponent) + " = 1 " + "x " + imaginaryUnit)
        print("i**" + str(exponent) + " = " + imaginaryUnit + "\n")


def outputLogFile():
    if logFileName.lower() != 'n':
        logfile = open(os.getcwd() + '/' + logFileName, 'w')

        logfile.write("Total execution time: " + str(elapsedtime) + "\n")
        if exponent < 4:
            logfile.write("i**" + str(exponent) + " = " + str(imaginaryUnit) + "\n")

        elif checkIfMultiple == True:
            logfile.write("i**" + str(exponent) + " = (i**4)**" + str(expandingFirstPower) + "\n")
            logfile.write("i**" + str(exponent) + " = (1)**" + str(expandingFirstPower) + "\n")
            logfile.write("i**" + str(exponent) + " = 1" + "\n")
        
        else:
            logfile.write("i**" + str(exponent) + " = i**" + str(powerOfFirstI) + " x i**" + str(powerOfSecondI) + "\n")
            logfile.write("i**" + str(exponent) + " = (i**4)**" + str(expandingFirstPower) + " x i**" + str(powerOfSecondI) + "\n")
            logfile.write("i**" + str(exponent) + " = (1)**" + str(expandingFirstPower) + " x i**" + str(powerOfSecondI) + "\n")
            logfile.write("i**" + str(exponent) + " = 1 " + "x " + imaginaryUnit + "\n")
            logfile.write("i**" + str(exponent) + " = " + imaginaryUnit + "\n")

        logfile.close()
        print("A logfile was published to ", os.getcwd()+'/'+logFileName)
    
    else:
        print("No log created")

        
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
    if (exponent % 4) == 0:
        return True
    else: 
        return False


main()
calculatePower()
outputLogFile()
