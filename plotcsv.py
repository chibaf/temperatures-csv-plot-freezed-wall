import csv
import sys
import matplotlib.pyplot as plt

a=[]
with open(sys.argv[1]) as csvfile:
  inputcsv=csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in inputcsv:
    a.append(row)
    
a=list(map(list,(zip(*a))))
a=a[1:len(a)-1]

x=range(0,len(a[1]))
plt.clf()
plt.ylim(-10,30)
for i in range(1,len(a)-1):
  plt.plot(x,a[i])
plt.show()
