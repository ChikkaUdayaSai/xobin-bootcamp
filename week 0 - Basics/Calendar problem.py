'''
As per the Calendar, the new year of the new millennium (Jan1st 2000) began on a saturday. Taking any year  as input , write a program to display which day of the week  shall the new year fall on .

Input

Input an Integer year Y such that 1800<Y<2400

Output

Display the day of the week on new year(1st Jan) in lowercase

Sample:

Input:

2001

Output:

monday
'''

import datetime

y = int(raw_input())

day = datetime.date(y,01,01)

print day.strftime("%A").lower()
