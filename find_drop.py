import json
from pathlib import Path
import os



fn=os.path.join(Path(__file__).parent,"airdrop_list.json")
    
key_list=["youaddress",
"0xd5e1DB000E8e87EE7B230fC0070CFB7360971893"]  

with open(fn,'r') as a:
    lucky_list = json.loads(a.read())

huge_set = set (lucky_list)

common_elements = [item for item in key_list if item in huge_set]

print(f'found{len(common_elements)}',common_elements)