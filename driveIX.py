import filecmp
import os
import shutil
from glob import glob
# import maya.cmds as mc

network_path = "O:/Devs/SDG/POC/"
local_path = "N:/working/characters/POC/"
model_path = "TASKS/MODEL/char/"
pubAsset_path = "PUBLISH/assets/char/"
pre_copy_path = "N:/working/characters/POC/TASKS/MODEL/unprocessed/"




result = filecmp.dircmp(network_path+model_path, local_path+model_path) # model.usda
result = filecmp.dircmp(network_path+pubAsset_path, local_path+pubAsset_path) # asset.usda
print(result.right_only)
# print(result.report())
# for results in result.right_only:
    # shutil.copy(local_path+pubAsset_path+results, pre_copy_path+results)

def rmTex():
    search_path = "N:/working/characters/POC/TASKS/MODEL/char/**/textures/"
    textures = [x.replace(os.sep, '/') for x in glob(search_path, recursive=True)]
    return textures
    # [shutil.rmtree(x) for x in textures]

def publishPrep():
    network_path = "O:/Devs/SDG/POC/TASKS/TEXTURE/char/skin/**"
    local_path = "N:working/characters/POC/TASKS/TEXTURE/char/skin/**"
    pre_copy_path = "N:/working/characters/POC/TASKS/MODEL/unprocessed/"
    return filecmp.dircmp(network_path, local_path)
    

    for results in result.right_only:
        shutil.copy(local_path+results, pre_copy_path+results)

# publishPrep()
sex = "female"
sex = "male"

dir_01 = "O:/Devs/SDG/POC/"
dir_02 = "N:working/characters/POC/"

dir_common = "TASKS/TEXTURE/char/skin/{}".format(sex)
network_path = dir_01+dir_common
local_path = dir_02+dir_common

print(network_path)
# result = filecmp.dircmp(network_path, local_path)
result = filecmp.dircmp(dir_01, dir_02)
print(result.right_only)

# for results in result.right_only:
#     shutil.copy(dir_02+results, dir_01+results)


###########

sourcelist = ["N:/working/characters/POC/TASKS/MODEL/char/f25_eu_c_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/f30_eu_n_baa_bba/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/f35_af_m_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/f35_eu_m_aaa_aaa/asset/asset.usda",
"N:/working/characters/POC/TASKS/MODEL/char/f35_eu_m_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/f60_af_m_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/f60_af_n_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/m25_eu_m_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/m28_eu_m_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/m30_eu_m_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/m45_eu_m_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/m45_eu_n_aah_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/m55_ei_c_aaa_aaa/asset/model.usda",
"N:/working/characters/POC/TASKS/MODEL/char/m60_as_m_aaa_aaa/asset/model.usda",]

destlist = [x.replace("N:/working/characters/POC/TASKS/MODEL/char/", "O:/Devs/SDG/TASK/CHARACTERS/SPECIFICS/") for x in sourcelist]


import shutil
import os
for a,b in zip(sourcelist, destlist):
    print(a, b)
    if not os.path.exists(b):
        os.makedirs(b)# "/".join(b.split('/')[:-1]))
    shutil.copy(a,b)

###################

# path = "O:/Devs/SDG/TASK/CHARACTERS/SPECIFICS/**/model"
path = "O:/Devs/SDG/TASK/CHARACTERS/SPECIFICS/**/asset/asset.usda"

from glob import glob

results = glob(path)
print(results)

import os
for result in results:
    os.remove(result)
    print(f'{result} removed.\n')

####################


def print_asset_lists():
    nodes = mc.ls(sl=1)
    for node in nodes:
        print(f'{node} = {mc.listRelatives(node)}')

# SPREAD OUT SELECTION ALONG X
for i, each in enumerate(mc.ls(sl=1), 0):
    mc.xform(each, t=[20*i, 0, 0])

# hide all hairs
hair_list = ["*Hair*", "*Bun*", "*Bang*", "*Side_part_wavy*", "*Short_blowback*", "*Classic_short*", "*Camila_Brow*", "*Female_Angled*", "*Female_Brow*", "*Kevin_Brow*", "*Mustache_Horseshoe*", "*Male_Bushy*", "*simon*", "*Sideburns_Narrow*", "*Chinstrap_Thick*", "*Soul_Path_Thick*", "*Stubble_Neck*"]
mc.hide(hair_list)

# move all to origin
mc.xform(mc.ls("???_??_?_???_???"), t=[0,0,0])



# import assets from /char/**
paths = [x.replace(os.sep, '/') for x in glob(path)]
names = [x.split("/")[-3] for x in paths]

for name,path in zip(names,paths):
    print(name, path)
    mc.file(path, i=True)
    mc.rename("World", name)






## search files for substring
import os
from glob import glob
search_path = "C:\\Scripts\\ov\\**.py"
results = [x.replace(os.sep, '/') for x in glob(search_path)]    

def get_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines

substring = "N:/working/characters/POC"
for result in results:
    script = get_lines(result)
    for i in range(len(script)):
        # print(script[i])
        ck = script[i]
        if substring in ck:
            print(result, i, ck)