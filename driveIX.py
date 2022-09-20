import filecmp
import os
import shutil
from glob import glob


network_path = "O:/Devs/dh_sdg_storage/POC/"
local_path = "N:/working/characters/POC/"
model_path = "TASKS/MODEL/char/"
pubAsset_path = "PUBLISH/assets/char/"
pre_copy_path = "N:/working/characters/POC/TASKS/MODEL/unprocessed/"




# result = filecmp.dircmp(network_path+model_path, local_path+model_path) # model.usda
result = filecmp.dircmp(network_path+pubAsset_path, local_path+pubAsset_path) # asset.usda
print(result.right_only)
# print(result.report())
for results in result.right_only:
    shutil.copy(local_path+pubAsset_path+results, pre_copy_path+results)

def rmTex():
    search_path = "N:/working/characters/POC/TASKS/MODEL/char/**/textures/"
    textures = [x.replace(os.sep, '/') for x in glob(search_path, recursive=True)]
    return textures
    # [shutil.rmtree(x) for x in textures]

def publishPrep():
    network_path = "O:/Devs/dh_sdg_storage/POC/PUBLISH/assets/char/"
    local_path = "N:/working/characters/POC/PUBLISH/assets/char/"
    pre_copy_path = "N:/working/characters/POC/TASKS/MODEL/unprocessed/"
    return filecmp.dircmp(network_path, local_path)
    

    for results in result.right_only:
        shutil.copy(local_path+results, pre_copy_path+results)