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

eyeSearchPath = rootPath+"TASKS/LOOKDEV/char/eyes/"
eyePaths = ["/".join(x.replace(os.sep, '/').split("/")[-5:]) for x in glob(eyeSearchPath+"/**.usda")]
eyeNames = [x.split("/")[-1].split(".")[0] for x in eyePaths]
eyeVarDict = dict(zip(eyeNames, eyePaths))


def varGen(stageName, variantDict, material):

    # CREATE STAGE
    if os.path.exists(stageName):
        stage = Usd.Stage.Open(stageName)
    else:
        stage = Usd.Stage.CreateNew(stageName)

    root_path = '/World'
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    stage.RemovePrim(root_path)
    root_prim  = stage.DefinePrim(root_path, 'Xform')
    refModel = stage.DefinePrim(f'{root_path}/Looks', 'Xform')
    root_prim = stage.GetPrimAtPath(root_path)
    stage.SetDefaultPrim(root_prim)

    for each in [refModel]:
        charvset = each.GetVariantSets().AddVariantSet('eyeVariant')
        for key in variantDict:
            charvset.AddVariant(key)
            charvset.SetVariantSelection(key)  # loop this from list?
            with charvset.GetVariantEditContext():
                refModel.GetReferences().AddReference(variantDict[key])

    # SAVE OUT CHANGES
    stage.GetRootLayer().Save()


# # Generate eye look Variants

usdName = "eyeVarSets.usda"
stageName = rootPath+usdName
material = "/World/Looks/Looks/Looks/c_eye_mtl"

varGen(rootPath+"eyeVarSets.usda", eyeVarDict, material)