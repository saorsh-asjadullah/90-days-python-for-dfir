from pathlib import Path
import json

#Task 23.1: Build and Inspect a Path
print("\nTask 23.1: Build and Inspect a Path\n")

p = Path("evidence/case_042/memory_dump.raw")
print(f"The file full name with extension is {p.name}")
print(f"The file name is {p.stem}")
print(f"The file type is {p.suffix}")
print(f"The parent folder is {p.parent}")

#Task 23.2: Join Paths the Right way

print("\nTask 23.2: Join Paths the Right way\n")

case_dir = Path("evidence") / "case_042"
memory_file = case_dir / "memory.dmp"
registry_file = case_dir / "ntuser.dat"
report_file = case_dir / "report.pdf"

print(f"The memory file with path is {memory_file}")
print(f"The registry file with path is {registry_file}")
print(f"The case report file is at this locatio {report_file}")

#Task 23.3 Check Existence and Type

print("\nTask 23.3 Check Existence and Type\n")

tool_path = Path("C:/Users/phoenix/Documents/Python_Labs_Codes/90-days-python-for-dfir/day_21/ioc_extractor.py")
fake_path = Path("C:/User/John/Documents/doc1.txt")

if_path_exist = False
if tool_path.exists():
    if_path_exist = True

if_file = False
if tool_path.is_file():
    if_file = True
if_dir = False
if tool_path.is_dir():
    if_dir = True

print()
print(f"The {tool_path} exist: {if_path_exist}")
print(f"The {fake_path} exist: {fake_path.exists()} ")
print(f"The {tool_path} is a file: {if_file}")
print(f"The {tool_path} is a directory: {if_dir}")


#Task 23.4: Extract the Filename Without Manual Splitting
print("\nTask 23.4: Extract the Filename Without Manual Splitting\n")

full_path = Path("C:/evidence/case_042/malware.exe")
print(f"The file name is {full_path.stem}")
print(f"The file extension is {full_path.suffix}")
print(f"The parent folder is {full_path.parent}")

#Task 23.5: List a Directory
print("\nTask 23.5: List a Directory\n")

current_path = Path(".")
print(f"The PWD is {current_path}")
for item in current_path.iterdir():
    print(item)
    if item.is_dir():
        print(f"The {item} is directory")
    else:
        print(f"The {item} is a file")

#The "Muscle Memory" Gauntlet (The Evidence Triage Scanner)
print('\nThe "Muscle Memory" Gauntlet (The Evidence Triage Scanner)\n')

new_directory = Path("day_23/test_evidence")
new_directory.mkdir(exist_ok=True)
notes_txt = new_directory /"notes.txt"
capture_pcap = new_directory /"capture.pcap"
malware_exe = new_directory /"malware.exe"
report_pdf = new_directory / "report.pdf"

notes_txt.write_text("This is test_data", encoding="utf-8")
capture_pcap.write_text("This is test_data", encoding="utf-8")
malware_exe.write_text("This is test_data", encoding="utf-8")
report_pdf.write_text("This is test_data", encoding="utf-8")

def scan_evidence(directory_path):
    ext_map = {}
    for item in Path(directory_path).iterdir():
        if item.is_file():
            suffix = item.suffix
            if suffix in ext_map:
                ext_map[suffix].append(item.name)
            else:
                ext_map[suffix] = [item.name]
    return ext_map

rep_dict = scan_evidence(new_directory)
print(rep_dict)
for extension, files in rep_dict.items():
    print(f"Extension {extension}: {len(files)} file(s)")
    for file in files:
        print(f"  {file}")
    if extension == ".exe":
        print("SUSPICIOUS: Executable files detected")
        for file in files:
            print(f"  {file}")

with open("day_23/evidence_scan.json", "w", encoding="utf-8", errors="ignore") as fwrite:
        json.dump(rep_dict, fwrite, indent=4)


