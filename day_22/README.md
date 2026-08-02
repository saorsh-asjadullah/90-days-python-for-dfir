Welcome to **Day 22**.

In [**Day 21**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_21), I built the IOC Extractor — a milestone tool that pulls, validates, and categorizes indicators from messy text. That tool tells me *what* happened. Today I learn to work with *when* it happened: **Date & Time Manipulation**.

In DFIR, time is the backbone of every investigation. I build timelines, correlate events across systems, and answer the question every incident hinges on: "What happened in the 10 minutes before the breach?" The problem is that timestamps come in dozens of formats — Windows uses `2024-06-15T09:22:41`, Apache uses `15/Jun/2024:09:22:41`, Unix uses epoch seconds. To correlate them, I must convert them all into one common format Python understands: the `datetime` object. Think of it like currency exchange — each log hands me a different currency, and I convert everything to one base currency before I can compare freely.

### Core Concepts

- **`datetime.strptime(string, format)`** — parses a string into a datetime object. (**p** = parse)
- **`dt.strftime(format)`** — formats a datetime object back into a string. (**f** = format)
- **`timedelta`** — represents a duration. Add or subtract it from a datetime for time math.
- **Comparison operators** (`<`, `>`, `==`) work directly on datetime objects to determine chronological order.

### Common Format Codes

- `%Y` 4-digit year, `%m` month, `%d` day
- `%H` hour (24h), `%M` minute, `%S` second
- `%b` abbreviated month name (Jun), `%A` weekday name, `%B` full month name

---

### The Tasks

I created `day_22/datetime_drills.py`.

#### Task 22.1: Parse a Timestamp

Convert a string timestamp into a datetime object with `strptime()` and confirm its type.

#### Task 22.2: Format a Timestamp

Reformat the datetime object three ways using `strftime()` — date only, time only, and full weekday/month name.

#### Task 22.3: Time Math with timedelta

Calculate the time 30 minutes after and 2 hours before an event using `timedelta`.

#### Task 22.4: The Duration Between Two Events

Subtract two datetimes to get a `timedelta`, then use `.total_seconds()` to find elapsed seconds.

#### Task 22.5: Parse a Different Format (Apache Style)

Parse an Apache-style timestamp (`15/Jun/2024:09:22:41`) using `%b` and the correct separators, then output it in ISO format.

---

### The "Muscle Memory" Gauntlet (The Timeline Sorter)

**The Mission:** I built a tool that takes out-of-order security events, sorts them chronologically, and isolates events within a suspicious time window.

1. Parse each event's timestamp string into a datetime object, storing `(datetime, message)` tuples.
2. Sort the list chronologically using `sorted()` with `key=lambda x: x[0]`.
3. Print the sorted timeline with readable formatting.
4. Define a suspicious window with parsed start and end datetimes.
5. Print only the events that fall within that window.

A **lambda** is a tiny inline function — `key=lambda x: x[0]` tells `sorted()` to sort by the first element of each tuple.
