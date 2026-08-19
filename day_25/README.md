Welcome to **Day 25**.

In [**Day 24**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_24), I learned recursive file walking with `rglob()` and `os.walk()` to sweep an entire evidence tree. Today I drop below the text layer and read **raw bytes**.

Everything I have read so far has been text — logs, CSVs, JSON. But most forensic artifacts are not text. A memory dump, an executable, a prefetch file, a registry hive, a disk image. Open any of those in text mode and I get garbage, or my script crashes on the first invalid byte. Think of it like this: text mode is reading a translated book — someone already decided how to interpret every symbol. Binary mode is being handed the original manuscript in a script I must decode myself. Slower and harder, but nothing is lost in translation, and sometimes the evidence is in the ink, not the words.

### Core Concepts

- **`open(path, "rb")`** — binary read mode. **No `encoding` parameter** — there is no translation happening.
- **`bytes` objects** display printable ASCII as characters and everything else as `\xNN` hex escapes.
- **Indexing gives an integer, slicing gives bytes.** `data[0]` → `77`. `data[0:1]` → `b'M'`.
- **`f.read(n)`** reads exactly `n` bytes — essential when the file is 4GB and I only need the header.
- **`f.seek(offset)`** jumps to a byte position. Every file format spec says where its fields live.
- **`.hex()`** converts bytes to a hex string; **`bytes.fromhex()`** converts back.

### File Signatures (Magic Numbers)

Every format begins with a byte sequence that identifies it regardless of extension. An attacker renames `malware.exe` to `invoice.pdf` — the extension lies, the magic number does not.

- `4D 5A` (`MZ`) — Windows executable (PE)
- `25 50 44 46` (`%PDF`) — PDF
- `50 4B 03 04` (`PK..`) — ZIP (also DOCX, XLSX, JAR)
- `89 50 4E 47` — PNG
- `FF D8 FF` — JPEG
- `7F 45 4C 46` — Linux ELF

---

### The Tasks

I created `day_25/binary_drills.py`.

#### Task 25.1: Create and Read Raw Bytes

Write a bytes literal to a file in `"wb"` mode, read it back in `"rb"`, and confirm the type is `bytes` not `str`.

#### Task 25.2: Index vs Slice

Print `data[0]` (an integer) and `data[0:2]` (a bytes object). Use `chr()` to convert the integer back to its character.

#### Task 25.3: Hex Conversion

Convert bytes to hex with `.hex()` and `.hex(" ")`. Convert the hex string `"25504446"` back to bytes and recognise the result.

#### Task 25.4: Read Only the Header

Read the first 4 bytes with `f.read(4)`, then `f.seek(0)` and read 2 bytes. Note why header-only reads matter on multi-gigabyte evidence.

#### Task 25.5: Build a Test File Set

Create dummy files with real magic numbers — including an executable disguised as a `.txt` and another disguised as a `.pdf`.

---

### The "Muscle Memory" Gauntlet (The File Signature Validator)

**The Mission:** I built a tool that walks a directory, reads each file's magic number, identifies its true type, and flags files whose extension lies about their content.

1. Build a `SIGNATURES` dictionary mapping hex signature strings to file type names.
2. Write `read_magic(file_path, num_bytes=8)` that opens in `"rb"`, reads the header, returns the hex string, and handles `PermissionError` and `OSError`.
3. Write `identify_file(magic_hex)` that loops the signature dictionary using `.startswith()` — signatures are different lengths, so equality would fail.
4. Write `validate_extension(file_path, identified_type)` comparing `.suffix` against expected extensions for that type.
5. Walk the directory with `.rglob("*")`, identify each file, and collect results.
6. Print a report with an `"EXTENSION MISMATCH DETECTED"` section.
7. Write results to `day_25/signature_report.json` with `indent=4`.
