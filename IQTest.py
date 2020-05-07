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

if len(sys.argv) != 2:      # if they did not input name of file
    sys.exit("Usage : python3 IQTest.py testname")      # output and leave code


with open(sys.argv[1], "r") as quiz: 
    data = quiz.read()
    data = data.split(')')          # split the data at )
    for i in data:          # for every index in data
        if data.index(i) != 0:      # if the index is not the first one
            if data[data.index(i)] and data[data.index(i)] != data[-1]:    
                if i.startswith('\na'):     # if i is the answer
                    answer = data[data.index(i)][10:]       # answer is equal to the index
                else:
                    print(i)        # print out the question
                    ans = input("Enter answer here : ")     # ask for input

                    if str(ans).lower() == str(answer).lower():     # compare ans to answer
                        score += 1          # if its the same, update score
        else:
            print(i)        # print question

    IQ = (score/5)*150      # initialize IQ

    print(f"Your score is : {score}")       # print out the score
    print(f"Your IQ is : {IQ}")         # print out the IQ
    
    if score <= 2:      # if the score is less than or equal to 2
        termcolor.cprint("Ooh, thats pretty bad, how about you try again?", "red")      # print out in red

    elif score > 2 and score <= 4:      # if score is greater than 2 and less than or equal to 4
        termcolor.cprint("You got an average score, how about you practice more?", "yellow")    # print out in yellow
    else:
        termcolor.cprint("You are a genius, my friend!", "green")       # print out in green
    
    showAnswers = input("Would you like to see the answers? ")      # ask if they would like to see answers
    if showAnswers.lower() == 'yes':        # if yes
        print(data[-1])     # print answers
    else:       # else
        print('Okay, not showing you the answers.')     # dont show answers
