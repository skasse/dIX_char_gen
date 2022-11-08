import os
import re
from glob import glob


# seach path
model_paths = "N:/working/characters/POC/TASKS/MODEL/char/**/asset/model.usda"

# replace os sep
models = [x.replace(os.sep, '/') for x in glob(model_paths)]
# models = ["N:/working/characters/POC/temp/model.usda"]
# models = ["N:/working/characters/POC/TASKS/MODEL/char/f60_af_n_aaa_aaa/asset/model.usda"]
# test = "N:/working/characters/POC/temp/test.txt"
# output = "N:/working/characters/POC/temp/model_new.usda"


def get_lines(filename):
    usd_file = open(filename, 'r')
    lines = usd_file.readlines()
    usd_file.close()
    return lines

def find_dup(lines):
    model_set = set()
    line_set = set()
    joint_set = set()
    dup_set = set()
    dup_dict = {}
    for i in range(len(lines)):
        ck = lines[i]
        if re.match(".*uniform token.*joints*", ck):
            joint_list = ck.lstrip(" ").rstrip("\n").split("=")[-1].rstrip("]").lstrip(" [").split(",")
            last_joint = ["/".join(x.split('/')[-1:]) for x in joint_list]
            dup_joints = [x for x in last_joint if last_joint.count(x) > 1]
            [dup_set.add(x) for x in dup_joints]
            for dup in dup_joints:
                for joint in joint_list:
                    if dup in joint:
                        joint_set.add(joint)
    if len(joint_set) > 0:
        print(model, dup_set)#, joint_set)
        # return min(joint_set)
    # if len(dup_set) > 0:
    #     return dup_set
            # if len(dup_joints) > 0:
            #     print(dup_joints)
                # for dup in dup_joints:
                #     joints_set.add(dup)
            # joints_set = set(dup_joints)
    # print(dup_joints)
    # for joint in joints_set:
    #     print(joint)
            # find joints from dup last joint
    #         if len(dup_joints) > 0:
    #             for joint in joint_list:
    #                 for dup in dup_joints:
    #                     if dup in joint:
    #                         joints_set.add(joint)
                    # print(joint)
            # if joint in joint_list:
                # print(joint)
        # print(joints_set)
                # print(model, i, dup_joints)   
            # [joints_set.add(x) for x in last_joint if last_joint.count(x) > 1]
    #     for j in joints_set:
    #         print(j, len(joints_set))
            # for dup in dup_joints:
            #     # print(dup)
            #     k = 0
            #     for joint in joint_list:
            #         if dup in joint:
            #             joints_set.add(joint)
                        # key = joint.split('/')[-1].strip('"')
                        # # print(key)
                        # newjoint = joint.replace(key, key+str(k))
                        # print(newjoint)
                        # k += 1
            # [joints_set.add(x) for x in dup_joints]
            # line_set.add(i)
            #     print(model, dup_joints, len(dup_joints))
            # for i, joint in enumerate(dup_joints, 0):
            #     print(i, joint)
            # print(f'{"/".join(dup_joints)}"')
                # print(dup_joints, "/".join(dup_joints), f'{dup_joints[0]}01', f'{dup_joints[1]}02')
            # print(f'replace /{"/".join(dup_joints)}" with /{dup_joints[0]}01/{dup_joints[1]}02", then /{dup_joints[0]}" with /{dup_joints[0]}01"')
            
            # newline = ck.replace(f'/{"/".join(dup_joints)}"',f'/{dup_joints[0]}01/{dup_joints[1]}02"').replace(f'/{dup_joints[0]}"',f'/{dup_joints[0]}01"')
            # print(newline)
            # dup_dict[i] = newline
            #     model_set.add(model)
            #     line_set.add(i)
            #     joints_set.add("/".join(dup_joints))
            #     dup_dict[model] = "/".join(dup_joints)
                # print(f'model: {model}\nline: {i}\nduplicates: {"/".join(dup_joints)}\n\n')
    # if len(joints_set) > 0:
    #     print(joints_set)
    # if len(model_set) > 0:
        # print(model_set, line_set, joints_set)
        # print(dup_dict)

for model in models:
    # print(model)
    find_dup(get_lines(model))
    # dups = find_dup(get_lines(model))
    # if dups:
    #     print(dups)
#     orig = get_lines(model)=
#     print(orig[corrected[0]])
#     print(corrected[1])
#     orig[corrected[0]] = corrected[1]
#     with open(output, 'w') as f:
#         for line in orig:
#             f.write(str(line))


# find the duplicates
# find the skel:joints w/ duplicate



"""
 "CC_Base_BoneRoot/CC_Base_Hip/CC_Base_Waist/CC_Base_Spine01/CC_Base_Spine02/CC_Base_NeckTwist01/CC_Base_NeckTwist02/CC_Base_Head/Camila_Brow"
 "CC_Base_BoneRoot/CC_Base_Hip/CC_Base_Waist/CC_Base_Spine01/CC_Base_Spine02/CC_Base_NeckTwist01/CC_Base_NeckTwist02/CC_Base_Head/Camila_Brow/Camila_Brow"

CC_Base_Head/Camila_Brow"
CC_Base_Head/Camila_Brow/Camila_Brow"






"Diamond_Earing/CC_Base_Pivot"
"Diamond_Earing_1_/CC_Base_Pivot"
"Diamond_Earing/CC_Base_Pivot/Cylinder_Cylinder_Material_001"
"Diamond_Earing_1_/CC_Base_Pivot/Cylinder_Cylinder_Material_001"
"Diamond_Earing/CC_Base_Pivot/Icosphere_Icosphere_001_Material"
"Diamond_Earing_1_/CC_Base_Pivot/Icosphere_Icosphere_001_Material"
"Diamond_Earing/CC_Base_Pivot/eyesteel_001_dmesh_001_Material_002"
"Diamond_Earing_1_/CC_Base_Pivot/eyesteel_001_dmesh_001_Material_002"
"Diamond_Earing/CC_Base_Pivot/eyesteel_dmesh_000_Material_003"
"Diamond_Earing_1_/CC_Base_Pivot/eyesteel_dmesh_000_Material_003"
"""