# input the number of readings
from cnor.py import numberofreadings
nor=numberofreading(eval(input("enter the number of readings: ")))
readings=list()

#read the readings of experiment
for i in range(nor):
    readings.append(eval(input("")))

print("the readings are",readings)

# Inbuit parameters
ductsize=0.015
diaoffin=0.012
diaoforifice=0.015
cod=0.64
ambtemp=30

#calcuations
averagetemp=sum(readings)/nor

tempdifference=average
