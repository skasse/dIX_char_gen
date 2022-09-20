"""
    creates a dictionary of texture dir paths, and self similar mtl names, 
    and injects that information into a material layers via material template usda
"""


from glob import glob
import os

sourcePath = "N:/working/characters/POC/"
texpath = sourcePath+"TASKS/TEXTURE/char/skin/"
lookdevPath = sourcePath+"TASKS/LOOKDEV/char/skin/"
template = lookdevPath+"template/skin_mtl_template.usda"
lookback = "../../../"

textures = [x.replace(os.sep, '/') for x in glob(texpath+"/**/", recursive=True)]

materials = {}
for texture in textures:
    # check correct name resolve
    if len(texture.split("_"))==2:
        print(texture)
        material_name = "".join(texture.split('/')[-2])#.replace("_", "")
        # material_name = "test"
        print(material_name)
        materials[material_name] = texture.replace(sourcePath+"TASKS/", lookback)
mtlcount = len(materials)

index = 0
if os.path.exists(template):
    s = None
    for mtl in materials:
        index+=1
        # print(mtl)
        newfile = (lookdevPath+"M_{}.usda".format(mtl)).replace("/", "/")
        # print(newfile)
        print(materials[mtl])
        with open(template, 'r') as f:
            s = f.read()
        with open(newfile, 'w') as f:
            s = s.replace("<material_name>", mtl)
            s = s.replace("<texture_path>", materials[mtl].replace('/', '/'))
            f.write(s)
        print("{0}/{1}".format(index, mtlcount))
    print("created {} materials".format(mtlcount))