import csv, networkx
import matplotlib.pyplot as plt

g = networkx.MultiDiGraph()
pennapps = {}
mhacks= {}
hackmit= {}
hackny = {}
hackru = {}
hackathons = {"University of Pennsylvania": pennapps, "University of Michigan": mhacks, "New York University": hackny, "Massachusetts Institute of Technology": hackmit, "Rutgers, The State University of New Jersey": hackru}
total = {}

def list_schools():
	return total.keys()

def outdeg(school):
	total = 0
	for data in hackathons.itervalues():
		if school in data:
			total += data[school]
	return total

def indeg(school):
	total = 0
	if school in hackathons:
		for data in hackathons[school]:
			total += hackathons[school][data]
	return total

def max_outdeg():
	return max(total, key = total.get)

def max_indeg():
	attendance = {}
	for hackathon in hackathons:
		attendance[hackathon] = (sum(hackathons[hackathon].itervalues()))
	return max(attendance)

# Import MLH Data from CSV File
with open ("../data/mlh.csv", "rb") as mlhfile:
	mlhreader = csv.reader(mlhfile, quoting=csv.QUOTE_ALL)
	for row in mlhreader:
		if row[1] != "0":
			if row[0] in pennapps:
				pennapps[row[0]] += int(row[1])
			else:
				pennapps[row[0]] = int(row[1])
			if row[0] in total:
				total[row[0]] += int(row[1])
			else:
				total[row[0]] = int(row[1])
		
		if row[2] != "0":
			if row[0] in mhacks:
				mhacks[row[0]] += int(row[2])
			else:
				mhacks[row[0]] = int(row[2])
			if row[0] in total:
				total[row[0]] += int(row[2])
			else:
				total[row[0]] = int(row[2])

		if row[3] != "0":
			if row[0] in hackny:
				hackny[row[0]] += int(row[3])
			else:
				hackny[row[0]] = int(row[3])
			if row[0] in total:
				total[row[0]] += int(row[3])
			else:
				total[row[0]] = int(row[3])

		if row[4] != "0":
			if row[0] in hackmit:
				hackmit[row[0]] += int(row[4])
			else:
				hackmit[row[0]] = int(row[4])
			if row[0] in total:
				total[row[0]] += int(row[4])
			else:
				total[row[0]] = int(row[4])

		if row[5] != "0":
			if row[0] in hackru:
				hackru[row[0]] += int(row[5])
			else:
				hackru[row[0]] = int(row[5])
			if row[0] in total:
				total[row[0]] += int(row[5])
			else:
				total[row[0]] = int(row[5])

# Add all schools to graph
for src_school in hackathons:
	for school in hackathons[src_school]:
		g.add_edge(school, src_school, weight=hackathons[src_school][school])
