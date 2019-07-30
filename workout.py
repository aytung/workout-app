
from functions import *
from exerciseData import *
from personalData import *
from email_functions import *
from exerciseList import *
from email_functions import *
import os


import sys
import subprocess
from functools import reduce 		

curWeek, weekSets = findWeekSets()

from exerciseData import warmups
# make a function for each workout

with open('tempFile.md', 'w') as writefile:

	writeline = lambda line : writefile.write(line + '\n')
	
	for setNum, weekSet in enumerate(weekSets, 1):


		program = getProgram(weekSet)

		writeline("## " + curWeek + str(setNum))
		writeline(reduce(lambda x, y : x + "|" + y.name, program, "") + "|")

		writeline("|" + ":---:|" * len(program))

		longestExerciseLen = max([len(exercise.sets) for exercise in program])
		 
		for index in range(0, longestExerciseLen):
			exerciseList = []
			for exercise in program:
		  		if index < len(exercise.sets):
		  			exerciseList.append(formatSet(exercise.sets[index]))
		  		else:
		  			exerciseList.append('')

			writeline('|' + '|'.join(exerciseList) + '|')

		writeline('')

writefile.close()			
subprocess.call('pandoc -s -o weeklyworkout.pdf tempFile.md'.split(' '))

fileencoding = sys.getfilesystemencoding()

user_email_password=os.environ["user_email_password"]
user_email=os.environ["user_email"]
user_name = os.environ["user_name"]

emailFile(user_name, user_email, user_email_password, "weeklyworkout.pdf", "Weekly Workout")

subprocess.call('rm tempFile.md weeklyworkout.pdf'.split(' '))
