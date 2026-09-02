Welcome to **Day 26**.

In [**Day 25**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_25), I learned to read raw bytes, convert them to hex, and identify files by their magic numbers. Today I learn the full set of conversions between text, bytes, hex, and **Base64** — and why attackers rely on all of them.

Malicious payloads are almost never stored in plain text. A PowerShell command in a scheduled task is Base64-encoded. A C2 configuration inside a binary is hex-encoded. An exfiltrated document is Base64 in an HTTP POST body. Attackers encode not to defeat cryptography, but to slip past pattern-matching detection and survive transmission through text-only channels. Think of encoding like packing a fragile item for shipping — the item does not change, it is just wrapped in a form that survives the journey. There is no key and no secret. Anyone can unwrap it, which is exactly why encoding is not encryption.

### Core Concepts

- **`.encode()` goes down to bytes, `.decode()` comes up to text.** This is the direction rule to memorize.
- **`base64.b64encode()` and `base64.b64decode()`** both take bytes and return bytes — never strings.
- **Recognizing Base64:** character set `A-Z a-z 0-9 + /`, length a multiple of 4, padded with `=`.
- **PowerShell `-EncodedCommand` decodes to UTF-16LE, not UTF-8.** Decoding it as UTF-8 leaves null bytes between every character. This detail comes up constantly in real incident response.
- **`base64.urlsafe_b64encode()`** uses `-` and `_` so the output survives inside URLs.

---

### The Tasks

I created `day_26/encoding_drills.py`.

#### Task 26.1: Text to Bytes and Back

Encode a command string to bytes with `.encode("utf-8")`, decode it back, and confirm the round trip preserves the original.

#### Task 26.2: The Full Conversion Chain

Move `"cmd.exe"` through every representation — string to bytes, bytes to hex, hex back to bytes, bytes back to string — printing each stage.

#### Task 26.3: Base64 Encode and Decode

Base64-encode a command, then decode it back, confirming the round trip.

#### Task 26.4: Decode a PowerShell EncodedCommand

Build an encoded payload by encoding a command as `utf-16-le` then Base64. Decode it back correctly, then try decoding as `utf-8` and observe what goes wrong.

#### Task 26.5: Base64 Detection

Write `looks_like_base64(text)` that checks length is a multiple of 4, characters match `[A-Za-z0-9+/=]`, and length is at least 16. Test it against real Base64, plain text, and a hex string.

---

### The "Muscle Memory" Gauntlet (The Payload Decoder)

**The Mission:** I built a tool that scans a command log for encoded PowerShell payloads, decodes them, and flags high-risk commands.

1. Write `extract_encoded_payload(line)` using regex to detect `-enc` or `-EncodedCommand` and capture the Base64 string that follows.
2. Write `decode_powershell(b64_string)` that Base64-decodes, then decodes as `utf-16-le`, wrapped in `try/except` returning `None` on malformed input.
3. Write `analyze_log(file_path)` that reads the log line by line, parses each timestamp with `datetime.strptime()`, extracts and decodes payloads, and returns a list of result dictionaries.
4. Print a report showing each decoded command with its timestamp.
5. Flag `"HIGH RISK"` when the decoded text contains `lsass`, `Invoke-`, `DownloadString`, `Mimikatz`, `-nop`, or `hidden`.
6. Write results to `day_26/decoded_payloads.json` with `indent=4`, outside the scanned location.
