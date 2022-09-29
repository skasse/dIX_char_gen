"""
This script takes processed skin channels/textures, renames and moves them to their respective name/image path.
"""

import os
from glob import glob
import shutil



sex = "male"
sex = "female"
sourcePath = "N:/working/characters/images/TG_processed/{}/".format(sex)
framesPath = "N:/working/characters/images/TG_processed/{}/frames/".format(sex)
outNukePath = "N:/working/characters/images/TG_processed/{}/out_nuke/".format(sex)

imagePath = "*.png"
# texturePaths = [x.replace(os.sep, '/') for x in glob(sourcePath+"**/"+imagePath)]
texturePaths = [x.replace(os.sep, '/') for x in glob(sourcePath+imagePath)]
modelNames = [x.split("/")[-1].split("__")[0] for x in texturePaths]

print("texturePaths\n", texturePaths[0:5])
print("modelNames\n", modelNames[0:5])

nameEnumDict = {}
for name,count in enumerate(modelNames):
    nameEnumDict[count] = name
# example result = {'m18_DavidChang': 0, 'm18_JackYien': 1, 'm18_JuanHsu': 2...}

# move sorted:names to /frames/#.png | keep association in nameEnumDict

def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

# get_key(nameEnumDict, 100)
destPath = "N:/working/characters/POC/TASKS/TEXTURE/char/skin/{}/".format(sex)
# do work
if not os.path.exists(destPath):
    os.mkdir(destPath)
    print("created dir:", destPath)
else:
    print("dir exists")
### find <channel>_<#>_<udim>.png and move to sorted/<name>/<channel>_<udim>.png

# get image paths from nuke exports
outNukeTexPath = [x.replace(os.sep, '/') for x in glob(outNukePath+"*_*_*.png")]
# example result = 'N:/working/characters/images/TG_processed/male/out_nuke/diff_0_1001.png'

# Extract original name and new path/imagename from path
frameNameDict = {}
for path in outNukeTexPath:
    imageName = path.split('/')[-1].split('.')[0]
    ext = path.split('/')[-1].split('.')[1]
    channel = imageName.split('_')[0]
    key = imageName.split("_")[1]
    udim = imageName.split("_")[2]
    newPath = "{4}/{0}".format(get_key(nameEnumDict, int(key)), channel, udim, ext, destPath)
    imageName = "{0}_{1}.{2}".format(channel, udim, ext)
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    # frameNameDict[path] = newPath
    if channel == "nm":
        shutil.copy(path, newPath+"/"+imageName)
        print("moved {} to {}".format(path, newPath+"/"+imageName))