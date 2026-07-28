import json
import re

def read_evidence(file_path) :
    # Reading the evidence
    try:
        with open(file_path,"r",encoding="utf-8",errors="ignore") as f:
            incident_data = f.read()
            return incident_data
    except FileNotFoundError:
        print(f"Error: file {file_path} is missing, check path and cwd!")
        return None




# Define compiled patterns using word boundaries (\b) and non-capturing groups (?:)
MD5_pattern = re.compile(r"\b[a-fA-F0-9]{32}\b")
SHA1_pattern = re.compile(r"\b[a-fA-F0-9]{40}\b")
SHA256_pattern = re.compile(r"\b[a-fA-F0-9]{64}\b")
ipv4_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
email_pattern = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b")
domain_pattern = re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b")
mac_pattern = re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b")



# Extract candidates 

def extract_iocs(text):

    raw_MD5 = MD5_pattern.findall(text)
    raw_SHA1 = SHA1_pattern.findall(text)
    raw_SHA256 = SHA256_pattern.findall(text)
    raw_ipv4 = ipv4_pattern.findall(text)
    raw_domain = domain_pattern.findall(text)
    raw_email = email_pattern.findall(text)
    raw_mac = mac_pattern.findall(text)


    #Step 4 — Validate and deduplicate
    valid_ip_list =[]
            
    def is_ip_valid(ip) :
        ip_parts = ip.split(".")
        for part in ip_parts:
            num =  int(part)
            if num < 0 or num > 255:
                return False        
        return True

    for item in raw_ipv4:
        if is_ip_valid(item) == True:
            valid_ip_list.append(item) 


    iocs = {
        "ipv4": list(set(valid_ip_list)),
        "md5": list(set(raw_MD5)),
        "sha1": list(set(raw_SHA1)),
        "sha256": list(set(raw_SHA256)),
        "email": list(set(raw_email)),
        "domain": list(set(raw_domain)),
        "mac": list(set(raw_mac))
    }
    
    return iocs

def write_report(iocs, output_path):
# Write the report to a new JSON file with indent=4 for human-readable formatting
    with open(output_path, "w", encoding="utf-8", errors="ignore") as fwrite:
        json.dump(iocs, fwrite, indent=4)

def main():
    input_file = "raw_incident_notes.txt"
    output_file = "extracted_iocs.json"

    text = read_evidence(input_file)
    if text is None:
        return
    extracted_iocs = extract_iocs (text)
    write_report(extracted_iocs,output_file)
    


if __name__ == "__main__":
    main()