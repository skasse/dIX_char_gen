import os
import shutil
from glob import glob


path_source = "N:/working/characters/POC/TASKS/MODEL/char/"

# LISTS GENERATED FROM MAYA "char_collection.ma"
NE_Asian = ['f22_eu_c_aaa_aaa', 'f22_eu_m_baa_bba', 'f30_eu_m_aaa_aaa', 'f40_eu_m_aaa_aaa', 'f03_as_n_aaa_aaa', 'f05_as_m_aaa_aaa', 'f07_as_m_aaa_aaa', 'f10_as_m_aaa_aaa', 'm04_ai_m_aaa_aaa', 'm10_as_c_aaa_aaa', 'm13_as_m_aaa_aaa']
African = ['f35_af_m_aaa_aaa', 'f50_ei_c_aaa_aaa', 'f60_af_m_aaa_aaa', 'f60_af_n_aaa_aaa', 'f30_eu_m_caa_cca', 'f30_eu_c_aaa_aaa', 'f30_eu_c_caa_cca', 'f30_eu_c_baa_bba', 'm30_af_m_aaa_aaa', 'm35_af_c_caa_bba', 'm35_af_c_caa_cca', 'm35_af_c_caa_dda', 'm35_af_m_aaa_aaa', 'm35_af_m_baa_bba', 'm35_af_m_caa_cca', 'm35_af_n_aaa_aaa', 'm35_af_n_aab_bba', 'm35_af_n_baa_bba']
Arctic = [None]
American = ['f22_eu_c_caa_cca', 'f30_eu_n_caa_ccb', 'f30_eu_n_baa_bba', 'f30_eu_n_aaa_aaa', 'm38_ei_c_aab_bba', 'm38_ei_n_aaa_aaa', 'm38_ei_n_aac_cca', 'm38_ei_c_aaa_aaa', 'm38_ei_c_aac_cca', 'm38_ei_m_aaa_aaa', 'm38_ei_m_aaa_bba', 'm38_ei_m_caa_cca', 'f10_hi_m_aaa_aaa', 'f10_hi_n_aaa_aaa', 'f13_hi_m_aaa_aaa', 'f13_hi_n_aaa_aaa', 'm14_hi_m_aaa_aaa', 'm13_hi_n_aaa_aaa']
SE_Asian = ['f25_as_c_aaa_aaa', 'm60_as_m_aaa_aaa', 'f03_as_m_aaa_aaa', 'f05_as_n_aaa_aaa', 'f07_as_n_aaa_aaa', 'f10_as_n_aaa_aaa', 'm03_as_m_aaa_aaa', 'm06_as_m_aaa_aaa', 'm10_as_m_aaa_aaa', 'm10_as_m_aaa_baa']
Pacific_Islander = ['f35_eu_m_aaa_aaa', 'm22_eu_c_aaa_aaa', 'm38_ei_n_aab_bba', 'm10_eu_n_aaa_aaa']
Oceanian = ['f50_ei_n_aaa_aaa', 'f50_ei_m_aaa_aaa', 'm50_aa_c_aaa_aaa', 'm50_aa_m_aaa_aaa', 'm50_aa_n_aaa_aaa']
Caucasoid = ['f22_eu_c_baa_bba', 'f22_eu_m_aaa_aaa', 'f22_eu_m_caa_cca', 'f22_eu_n_aaa_aaa', 'f22_eu_n_baa_bba', 'f22_eu_n_caa_cca', 'f60_eu_m_aaa_aaa', 'f25_eu_c_aaa_aaa', 'f30_eu_m_baa_bba', 'm25_eu_m_aaa_aaa', 'm28_eu_m_aaa_aaa', 'm30_eu_m_aaa_aaa', 'm55_ei_c_aaa_aaa', 'm45_eu_n_aah_aaa', 'm45_eu_m_aaa_aaa', 'f15_ei_c_aaa_aaa', 'f15_ei_m_aaa_aaa', 'f15_ei_n_aaa_aaa', 'm15_ei_n_aaa_aaa', 'm15_ei_c_aaa_aaa', 'm10_as_n_aaa_aaa']


model_paths = [x.replace(os.sep, '/') for x in glob(path_source+"*", recursive=False)]
# print(model_paths)
model_names = [x.split('/')[-1] for x in model_paths]

# for path, name in zip(model_paths, model_names):
#     print(path_source+name)

# model_tokens = [x.split('_') for x in model_names]
# for token in model_tokens:

for model in model_names:
    new_name = model.split("_")
    if model in American:
        new_name[1] = "am"
    if model in SE_Asian:
        new_name[1] = "se"
    if model in Pacific_Islander:
        new_name[1] = "pi"
    if model in Oceanian:
        new_name[1] = "oc"
    if model in Caucasoid:
        new_name[1] = "ca"
    if model in African:
        new_name[1] = "af"
    if model in NE_Asian:
        new_name[1] = "ne"
    if model in Arctic:
        new_name[1] = "ar"
    new_name = "_".join(new_name)
    print(f'changing {path_source+model} to {path_source+new_name}')
    os.rename(path_source+model, path_source+new_name)




# genetic_tokens = set()
# for token in model_tokens:
#     genetic_tokens.add(token[1]) # {'eu', 'af', 'hi', 'ei', 'aa', 'ai', 'as'}

# # {'eu', 'af', 'hi', 'ei', 'aa', 'ai', 'as'}

# genetic_tokens = {'eu':'ca', 'af':'af', 'hi':'am', 'ei':'ca', 'aa':'oc', 'ai':'am', 'as':'as'}
# for token in model_tokens:
#     if token[1] in genetic_tokens:
#         token[1] = genetic_tokens[token[1]]

# model_names_mod = ['_'.join(x) for x in model_tokens]

# for i in range(0, len(model_names)):
#     print("{0} changed to {1}".format(path_source[:-1]+model_names[i], path_source[:-1]+model_names_mod[i]))

# # for name in model_names_mod:
# #     print(path_source[:-1]+name)