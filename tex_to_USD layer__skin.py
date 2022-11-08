"""
    creates a dictionary of texture dir paths, and self similar mtl names, 
    and injects that information into a material layers via material template usda
"""


from glob import glob
import os

sourcePath = "N:/working/characters/POC/"
texpath = sourcePath+"TASKS/TEXTURE/char/skin/1k/"
lookdevPath = sourcePath+"TASKS/LOOKDEV/char/skin/"
template = lookdevPath+"template/skin_mtl_template.usda" #N:/working/characters/POC/TASKS/LOOKDEV/char/skin/template/skin_mtl_template.usda
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


custom_shader_settings = {
    "sss_radius_mfp" : "(1.11, 0.84, 0.61)",
    "sss_scale" : ".26"
}
u18_shader_settings = {
    "sss_radius_mfp" : "(1.11, 0.84, 0.61)",
    "sss_scale" : ".42"
}

if os.path.exists(template):
    s = None
    for index, mtl in enumerate(materials, 1):
        # print(mtl)
        newfile = f'{lookdevPath}M_{mtl}.usda'
        # print(newfile)
        print(materials[mtl])
        # read template
        with open(template, 'r') as f:
            s = f.read()
        # write variable to template and write out new
        with open(newfile, 'w') as f:
            s = s.replace("<material_name>", mtl)
            s = s.replace("<texture_path>", materials[mtl].replace('/', '/'))
            if "u18" in mtl:
                s = s.replace("<sss_radius_mfp>", u18_shader_settings["sss_radius_mfp"])
                s = s.replace("<sss_scale>", u18_shader_settings["sss_scale"])
            else:
                s = s.replace("<sss_radius_mfp>", custom_shader_settings["sss_radius_mfp"])
                s = s.replace("<sss_scale>", custom_shader_settings["sss_scale"])
            f.write(s)
        print("{0}/{1}".format(index, mtlcount))
    print("created {} materials".format(mtlcount))