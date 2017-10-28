import itertools
import csv
import numpy as np
from math import sqrt
from operator import itemgetter

# Calculating Standard Deviation
def standard_deviation(data):
  differences=[]
  for i in range(1,row+1):
    if data[i] is not ' ':
      differences.append(int(data[i])-average[i])
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd /count[i]
    sd = sqrt(variance)
  return sd

# Taking wells data
data = [] 
maReader = csv.reader(open('../static/analytics/wells2.csv', 'rt'), delimiter=',', quotechar='"')
for rindex, row in enumerate(maReader):
  for iindex, item in enumerate(row):
    try:
      data[iindex].append(item)
    except IndexError:
      data.append([item])
print (data)
spare1=[]
spare1 =np.transpose(data)

print ('Number of Wells ',iindex)
print ("xxxxxxxxxxxxxxxxxxx")
#finding average
row=rindex
col=iindex
average=[]
count=[]  
for i in range(0,col+1):
  average.append(0)
  count.append(0)
for i in range(1,col+1):
  for j in range(1,row+1):
    if data[i][j] is ' ':
      continue
    average[i]=average[i]+int(data[i][j])
    count[i]+=1
  average[i]=average[i]/count[i]

sta_dev=[]
for data_record in data[1: ]:
  #print data_record
  sta_dev.append(standard_deviation(data_record))

#Initializing based on standard deviation values
for i in range(1,col+1):
  for j in range(1,row+1):
    if data[i][j] is ' ':
      data[i][j]=0
    elif int(data[i][j]) >= sta_dev[i-1]:
      data[i][j]=1
    else:
      data[i][j]=-1

data=data[1:]
for i in range(0,col):
  data[i]=data[i][1:]
#print data


matrix=np.transpose(data)
print(matrix)
print ("xxxxxxxxxxxxxxxxxxx")
# Finding correlation
numberofrows = len(matrix)
numberofcolumn = len(matrix[0])
diffrencelist = np.zeros((numberofcolumn,numberofcolumn))
for columns in range (0,numberofcolumn-1):
  for i in range (columns+1,numberofcolumn):
    for rows in range (0,numberofrows):
      if (matrix[rows][columns] != matrix[rows][i]) and (matrix[rows][columns]!=0) and (matrix[rows][i]!=0) :
        diffrencelist[i][columns] = diffrencelist[i][columns] + 1
        diffrencelist[columns][i] = diffrencelist[i][columns]
        diffrencelist=diffrencelist.astype(int)
print (diffrencelist) 
print ("xxxxxxxxxxxxxxxxxxx")
#Finding not at all related cluster pairs
worlist=[]
for i in range(0,numberofcolumn):
  for j in range(i+1,numberofcolumn):
    if (diffrencelist[i][j]==0):
      worlist.append((i,j))
#print worlist
#print  "xxxxxxxxxxxxxxxxxxx"
worlilen=len(worlist)
bestlist=[]
for i in range(0,numberofcolumn):
  for j in range(i+1,numberofcolumn):
    if (np.max(diffrencelist[i])==diffrencelist[i][j]):
      bestlist.append((i,j,diffrencelist[i][j]))
#print bestlist
bestlilen=len(bestlist)

fulllist=[]
for i in range(0,numberofcolumn):
  for j in range(i+1,numberofcolumn):
    fulllist.append((i,j,diffrencelist[i][j]))
    fulllist=sorted(fulllist,key=lambda x: x[2])
#print fulllist

a =np.max(diffrencelist)
b=np.min(diffrencelist)
c=np.unique(diffrencelist)
d=len(c)

newlis=[]
for i in range(0,d):
  temp=[]
  newlis.append(temp)

for i in range(0,d):
  for j in range(0,numberofcolumn):
    for k in range(j+1,numberofcolumn):
      if (diffrencelist[j][k]==c[i]):
        newlis[i].append((j,k))
#print newlis[i] 
#print "yyyyyyy"
#Finding Clusters
cluslis=[]
stupidlis=[]
for i in range(0,10000):
  tempy=[]
  cluslis.append(tempy)

for k in range(d-1,0,-1):
  for x in newlis[k]:
      cluslis[k].append(x[0]+1)
      cluslis[k].append(x[1]+1)
# print cluslis[k] 

for k in range(d-1,0,-1):
  cluslis[k]=np.unique(cluslis[k])
#print cluslis[k]

for k in range(d,0,-1):
  for j in range(d-1,k,-1):
    cluslis[k]= [x for x in cluslis[k] if x not in cluslis[j]]



clusterlist1=[]
for i in range(0,10000):
  tempy2=[]
  clusterlist1.append(tempy2)
clusterlist=[]
for i in range(0,10000):
  tempy1=[]
  clusterlist.append(tempy1)
  count1=0
print ("Clusters :")
for x in range(0,10000):
  if cluslis[x] != []:
    clusterlist[x]=cluslis[x]
    count1+=1
    clusterlist1[count1]=clusterlist[x]

p=[]
h=[]
for x in range(0,10000):
  for a in clusterlist[x]:
    p.append(a)
p=np.sort(p)
spare2=[]
spare2=np.array(spare1[0])
index=[0]
spare2=np.delete(spare2,index)
spare2=spare2.astype(np.int)
nn=[]
store_list = []
nn = [x for x in spare2 if x not in p]
k=len(nn)
templist = []
for i in range(1,k+1):
   if i==0:
     pass
   templist=nn[i-1:i]
   clusterlist1[count1+i]=templist
for i in range(1,count1+1+k):
 print (clusterlist1[i],i)
print ('Number of Clusters: ',count1+k)

# Reading lon lat
latlon=[]
maReader = csv.reader(open('../static/analytics/latlon.csv', 'rt'), delimiter=',',quotechar='"')
for rindex, row in enumerate(maReader):
  for iindex, item in enumerate(row):
    try:
      latlon[iindex].append(item)
    except IndexError:
      latlon.append([item])
#print latlon
pare=[]
pare =np.transpose(latlon)
#appending clusterid and wellid
clulis=[]
for j in range(1,rindex+2):
  tem=[]
  clulis.append(tem)
for j in range(1,rindex+1):
  for i in range(1,k+1+count1):
    if int(pare[j][0]) in clusterlist1[i]:
      clulis[j].append([pare[j][0],i])

clulis12=[]
for i in range(1,rindex+2):
  tem12=[]
  clulis12.append(tem12)

for j in range(1,rindex+1):
 clulis12[j]=clulis[j][0]
 print (clulis12[j])

with open('../static/analytics/latlon.csv') as fpi, open('../static/analytics/out.csv', 'w') as fpo:
    reader = csv.reader(fpi)
    writer = csv.writer(fpo)

    #optionaly handle csv header
    headers = next(reader)
    headers.append('cluster')
    writer.writerow(headers)

    for index, row in enumerate(reader):
      row.append(clulis12[index+1][1])
      writer.writerow(row)