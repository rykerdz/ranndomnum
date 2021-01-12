import datetime
from time import sleep
l=[]
tym=[]

n=int(raw_input("Enter the no. of numbers to be generated: "))

for i in range (n):
    time=datetime.datetime.now()
    t=time.microsecond

    l.append(t)
    sleep(0.037)

for i in (l):
    tym.append(i/10000)

print tym
