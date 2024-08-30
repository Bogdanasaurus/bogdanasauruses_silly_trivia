import random
import time
import questions

POINTS = 0

print("Welcome to trivia!")
time.sleep(2)
print("You will be answering questions up until you fail.")
time.sleep(1)
print("See how many points you can get!")
time.sleep(2)
while True:
    SELECTED_QUESTION = random.randint(1,3) # Change the last value to how many questions you make
    if SELECTED_QUESTION == 1:
        print(questions.QUESTION_1)
        ANSWER_1 = input("What is your answer?")
        if ANSWER_1 == "50":
            POINTS = POINTS + 1
            print("Correct!")
            print("Points: " + str(POINTS))
            time.sleep(2)
        else:
            print("Incorrect! Trivia is over.")
            break
    if SELECTED_QUESTION == 2:
        print(questions.QUESTION_2)
        ANSWER_2 = input("What is your answer?")
        if ANSWER_2 == "1939":
            POINTS = POINTS + 1
            print("Correct!")
            print("Points: " + str(POINTS))
            time.sleep(2)
        else:
            print("Incorrect! Trivia is over.")
            break
    if SELECTED_QUESTION == 3:
        print(questions.QUESTION_3)
        ANSWER_3 = input("What is your answer?").lower()
        if ANSWER_3 == "washington":
            POINTS = POINTS + 1
            print("Correct!")
            print("Points: " + str(POINTS))
            time.sleep(2)
        else:
            print("Incorrect! Trivia is over.")
            break
# You need to add a new block of code for each question you make
# Add new questions in questions.py
print("Trivia is done.")
time.sleep(2)
print("Here is how many points you gained:")
time.sleep(1)
print(POINTS)
input("Press enter to exit")
