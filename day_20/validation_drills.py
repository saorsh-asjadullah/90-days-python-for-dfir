import re
import json

#Task 20.1: IP Address Validator
mixed_list = ["192.168.1.1", "10.0.0", "not.an.ip.address", "172.16.8.8", "999.999.999.999"]
reg_ip = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$" # Note: the pattern \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} will accept 999.999.999.999 because each octet just needs to be 1-3 digits. This is a known limitation
for i in mixed_list:
    match_ip = re.search(reg_ip,i)
    if match_ip is not None:       
        print(match_ip.group())


#Task 20.2: Hash Type Detector

mixed_hash_strings = ["5d41402abc4b2a76b9719d911017c592","aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","not_a_hash","5d41402abc4b2a76b9719d911017c59"]

MD5_pattern = re.compile(r"^[a-fA-F0-9]{32}$")
SHA1_pattern = re.compile(r"^[a-fA-F0-9]{40}$")
SHA256_pattern = re.compile(r"^[a-fA-F0-9]{64}$")

for i in mixed_hash_strings:
    if MD5_pattern.fullmatch(i):
        print(f"This hash '{i}' is MD5")
    elif SHA1_pattern.fullmatch(i):
        print(f"This hash '{i}' is SHA1")
    elif SHA256_pattern.fullmatch(i):
        print(f"This hash '{i}' is SHA256")
    else:
        print(f"This '{i}' is of unkown format")

#Task 20.3: Method + Status Validator (Alternation)

method_list = ["GET", "POST", "DELETE", "TRACE", "HACK", "PUT"]
allowed_method = re.compile(r"GET|POST|PUT")
for method in method_list:
    if allowed_method.fullmatch(method):
        print(f"This method '{method}' is allowed")
    else:
        print(f"This method '{method}' is blocked")

#Task 20.4: Pre-Compiled Pattern

mixed_ip_list = [
    "192.168.1.45", "10.0.12.3", "172.16.254.1", "8.8.8.8", "1.1.1.1",
    "200.100.50.25", "127.0.0.1", "224.0.0.1", "255.255.255.255", "0.0.0.0",
    "256.100.0.1", "192.168.1.300", "999.999.999.999", "10.256.0.1",
    "10.0.0", "172.16.0.1.2", "192.168.1.", "10.10",
    "192.168.1.abc", "10.0.o.1", "172. 16.1.1", "192.168.1.1a",
    "not_an_ip", "http://192.168.1.1", "192.168.1.1/24", "...1"
]
counter_valid = 0
counter_invalid = 0
valid_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
for ip in mixed_ip_list:
    if valid_ip.fullmatch(ip):
        print(ip)
        counter_valid +=1
    else:
        counter_invalid +=1
print(f"This number of valid ip {counter_valid} and this is number of {counter_invalid}")


#Task 20.5: re.fullmatch vs re.search
text = "my email is test@example.com inside the message"
reg1 = re.search(r"^\w+@\w+\.\w+$", text) # this didnt match cause from begining if we start there is space and .com follows space
reg2 = re.search(r"\w+@\w+\.\w+", text) # this matched because this searched for specific pattern in the entire text
reg3 = re.fullmatch(r"\w+@\w+\.\w+", text) # this didnt match as the entire string was not email there are spaces 
reg4 = re.fullmatch(r"\w+@\w+\.\w+", "test@example.com") # this matched the complete string against the text provided which was email

print(reg1)
print(reg2.group())
print(reg3)
print(reg4.group())


#The "Muscle Memory" Gauntlet (The IOC Validator)

indicators = [
    "192.168.1.50",
    "evil-domain.ru",
    "5d41402abc4b2a76b9719d911017c592",
    "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d",
    "not_valid_data",
    "999.999.999.999",
    "phishing-site.example.com",
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "11:22:33:44:55:66",
    "incomplete_hash_5d41402a",
    "10.0.0.5",
    "JUNK"
]

MD5_pattern = re.compile(r"^[a-fA-F0-9]{32}$")
SHA1_pattern = re.compile(r"^[a-fA-F0-9]{40}$")
SHA256_pattern = re.compile(r"^[a-fA-F0-9]{64}$")
ipv4_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
domain_pattern = re.compile(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
mac_address_pattern = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$")

categorized = {"ipv4": [], "md5": [], "sha1": [], "sha256": [], "domain": [], "mac": [], "invalid": []}

for item in indicators:
    if ipv4_pattern.fullmatch(item):
        categorized["ipv4"].append(item)
    elif MD5_pattern.fullmatch(item):
        categorized["md5"].append(item)
    elif SHA1_pattern.fullmatch(item):
        categorized["sha1"].append(item)
    elif SHA256_pattern.fullmatch(item):
        categorized["sha256"].append(item)
    elif domain_pattern.fullmatch(item):
        categorized["domain"].append(item)
    elif mac_address_pattern.fullmatch(item):
        categorized["mac"].append(item)
    else:
        categorized["invalid"].append(item)

print(f"Summary:")
print(f"Count of IPv4 - {len(categorized['ipv4'])} \n {categorized['ipv4']} ")
print(f"Count of MD5 - {len(categorized['md5'])} \n {categorized['md5']} ")
print(f"Count of SHA1 - {len(categorized['sha1'])} \n {categorized['sha1']} ")
print(f"Count of SHA256 - {len(categorized['sha256'])} \n {categorized['sha256']} ")
print(f"Count of domain - {len(categorized['domain'])} \n {categorized['domain']} ")
print(f"Count of mac - {len(categorized['mac'])} \n {categorized['mac']} ")
print(f"Count of invalid - {len(categorized['invalid'])} \n {categorized['invalid']} ")

#Clean Way 
print("Summary:")
for category, items in categorized.items():
    print(f"Count of {category} - {len(items)}")
    print(f"  {items}")

with open("categorized_iocs.json", "w", encoding="utf-8", errors="ignore") as f:
    json.dump(categorized, f, indent=4)



