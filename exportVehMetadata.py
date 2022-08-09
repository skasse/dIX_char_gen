#===================================================================
# Instructions
# Quad draw BB's
# Name objects cushions_bb and backrests_bb

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

#print("\ncontactPoints = \n{}".format(np.array(getContacts("cushions_bb"))))

print("[contactPoints]\nseats = [\n{0}\n]\n\n[seats]\ncushions = [\n{1}\n]\n\nbackrests = [\n{2}\n]\n\n".format(np.array(getContacts("cushions_bb")).tolist(),
                                                                                                                np.array(getBBMatrix("cushions_bb")).tolist(), 
                                                                                                                np.array(getBBMatrix("backrests_bb")).tolist()))

# END