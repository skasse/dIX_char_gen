import filecmp
import os
import shutil
from glob import glob


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



# Adult Characters
American = ['f22_eu_c_caa_cca', 'f30_eu_n_caa_ccb', 'f30_eu_n_baa_bba', 'f30_eu_n_aaa_aaa', 'm38_ei_c_aab_bba', 'm38_ei_n_aaa_aaa', 'm38_ei_n_aac_cca', 'm38_ei_c_aaa_aaa', 'm38_ei_c_aac_cca', 'm38_ei_m_aaa_aaa', 'm38_ei_m_aaa_bba', 'm38_ei_m_caa_cca']
SE_Asian = ['f25_as_c_aaa_aaa', 'm60_as_m_aaa_aaa']
PacificIslander = ['f35_eu_m_aaa_aaa', 'm22_eu_c_aaa_aaa', 'm38_ei_n_aab_bba']
Oceanian = ['f50_ei_n_aaa_aaa', 'f50_ei_m_aaa_aaa', 'm50_aa_c_aaa_aaa', 'm50_aa_m_aaa_aaa', 'm50_aa_n_aaa_aaa']
Caucasoid = ['f22_eu_c_baa_bba', 'f22_eu_m_aaa_aaa', 'f22_eu_m_caa_cca', 'f22_eu_n_aaa_aaa', 'f22_eu_n_baa_bba', 'f22_eu_n_caa_cca', 'f60_eu_m_aaa_aaa', 'f25_eu_c_aaa_aaa', 'f30_eu_m_baa_bba', 'm25_eu_m_aaa_aaa', 'm28_eu_m_aaa_aaa', 'm30_eu_m_aaa_aaa', 'm55_ei_c_aaa_aaa', 'm45_eu_n_aah_aaa', 'm45_eu_m_aaa_aaa']
African = ['f35_af_m_aaa_aaa', 'f50_ei_c_aaa_aaa', 'f60_af_m_aaa_aaa', 'f60_af_n_aaa_aaa', 'f30_eu_m_caa_cca', 'f30_eu_c_aaa_aaa', 'f30_eu_c_caa_cca', 'f30_eu_c_baa_bba', 'm30_af_m_aaa_aaa', 'm35_af_c_caa_bba', 'm35_af_c_caa_cca', 'm35_af_c_caa_dda', 'm35_af_m_aaa_aaa', 'm35_af_m_baa_bba', 'm35_af_m_caa_cca', 'm35_af_n_aaa_aaa', 'm35_af_n_aab_bba', 'm35_af_n_baa_bba']
NE_Asian = ['f22_eu_c_aaa_aaa', 'f22_eu_m_baa_bba', 'f30_eu_m_aaa_aaa', 'f40_eu_m_aaa_aaa']

