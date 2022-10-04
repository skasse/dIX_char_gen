"""
implementing pxr Usd into my previous python string parser.
TODO:
# 1. separate models from eye
2. add eye variants lookdev

"""


import os
from glob import glob
from pxr import Usd, UsdGeom, UsdShade

# SET/GET VARS
rootPath = "N:/working/characters/POC/"

lookdevPath = rootPath+"TASKS/LOOKDEV/cloth/shirt/tshirt/"
lookdevPaths_formatted = ["/".join(x.replace(os.sep, '/').split("/")[-6:]) for x in glob(lookdevPath+"/**.usda")]
varNames = [x.split("/")[-1].split(".")[0] for x in lookdevPaths_formatted]
varDict = dict(zip(varNames, lookdevPaths_formatted))


def varGen(stageName, variantDict, material, variantSetName):

    # CREATE STAGE OR OPEN EXISTING
    if os.path.exists(stageName):
        stage = Usd.Stage.Open(stageName)
    else:
        stage = Usd.Stage.CreateNew(stageName)


    root_path = '/World'
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    # Clear/Clean Stage
    stage.RemovePrim(root_path)
    root_prim  = stage.DefinePrim(root_path, 'Xform')
    mtl_target = stage.DefinePrim(f'{root_path}/Looks', 'Xform')
    root_prim = stage.GetPrimAtPath(root_path)
    stage.SetDefaultPrim(root_prim)

    for each in [mtl_target]:
        charvset = each.GetVariantSets().AddVariantSet(variantSetName)
        for key in variantDict:
            charvset.AddVariant(key)
            charvset.SetVariantSelection(key)  # loop this from list?
            with charvset.GetVariantEditContext():
                mtl_target.GetReferences().AddReference(variantDict[key])

    # SAVE OUT CHANGES
    stage.GetRootLayer().Save()


# # Generate eye look Variants

usdName = "shirt_tshirt_VarSets.usda"
stageName = rootPath+usdName
material = "/World/Looks/c_shirt_tshirt_mtl"
variantSetName = 'shirt_tshirt__Variant'

varGen(stageName, varDict, material, variantSetName)