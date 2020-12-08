"""
    magic_8_ball.py
    @author Oleksandr Shalbanov
    @version 2017-09-17
"""

import random

def main():
    game=magic8ball()
    game.greeting()
    repeate=True
    while repeate:
        game.getQuestion()
        game.generateAnswer()
        repeate=game.finishQuestion()
    game.farewell()

class magic8ball:
    def __init__(self):
        pass

    def generateAnswer(self):
        print(random.choice('Yes!#No!#Maybe...#Not today...#Try again...'.split('#')))

    def getQuestion(self):
        self.question = input("Enter a Yes/No question: ")

    def finishQuestion(self):
        goAgain=input("Would you like to give one more question(y/n): ")
        return False if goAgain.lower()=='n' else True

    def greeting(self):
        print("Magic ball predicts the future\n")

    def farewell(self):
        print("Goodbye")

if __name__ == '__main__':
    main()