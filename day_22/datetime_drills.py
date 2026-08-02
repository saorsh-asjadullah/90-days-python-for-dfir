from datetime import datetime
from datetime import timedelta

#Task 22.1 Parse a Timestamp

print("Task 22.1 Pare a Timestamp\n")

log_time = "2024-06-15 09:22:41"

dt = datetime.strptime(log_time, "%Y-%m-%d %H:%M:%S")
print(dt)
print(type(dt))

#Task 22.2: Format a TimeStamp

print("\n Task 22.2 Format a timestamp\n")
formated_time_1 = dt.strftime("%d/%m/%Y")
formated_time_2 = dt.strftime("%H:%M:%S")
# %A: The full weekday name (e.g., Sunday, Monday).
# %B: The full month name (e.g., January, August).
# %C: The century as a two-digit decimal number (e.g., 20 for the year 2026).
# %D: An alias for the complete short date format shortcut %m/%d/%y (e.g., 08/02/26).
formated_time_3 = dt.strftime("%A,%B,%C,%D")


print(f"The format1 is {formated_time_1}")
print(f"The format2 is {formated_time_2}")
print(f"The format3 is {formated_time_3}")

#Task 22.3: Time Math with timedelta
print("\nTask 22.3: Time Math with timedelta\n")

parsed_time = dt
later_time = parsed_time + timedelta(minutes= 30)
earlier_time = parsed_time - timedelta(hours= 2)

print(f"The earlier time is {earlier_time} and later time is {later_time}")

#Task 22.4: The Duration Between Two Events
print("\nTask 22.4: The Duration Between Two Events\n")

start = "2024-06-15 09:22:41" 
end = "2024-06-15 09:47:13"
start_time = datetime.strptime(start,"%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime(end,"%Y-%m-%d %H:%M:%S")

timedelta_1 = end_time - start_time
print(timedelta_1)
total_second = timedelta_1.total_seconds()
print(f"The total seconds elapsed is {total_second}")

#Task 22.5: Parse a Different Format (Apache Style)
print("\n Task 22.5: Parse a Different Format (Apache Style) \n")
apache_format = parsed_time.strftime("%d/%b/%Y:%H:%M:%S")
print(f"Time in apache format is {apache_format}")
ISO_format = parsed_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Time in ISO format is {ISO_format}")

#The "Muscle Memory" Gauntlet (The Timeline Sorter)
print("\nThe \"Muscle Memory\" Gauntlet (The Timeline Sorter)\n")
events = [
    ("2024-06-15 09:47:13", "User admin logged in"),
    ("2024-06-15 09:22:41", "Failed login from 10.0.0.5"),
    ("2024-06-15 10:15:02", "File deleted: payroll.xlsx"),
    ("2024-06-15 09:23:05", "Failed login from 10.0.0.5"),
    ("2024-06-15 09:48:30", "Privilege escalation detected")
]

print(events)

# A list containing nested tuples (each tuple has 3 elements)
#data_list = [("Apple", 1.20, 10), ("Banana", 0.50, 24), ("Cherry", 2.50, 15)]

# Unpack the tuple elements directly in the loop
#for item_name, price, stock in data_list:
    #print(f"Item: {item_name} | Total Value: ${price * stock}")

temp_list = []
for time, message in events:
    event_time = datetime.strptime(time,"%Y-%m-%d %H:%M:%S")
    temp_list.append((event_time,message))

sorted_list = sorted(temp_list,key=lambda x: x[0]) # sorted() loops through temp_list, extracts index 0 (the datetime), and uses it to sort earliest to latest.

for time,message in sorted_list:
    formated_time = datetime.strftime(time,"%d/%b/%Y:%H:%M:%S")
    print(f"{message} at {formated_time}")

window_start = datetime.strptime("2024-06-15 09:22:00","%Y-%m-%d %H:%M:%S")
window_end = datetime.strptime("2024-06-15 09:30:00", "%Y-%m-%d %H:%M:%S")

print(f"\nBetween start {window_start} and end time {window_end}\n")
for time,message in sorted_list:
        if window_start <= time and time <= window_end :
             formated_time = datetime.strftime(time,"%d/%b/%Y:%H:%M:%S")
        
             print(f"{message} at {formated_time}")


