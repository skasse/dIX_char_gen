import pymel.core as pm
import maya.OpenMaya as OpenMaya

def bbExport(arg):
    faces = mc.ls("{}.f[*]".format(arg))
    verts = mc.xform(faces, q=1, t=1)
    contactPoints = []
    for face in faces:
        print face
        contactPoints.append(mc.objectCenter(face))
        print contactPoints
    return faces, verts, contactPoints

cushions = bbExport("cushions_bb")
backrests = bbExport("backrests_bb")

cushionMatrix = [cushions[1][k:k+3] for k in range(0, len(cushions[1]), 3)]
seatMatrix = [cushionMatrix[k:k+4] for k in range(0, len(cushionMatrix), 4)]
backrestMatrix = [backrests[1][k:k+3] for k in range(0, len(backrests[1]), 3)]

## OUTPUT
print("[contactPoints]\nseats = [\n{0}\n]\n\n[seats]\ncushions = [\n{1}\n]\n\nbackrests = [\n{1}\n]\n\n".format(cushions[2], cushionMatrix, backrestMatrix))

arg = "backrests_bb"
faces = mc.ls("{}.f[*]".format(arg))
verts = mc.xform(faces, q=1, t=1)
contactPoints = []
faceCount = int(faces[0][-2])
for i in range(0, faceCount):
    contactPoints.append(mc.objectCenter("{0}.f[{1}]".format(arg, i)))

for pos in contactPoints:
    mc.spaceLocator(p=pos)

arg = "cushions_bb"

## CONTACT POINTS
contactPoints = []
verts = []
for poly in mc.listRelatives(arg, c=1):
    contactPoints.append(mc.objectCenter(poly))

## NEW LIST
faces = []
for poly in mc.listRelatives("cushions_bb", c=1):
    faces.append(mc.ls("{}.f[*]".format(poly)))
posMatrix = []
for face in faces:
    polyVertPos = mc.xform(face, q=1, t=1)
    polyVertOrg = [polyVerts[k:k+3] for k in range(0, len(polyVerts), 3)]
    posMatrix.append(polyVertOrg)
mc.xform('polySurface1.f[0]', q=1, t=1)    
mc.xform(verts, q=1)
faces = mc.listRelatives("cushions_bb", c=1)
mc.xform(faces, q=1, t=1)

face = pm.MeshFace("cushions_bb.f[0]")
pt = face.__apimfn__().center(OpenMaya.MSpace.kWorld)
centerPoint = pm.datatypes.Point(pt)


face = mc.ls("cushions_bb.f[0]")
bb = mc.polyEvaluate(face, b=1)
(bb[0][0]+bb[0][1])/2




arg = "backrests_bb"

## CONTACT POINTS
def getContacts(arg):
    contactPoints = []
    verts = []
    for poly in mc.listRelatives(arg, c=1):
        contactPoints.append(mc.objectCenter(poly))
    return contactPoints

## vert pos organized by seat
def getBBMatrix(arg):
    faces = []
    for poly in mc.listRelatives(arg, c=1):
        faces.append(mc.ls("{}.f[*]".format(poly)))
    posMatrix = []
    for face in faces:
        polyVertPos = mc.xform(face, q=1, t=1, ws=1)
        polyVertOrg = [polyVertPos[k:k+3] for k in range(0, len(polyVertPos), 3)]
        posMatrix.append(polyVertOrg)
    return posMatrix

print("[contactPoints]\nseats = [\n{0}\n]\n\n[seats]\ncushions = [\n{1}\n]\n\nbackrests = [\n{2}\n]\n\n".format(getContacts("cushions_bb"), getBBMatrix("cushions_bb"), getBBMatrix("backrests_bb")))


getBBMatrix("cushions_bb")
for i in getBBMatrix("backrests_bb"):
    for k in i:
        print k
        mc.spaceLocator(p=k)



        
#===================================================================
# Instructions
# 1. isolate seats and make live
# 2. Quad draw BB's
# 3. Name objects cushions_bb and backrests_bb


# BEGIN
import numpy as np

for mesh in ["cushions_bb", "backrests_bb"]:
    mc.polySeparate(mesh, ch=0)

## CONTACT POINTS
def getContacts(arg):
    contactPoints = []
    verts = []
    for poly in mc.listRelatives(arg, c=1):
        contactPoints.append(mc.objectCenter(poly))
    return contactPoints

## vert pos organized by seat
def getBBMatrix(arg):
    faces = []
    for poly in mc.listRelatives(arg, c=1):
        faces.append(mc.ls("{}.f[*]".format(poly)))
    posMatrix = []
    for face in faces:
        polyVertPos = mc.xform(face, q=1, t=1, ws=1)
        polyVertOrg = [polyVertPos[k:k+3] for k in range(0, len(polyVertPos), 3)]
        posMatrix.append(polyVertOrg)
    return posMatrix

print("\ncontactPoints = \n{}".format(np.array(getContacts("cushions_bb"))))

print("[contactPoints]\nseats = [\n{0}\n]\n\n[seats]\ncushions = [\n{1}\n]\n\nbackrests = [\n{2}\n]\n\n".format(np.array(getContacts("cushions_bb")).tolist(),
                                                                                                                np.array(getBBMatrix("cushions_bb")).tolist(), 
                                                                                                                np.array(getBBMatrix("backrests_bb")).tolist()))

# END



#====================================================================================
# trying to decompose matrix to place locators
# ref lightingTools.py ln: 748
#

def placeLocators(arg):
    for i in getBBMatrix(arg):
        for k in i:
            print k
            mc.spaceLocator(p=k)
placeLocators("cushions_bb")
placeLocators("backrests_bb")

m_cushions = np.array(getBBMatrix("cushions_bb"))
m_rests = np.array(getBBMatrix("backrests_bb"))
m_contacts = np.array(getContacts("cushions_bb"))

print(m_cushions.tolist(), getBBMatrix("cushions_bb"))

m = getBBMatrix("cushions_bb")
def locatorMatrix(arg):
    
def islist(x):
    return type(x) == list

def recursion(input):
    if len(input) > 0:
       if islist(input[0]):
    if islist(input[0]):
        print("list = {}".format(input[0]))
        recursion(input[1:])

                recursion(input[0])
                recursion(input[1:])
            else:
                print input
                recursion(input[1:])
    else:
        print("done")
recursion(m)
len(m)
map(type, m)

arg = "cushions_bb"
## CONTACT POINTS
def getContacts(arg):
    contactPoints = []
    verts = []
    for poly in mc.listRelatives(arg, c=1):
        contactPoints.append(mc.objectCenter(poly))
    return contactPoints

