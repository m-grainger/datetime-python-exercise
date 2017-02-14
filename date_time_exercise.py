

import datetime
from datetime import timedelta

pdx_t = datetime.datetime.now()
nyc_t = pdx_t + datetime.timedelta(hours = 3)
lon_t = pdx_t + datetime.timedelta(hours = 8)

def open_or_closed(x):
    if(x.hour >= 9 and x.hour <=  21):
        return('OPEN.')
    else:
        return ('CLOSED.')
        
print('Hello! the New York City branch is: {}'.format(open_or_closed(nyc_t))) 

print('The London branch is: {}'.format(open_or_closed(lon_t)))

