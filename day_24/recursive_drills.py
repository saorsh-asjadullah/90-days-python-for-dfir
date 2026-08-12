import json
import os
from pathlib import Path

#Task 24.1: Build a Nested Test Structure
print("\nTask 24.1: Build a Nested Test Structure\n")

root = Path("day_24/evidence_root")
root.mkdir(parents=True,exist_ok=True)
Documents = root/"Users/jsmith/Documents/"
Documents.mkdir(parents=True,exist_ok=True)
Temp = root/"Users/jsmith/AppData/Local/Temp/"
Temp.mkdir(parents=True,exist_ok=True)
Prefetch = root/"Windows/Prefetch/"
Prefetch.mkdir(parents=True,exist_ok=True)
System32 = root/"Windows/System32/"
System32.mkdir(parents=True,exist_ok=True)

test_files = {
    "notes.txt" : "Investigation notes.\nUser downloaded suspicious attachment.",
    "report.pdf" :  "%PDF-1.7 Dummy PDF",
    "dropper.exe" : "MZ Dummy Executable Dropper",
    "tmp001.tmp" : "MZ Dummy Executable",
    "CMD.EXE-12345.pf" : "MAM Dummy Prefetch for cmd",
    "POWERSHELL.EXE-67890.pf" : "MAM Dummy Prefetch for powershell",
    "svchost.exe": "MZ Dummy Executable svchost",
    "config.ini" : "[owner] \nname = John Doe \n organization = Acme Widgets Inc."
}

for filename,content in test_files.items():
    if filename in ("notes.txt","report.pdf") :
        (Documents/filename).write_text(content,encoding="utf-8")
    elif filename in ("dropper.exe","tmp001.tmp") :
        (Temp/filename).write_text(content,encoding="utf-8")
    elif filename in ("CMD.EXE-12345.pf","POWERSHELL.EXE-67890.pf") :
        (Prefetch/filename).write_text(content,encoding="utf-8")
    else:
        (System32/filename).write_text(content,encoding="utf-8")

# Alternate way to do the same this is after googling and AI usage 
# Benefits
# Easier to read.
# No long if/elif chain.
# Adding a new folder only requires updating the placements dictionary.
# Common pattern in Python because the code is data-driven rather than logic-driven.


# # Root directory
# root = Path("day_24/evidence_root")

# # Create directory structure
# directories = {
#     "Documents": root / "Users/jsmith/Documents",
#     "Temp": root / "Users/jsmith/AppData/Local/Temp",
#     "Prefetch": root / "Windows/Prefetch",
#     "System32": root / "Windows/System32",
# }

# for directory in directories.values():
#     directory.mkdir(parents=True, exist_ok=True)

# # File contents
# test_files = {
#     "notes.txt": "Investigation notes.\nUser downloaded suspicious attachment.",
#     "report.pdf": "%PDF-1.7 Dummy PDF",
#     "dropper.exe": "MZ Dummy Executable Dropper",
#     "tmp001.tmp": "MZ Dummy Executable",
#     "CMD.EXE-12345.pf": "MAM Dummy Prefetch for cmd",
#     "POWERSHELL.EXE-67890.pf": "MAM Dummy Prefetch for powershell",
#     "svchost.exe": "MZ Dummy Executable svchost",
#     "config.ini": "[owner]\nname = John Doe\norganization = Acme Widgets Inc."
# }

# # Which files belong in which folder
# placements = {
#     directories["Documents"]: [
#         "notes.txt",
#         "report.pdf",
#     ],
#     directories["Temp"]: [
#         "dropper.exe",
#         "tmp001.tmp",
#     ],
#     directories["Prefetch"]: [
#         "CMD.EXE-12345.pf",
#         "POWERSHELL.EXE-67890.pf",
#     ],
#     directories["System32"]: [
#         "svchost.exe",
#         "config.ini",
#     ],
# }

# # Write the files
# for destination, filenames in placements.items():
#     for filename in filenames:
#         (destination / filename).write_text(
#             test_files[filename],
#             encoding="utf-8"
#         )

# print("Evidence structure created successfully.")

#Task 24.2: Flat vs Recursive
print("\nTask 24.2: Flat vs Recursive\n")
root = Path("day_24/evidence_root") #Re iterating for explanation may comment later understand there is repetion 
count = 0
for files in root.iterdir():
    count = count + 1
    print(files)

print(f"The count of item : {count}\n")

rglob_count = 0
for files in root.rglob("*"):
    rglob_count += 1
    print(files)
print(f"The count of items : {rglob_count}\n")
glob_count = 0
for files in root.glob("*"):
    glob_count += 1
    print(files)
print(f"The count of items : {glob_count}\n")

#Task 24.3: Pattern-Based Recursive Search
print("\nTask 24.3: Pattern-Based Recursive Search\n")

extension = ["*.exe","*.pf","*.txt"]
print(extension)
for ext in extension:
    
    for files in root.rglob(ext):
        rglob_count += 1
        print(files)
    
#Task 24.4: The os.walk Equivalent
print("\nTask 24.4: The os.walk Equivalent\n")
count_dir = 0
count_files = 0
for rdir, dirs, files in os.walk(root):
    print(f"The current root is {rdir}")
    for dir in dirs:
        print(dir)
        count_dir +=1
    for file in files:
        fullname = os.path.join(rdir,file)
        print(fullname)
        count_files +=1
print(f"sub directory:{count_dir}")
print(f"file number :{count_files}")   

#Drill 24.5: Defensive Walking
print("\nDrill 24.5: Defensive Walking\n")
for file in root.rglob("*"):
    try:
        if file.is_file():
            print(file)
            file_size = file.stat().st_size
            print(f"{file.name} :: {file_size} bytes")
            
    except PermissionError:
        print("There is a permission Error")
    except OSError:
        print("There is OS Error")

# The "Muscle Memory" Gauntlet (The Forensic Sweep)


def forensic_sweep(root_path):
    file_dict = {
    "suspicious": {},
    "other": {}
    }


    sus_ext = [".exe", ".dll", ".ps1", ".bat", ".vbs", ".scr"]
    root_path_obj = Path(root_path)
    for files in root_path_obj.rglob("*"):
        try:
            if files.is_file():
                file_path = str(files.parent)
                file_name = files.name
                file_extension = files.suffix.lower()
                file_size = files.stat().st_size
                if file_extension in sus_ext:
                    file_dict["suspicious"][file_name] = {
                        "f_path" : file_path,
                        "f_extension" : file_extension,
                        "f_size" : file_size
                    }
                else:
                    file_dict["other"][file_name] = {
                        "f_path" : file_path,
                        "f_extension" : file_extension,
                        "f_size" : file_size
                    }
        except PermissionError:
            print(f"Permission denied: {files}")
        except OSError as e:
            print(f"Error accessing {files} :{e}")
    return file_dict



def print_sweep_report(results):
    file_counter = 0
    cat_file_counter = 0
    for category,files in results.items():
        
        if category == "suspicious":
                for file_name,metadata  in files.items():
                    print(f"File: {file_name}")
                    print(f"Path: {metadata['f_path']}")
                    print(f"Extension: {metadata['f_extension']}")
                    print(f"Size: {metadata['f_size']} bytes")                
                    cat_file_counter = cat_file_counter + 1
                    file_counter = file_counter + 1
                print(f"The number of files in {category} is {cat_file_counter}")
        else:
            for file_name,metadata in files.items():
                file_counter = file_counter + 1
    print(f"The total number of files are: {file_counter}")

file_dict = forensic_sweep(root)
print_sweep_report(file_dict)
        
with open("day_24/sweep_report.json","w",encoding="utf-8",errors="ignore") as fwrite:
    json.dump(file_dict,fwrite,indent=4)