import sys
import hashlib
import hmac
import re
from binascii import unhexlify, hexlify

key = "8544E3B47ECA58F9583043F8"

if len(sys.argv) != 2:
    print("Usage: supermicro-ipmi-key <MAC>")
    sys.exit(1)

mac = sys.argv[1]


def calculate_key(data, key):
    data_bytes = unhexlify(data)
    key_bytes = unhexlify(key)
    return hmac.new(key_bytes, data_bytes, hashlib.sha1).hexdigest()


if re.match(r"^([\da-zA-z][\da-zA-z]:){5}[\da-zA-z][\da-zA-z]$", mac):
    mac = mac.replace(":", "")
    license_key = calculate_key(mac, key)[:24]

    for i in range(0, 24, 4):
        print(license_key[i:i+4], end=" ")
    print()
else:
    print(f"Invalid mac address: {mac}")
