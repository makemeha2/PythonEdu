import sys
import simpleset

#sys.path.append()
print(sys.path)


setA = [1,3,7,10,13]
setB = [2,3,4,9,13]

#print(simpleset.intersect(setA, setB))
#print(simpleset.union(setA, setB))
#print(simpleset.difference(setA, setB))
print(simpleset.__intersectSC(setA, setB))
#print(dir(simpleset))