import base64
import re

# Task 26.1: Text ↔ Bytes
print("\nTask 26.1: Text ↔ Bytes")

command = "net user administrator /active:yes"
command_bytes = command.encode("utf-8")
decoded_command_bytes = command_bytes.decode("utf-8")
print(f"The decoded string is '{decoded_command_bytes}'")

# Task 26.2: The Full Conversion Chain
print('\nTask 26.2: The Full Conversion Chain')
command_string = "cmd.exe"
print(f'Command {command_string} in string')
print(command_string)
command_bytes = command_string.encode("utf-8")
print(f"Command {command_string} in bytes")
print(command_bytes)
command_hex = command_bytes.hex()
print(f"Command {command_string} in Hex")
print(command_hex)
command_back_to_bytes = bytes.fromhex(command_hex) # hex string → bytes
print(f"Command {command_string} Converted Back to bytes from {command_hex}")
print(command_back_to_bytes)
command_back_to_strings = command_back_to_bytes.decode("utf-8")
print(f"Command {command_string} Converted Back to Strings from {command_back_to_bytes}")
print(command_back_to_strings)

#Task 26.3: Base64 Encode and Decode
print("\nTask 26.3: Base64 Encode and Decode")
command = "whoami /priv"
command_bytes = command.encode("utf-8")
command_b64 = base64.b64encode(command_bytes).decode()
print(f"Printing {command} in base64 - > {command_b64}")
command_b64_decode = base64.b64decode(command_b64)
command_b64_decode_string = command_b64_decode.decode("utf-8")
print(f"Printing encoded command '{command_b64}' into bytes '{command_b64_decode_string}'")

#Task 26.4: Decode a PowerShell EncodedCommand
print("\nTask 26.4: Decode a PowerShell EncodedCommand")
payload = "Get-Process | Where-Object {$_.Name -eq 'lsass'}"
print(f"The payload is '{payload}'")
enc_payload = base64.b64encode(payload.encode("utf-16-le")).decode()
print(f"The encoded payload is '{enc_payload}'")
dec_payload = base64.b64decode(enc_payload).decode("utf-16-le")
print(f"The decoded payload is '{dec_payload}'")

#Task 26.5: Base64 Detection
print('\nTask 26.5: Base64 Detection')
def looks_like_base64(text):
    try:
        reg_base64 = r"^([A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"
        len_text = len(str(text))
        if len_text % 4 == 0 and len_text > 15:
            match_b64 = re.search(reg_base64,text)
            if match_b64 is not None:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"The error is {e}")

boolean1 = looks_like_base64(payload)
boolean2 = looks_like_base64(enc_payload)
boolean3 = looks_like_base64(command_hex)
print(f"The payload '{payload}' is base64 ? {boolean1}")
print(f"The payload '{enc_payload}' is base64 ? {boolean2}")
print(f"The payload '{command_hex}' is base64 ? {boolean3}")
