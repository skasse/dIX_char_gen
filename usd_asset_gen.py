""" 
    This file crawls the path variables looking for:
    skin materials
    asset models
    ...cont'd
    creating an array from all permutations and outputting them into unique asset.usda
    from an original template.usda
"""


from glob import glob
import os



# path variables
sourcePath = "N:/working/characters/POC/"
# sourcePath = "O:/Projects/drive_ix_content/users/skassekert/POC/"
skinpath = sourcePath+"TASKS/LOOKDEV/char/skin/"
modelpath = sourcePath+"TASKS/MODEL/char/**/asset/"
mtldef = sourcePath+"TASKS/LOOKDEV/default/material_assignments.usda"
destPath = sourcePath+"PUBLISH/assets/char/"
template = sourcePath+"variations/template/asset_template.usda"
lookback = "../../../"


# get existing skin texture layers
layers = [x.replace(os.sep, '/') for x in glob(skinpath+"/**.usda")]

# get existing asset models
models = [x.replace(os.sep, '/') for x in glob(modelpath+"/model.usda")]

variations = {}
# mindex = 0
for model in models:
    for layer in layers:
        n0 = model.split("/")[-3]#.replace("_", "")
        n1 = layer.split("/")[-1].split(".")[0]#.replace("_", "")
        varName = "CH_{0}__{1}".format(n0, n1)
        variations[varName]='subLayers = [\n\t@{0}@, \n\t@{1}@, \n\t@{2}@\n]'.format(
            layer.replace(sourcePath, lookback),
            mtldef.replace(sourcePath, lookback),
            model.replace(sourcePath, lookback)
            )



if not os.path.exists(destPath):
    os.mkdir(destPath)
    print("created dir:", destPath)
else:
    print("already exists")

varcount = len(variations)
index = 0
if os.path.exists(template):
    # print(filename)
    s = None
    for var in variations:
        # print(vars)
        index+=1
        newfile = destPath+"{}.usda".format(str(var))
        #  print(newfile)
        with open(template, 'r') as f:
            s = f.read()
        with open(newfile, 'w') as f:
            s = s.replace("subLayers = []", variations[var])
            f.write(s)
        print("{0}/{1}".format(index, varcount))
print("created {0} assets, from {1} models and {2} skin materials".format(len(variations), len(models), len(layers)))