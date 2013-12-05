import mlh_graph, sys

for school in mlh_graph.schools():
	print school + " : " + str(mlh_graph.total[school])
print "Total schools: " + str(len(mlh_graph.schools()))

sys.stdin.read(1)
print
print
print

max = mlh_graph.max_outdeg()
print "Maximum degree: " + max + " : " + str(mlh_graph.total[max])
print "Average degree: " + str(mlh_graph.avg_deg())

sys.stdin.read(1)

import draw_cliques
