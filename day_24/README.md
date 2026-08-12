Welcome to **Day 24**.

In [**Day 23**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_23), I learned `pathlib` and scanned a single directory with `.iterdir()`. Today I learn to walk an entire directory **tree** recursively.

`.iterdir()` only looks at one level. Real evidence is never flat — a KAPE triage collection gives me a nested tree with `Users/jsmith/AppData/Local/Temp/`, `Windows/Prefetch/`, `Windows/System32/winevt/Logs/`, often ten levels deep with thousands of files scattered throughout. Think of it like searching a building: `.iterdir()` is standing in the lobby listing every door I can see. Recursive walking is opening every one of those doors, walking into every room, opening every closet inside those rooms, and continuing until I have been everywhere. That is what a forensic sweep actually requires.

### Core Concepts

- **`Path.rglob(pattern)`** — the modern way. The `r` means **recursive**. `root.rglob("*.exe")` finds every executable at any depth in one line.
- **`Path.glob(pattern)`** — same syntax but searches only one level deep.
- **`os.walk(path)`** — the classic way. Yields `root`, `dirs`, `files` for every directory in the tree. I must join `root` and filename myself.
- **`.stat().st_size`** — file size in bytes.
- **Permissions matter.** Walking a real filesystem hits unreadable directories. Always wrap file access in `try/except PermissionError` — a sweep that dies at file 400 of 50,000 is worthless.

---

### The Tasks

I created `day_24/recursive_drills.py`.

#### Task 24.1: Build a Nested Test Structure

Use `.mkdir(parents=True, exist_ok=True)` and `.write_text()` to build a realistic nested evidence tree — user profile folders, AppData Temp, Windows Prefetch, and System32 — each populated with dummy files.

#### Task 24.2: Flat vs Recursive

Loop through `.iterdir()` and count the items. Then loop through `.rglob("*")` and count again. Note the difference — one level versus the whole tree.

#### Task 24.3: Pattern-Based Recursive Search

Use `.rglob("*.exe")`, `.rglob("*.pf")`, and `.rglob("*.txt")` to find files by type regardless of depth.

#### Task 24.4: The os.walk Equivalent

Walk the same tree with `os.walk()`, printing the current directory, subdirectory count, and file count for each iteration. Build full paths with `os.path.join()`.

#### Task 24.5: Defensive Walking

Walk the tree with `.rglob("*")`, wrapping each file inspection in `try/except` to catch `PermissionError` and `OSError` without crashing.

---

### The "Muscle Memory" Gauntlet (The Forensic Sweep)

**The Mission:** I built a recursive sweep tool that flags files of forensic interest across an entire evidence tree.

1. Define a list of suspicious extensions: `.exe`, `.dll`, `.ps1`, `.bat`, `.vbs`, `.scr`.
2. Write `forensic_sweep(root_path)` that walks the tree with `.rglob("*")`, skips non-files, collects full path, filename, extension, and size for each, wraps access in `try/except`, and returns a dictionary split into `"suspicious"` and `"other"`.
3. Write `print_sweep_report(results)` that prints total file count, suspicious count, and each suspicious file with path and size.
4. Write the results to `day_24/sweep_report.json` with `indent=4` — **outside** the scanned directory.
5. Use the dictionary-as-counter pattern to count files per extension across the tree.
