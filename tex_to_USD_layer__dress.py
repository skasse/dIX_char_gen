"""
    creates a dictionary of texture dir paths, and self similar mtl names, 
    and injects that information into a material layers via material template usda
"""


from glob import glob
import os

sourcePath = "N:/working/characters/POC/"
texpath = sourcePath+"TASKS/TEXTURE/cloth/dress/summer/default/"
lookdevPath = sourcePath+"TASKS/LOOKDEV/cloth/dress/summer/"
template = lookdevPath+"template/dress_summer_mtl_template.usda"
lookback = "../../../../"
variant_name = "dressFabric"

textures = [x.replace(os.sep, '/') for x in glob(texpath+"**/**.png", recursive=True)]
# print("textures = \n", textures)
variants = set([x.split('/')[-2] for x in textures])


# get variant folders of textures
variantPaths = [x.replace(os.sep, '/') for x in glob(texpath+'**')]
print(variants)
# get textures inside these folders
vartex = {}
for path in variantPaths:
    vartex[path] = [x.replace(os.sep, '/').split('/')[-1] for x in glob(path+'/**.png')]

# for key in texts:
#     print(key, texts[key])

# insert these textures into the template based on their naming. 
if os.path.exists(template):
    print("yay!")
    for var in vartex:
        newfile = lookdevPath+f"M_{variant_name}_{var.split('/')[-1]}.usda"
        print(var)
        with open(template, 'r') as f:
            s = f.read()
        for tex in vartex[var]:
            with open(newfile, 'w') as f:
                if "BaseColor" in tex:
                    print(tex)
                    s = s.replace('<base_color_path>', var+'/'+tex)
                if "Specular" in tex:
                    print(tex)
                    s = s.replace('<specular_path>', var+'/'+tex)
                if "Roughness" in tex:
                    print(tex)
                    s = s.replace('<roughness_path>', var+'/'+tex)
                if "Normal" in tex:
                    print(tex)
                    s = s.replace('<normal_path>', var+'/'+tex)
                f.write(s)
            

        # # File writing

#     print("created {} materials".format(mtlcount))
# else:
#     print("error")