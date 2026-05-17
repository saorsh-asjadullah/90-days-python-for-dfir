import re


print("TASK 18.1: The IP Finder (FIRST MATCH)")

log_line = "Failed Password for root from 192.168.1.45 port 22 ssh2"

match = re.search(r"\d+\.\d+\.\d+\.\d+",log_line)

print(f"Attacker IP: {match.group()}")

print(f"Attacker IP: {re.search(r"\d+\.\d+\.+\d+\.+\d+",log_line).group()}") #alternate way

print("\nTASK 18.2 The port extractor (Find All)")
traffic = "Connection on port 443, port 80, port 8080, and port 22"
match = re.findall(r"\d+",traffic)
print(f"The indentified port are {match}")

print("\nTASK 18.3: The Dot Trap (Escaping the Special Charecter")
test1 = "192.168.1.1"
test2 = "192X168Y1Z1"
match1 = re.search(r"192.168.1.1",test1)
match2 = re.search(r"192.168.1.1",test2)
print(match1.group())
print(match2.group())
match3 = re.search(r"192\.168\.1\.1",test1)
match4 = re.search(r"192\.168\.1\.1",test2)
print(match3.group())
if match4 is None: # dont use match4 = "None"
   # print(type (match4)) -- this gives data types as None which means NULL in other language
    print(match4)
else:
    print(match4.group())

print("\nTASK 18.4:The Hash Hunter(Charecter Classes)")
evidence = "Found Hash: 72733B26C5CE51EF924BE3D9FB9336DF in memory dump"
match = re.findall(r"[a-fA-F0-9]{32}",evidence)
print(f"The has found is {match[0]}")

print("\nTASK 18.5: The Extension Filter(Anchors + Loop)")
files = ["malware.exe", "notes.txt", "trojan.exe", "report.pdf", "loader.exe"]
for i in files:
    if re.search(r"\.exe$",i) is not None:
        print(i)

print('\nThe "Muscle Memory" Gauntlet (The Auth Log Analyzer)')

log_data = """Mar 1 10:15:01 server sshd: Failed password for admin from 10.0.0.5 port 22
Mar 1 10:15:03 server sshd: Failed password for root from 192.168.1.100 port 22
Mar 1 10:15:05 server sshd: Accepted password for admin from 10.0.0.5 port 22
Mar 1 10:16:01 server sshd: Failed password for guest from 172.16.0.9 port 2222
Mar 1 10:16:05 server sshd: Failed password for root from 192.168.1.100 port 22"""
denied_count = 0
failed_dict = {}
log_data_list = log_data.split("\n")
match = re.findall(r"\d+\.\d+\.\d+\.\d+",log_data)
print(match)
for i in log_data_list:
    if "Failed" in i:
        match_user = re.search(r"for (\w+) from",i)
        match_ip = re.search(r"\d+\.\d+\.\d+\.\d+",i)
        username = match_user.group(1)
        ip_address = match_ip.group()
        print(f"Failed Login: user = {username} from IP = {ip_address}")
       
        if ip_address in failed_dict:
            failed_dict[ip_address] += 1
        else:
            failed_dict[ip_address] = 1

print("\nFinal Dictionary Result:")
print(failed_dict)


#because of findall the search is looking for all the match of digits in the string  \d matches one digit and dot breakts the series of numbers in continuation so then there is new series of number