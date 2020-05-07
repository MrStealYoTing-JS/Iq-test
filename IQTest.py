import sys
import cprint
import termcolor
import time
import concurrent.futures

seconds = 180
score = 0
IQ = 0
answer = ''
ans = ''

if len(sys.argv) != 2:
    sys.exit("Usage : python3 IQTest.py testname")


with open(sys.argv[1], "r") as quiz:
    data = quiz.read()
    data = data.split(')')
    for i in data:
        if data.index(i) != 0:
            if data[data.index(i)] and data[data.index(i)] != data[-1]:
                if i.startswith('\na'):
                    answer = data[data.index(i)][10:]
                else:
                    print(i)
                    ans = input("Enter answer here : ")

                    if str(ans).lower() == str(answer).lower():
                        score += 1
        else:
            print(i)

    IQ = (score/5)*150

    print(f"Your score is : {score}")
    print(f"Your IQ is : {IQ}")

    if score <= 2:
        termcolor.cprint("Ooh, thats pretty bad, how about you try again?", "red")

    elif score > 2 and score <= 4:
        termcolor.cprint("You got an average score, how about you practice more?", "yellow")
    else:
        termcolor.cprint("You are a genius, my friend!", "green")
    
    showAnswers = input("Would you like to see the answers? ")
    if showAnswers.lower() == 'yes':
        print(data[-1])
    else:
        print('Okay, not showing you the answers.')