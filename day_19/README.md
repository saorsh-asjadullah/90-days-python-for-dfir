Welcome to **Day 19**.

In [**Day 18**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_18), I learned regex basics — `re.search()`, `re.findall()`, character classes, anchors, and the dot trap. Today, I learn to **extract specific pieces** from inside those patterns using **capture groups**.

I saw a preview yesterday when I wrote `r"for (\w+) from"` and called `.group(1)`. Today I understand exactly what the parentheses do and why they are the most important regex feature for DFIR. Think of it like this: yesterday's regex was a metal detector that beeped when it found something. Today's regex is a metal detector that also tells me exactly what it found — the coin, the nail, or the bottle cap — separately, so I can sort them.

### Core Concepts

- **Capture groups** — parentheses `()` mark sections of a pattern to capture separately.
- **`.group(0)`** returns the entire match. **`.group(1)`, `.group(2)`** return individual captured sections.
- **`.groups()`** returns all captured sections as a tuple, perfect for unpacking: `username, ip = match.groups()`.
- **Named groups** use the syntax `(?P<name>pattern)` for clearer code. Access them with `.group("name")` or get them all as a dictionary with `.groupdict()`.
- **`re.findall()` with groups** returns a list of tuples (one tuple per match) instead of a list of strings.
- **`re.match()`** is like `search()` but only checks the **beginning** of the string.

---

### The Tasks

I created `day_19/regex_groups.py`.

#### Task 19.1: Single Group Extraction

1. Create a string with a username embedded in it.
2. Write a pattern that captures just the username inside parentheses.
3. Use `re.search()` and print both `.group(0)` (the full match) and `.group(1)` (the username).

#### Task 19.2: Multiple Group Extraction

1. Create a connection string with source IP, destination IP, and port.
2. Write a pattern with three capture groups — one for each field.
3. Print each group individually using `.group(1)`, `.group(2)`, `.group(3)`.
4. Then use `.groups()` to unpack all three into variables in one line.

#### Task 19.3: findall with Groups

1. Create a multi-line auth log with three failed login lines.
2. Use `re.findall()` with two capture groups (username and IP).
3. Observe the result is a list of tuples.
4. Loop through the result, unpacking each tuple directly: `for username, ip in results:`.

#### Task 19.4: Named Groups (Cleaner Code)

1. Rewrite the connection pattern using named groups: `(?P<src>...)`, `(?P<dst>...)`, `(?P<port>...)`.
2. Access groups by name: `match.group("src")`.
3. Use `.groupdict()` to get all named groups as a dictionary.

#### Task 19.5: re.match vs re.search

1. Test `re.match()` vs `re.search()` on a string where the pattern is at the start, and another where it is in the middle.
2. Understand: `match` only checks the beginning; `search` scans the whole string.

---

### The "Muscle Memory" Gauntlet (The Apache Log Parser)

**The Mission:** I built a regex-based Apache access log parser using named groups.

1. Write a single pattern with named groups capturing four fields: `ip`, `method` (GET/POST), `path` (the URL), and `status` (the response code).
2. Loop through each log line and use `re.search()` to extract the fields by name.
3. Print a structured line for each entry: `f"[{status}] {method} {path} from {ip}"`.
4. Use the dictionary-as-counter pattern to count requests per status code.
5. Print the status code summary at the end.