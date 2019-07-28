
from collections import namedtuple

Exercise = namedtuple('Exercise', 'name sets')
FullExercise = namedtuple('FullExercise', 'name sets')
Exercise = namedtuple('Exercise', 'name sets')
Sets = namedtuple('Sets', 'weight sets reps amrap', defaults=(None,))
bench = 'Bench Press'
squat = 'Squat'
overhead = 'Overhead Press'
chins = 'Chinups'
deadlift = 'Deadlift'
rows = 'Barbell Rows'

workingWeights = { bench : 180, squat : 135, overhead : 90, deadlift : 110, chins : None, rows : 90}
# each Workout has a dictionary containing the values
# check out the warmups via those keys

A1 = [ Exercise(bench, Sets(1, 4, 4)), Exercise(squat, Sets(1, 4, 8)), Exercise(overhead, Sets(1, 4, 8)), Exercise(chins, Sets(1, 4, 8))]
A2 = [ Exercise(bench, Sets(.9, 4, 8)), Exercise(deadlift, Sets(1, 4, 4)), Exercise(overhead, Sets(1, 4, 4)), Exercise(rows, Sets(.9, 4, 8))]
A3 = [ Exercise(bench, Sets(1, 3, 4, True)), Exercise(squat, Sets(1, 3, 4, True)), Exercise(overhead, Sets(.9, 3, 8)), Exercise(chins, Sets(1, 4, 4))]

B1 = [ Exercise(bench, Sets(.9, 4, 8)), Exercise(deadlift, Sets(.9, 4, 8)), Exercise(overhead, Sets(1, 4, 4)), Exercise(rows, Sets(1, 4, 4))]
B2 = [ Exercise(bench, Sets(1, 4, 4)), Exercise(squat, Sets(.9, 4, 8)), Exercise(overhead, Sets(.9, 4, 8)), Exercise(chins, Sets(1, 4, 8))]
B3 = [ Exercise(bench, Sets(.9, 4, 8)), Exercise(deadlift, Sets(1, 3, 4, True)), Exercise(overhead, Sets(1, 3, 4, True)), Exercise(rows, Sets(.9, 4, 8))]


workouts = {'A1' : A1, 'A2' : A2, 'A3' : A3, 'B1' : B1, 'B2' : B2, 'B3' : B3}
rowsWarmup = [Sets(.4, 2, 5), Sets(.7, 1, 3), Sets(.9, 1, 2)]
overheadWarmup = [Sets(0, 2, 5), Sets(.55, 1, 5), Sets(.7, 1, 3), Sets(.85, 1, 2)]
benchWarmup = [Sets(0, 2, 5), Sets(.5, 1, 5), Sets(.7, 1, 3), Sets(.9, 1, 2)]
deadliftWarmup = [Sets(.4, 2, 5), Sets(.6, 1, 3), Sets(.85, 1, 2)]
squatWarmup = [Sets(0, 2, 5), Sets(.4, 1, 5), Sets(0.6, 1, 3), Sets(0.8, 1, 2)]

warmups = { bench : benchWarmup, squat : squatWarmup, overhead : overheadWarmup, chins : [] , deadlift : deadliftWarmup, rows : rowsWarmup }
currentWorkout = None 
while not currentWorkout:
	choice = input("Please enter your workout")
	if choice in workouts:
		currentWorkout = workouts[choice]

# TODO: calculate weight
def calculateWeight(exerciseName, currentWeight, multiplier):
	minWeight = 45
	if exerciseName == deadlift:
		minWeight = 55


	currentWeight = ((currentWeight * multiplier) // 5) * 5
	if currentWeight < minWeight:
		currentWeight = minWeight

	return int(currentWeight)




# TODO, convert weights
def convertWeights(exerciseName, sets, workingWeight):
	if exerciseName == chins:
		return 

	for index, curSet in enumerate(sets):
		sets[index] = sets[index]._replace(weight = calculateWeight(exerciseName, workingWeight, curSet.weight))
		print(curSet.weight)

	return sets


program = []

for exercise in currentWorkout:
	# iterate over each, and create list consisting of the name
	# the weights, and the sets
	warmup = warmups[exercise.name]
	finalSet = exercise.sets

	# edge cases:
	# deadlift starts at 55
	# chinups have no weight involved
	fullExercise = FullExercise(exercise.name, convertWeights(exercise.name, warmup + [finalSet], workingWeights[exercise.name]))
	program.append(FullExercise(exercise.name, fullExercise))

# TODO: when the starting weights get weird, start forcing float(-inf)
# so that weights start at bar/stop hard-coding the weights?

# have a simple switch statement that output the correct file, and both writes it to a txt file
# and emails it to the kindle

# pseudocode
# hard code weights
# then, for each of those weights, output the workouts
# to a .txt file so that the values can be printed out
import pdb; pdb.set_trace()









