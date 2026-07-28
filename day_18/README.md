Welcome to **Day 18**.
 
In [**Day 17**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_17), I learned how `with` works under the hood and used dual context managers to build read-filter-write pipelines. Today, I learn the fundamentals of regular expressions using Python's `re` module — the single most powerful text-processing tool in DFIR.
 
Every log line I have ever eyeballed for an IP address, every time I manually scanned a dump for an email or a hash — regex automates that pattern recognition at machine speed. In incident response, speed is evidence preservation. The faster I can rip indicators out of a thousand-line log, the faster I scope the compromise. Think of regex like a YARA rule for text: a YARA rule describes a byte pattern and says "flag every file that matches." A regex describes a string pattern and says "flag every line that matches." I am not searching for a specific known string — I am describing the *shape* of what I am looking for.
 
---
 
### Core Concept
 
The `re` module is part of Python's standard library. I import it with `import re` and use its functions to search strings for patterns. The two functions I use most today are `re.search()` and `re.findall()`. `re.search(pattern, string)` scans the string and returns a match object for the first occurrence, or `None` if nothing matches. `re.findall(pattern, string)` returns a list of every non-overlapping match. Patterns should be prefixed with `r` to make them raw strings so Python does not interpret backslashes before regex gets them.
 
Key symbols: `\d` (digit), `\w` (word character), `\s` (whitespace), `.` (any character), `+` (one or more), `*` (zero or more), `?` (zero or one), `{n}` (exactly n), `{n,m}` (between n and m), `[]` (character class), `^` (start of string), `$` (end of string), `\b` (word boundary), `\` (escape a special character).
 
Two critical points: the dot `.` matches anything, so a literal dot (like in an IP address) must be escaped as `\.`. And `re.search()` returns a match object, not a string — I call `.group()` to extract the text, but must check for `None` first to avoid crashing.
 
---
 
### The Tasks
 
Create `day_18/regex_drills.py`.
 
#### Task 18.1: The IP Finder (First Match)
 
Goal: Use `re.search()` to find the first port number in a firewall log entry.
 
1. Import re.
2. Create a variable: log_line = "Failed password for root from 192.168.1.45 port 22 ssh2".
3. Use re.search() with the pattern r"\d+\.\d+\.\d+\.\d+" to find the IP address.
4. If a match is found, print the matched text using .group().
5. Print: f"Attacker IP: {match.group()}".
 
#### Task 18.2: The Port Extractor (Find All)
 
1. Create a variable: traffic = `"Connections on port 443, port 80, port 8080, and port 22"`.
2. Use `re.findall()` with pattern `r"\d+"` to extract all numbers.
3. Print the resulting list.
4. Observe: the result is a list of strings, not integers.
   
#### Task 18.3: The Dot Trap (Escaping Special Characters)
  
1. Create two test strings: `test1 = "192.168.1.1"` and `test2 = "192X168Y1Z1"`.
2. Use `re.search()` with pattern `r"192.168.1.1"` against both strings. Print whether each matched.
3. Observe: both match because `.` means "any character."
4. Fix the pattern by escaping the dots: `r"192\.168\.1\.1"`.
5. Run again. Now only test1 should match.

#### Task 18.4: The Hash Hunter (Character Classes)
 
Goal: Use quantifiers and character classes to check if a string looks like a valid MD5 hash.
 
1. Create a variable: `evidence = "Found hash: 5d41402abc4b2a76b9719d911017c592 in memory dump"`.
2. Use `re.findall()` with pattern `r"[a-fA-F0-9]{32}"` to extract the MD5 hash.
3. Print the result.
   
#### Task 18.5: The Extension Filter (Anchors + Loop)
 
Goal: Use word boundaries to extract exact process names.
 
1. Create a list: `files = ["malware.exe", "notes.txt", "trojan.exe", "report.pdf", "loader.exe"]`.
2. Loop through the list.
3. For each filename, use `re.search()` with pattern` r"\.exe$" `to check if it ends with `.exe`.
4. Print only the filenames that match.
---
 
### The "Muscle Memory" Gauntlet (The Auth Log Analyzer)
 
**The "Muscle Memory" Gauntlet (The Auth Log Analyzer)**

Create a multi-line string simulating an auth log:

```
log_data = """Mar 1 10:15:01 server sshd: Failed password for admin from 10.0.0.5 port 22
Mar 1 10:15:03 server sshd: Failed password for root from 192.168.1.100 port 22
Mar 1 10:15:05 server sshd: Accepted password for admin from 10.0.0.5 port 22
Mar 1 10:16:01 server sshd: Failed password for guest from 172.16.0.9 port 2222
Mar 1 10:16:05 server sshd: Failed password for root from 192.168.1.100 port 22"""
```

Task:

1. Split the string into individual lines.
2. Use `re.findall()` with the IP pattern to extract all IP addresses from the entire `log_data` string. Print the list.
3. Loop through each line. If the line contains `"Failed"`:
    - Use `re.search()` with pattern `r"for (\w+) from"` to extract the username. The parentheses create a group — use `.group(1)` to get just the username. I will explain groups properly on Day 19, but for today treat this as a preview.
    - Use `re.search()` with the IP pattern to extract the IP.
    - Print: `f"Failed login: user={username} from={ip}"`.
4. Count how many times each IP appears in the failed lines using the dictionary-as-counter pattern from Day 15.
5. Print each IP and its count.
