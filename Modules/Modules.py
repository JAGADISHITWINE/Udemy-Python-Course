## Random module
import random as re

result  = re.randint(1,10)
print(result)

## Datetime module
from datetime import date,datetime
today_date = date.today()
print(today_date)
current_time = datetime.now().strftime('%H:%M:%S')
print(current_time)