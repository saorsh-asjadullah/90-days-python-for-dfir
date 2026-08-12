Welcome to **Day 23**.

In [**Day 22**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_22), I learned to parse, format, and do math with timestamps using `datetime` and `timedelta`. Today I learn the modern, correct way to handle file paths: **`pathlib`**.

I have been writing file paths as raw strings since Day 6. That works until it does not — Windows uses backslashes, Linux uses forward slashes, and hardcoding one breaks my script on the other. On Day 10 I even split a path manually on `"\\"` just to extract a filename. `pathlib` eliminates all of that. Think of it like the difference between handwritten directions and a GPS — raw string paths assume a fixed landscape and fall apart when it changes, while `pathlib` knows the terrain (my OS) and adjusts automatically.

### Core Concepts

- **`Path("folder/file.txt")`** creates a Path object — not a string, but an object with built-in methods.
- **The `/` operator joins paths:** `Path("evidence") / "case_042" / "dump.raw"` — the correct separator is inserted for my OS.
- **Inspection properties:** `.name` (filename), `.stem` (name without extension), `.suffix` (extension), `.parent` (containing folder).
- **Checks:** `.exists()`, `.is_file()`, `.is_dir()`.
- **I/O helpers:** `.read_text()` and `.write_text()` for small files; `Path` objects also work inside `open()`.
- **`.iterdir()`** lists directory contents, each already a full Path object.

---

### The Tasks

I created `day_23/pathlib_drills.py`.

#### Task 23.1: Build and Inspect a Path

Create a path object and print `.name`, `.stem`, `.suffix`, and `.parent` — extracting each piece without string slicing.

#### Task 23.2: Join Paths the Right Way

Build a base directory with `/` and join file paths onto it. Observe the OS-correct separators.

#### Task 23.3: Check Existence and Type

Use `.exists()`, `.is_file()`, and `.is_dir()` on a real file and a non-existent one.

#### Task 23.4: Extract the Filename Without Manual Splitting

Take a messy path and use pathlib properties to pull the filename, extension, and parent — compared to the Day 10 manual `"\\"` split.

#### Task 23.5: List a Directory

Loop through `.iterdir()` on the current directory, printing each item's name and whether it is a file or directory.

---

### The "Muscle Memory" Gauntlet (The Evidence Triage Scanner)

**The Mission:** I built a directory scanner that categorizes files by extension using pathlib throughout.

1. Create a test directory with `.mkdir(exist_ok=True)` and populate it with dummy files of different extensions using `write_text()`.
2. Define `scan_evidence(directory_path)` that loops through `.iterdir()`, reads each file's `.suffix`, and builds a dictionary mapping each extension to a list of matching filenames.
3. Call the function and print a report — extension, count, and filenames.
4. Flag any `.exe` files with a `"SUSPICIOUS: Executable files detected"` warning.
5. Write the categorized dictionary to `day_23/evidence_scan.json` with `indent=4`.