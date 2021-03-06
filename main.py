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

def calculatePower():
    if multipleOfFour() == False:
        powerOfSecondI = exponent % 4
        imaginaryUnit = powersOfI[powerOfSecondI]
        
    else:
        imaginaryUnit = 1



def main():
    if __name__ == '__main__':
        if args.login == None:
            logFileName = askToLogOrNot()
        elif args.login[0].lower() != 'no' or args.login[0].lower() != n:
            logFileName = args.login[0]
        else:
            logFileName = 'n'

        """
        if multipleOfFour() == True:
            print("true")
        else:
            print("false")
        """

main()