Welcome to **Day 20**.

In [**Day 19**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_19), I learned capture groups, named groups, and the difference between `re.match()` and `re.search()`. Today, I learn the third use of regex: **validation** — confirming that data matches an expected format before processing it.

In DFIR, validation matters because evidence is messy. An analyst types a malformed IP into a ticket. A log line contains a corrupted hash. A username field has a SQL injection payload instead of a name. Validation lets my script reject malformed input before it crashes or processes garbage data. Think of validation like an evidence intake checklist — before an item enters chain of custody, I verify it has a tag, a hash, and a timestamp. Regex validation is the script-level version of that checklist.

### Core Concepts

- **Anchors transform search into validation.** `^pattern$` requires the pattern to match the **entire** string.
- **`re.fullmatch()`** does the same job — requires the entire string to match — without needing `^` and `$`.
- **For validation, I do not need `.group()`.** I only check whether the match succeeded.
- **Alternation `|`** matches one of several options: `r"GET|POST|PUT"`.
- **`re.compile()`** pre-compiles a pattern. Faster and cleaner when used many times in a loop.

### Common DFIR Validation Patterns

- **IPv4 (basic):** `r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"`
- **MD5:** `r"^[a-fA-F0-9]{32}$"`
- **SHA1:** `r"^[a-fA-F0-9]{40}$"`
- **SHA256:** `r"^[a-fA-F0-9]{64}$"`
- **Domain:** `r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"`
- **MAC address:** `r"^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$"`

---

### The Tasks

I created `day_20/validation_drills.py`.

#### Task 20.1: IP Address Validator

1. Create a list of mixed valid and malformed IP strings.
2. Write a basic IPv4 pattern using `^` and `$`.
3. Loop through and print whether each is valid or invalid.
4. Note in a comment: the basic pattern accepts `999.999.999.999` since each octet just needs to be 1-3 digits.

#### Task 20.2: Hash Type Detector

1. Create a list of mixed hashes (MD5, SHA1, SHA256, junk, truncated).
2. Write three patterns — one for each hash length.
3. Loop through and identify the hash type or print "Unknown format."

#### Task 20.3: Method + Status Validator (Alternation)

1. Create a list of HTTP methods.
2. Use `|` alternation to match only safe methods (GET, POST, PUT).
3. Print allowed vs blocked methods.

#### Task 20.4: Pre-Compiled Pattern

1. Compile the IP validation pattern once with `re.compile()`.
2. Use it inside a loop over 20+ mixed IPs.
3. Count valid matches.

#### Task 20.5: re.fullmatch vs re.search

1. Test the same email pattern with anchors, without anchors, with `fullmatch`, on a string with extra text and on a clean email.
2. Explain in comments why each behaves as it does.

---

### The "Muscle Memory" Gauntlet (The IOC Validator)

**The Mission:** I built a tool that validates and categorizes IOCs from a threat intelligence feed.

1. Compile separate patterns for IPv4, MD5, SHA1, SHA256, domain, and MAC address.
2. Create a dictionary with keys for each category plus `"invalid"`.
3. Loop through the indicator list. Test each against every pattern.
4. Append matching IOCs to the right category, unmatched ones to `"invalid"`.
5. Print a summary count per category, then the full lists.
6. Write the categorized result to `categorized_iocs.json` with `indent=4`.

The order of pattern checks matters. The most specific patterns get tested first.