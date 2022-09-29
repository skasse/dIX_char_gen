import os
from turtle import color
from pxr import Usd, UsdGeom, Sdf, Gf


# PATHS/VARS
sourcePath = "N:/working/characters/POC/"
usdName = 'helloWorld.usda'
stageName = sourcePath+usdName

# CHECK EXISTS
if os.path.exists(stageName):
    stage = Usd.Stage.Open(stageName)
else:
    stage = Usd.Stage.CreateNew(stageName)

# DEFINE STAGE
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
default = stage.DefinePrim('/World', "Xform")
sphere = stage.DefinePrim('/World/sphere', "Sphere")
material1 = stage.OverridePrim("/World/Looks/material1")
material1.GetPayloads().AddPayload("N:/working/characters/POC/material.usda")

# DEF VARIANTS
texvset = material1.GetVariantSets().AddVariantSet('colorSelect')
variants = {"red":[1, 0, 0],"green":[0, 1, 0],"blue":[0, 0, 1] }
for key in variants:
    texvset.AddVariant(key)
    texvset.SetVariantSelection(key)
    with texvset.GetVariantEditContext():
        attr = material1.CreateAttribute("inputs:diffuseColor", Sdf.ValueTypeNames.Color3f, False)
        attr.Set(Gf.Vec3f(variants[key]))

# SAVE CLOSE FILE
stage.GetRootLayer().Save()