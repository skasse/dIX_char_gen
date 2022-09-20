"""
implementing pxr Usd into my previous python string parser.
TODO:
# 1. separate models from skin
2. add eye variants lookdev

"""


import os
from glob import glob
from pxr import Usd, UsdGeom, UsdShade

# SET/GET VARS
rootPath = "N:/working/characters/POC/"

skinSearchPath = rootPath+"TASKS/LOOKDEV/char/skin/"
skinPaths = ["/".join(x.replace(os.sep, '/').split("/")[-5:]) for x in glob(skinSearchPath+"/**.usda")]
skinNames = [x.split("/")[-1].split(".")[0] for x in skinPaths]
skinVarDict = dict(zip(skinNames, skinPaths))

usdName = "skinVarSets.usda"
stageName = rootPath+usdName

material = "/World/Looks/Looks/Looks/c_skin_mtl"

def varGen(stageName, variantDict, material):
    # CREATE STAGE
    if os.path.exists(stageName):
        stage = Usd.Stage.Open(stageName)
    else:
        stage = Usd.Stage.CreateNew(stageName)

    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    stage.RemovePrim('/World')
    
    refModel = stage.OverridePrim('/World/Looks')
    # primAssignments = ["Std_Skin_Head", "Std_Skin_Body", "Std_Skin_Arm", "Std_Skin_Leg"]
    # stageMaterial = UsdShade.Material.Define(stage, material)
    # for prims in primAssignments:
    #     prims = stage.OverridePrim('/World/Char/CC_Base_BoneRoot0/CC_Base_Body/{}'.format(prims))
    #     UsdShade.MaterialBindingAPI(prims).Bind(stageMaterial)
    for each in [refModel]:
        charvset = each.GetVariantSets().AddVariantSet('skinVariant')
        for key in variantDict:
            charvset.AddVariant(key)
            charvset.SetVariantSelection(key)  # loop this from list?
            with charvset.GetVariantEditContext():
                refModel.GetReferences().AddReference(variantDict[key])

    # UsdShade.MaterialBindingAPI(refModel).Bind(stageMaterial)
    # SAVE OUT CHANGES
    stage.GetRootLayer().Save()


# # Generate skin look Variants
varGen(rootPath+"skinVarSets.usda", skinVarDict, material)