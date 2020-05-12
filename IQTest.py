import sys
import cprint
import termcolor
import time

seconds = 900
IQ = 0
answer = ''
ans = ''
finished = False

if len(sys.argv) != 2:
    sys.exit("Usage : python3 IQTest.py testname")

def main():
    score = 0
    with open(sys.argv[1], "r") as quiz:
        data = quiz.read()
        data = data.split(')')

        for line in data:
            finished = False
            if time.perf_counter() >= seconds:
                print('Time\'s up! ')
                return
            if data.index(line) != 0:
                if data[data.index(line)] != data[-1]:
                    if line.startswith('\na'):
                        answer = data[data.index(line)][10:]
                    else:
                        if time.perf_counter() >= seconds:
                            print('Time\'s up! ')
                            return
                        print(line)
                        ans = input("Enter answer here : ")

                        if str(ans).lower() == str(answer).lower():
                            score += 1
                            
            else:
                if time.perf_counter() > seconds:
                    print('Time\'s up! ')
                    return
                print(line)

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
        print('Okay, not showing you the answers')
            
main()          


