import re
from glob import glob
import os

#path = "C:\\tmp\\"
varpath = "N:/working/characters/POC/variations/"
filename = varpath+"/template/asset_template.usda"
newfile = varpath+"asset_01.usda"

if os.path.exists(filename):
    print(filename)
    s = None
    with open(filename, 'r') as f:
        s = f.read()
    with open(newfile, 'w') as f:
        s = s.replace("subLayers = []", newLayers)
        # s = re.sub(r'(\w*_{2})', 'base__', s)
        f.write(s)


# subLayers = \[(.*\n*.*)*[^/[]