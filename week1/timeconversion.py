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
