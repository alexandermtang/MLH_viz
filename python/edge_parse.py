import csv

pennapps = {}
mhacks= {}
hackmit= {}
hackny = {}
hackru = {}
hackathons = {"University of Pennsylvania": pennapps, "University of Michigan": mhacks, "New York University": hackny, "Massachusetts Institute of Technology": hackmit, "Rutgers, The State University of New Jersey": hackru}
total = {}


subgraphs = [pennapps, mhacks, hackmit, hackny, hackru]

def write_csv(outfile, src_school, data):
	with open(outfile, "wb") as csvfile:
		csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
		for key in data.keys():
			if src_school not in [key]:
				csvwriter.writerow([key, src_school])

def list_schools():
	return total.keys()

def outdeg(school):
	total = 0
	for data in subgraphs:
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

'''
write_csv("pennapps.csv", "University of Pennsylvania", pennapps)
write_csv("mhacks.csv", "University of Michigan", mhacks)
write_csv("hackny.csv", "New York University", hackny)
write_csv("hackmit.csv", "Massachusetts Institute of Technology", hackmit)
write_csv("hackru.csv", "Rutgers, The State University of New Jersey", hackru)
'''

'''
Highest indeg, highest outdeg
Strongly connected components
'''
if __name__ == "__main__":
	#print total
	print outdeg("Massachusetts Institute of Technology")
	print indeg("Massachusetts Institute of Technology")
	print max_outdeg()
	print max_indeg()
	print list_schools()
