#!/usr/bin/env python3
# coding: utf-8

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

states = list(capitals.keys())

for num in range(35):
    # shuffle the order of states
    random.shuffle(states)

    with open('quiz_text%s.txt' % (num + 1), 'w') as quizFile, open('quiz_ans_text%s' % (num + 1), 'w') as answerKeyFile:
        quizFile.write('name:\n\ndate:\n\nperiod:\n\n')
        quizFile.write(' ' * 20 + 'State Capitals Quiz (Form %s)' % (num + 1))
        quizFile.write('\n\n')

        # get right and wrong answers.abs
        for questionNum in range(50):
            correctAns = capitals[states[questionNum]]
            wrongAns = list(capitals.values())
            del wrongAns[wrongAns.index(correctAns)]
            wrongAns = random.sample(wrongAns, 3)
            answerOptions = wrongAns + [correctAns]
            random.shuffle(answerOptions)

            quizFile.write('%s. What is the callable of %s\n' %
                           (questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write('%s. %s\n' % ('ABCD'[i], answerOptions[i]))
                

            quizFile.write('\n')

            # write answer Key
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAns)]))
            