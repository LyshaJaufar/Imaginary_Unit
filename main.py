import os, time, datetime, argparse, re

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
    exponent = powerOfImaginaryUnit()
    if (exponent % 4) == 0:
        pass
    else: 
        powerOfSecondI = exponent % 4
        if powerOfSecondI == 3:
            

def main():
    if __name__ == '__main__':
        if args.login == None:
            logFileName = askToLogOrNot()
        elif args.login[0].lower() != 'no' or args.login[0].lower() != n:
            logFileName = args.login[0]
        else:
            logFileName = 'n'


main()