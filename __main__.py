import os, sys
import importlib

def main():
    if len(sys.argv) > 1:
        userInput = sys.argv[1]
        if validateInput(userInput):
            importProblem(userInput)
        else:
            print("Not a valid input!")
    else:
        while True:
            userInput = input('Which Project Euler problem do you want to solve: ')
            if(validateInput(userInput)):
                importProblem(userInput)
                break
            else:
                print("Not a valid input!")
                continue

def validateInput(input):
    try:
        userInput = int(input)
        if userInput < 0:
            return False
    except ValueError:
        return False
    else:
        return True

def importProblem(input):
    directory = os.path.dirname(__file__)+ "/solutions/" +  str(input) + '.py'
    if(os.path.isfile(directory)):
        problem = importlib.import_module('solutions.'+ str(input))
        try:
            f = open(directory, 'r')
            print('\033[1m' + '\nFile:' + '\033[0m')
            print('***********************************************')
            print (f.read())
            print('***********************************************')
            print('\n\033[1m' + 'Answer: ' + '\033[0m')
            f.close()
        except IOError:
            print ("File " + directory + " does not exist.")
        problem.solve()
        print ('\n')
    else:
        print ("File " + directory + " does not exist.")


if __name__ == "__main__":
    main()
