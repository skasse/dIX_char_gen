"""
implementing pxr Usd into my previous python string parser.
"""


import os
from glob import glob
from typing import overload
from pxr import Usd, UsdGeom, Sdf


sourcePath = "N:/working/characters/POC/"
modelSearchPath = sourcePath+"TASKS/MODEL/char/**/asset/"
modelNames = [x.replace(os.sep, '/').split("/")[-3] for x in glob(modelSearchPath+"/model.usda")]
modelPaths = ["/".join(x.replace(os.sep, '/').split("/")[-6:]) for x in glob(modelSearchPath+"/model.usda")]
if len(modelNames) == len(modelPaths):
    modelVarDict = dict(zip(modelNames,modelPaths))

usdName = 'RefExample.usda'
stageName = sourcePath+usdName

if os.path.exists(stageName):
    stage = Usd.Stage.Open(stageName)
else:
    stage = Usd.Stage.CreateNew(stageName)


# # # UsdGeom returns a schema object on which the full schema-specific API
# # xformPrim = UsdGeom.Xform.Define(stage, '/hello')
# # # DefinePrim which returns a generic UsdPrim
# # xformGeneric = stage.DefinePrim('/hello2', 'Xform')
# # spherePrim = UsdGeom.Sphere.Define(stage, '/hello/world')
# # spherePrimGeneric = stage.DefinePrim('/hello2/world2', 'Sphere')
# # stage.GetRootLayer().Save()

# xform = stage.GetPrimAtPath('/hello')
# sphere = stage.GetPrimAtPath('/hello/world')
# xformGeneric = stage.GetPrimAtPath('/hello2')
# sphereGeneric = stage.GetPrimAtPath('/hello2/world2')

# # print(xform.GetPropertyNames())
# # print(sphere.GetPropertyNames())
# print(sphere.GetProperties())
# # print(xformGeneric.GetPropertyNames())
# # print(sphereGeneric.GetPropertyNames())

# # extentAttr = sphere.GetAttribute('extent')
# # for each in sphere.GetProperties():
#     # print(each)
# UsdGeom.Sphere(sphere).GetDisplayColorAttr().Get()
# UsdGeom.Sphere(sphere).GetDisplayColorAttr().Set([(0,0,1)])

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
stage.RemovePrim('/World')
xformPrim = UsdGeom.Xform.Define(stage, '/World')
refModel = stage.OverridePrim('/World')
# refModel.GetPayloads().AddPayload('N:/working/characters/POC/TASKS/MODEL/char/f03_as_m_aaa_aaa/asset/model.usda')
# refModel2 = stage.OverridePrim('/World/Char/CharTest2')
# refModel2.GetReferences().AddReference('N:/working/characters/POC/TASKS/MODEL/char/f07_as_n_aaa_aaa/asset/model.usda')
# maybe OOP is a good idea from this point??

# print(stage.GetRootLayer().ExportToString())

# print(Sdf.Layer.GetLoadedLayers())

# # Traversing a stage
# print([x for x in Usd.Stage.Traverse(stage)])

# # adding SHADING variants?
# # for each in [refModel, refModel2]:
# for each in [refModel]:
#     vset = each.GetVariantSets().AddVariantSet('shadingVariant')
#     vset.AddVariant('red')
#     vset.AddVariant('green')
#     vset.AddVariant('blue')
#     # print(each.GetPropertyNames())
#     vset.SetVariantSelection('red')
#     # with vset.GetVariantEditContext():
#         # each.GetAttribute('extent').Set([(1,0,0)])  # Doesnt work with references objects?
#         # each.GetAttribute('xformOpOrder').Set([(1,0,0),(1,0,0),(1,0,0)])
#         # each.SetXformOpOrder([1,0,0])


# # ADDING CHARACTER VARIANTS
# charVarsDict = {
#     "red":"N:/working/characters/POC/TASKS/MODEL/char/f03_as_m_aaa_aaa/asset/model.usda",
#     "green":"N:/working/characters/POC/TASKS/MODEL/char/f07_as_m_aaa_aaa/asset/model.usda",
#     "blue":"N:/working/characters/POC/TASKS/MODEL/char/m03_as_m_aaa_aaa/asset/model.usda"
#     }
# for each in [refModel]:
#     charvset = each.GetVariantSets().AddVariantSet('charVariant')
#     for key in modelVarDict:
#         charvset.AddVariant(key)
#         charvset.SetVariantSelection(key)  # loop this from list?
#         with charvset.GetVariantEditContext():
#             refModel.GetReferences().AddReference(modelVarDict[key])

# for var in refModel.GetVariantSets().GetNames():
#     print(var)




stage.GetRootLayer().Save()

# create material
    # create input?
# create over
    # create input?