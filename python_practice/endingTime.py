# This program takes two lines of input. 
# The first line is a "starting time" expressed in a 24-hour clock with leading zeroes
# like 08:30 or 14:07. The second line is a duration D in minutes
# Print out what time it will be D minutes after the starting time.
time = input()
duration = input()
hour = int(time[0:2])
minutes = int(time[3:5])
totalMinutes = (minutes + int(duration))
newMinutes = totalMinutes % 60
newHour = hour + totalMinutes//60


if newMinutes >=10:
   if newHour < 10:
       print('0' + str(newHour) +':' + str(newMinutes))
   if newHour >=10 and newHour < 24:
       print(str(newHour) +':' + str(newMinutes))
   if newHour >= 24:
      if newHour % 24 < 10:
          print('0' + str(newHour % 24) +':' + str(newMinutes))
      if  newHour - 24 >= 10 and newHour - 24 < 24:
         print(str(newHour % 24) +':' + str(newMinutes))
if newMinutes < 10:
   if newHour < 10:
       print('0' + str(newHour) +':' + '0'+ str(newMinutes))
   if newHour >=10 and newHour < 24:
       print(str(newHour) +':' + '0' +str(newMinutes))
   if newHour >= 24:
      if newHour % 24 < 10:
          print('0' + str(newHour % 24) +':' + '0'+ str(newMinutes))
      if  newHour - 24 >= 10 and newHour - 24 < 24:
         print(str(newHour % 24) +':' + '0'+ str(newMinutes))
