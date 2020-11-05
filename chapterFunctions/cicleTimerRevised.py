import time
import sys

try:
    def timeOn(tOn):
        while tOn > 0:
            tOn -= 1
            time.sleep(1)
            print('On ' + str(tOn) + 's')


    def timeOff(tOff):
        while tOff > 0:
            tOff -= 1
            time.sleep(1)
            print('Off ' + str(tOff) + 's')


    def cicleTime():
        global secondsOn, secondsOff
        print('How many second to stay On?')
        secondsOn = int(input())
        print('How many second to stay Off?')
        secondsOff = int(input())


    print('Do you want to run this program for a set number of times or indefenetly?')
    print('Please respond with Yes or No:')
    choice = input()

    if choice == 'Yes':
        print('How many cycles do you want?')
        numberOfCycles = int(input())
        cicleTime()

        while 0 < numberOfCycles:
            timeOn(secondsOn)
            timeOff(secondsOff)
            numberOfCycles -= 1
    else:
        cicleTime()
        while True:
            timeOn(secondsOn)
            timeOff(secondsOff)

except KeyboardInterrupt:
    sys.exit()
