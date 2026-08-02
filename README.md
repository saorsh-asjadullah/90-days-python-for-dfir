# Python for DFIR — 90-Day Apprenticeship

This repository documents a 90-day, exercise-driven journey to build **practical Python proficiency for Digital Forensics and Incident Response (DFIR)**.

The focus is not on learning Python syntax in isolation, but on developing **muscle memory** and **analyst-style thinking** through small, repeatable, real-world tasks.

---

## Philosophy

- One focused task per day  
- Every task produces a **working, reviewable artifact**
- No filler, no copy-paste exercises
- Emphasis on correctness, clarity, and deterministic output
- DFIR mindset from Day 1 (text, logs, artifacts, structure)

This mirrors how DFIR skills are built in practice: incrementally, deliberately, and with attention to detail.

---

## What This Demonstrates

By the end of this series, this repository will show:

- Progressive Python skill development
- Comfort with strings, files, control flow, and data structures
- Ability to translate investigative logic into code
- Consistent delivery and version control discipline
- Practical foundations for DFIR automation and tooling

---

## Progress Tracking
- [ ] Phase 1: The Scripter (Days 1-30) - **In Progress**
- [ ] Phase 2: The Automator (Days 31-60)
- [ ] Phase 3: The Analyst (Days 61-90)

## Day 1: The Interrogation (Input/Output)
**Goal:** Master variable assignment, user input, and formatted output.

### Day 1: Learning Reflections
- **Technical Progress:** Learned to capture user input, use f-strings for reporting, and sanitize strings with `.strip()`.
- **Logic Insight:** Confirmed that `input()` defaults to string data even if I intend to use it as a number.
- **Muscle Memory:** Practiced the `f"[TAG] {variable}"` pattern which is the bread and butter of log generation.

### Exercises Completed:
1. **triage_report.py**: Captures Analyst name, Case ID, and Target IP.
2. **variable_swap.py**: Practicing re-assignment of network configurations.
3. **evidence_string.py**: Building alert strings from multiple data types.

## Day 2: String Slicing & Methods
- **Technical Progress:** Mastered slicing `[start:stop]`, negative indexing `[-n]`, and sanitization methods (`.lower()`, `.replace()`).
- **Logic Insight:** The "Stop" index is exclusive. To get characters 0-4, I must type `[0:5]`.
- **Scar Tissue:** Escape characters! I learned that `\` inside a string needs to be written as `\\`.

## Day 3: Logic & Control Flow
- **Technical Progress:** Learned `if`, `elif`, `else`, comparators (`==`, `!=`, `>`), and the powerful `in` operator.
- **Logic Insight:** Python evaluates conditionals top-to-bottom. The first expression that evaluates to `True` wins, and the rest are ignored. Order matters!
- **Muscle Memory:** Practiced compound logic (`and`/`or`) to create "Kill Chain" rules for flagging threats.

## Day 4: Lists & Loops
- **Technical Progress:** Mastered the `for` loop to iterate through lists. Learned the "Accumulator Pattern" (counters) to summarize data.
- **Logic Insight:** A loop repeats the *same* block of code for *different* data items. Variables defined outside the loop (like counters) persist and grow; variables inside the loop reset on every iteration.
- **Muscle Memory:** Combined `if` statements inside `for` loops to create filters (Search & Destroy).

## Day 5: Lists & Dictionaries
- **Technical Progress:** Learned to dynamically build lists using `.append()`. Mastered Dictionary lookups (`key -> value`).
- **Logic Insight:** - Lists (`[]`) are for ordered items (logs, files).
    - Dictionaries (`{}`) are for mapping data (IP->Country, Port->Protocol).
    - `KeyError` happens when asking a dictionary for a key that doesn't exist.
- **Muscle Memory:** Combined loops with `if` statements to filter data into new lists.

## Day 6: File I/O
- **Technical Progress:** Learned to Open, Read, and Write files using the `with` context manager.
- **Logic Insight:** `write()` is literal. It does not add newlines automatically; I must explicitly add `\n`.
- **Muscle Memory:** Adopted the "Load-Process-Save" pattern: Read data into a list -> Manipulate it in memory -> Write the results to a new file.
- **Defense:** Used `errors="ignore"` to prevent script crashes when reading non-text bytes.

## Day 7: Milestone - The Log Parser
- **Technical Progress:** Built a complete "ETL" script (Extract, Transform, Load). Extracted IPs from raw logs, filtered for specific keywords, deduplicated the results, and saved a report.
- **Logic Insight:** "Parallel Arrays" (separate lists for related data) work but are risky. Deduplication requires checking existence (`if x not in list`) before appending.
- **Muscle Memory:** Combined File I/O + String Splitting + List Appending + Loops into a single workflow.
- **Correction:** Must verify that `f.write()` includes `\n` or the report is unreadable.

## Day 8: Functions
- **Technical Progress:** Refactored linear scripts into reusable functions (`def`). Used `return` to pass data back to the main program.
- **Logic Insight:** `return` stops the function and sends value out. Without it, the result is lost (None).
- **Muscle Memory:** Parameter unpacking: `ip, time = extract_data(line)`.

## Day 9: Error Handling
- **Technical Progress:** implemented `try/except` blocks to prevent script crashes. Used `pass` to silently ignore errors and `except Exception as e` to debug unknown crashes.
- **Logic Insight:** A "Bare Except" (`except:`) catches ALL errors, which can be dangerous. It is better to catch specific errors like `FileNotFoundError` or `ValueError`.
- **Muscle Memory:** Wrapping file operations in `try` blocks is mandatory when dealing with external evidence.

## Day 10: Standard Library (os & time)
- **Technical Progress:** Utilized the `os` module for file system navigation and metadata extraction. Used `time` for timestamps.
- **Logic Insight:** Operating system interactions require defensive checks. `os.mkdir()` crashes if the folder exists; `os.path.exists()` should be used prior to taking action.
- **Muscle Memory:** Combined directory listing (`os.listdir`) with string methods (`.endswith`) and path sizing (`os.path.getsize`).

## Day 11: String Splitting & Joining
- **Technical Progress:** Mastered `.split(delimiter)` to break complex strings into lists and `delimiter.join(list)` to reconstruct them.
- **Logic Insight:** Consecutive delimiters (like `,,`) create empty strings in the resulting list. They do not collapse automatically.
- **Muscle Memory:** Combined string splitting with deduplication logic to extract unique observables from raw data.

## Day 12: Lists vs. Tuples vs. Sets
- **Technical Progress:** Explored the specialized roles of Tuples (immutability) and Sets (uniqueness/math operations).
- **Logic Insight:** Sets are not just for deduplication; they allow for powerful Venn-style operations like intersections (`&`) and differences (`-`) to filter traffic in one line of code.
- **Muscle Memory:** Used set subtraction to instantly filter whitelisted IPs out of a noisy traffic log.

## Day 13: sys & CLI Arguments
- **Technical Progress:** Used `sys.argv` to accept dynamic inputs from the command line. Built input validation with `len(sys.argv)` and `sys.exit()`.
- **Logic Insight:** Every element in `sys.argv` is a string. The `+` operator concatenates strings rather than adding them mathematically. Cast with `int()` if math is needed.
- **Muscle Memory:** Combined CLI argument handling with file parsing functions to build a reusable, dynamic log hunter.

## Day 14: Milestone 2 — The CLI Log Analyzer
- **Technical Progress:** Built a complete CLI tool combining functions, error handling, file I/O, string splitting, sets, and sys.argv into one modular script.
- **Logic Insight:** Checking for flags with `if "--flag" in sys.argv` is cleaner than positional elif chains. Flags can appear in any order and any combination.
- **Muscle Memory:** Write-once report logic with a conditional print — never duplicate an entire block just to add screen output.

## Day 15: CSV Files
- **Technical Progress:** Learned `csv.reader` (rows as lists) and `csv.DictReader` (rows as dictionaries). Used `csv.writer` to produce structured output files.
- **Logic Insight:** CSV fields are always strings, even if they look like numbers. Must cast with `int()` or `float()` before doing math or numeric comparisons.
- **Muscle Memory:** The dictionary-as-counter pattern (`if key in dict: dict[key] += 1 else: dict[key] = 1`) for grouping and summarizing log data.

## Day 16: JSON Data
- **Technical Progress:** Learned `json.load()` for files and `json.loads()` for strings. Accessed nested data with chained keys like `data["source"]["ip"]`. Used `json.dump()` with `indent=4` for readable output.
- **Logic Insight:** `json.load()` reads from a file object; `json.loads()` reads from a string. JSON numbers come in as actual Python ints/floats (unlike CSV where everything is a string).
- **Muscle Memory:** The dictionary-as-counter pattern applies to JSON the same way it applies to CSV — one loop, dynamic keys, no hardcoded variables per category.

## Day 17: Context Managers (Deep Dive into with)

- **Technical Progress:** Learned that `with` automatically closes file handles on block exit by calling __exit__, even when the code inside crashes.
- **Logic Insight:**  A file handle is closed the moment execution leaves the with block — calling `f.write()` or `f.read()` after that raises `ValueError: I/O` operation on closed file.
- **Muscle Memory:** The dual context manager pattern — two files opened in a single with statement separated by a comma — is the correct structure for all read-filter-write pipelines.

## Day 18: Regular Expressions — Basics
- **Technical Progress:** Learned `re.search()` for first match and `re.findall()` for all matches. Used `\d+`, `\.`, character classes `[a-fA-F0-9]{32}`, and anchors `$`.
- **Logic Insight:** `\d+` matches consecutive digits only — dots break the sequence, which is why an IP returns four separate matches instead of one.
- **Muscle Memory:** Combined regex extraction with the dictionary-as-counter pattern to count failed login attempts per IP from an auth log.

## Day 19: Regex Groups & Extraction
- **Technical Progress:** Learned capture groups with parentheses, named groups with `(?P<name>...)`, `.group(n)`, `.groups()`, `.groupdict()`, and the difference between `re.match()` and `re.search()`.
- **Logic Insight:** `re.findall()` behavior depends on group count — no groups returns strings, one group returns strings (just the group), multiple groups returns tuples.
- **Muscle Memory:** Used named groups to parse Apache logs into structured fields and combined extraction with the dictionary-as-counter pattern for status code summaries.

## Day 20: Regex Validation Patterns
- **Technical Progress:** Used anchors (`^` and `$`) and `re.fullmatch()` to validate entire strings. Compiled patterns with `re.compile()` for performance. Applied alternation with `|`.
- **Logic Insight:** `re.search()` finds patterns anywhere — use for extraction. `re.fullmatch()` requires the whole string to match — use for validation. The distinction defines whether your script accepts garbage or rejects it at the door.
- **Muscle Memory:** Built a multi-pattern IOC categorization tool that validates each indicator against a chain of compiled patterns, sorts into a typed dictionary, and exports to JSON.

## Day 21: Milestone 3 — The IOC Extractor
- **Technical Progress:** Built a complete IOC extraction tool combining regex extraction, octet-range IP validation, set deduplication, dictionary categorization, and JSON export — structured into modular functions with defensive error handling.
- **Logic Insight:** Without `\b` word boundaries, a fixed-length hash pattern matches substrings of longer hashes, producing corrupted IOCs that can derail an investigation. Word boundaries force exact-length matching.
- **Muscle Memory:** The read → extract → validate → deduplicate → categorize → report pipeline, wrapped in functions and driven by a main block with a None guard.

## Day 22: Date & Time Manipulation
- **Technical Progress:** Used `strptime()` to parse strings into datetime objects, `strftime()` to format them back, and `timedelta` for time math. Sorted events chronologically with `sorted(key=lambda x: x[0])`.
- **Logic Insight:** Comparing timestamps as strings is dangerous — Python compares character by character, so "10:00:00" sorts before "9:00:00". Always parse to datetime objects before comparing or sorting.
- **Muscle Memory:** The parse → sort → filter-by-window pipeline for building forensic timelines from unordered multi-source events.