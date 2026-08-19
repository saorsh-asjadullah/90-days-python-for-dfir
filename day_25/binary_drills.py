from pathlib import Path
import json

path = Path("C:\\Users\\phoenix\\Documents\\Python_Labs_Codes\\90-days-python-for-dfir\\day_25")

file_path = Path(path/"test_binary.bin")

# Task 25.1: Create and Read Raw Bytes
print("\nTask 25.1: Create and Read Raw Bytes\n")

with open(file_path, "wb") as f:
    wdata = b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00'
    f.write(wdata)

with open(file_path, "rb") as f:
    rdata = f.read()
    brdata = str(rdata)
    print(rdata)
    print(type(rdata)) # gives <class 'bytes'>
    print(type(brdata)) # gives <class 'str'>

# Task 25.2: Index vs Slice
print("\nTask 25.2: Index vs Slice\n")
print(rdata[0])  # 77  (the ASCII value of 'M')
print(type(rdata[0])) 
print(rdata[0:2]) # b'MZ'  (slicing gives you bytes back)
print(type(rdata[0:2]))
print(chr(rdata[0])) #convert the integer back to its character


#Task 25.3: Hex Conversion
print("\nTask 25.3: Hex Conversion\n")
data = b"MZ Dummy Executable"
print(data.hex()) #Convert your data to a hex string
print(type(data.hex())) #gives <class 'str'> as .hex() Convert your data to a hex string
print(data.hex(" "))
byte_hex_string = "25504446"
print(bytes.fromhex(byte_hex_string)) #bytes.fromhex - convert it to bytes

#Task 25.4: Read Only the Header
print("\n#Task 25.4: Read Only the Header\n")
with open(file_path,"rb") as f:
    header = f.read(4)
    print(header)
    print(header.hex(" "))
    f.seek(0)
    signature = f.read(2)
    print(signature)


# Task 25.5: Build a Test File Set


test_files = {
    "fake_exe.txt": b"MZ\x90\x00Dummy Executable",
    "real_pdf.pdf": b"%PDF-1.7 Dummy PDF",
    "fake_pdf.pdf": b"MZ\x90\x00Dummy Executable disguised as PDF",
    "archive.zip": b"PK\x03\x04Dummy ZIP archive",
    "image.png": b"\x89PNG\r\n\x1a\nDummy PNG image",
}

# Write the files
# path.mkdir(parents=True,exist_ok=True)
# for filename, data in test_files.items():
#     (path / filename).write_bytes(data)

for filename,data in test_files.items():
    file_p = path/filename
    with open (file_p,"wb") as fw:
        fw.write(data)


print("Test file set created successfully.")

# The "Muscle Memory" Gauntlet (The File Signature Validator)
print('\nThe "Muscle Memory" Gauntlet (The File Signature Validator)\n')

SIGNATURES = {
    "4d5a": "Windows Executable (PE)",
    "25504446": "PDF Document",
    "504b0304": "ZIP Archive",
    "89504e47": "PNG Image",
    "ffd8ff": "JPEG Image",
    "7f454c46": "Linux Executable (ELF)"
}

def read_magic(file_path,num_bytes=8):
    try:
        with open(file_path,"rb") as rb_file:
            header = rb_file.read(num_bytes)
            hex_header = header.hex()
            return hex_header
    except(PermissionError,OSError) as e:
        print(f"Encountered {e}")
        return None
    
def identify_file(magic_hex):
    if magic_hex is None:
        return "Unknown"
    for sign, file_type in SIGNATURES.items():
        if magic_hex.startswith(sign):
            return file_type
        
    return "Unkown"

def validate_extension(file_path,identified_type):
    MAPPING = {
        "Windows Executable (PE)" : [".exe",".dll",".sys"],
        "PDF Document" : [".pdf"],
        "ZIP Archive" : [".zip"],
        "PNG Image" : [".png"],
        "JPEG Image" :[".jpeg",".jpg"],
        "Linux Executable (ELF)" :[".elf"]

    }
    extension = file_path.suffix
    extension = extension.lower()

    if extension in MAPPING.get(identified_type,[]):
        return True
    else:
        return False

result_dict = {
    "matched": {},
    "EXTENSION MISMATCH DETECTED": {}
}
for file in path.rglob("*"):
    try:
        if file.is_file():
            print(file)
            magic_hex=read_magic(file)
            sign = identify_file(magic_hex)
            if validate_extension(file,sign) == True:
                result_dict["matched"][str(file)] = sign
            else:
                result_dict["EXTENSION MISMATCH DETECTED"][str(file)] = sign



    except(PermissionError,OSError) as e:
        print(f"{file} has {e}")

report_path = path / "signature_report.json"

with open(report_path, "w") as fw:

    json.dump(
        result_dict,
        fw,
        indent=4
    )
