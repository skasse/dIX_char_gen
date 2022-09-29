import os
from pxr import Usd, UsdGeom, UsdShade, Sdf, Vt, Gf


# PATHS/VARS
sourcePath = "N:/working/characters/POC/"
usdName = 'layerOver.usda'
stageName = sourcePath+usdName

# CHECK EXISTS
if os.path.exists(stageName):
    stage = Usd.Stage.Open(stageName)
else:
    stage = Usd.Stage.CreateNew(stageName)


# RESET STAGE?
stage.RemovePrim('/World')
stage.RemovePrim('/Looks')

# DEFINE STAGE
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
world = stage.DefinePrim("/World")
material1 = stage.DefinePrim("/World/Looks/material1")
material = UsdShade.Material.Define(stage, "/World/Looks/material1")
shader = UsdShade.Shader.Define(stage, "/World/Looks/material1/shader")
shader.CreateIdAttr("UsdPreviewSurface")
material.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "out")
texvset = material1.GetVariantSets().AddVariantSet('colorSelect')
variants = {"red":[1, 0, 0],"green":[0, 1, 0],"blue":[0, 0, 1] }
for key in variants:
    texvset.AddVariant(key)
    texvset.SetVariantSelection(key)
    with texvset.GetVariantEditContext():
        shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(variants[key]))
# 




# shader = UsdShade.Shader.Define(stage, "/World/Looks/material1/shader")
# shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f([1.0, 1.0, 1.0]))
# shader.GetPrim().SetSpecifier(Sdf.SpecifierOver)


stage.GetRootLayer().Save()


# attr = material1.CreateAttribute("inputs:diffuseColor", Sdf.ValueTypeNames.Color3f, False)
# attr.Set(Gf.Vec3f([0,0,0]))

# material1.GetPrim().CreateAttribute("diffuseColor")
# material2 = stage.OverridePrim("/World/Looks/material2")
# material1.GetPayloads().AddPayload("N:/working/characters/POC/material.usda")
# prim = stage.GetPrimAtPath("/World/Looks/material1/shader")
        # material1.GetReferences().AddReference("./{}.usda".format(key))



# # THIS WORKS FOR SELECTION< NOT APPLICATION
# # DEFINE STAGE
# UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
# world = stage.DefinePrim("/World")
# material1 = stage.DefinePrim("/World/Looks/material1")
# # material1 = stage.OverridePrim("/World/Looks/material1/shader")
# texvset = material1.GetVariantSets().AddVariantSet('colorSelect')
# variants = {"red":[1, 0, 0],"green":[0, 1, 0],"blue":[0, 0, 1] }
# for key in variants:
#     texvset.AddVariant(key)
#     texvset.SetVariantSelection(key)
#     with texvset.GetVariantEditContext():
#         # attr = material.CreateAttribute("inputs:diffuseColor", Sdf.ValueTypeNames.Color3f, False)
#         # attr.Set(Gf.Vec3f(variants[key]))
#         material = UsdShade.Material.Define(stage, "/World/Looks/material1")
#         shader = UsdShade.Shader.Define(stage, "/World/Looks/material1/shader")
#         shader.CreateIdAttr("UsdPreviewSurface")
#         material.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(variants[key]))
#         material.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "out")