import csv, mlh_graph

def write_csv(outfile, src_school, data):
	with open(outfile, "wb") as csvfile:
		csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
		for key in data.keys():
			if src_school not in [key]:
				csvwriter.writerow([key, src_school, data[key]])

write_csv(os.path.join("..", "data", "pennapps.csv"), "University of Pennsylvania", mlh_graph.pennapps)
write_csv(os.path.join("..", "data", "mhacks.csv"), "University of Michigan", mlh_graph.mhacks)
write_csv(os.path.join("..", "data", "hackny.csv"), "New York University", mlh_graph.hackny)
write_csv(os.path.join("..", "data", "hackmit.csv"), "Massachusetts Institute of Technology", mlh_graph.hackmit)
write_csv(os.path.join("..", "data", "hackru.csv"), "Rutgers, The State University of New Jersey", mlh_graph.hackru)
