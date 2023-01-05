from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y")
tm_string=now.strftime("%H:%M:%S")
print("date: ", dt_string)
print("time: ",tm_string)
