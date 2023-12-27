import csv
import sys
import matplotlib.pyplot as plt

# read csv file(sys.argv[1])
a=[]
with open(sys.argv[1]) as csvfile:
  inputcsv=csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in inputcsv:
    a.append(row)

# transpose matrix and remove the first row   
a=list(map(list,(zip(*a))))
a=a[1:len(a)-1]

# plot data
lines=[]
x=range(0,len(a[1]))
plt.clf()
plt.ylim(-10,30)
for i in range(1,len(a)-1):
  lin,=plt.plot(x,a[i],label="L"+str(i))
  lines.append(lin)
plt.legend(handles=lines)
plt.show()
