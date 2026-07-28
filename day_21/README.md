Welcome to **Day 21**.

In [**Day 20**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_20), I learned regex validation patterns using anchors and `re.fullmatch()` to confirm data matches an expected format. Today is a **Milestone** — no new concepts. I weaponize everything from Days 18, 19, and 20 into a single tool: **The IOC Extractor**.

The scenario: an analyst forwards me a raw incident note — text copied from an email body, a memory strings dump, and firewall log fragments, all jumbled together. Buried in that noise are IPs, domains, hashes, and email addresses. My job is to extract, validate, deduplicate, categorize, and report them. Manually this takes 20 minutes of careful reading. My script does it in milliseconds. Think of it like panning for gold — the raw text is river silt, regex is the screen that catches particles of the right shape, validation is the loupe that confirms each nugget is real, and the categorized JSON is the labeled tray I hand to the next analyst.

### Concepts Combined

- **Extraction** (Day 18): `re.findall()` to pull candidates from running text.
- **Groups** (Day 19): capturing specific fields.
- **Validation** (Day 20): confirming each candidate is well-formed.
- **Word boundaries** `\b`: new this milestone — prevents a short hash pattern from matching a substring of a longer hash.
- **Sets** (Day 12): deduplication.
- **Dictionaries** (Day 5, 16): categorization.
- **Functions** (Day 8) and **context managers** (Day 17): structure.
- **JSON** (Day 16): structured output.

---

### The Setup

I created `day_21/raw_incident_notes.txt` — a deliberately messy block of text containing valid IOCs (IPs, domains, MD5/SHA1/SHA256 hashes, emails, a MAC address) mixed with noise (a malformed IP `999.999.999.999`, a partial hash, and junk lines).

---

### The Mission

I built `day_21/ioc_extractor.py`.

#### Step 1 — Read the evidence

Open the raw text file with a context manager and read the entire content into one string.

#### Step 2 — Define patterns

Compile patterns for IPv4, MD5, SHA1, SHA256, email, and domain. For extraction from running text I do not use `^...$` anchors — those validate a string in isolation. Instead I extract candidates, then validate. Use `\b` word boundaries on hash patterns so the MD5 pattern (32 hex) does not grab the first 32 characters of a SHA256 hash (64 hex).

#### Step 3 — Extract candidates

Use `re.findall()` for each pattern against the full text.

#### Step 4 — Validate and deduplicate

Write `is_valid_ip(ip)` that splits on dots and confirms every octet is 0-255, rejecting `999.999.999.999`. Deduplicate every category with `set()`.

#### Step 5 — Categorize

Populate a dictionary with keys for each IOC type, holding validated, deduplicated, sorted results.

#### Step 6 — Report

Print a readable summary to the terminal, then write the full dictionary to `extracted_iocs.json` with `indent=4`.

#### Step 7 — Structure as functions

Wrap the logic in `read_evidence()`, `is_valid_ip()`, `extract_iocs()`, and `write_report()`, called in sequence from a main block.

---

### The "Muscle Memory" Gauntlet (Defanging)

In threat intelligence reports, IOCs are "defanged" so nobody accidentally clicks a malicious link and tools do not auto-block while reading. `192.168.1.50` becomes `192[.]168[.]1[.]50`.

I added a `defang(ioc)` function that replaces every `.` with `[.]`, applied it to IPs and domains, and wrote a second output file `defanged_iocs.json`. The syntax is a simple `.replace()` — the DFIR skill is knowing *why* defanging matters.
