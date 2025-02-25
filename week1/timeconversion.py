#Question

#Given a time in -hour AM/PM format, convert it to military (24-hour) time.

#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#Example

#12:01:00PM.
#Return '12:01:00'

#12:01:00AM.
#Return '00:01:00'.

#Function Description

#Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

#timeConversion has the following parameter(s):

#string s: a time in  hour format
#Returns

#string: the time in  hour format

#Answer

def timeConversion(s):
    period = s[-2:]
    time = s[:-2]
    hours, minutes, seconds = map(int, time.split(':'))
  
    if period == 'AM':
        if hours == 12:
            hours = 0  
    else:  
        if hours != 12:
            hours += 12  
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

input_time = input( )
output_time = timeConversion(input_time)
print( output_time)
