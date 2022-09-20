"""
implementing pxr Usd into my previous python string parser.
TODO:

"""


import os
from glob import glob
from pxr import Usd, UsdGeom, UsdShade

# SET/GET VARS
rootPath = "N:/working/characters/POC/"
modelSearchPath = rootPath+"TASKS/MODEL/char/**/asset/"
modelPaths = ["/".join(x.replace(os.sep, '/').split("/")[-6:]) for x in glob(modelSearchPath+"/model.usda")]
modelNames = [x.split("/")[-3] for x in modelPaths]
modelVarDict = dict(zip(modelNames,modelPaths))



# pathing must be absolute
# can retrieve from alternate config file

mtlAssignments = {
    "/World/Looks/Looks/c_skin_mtl": [
        "/World/Char/CC_Base_BoneRoot0/CC_Base_Body/Std_Skin_Head",
        "/World/Char/CC_Base_BoneRoot0/CC_Base_Body/Std_Skin_Body",
        "/World/Char/CC_Base_BoneRoot0/CC_Base_Body/Std_Skin_Arm",
        "/World/Char/CC_Base_BoneRoot0/CC_Base_Body/Std_Skin_Leg"
        ], 
    "/World/Looks/Looks/c_eye_mtl": [
        "/World/Char/CC_Base_BoneRoot0/CC_Base_Eye/Std_Eye_L",
        "/World/Char/CC_Base_BoneRoot0/CC_Base_Eye/Std_Eye_R"
        ]
    }

def varGen(stageName, variantDict, mtlAssignments):

    # CHECK IF STAGE EXISTS, if not CREATE STAGE.  API WILL NOT OVERWRITE EXISTING STAGES
    if os.path.exists(stageName):
        stage = Usd.Stage.Open(stageName)
    else:
        stage = Usd.Stage.CreateNew(stageName)

    # Set z-up axis
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    
    # remove /World clears the stage and creates blank slate
    root_path = '/World'
    stage.RemovePrim(root_path)
    root_prim  = stage.DefinePrim(root_path, 'Xform')
    refModel = stage.DefinePrim(f'{root_path}/Looks', 'Xform')
    root_prim = stage.GetPrimAtPath(root_path)
    stage.SetDefaultPrim(root_prim)
    

    refModel = stage.OverridePrim('/World/Char')
    for key in mtlAssignments:
        stageMaterial = UsdShade.Material.Define(stage, key)
        for prim in mtlAssignments[key]:
            prims = stage.OverridePrim(prim)
            UsdShade.MaterialBindingAPI(prims).Bind(stageMaterial)
    for each in [refModel]:
        charvset = each.GetVariantSets().AddVariantSet('charVariant')
        for key in variantDict:
            charvset.AddVariant(key)
            charvset.SetVariantSelection(key)  # loop this from list?
            with charvset.GetVariantEditContext():
                refModel.GetReferences().AddReference(variantDict[key])

    # UsdShade.MaterialBindingAPI(refModel).Bind(stageMaterial)
    # SAVE OUT CHANGES
    stage.GetRootLayer().Save()



# Generate Model Variants
usdName = "modelVarSets.usda"
stageName = rootPath+usdName
varGen(stageName, modelVarDict, mtlAssignments)