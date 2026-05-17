import re
#Task 19.1: Single Group Extraction

event = "User johndoe logged in successfully"
match_pattern = re.search(r"User (\w+) logged in",event)
print(match_pattern.group(0))
print(match_pattern.group(1))

#Task 19.2: Multiple Group Extraction

connection = "Connection from 192.168.1.50 to 45.33.22.11 on port 443"
match_three = re.search(r"from (\d+\.\d+\.\d+\.\d+) to (\d+\.\d+\.\d+\.\d+) on port (\d+)",connection)
print(match_three.group(1))
print(match_three.group(2))
print(match_three.group(3))
src,dst,port = match_three.groups()
print(f"Source: {src} -> Dest: {dst} on port {port}")

#Task 19.3: findall with Groups
log_data = """Mar 1 10:15:01 server sshd: Failed password for admin from 10.0.0.5 port 22
Mar 1 10:15:03 server sshd: Failed password for root from 192.168.1.100 port 22
Mar 1 10:15:05 server sshd: Accepted password for admin from 10.0.0.5 port 22
Mar 1 10:16:01 server sshd: Failed password for guest from 172.16.0.9 port 2222
Mar 1 10:16:05 server sshd: Failed password for root from 192.168.1.100 port 22"""

match_findall = re.findall(r"for (\w+) from (\d+\.\d+\.\d+\.\d+)",log_data)
print(match_findall)
for username,ip in match_findall:
    print(username,ip)

#Task 19.4: Named Groups (Cleaner Code)

match_group = re.search(r"from (?P<src>\d+\.\d+\.\d+\.\d+) to (?P<dst>\d+\.\d+\.\d+\.\d+) on port (?P<port>\d+)",connection)
print(match_group.group("src"))
print(match_group.group("dst"))
print(match_group.group("port"))
print(match_group.groupdict())


#Task Drill 19.5: re.match vs re.search

valid = "ERROR: Authentication failed"
invalid = "INFO: ERROR message in body"

check1 = re.match(r"ERROR", valid) #This one matches
check2 = re.match(r"ERROR", invalid)

print(check1.group(),check2)

check3 = re.search(r"ERROR", valid) #both Match
check4 = re.search(r"ERROR", invalid) #both match 

#use match when i have to check  checks the beginning of the string use search when i have to search throughout 


#Task: The "Muscle Memory" Gauntlet (The Apache Log Parser)

log_data = """192.168.1.10 - - [10/Oct/2024:13:55:36] "GET /index.html HTTP/1.1" 200 2326
10.0.0.5 - - [10/Oct/2024:13:55:38] "POST /admin/login.php HTTP/1.1" 401 532
172.16.0.1 - - [10/Oct/2024:13:55:40] "GET /images/logo.png HTTP/1.1" 200 5032
192.168.1.10 - - [10/Oct/2024:13:56:01] "GET /about.html HTTP/1.1" 200 4123
10.0.0.5 - - [10/Oct/2024:13:56:10] "POST /admin/dashboard HTTP/1.1" 403 211
45.33.22.11 - - [10/Oct/2024:13:56:30] "GET /etc/passwd HTTP/1.1" 404 156"""


status_dict ={}


regmatch = re.findall(r"(?P<ip>\d+\.\d+\.\d+\.\d+) .*\"(?P<method>\w+) (?P<path>\S+) HTTP.*\" (?P<status>\d{3})",log_data)
for ip,method,path,status in regmatch:
    print (f"[{status}] {method} {path} from {ip}")
    if status in status_dict:
        status_dict[status] += 1
    else:
        status_dict[status] = 1


print("\nstatus code summary:")
print(status_dict)

