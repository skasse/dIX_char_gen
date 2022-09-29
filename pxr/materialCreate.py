import os
from pxr import Usd, UsdGeom, UsdShade, Sdf, Gf

# PATHS/VARS
sourcePath = "N:/working/characters/POC/"
usdName = 'material.usda'
stageName = sourcePath+usdName

# # CHECK EXISTS
if os.path.exists(stageName):
    stage = Usd.Stage.Open(stageName)
else:
    stage = Usd.Stage.CreateNew(stageName)


# RESET STAGE?
stage.RemovePrim('/World')
stage.RemovePrim('/Looks')

# DEFINE STAGE
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
looks = stage.DefinePrim("/World", "Xform")
stage.SetDefaultPrim(stage.GetPrimAtPath("/World"))

# DEF SHADER

material = UsdShade.Material.Define(stage, "/World/Looks/material1")
shader = UsdShade.Shader.Define(stage, "/World/Looks/material1/shader")
shader.CreateIdAttr("UsdPreviewSurface")
shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f([1.0, 1.0, 1.0]))
material.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "out")

stage.GetRootLayer().Save()