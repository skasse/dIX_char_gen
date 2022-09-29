from pxr import Usd, UsdGeom
stage = Usd.Stage.Open('HelloWorld.usda')

xform = stage.DefinePrim('/hello', 'Xform')
sphere = stage.DefinePrim('/hello/world', 'Sphere')


prim = stage.DefinePrim("/XformPrim", "Xform")
xform = UsdGeom.Xform(prim)

xform_faster = UsdGeom.Xform.Define(stage, "/AnotherXform")


#stage.RemovePrim("/hello/world")


xform = stage.GetPrimAtPath("/hello")
sphere = stage.GetPrimAtPath("/hello/world")
print(xform.GetPropertyNames())
print(sphere.GetPropertyNames())
extentAttr = sphere.GetAttribute("extent")
print(extentAttr.Get())

radiusAttr = sphere.GetAttribute("radius")
radiusAttr.Set(2)
sphereSchema = UsdGeom.Sphere(sphere)
color = sphereSchema.GetDisplayColorAttr()
color.Set([(0,0,1)])


stage.GetRootLayer().Save()