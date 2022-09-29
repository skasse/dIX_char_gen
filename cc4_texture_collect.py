"""
scrapes textures from a source, renames, and moves them to a new dir
"""

import re
from glob import glob
import os
import shutil

#path = "C:\\tmp\\"
udim = {"Head":1001,
        "Body":1002,
        "Arm":1003,
        "Leg":1004,
        "Nails":1005}
# print(udim["Head"])
asset = "male_0005"
sourcePath = "N:\\working\\characters\\POC\\assets\\char\\{0}\\cc4".format(asset)
destPath = "N:\\working\\characters\\POC\\assets\\char\\{0}\\textures_collected".format(asset)
# if not os.path.isdir(destPath):
if not os.path.exists(destPath):
    os.mkdir(destPath)
    print("created dir:", destPath)
else:
    print("dir exists")
# genderPath = sourcePath.split("\\")[-1].split("_")[0]
# ethnicPath = sourcePath.split("\\")[-1].split("_")[1]
# indexPath = sourcePath.split("\\")[-1].split("_")[-1]
# print(genderPath, ethnicPath, indexPath)
# destPath = "N:\\working\\characters\\texture\\UDIM\\{0}\\{1}\\skin_{2}".format(genderPath, ethnicPath, indexPath)
textures = [x for x in glob(sourcePath+"\\**\\*.*", recursive=True)]
for texture in textures:
    print(len(texture))
    # print(texture)
    texName = texture.split("\\")[-1]
    if texName.split(".")[-1] == "fbm":
        continue
    elif "Std_Skin_" in texName:
        bodyPart = texName.split("_")[2]
        texNameSplit = texName.split("_")[-1].split(".")
        mapType = texNameSplit[0]
        texExt = texNameSplit[-1]
        # print(texName, bodyPart, udim[bodyPart], mapType, texExt)
        udimName = "skin_base_{0}.{1}.{2}".format(mapType, udim[bodyPart], texExt)
        texName = udimName
    print("copy {0} to \n {1}".format(texture, destPath+"\\{0}_{1}".format(asset, texName)))
    shutil.copy(texture, destPath+"\\"+texName)
    # print("copy complete")

