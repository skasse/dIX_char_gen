# this script copies the TG images from g drive to local drive. 

import os
from glob import glob
import shutil

# sourcePath = "G:/Shared drives/TriplegangersFemaleData/neutrals/"
# destPath = "N:/working/characters/images/TG_processed/female/"
# sex = "f"

sex = "Male"
# sex = "Female"
sourcePath = f'"G:/Shared drives/Triplegangers{sex}Data/neutrals/"'
destPath = f'"N:/working/characters/images/TG_processed/{sex.lower()}/"'

print(sourcePath, destPath )

if not os.path.exists(destPath):
    os.mkdir(destPath)
    print("created dir:", destPath)
else:
    print("dir exists")

imagePath = "processed/models/01_Neutral_mm_wrap_noHaircap.png"
texturePaths = [x.replace(os.sep, '/') for x in glob(sourcePath+"**/"+imagePath)]
modelName = [x.split("/")[4].replace("Age", sex).replace("-", "_") for x in texturePaths]
# print(texturePaths)
# print(modelName)


texturePaths_Dest = [destPath+x+"__01_Neutral_mm_wrap_noHaircap.png" for x in modelName]
# print(texturePaths_Dest)

for a,b in zip(texturePaths, texturePaths_Dest):
    print("moving from:\n{0}\nto \n{1}".format(a, b))
    # shutil.copy(a, b)