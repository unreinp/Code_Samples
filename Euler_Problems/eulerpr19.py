int year = 1900
int weekday = 1
int month = 1
int day = 1
int counter = 0
list thirty = [9,4, 6, 11]
list thirtyone = [1,3,5,7,8,10,12]
int feb = 2
def hardCount():
    while(True):
	# end of year
	if year == 2001:
	    return
	#first of month check
	elif weekday == 1:
	    counter +=1
	else:
	    counter == counter
        #check change in weekday
	if month in thirty:
	    weekday += 30%7
	elif month in thirtyone:
	    weekday += 31%7
	elif month == feb:
	    if year%400 ==0:
                weekday += 29 %7
            elif year%4 == 0:
                weekday += 29 %7
            else:
                weekday += 28%7
        if month == 13:
            month = 1
            year += 1
hardCount()
print(counter)
print(year)
print(weekday)
