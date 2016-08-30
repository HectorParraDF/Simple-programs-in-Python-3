import random

#Set up the lists
data  = []
histo = []
    for a in range(21):
        histo.append(0)
        (a)

#Counter variable for the progress percentage as the program
#takes a while to load.
prog    = 0

#Generates pseudo-random data entries. If real data is to be used, them we just
#have to modify this part of the script.
for i in range(10000):
    data.append(random.randrange(21))
(i)

#Checks for each value in all the entries of the data list and adds
#them accordingly to the histo list.
for j in range(21):
    for k in range(len(data)):
        if j in data:
            histo[j] += 1
            data.remove(j)  #This speeds up the program
            prog += 1
        (k)
    print(prog*100/10000, "%")  #Progress percentage
    (j)

#Prints the histogram itself
for l in range(21):
    print("{0:3}{1:3}{2:4}{3:65}".format(l," : ",histo[l],"*"*int(histo[l]/max(histo)*60)))
    (l)
