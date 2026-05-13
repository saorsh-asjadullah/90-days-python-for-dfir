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
 
#### Task 18.1: Detect a Port Number in a Log Line
 
Goal: Use `re.search()` to find the first port number in a firewall log entry.
 
1. Import the `re` module.
2. Create a string variable holding this log line: `"2025-06-15 08:22:11 DENY TCP 10.0.0.5 192.168.1.1 443 80"`
3. Write a regex pattern that matches one or more digits.
4. Use `re.search()` with the pattern against the log line.
5. Check if the result is not `None`, then print the matched text using `.group()`.
6. Observe which number it finds first and consider why.
#### Task 18.2: Extract All Hex Strings
 
Goal: Use `re.findall()` to pull every hex-like token from a memory dump snippet.
 
1. Create a string variable: `"addr=0x7FFE0300 offset=0x0041A000 value=0xDEADBEEF flag=0x00"`
2. Write a regex pattern that matches `0x` followed by one or more hex characters (`0-9`, `a-f`, `A-F`) using a character class.
3. Use `re.findall()` to get every match.
4. Loop through the results and print each one.
#### Task 18.3: Match a Filename Ending in .exe
 
Goal: Detect whether a process name ends with `.exe` using anchors and escaping.
 
1. Create a list of five strings: `["svchost.exe", "explorer.exe", "payload.dll", "cmd.exe", "config.sys"]`
2. Write a regex pattern that matches any string ending in `.exe`. Escape the dot and use the end-of-string anchor.
3. Loop through the list. For each string, use `re.search()` to test it.
4. Print only the strings that match.
#### Task 18.4: Validate an MD5 Hash Shape
 
Goal: Use quantifiers and character classes to check if a string looks like a valid MD5 hash.
 
1. Create a list: `["d41d8cd98f00b204e9800998ecf8427e", "ZZZZ8cd98f00b204e9800998ecf8427e", "d41d8cd98f00b204", "5d41402abc4b2a76b9719d911017c592"]`
2. An MD5 hash is exactly 32 hexadecimal characters. Write a regex using `^`, `$`, a hex character class, and `{32}`.
3. Loop through the list. For each string, test it and print whether it is a valid MD5 shape or not.
#### Task 18.5: Find Process Names in a Log
 
Goal: Use word boundaries to extract exact process names.
 
1. Create this string: `"Process svchost.exe spawned by services.exe, not svchost_update.exe"`
2. Write a regex pattern that matches exactly `svchost.exe` as a whole word using `\b` on both sides. Escape the dot.
3. Use `re.findall()` and print the results.
4. Observe whether `svchost_update.exe` appears in the results and understand why or why not.
---
 
### The Muscle Memory Gauntlet
 
**Mission:** Build a script that reads a list of firewall log lines, uses regex to extract IP-address-shaped patterns from each line, and reports which lines contain a specific suspicious IP.
 
1. Create a list of at least six strings, each simulating a firewall log entry. Include source and destination IPs. Make at least two lines contain `10.10.14.99` and at least one line contain no valid IP pattern at all.
2. Define a function called `extract_ips` that takes a single log line as a parameter. Inside it, write a regex pattern matching the general shape of an IPv4 address (one to three digits, literal dot, four groups). Use `re.findall()` to return every match.
3. Define a function called `flag_suspicious` that takes a list of IPs and a target IP string. Return `True` if the target is in the list, `False` otherwise.
4. Create a variable for the suspicious IP: `"10.10.14.99"`.
5. Loop through each log line. Call `extract_ips` to get the IPs, then call `flag_suspicious` to check. Print the line and extracted IPs. If flagged, print a warning.
6. After the loop, print a summary count of how many lines were flagged.