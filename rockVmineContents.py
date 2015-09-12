from urllib.request import urlopen
import sys

# read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urlopen(target_url)

# arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
	# split on comma
	row = line.strip().split(b",")
	xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

for col in range(ncol):
	for row in xList:
		try:
			a = float(row[col])
			if isinstance(a, float):
				type[0] += 1
		except ValueError:
			if len(row[col]) > 0:
				type[1] += 1
			else:
				type[2] += 2

	colCounts.append(type)
	type = [0]*3

sys.stdout.write("Col#" + '\t\t' + "Number" + '\t\t' +
		"Strings" + '\t\t' + "Other\n")
iCol = 0
for types in colCounts:
	sys.stdout.write(str(iCol) + '\t\t' + str(types[0]) + '\t\t' +
			str(types[1]) + '\t\t' + str(types[2]) + "\n")
	iCol += 1

