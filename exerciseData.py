from exerciseList import *
from collections import namedtuple
Exercise = namedtuple('Exercise', 'name sets')
FullExercise = namedtuple('FullExercise', 'name sets')
Exercise = namedtuple('Exercise', 'name sets')
SetsT = namedtuple('Sets', 'weight sets reps amrap')#, defaults=(None,))
def Sets(weight, sets, reps, amrap=None):
	return SetsT(weight, sets, reps, amrap)



# each Workout has a dictionary containing the values
# check out the warmups via those keys

A1 = [ Exercise(bench, Sets(1, 4, 4)), Exercise(squat, Sets(1, 4, 8)), Exercise(overhead, Sets(1, 4, 8)), Exercise(chins, Sets(1, 4, 8))]
A2 = [ Exercise(bench, Sets(.9, 4, 8)), Exercise(deadlift, Sets(1, 4, 4)), Exercise(overhead, Sets(1, 4, 4)), Exercise(rows, Sets(.9, 4, 8))]
A3 = [ Exercise(bench, Sets(1, 3, 4, True)), Exercise(squat, Sets(1, 3, 4, True)), Exercise(overhead, Sets(.9, 4, 8)), Exercise(chins, Sets(1, 4, 4))]

B1 = [ Exercise(bench, Sets(.9, 4, 8)), Exercise(deadlift, Sets(.9, 4, 8)), Exercise(overhead, Sets(1, 4, 4)), Exercise(rows, Sets(1, 4, 4))]
B2 = [ Exercise(bench, Sets(1, 4, 4)), Exercise(squat, Sets(.9, 4, 8)), Exercise(overhead, Sets(.9, 4, 8)), Exercise(chins, Sets(1, 4, 8))]
B3 = [ Exercise(bench, Sets(.9, 4, 8)), Exercise(deadlift, Sets(1, 3, 4, True)), Exercise(overhead, Sets(1, 3, 4, True)), Exercise(rows, Sets(.9, 4, 8))]


workouts = {'A1' : A1, 'A2' : A2, 'A3' : A3, 'B1' : B1, 'B2' : B2, 'B3' : B3}
weekWorkouts = {'A' : [A1, A2, A3], 'B' : [B1, B2, B3]}
rowsWarmup = [Sets(.4, 2, 5), Sets(.7, 1, 3), Sets(.9, 1, 2)]
overheadWarmup = [Sets(0, 2, 5), Sets(.55, 1, 5), Sets(.7, 1, 3), Sets(.85, 1, 2)]
benchWarmup = [Sets(0, 2, 5), Sets(.5, 1, 5), Sets(.7, 1, 3), Sets(.9, 1, 2)]
deadliftWarmup = [Sets(.4, 2, 5), Sets(.6, 1, 3), Sets(.85, 1, 2)]
squatWarmup = [Sets(0, 2, 5), Sets(.4, 1, 5), Sets(0.6, 1, 3), Sets(0.8, 1, 2)]

warmups = { bench : benchWarmup, squat : squatWarmup, overhead : overheadWarmup, chins : [] , deadlift : deadliftWarmup, rows : rowsWarmup }