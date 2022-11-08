from hashlib import new
import os
from glob import glob
import shutil

path = 'N:/working/characters/POC/TASKS/TEXTURE/char/skin/1k/'
path = 'N:/working/characters/POC/TASKS/TEXTURE/char/skin/u18/'

# texture = [x.replace(os.sep, '/') for x in glob(path+"**/**.png")]
origname = [x.replace(os.sep, '/') for x in glob(path+'*')]
oldname = [x.replace(os.sep, '/').rpartition('/')[-1].rpartition('_')[-1] for x in glob(path+'*')]
newname = ["".join([path, 'u18_', x]) for x in oldname]
# print(newname)

for old, new in zip(origname, newname):
    os.rename(old, new)
