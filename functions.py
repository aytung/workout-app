from exerciseList import *
from personalData import workingWeights
from exerciseData import FullExercise
from exerciseData import warmups




def getProgram(weekSet):
	program = []
	for exercise in weekSet:
		# iterate over each, and create list consisting of the name
		# the weights, and the sets
		warmup = warmups[exercise.name]
		finalSet = exercise.sets
		# edge cases:
		# deadlift starts at 55
		# chinups have no weight involved
		fullExercise = FullExercise(exercise.name, convertWeights(exercise.name, warmup + [finalSet]))
		program.append(fullExercise)
	return program
def calculateWeight(exerciseName, currentWeight, multiplier):
	minWeight = 45
	if exerciseName == deadlift:
		minWeight = 55


	currentWeight = ((currentWeight * multiplier) // 5) * 5
	if currentWeight < minWeight:
		currentWeight = minWeight

	return int(currentWeight)


def findWeekSets():
	weekSets = None
	curWeek = None 
	from exerciseData import weekWorkouts 
	while not weekSets:
		curWeek = input("Please enter your workout")
		if curWeek in weekWorkouts.keys():
			return curWeek, weekWorkouts[curWeek]


# TODO, convert weights
def convertWeights(exerciseName, sets):
	workingWeight = sets[-1].weight * workingWeights[exerciseName]
	sets[-1] = sets[-1]._replace(weight = 1)

	if exerciseName == chins:
		return [sets[0]._replace(weight=" ")]

	for index, curSet in enumerate(sets):
		sets[index] = sets[index]._replace(weight = calculateWeight(exerciseName, workingWeight, curSet.weight))

	return sets


def formatSet(curSet):
	return (' ' * (3 - len(str(curSet.weight)))   + str(curSet.weight) + " " + str(curSet.sets) + "x" + str(curSet.reps) + (" + AMRAP" if curSet.amrap else ""))
