import csv
import sys

a=[]
with open(sys.argv[1]) as csvfile:
  inputcsv = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in inputcsv:
    a.append(row)
    
a=list(map(list, (zip(*a))))
#print(a[1])
a=a[1:len(a)]
print(a)