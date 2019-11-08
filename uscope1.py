from raytracing import *

path = ImagingPath()
path.label = "Microscope system"
path.objectHeight = .25
path.fanAngle=0.25 # default=0.5
path.fanNumber=5 # default=9
path.rayNumber=3 # number of point source locations along objectHeight, default=3

path.append(Space(d=12.)) #12, 15
path.append(Lens(f=10, diameter=4, label='f1'))
path.append(Space(d=80)) #80, 50
path.append(Lens(f=20,diameter=15.0, label='f2'))
path.append(Space(d=18))
path.append(Aperture(diameter=4))
path.append(Lens(f=17,diameter=10.0, label='f3'))
path.append(Space(d=17))
#plt.grid(True)
path.display(onlyChiefAndMarginalRays=True, limitObjectToFieldOfView=True)
#path.display(onlyChiefAndMarginalRays=False, limitObjectToFieldOfView=True)

M=path.transferMatrix()
print(M)
m=path.magnification()
AS=path.apertureStop()
FS=path.fieldStop()
FOV=path.fieldOfView()
print("MT=%.3f FOV=%.3f AS=%.1f(D=%.1f) FS=%.1f(D=%.1f)" % (m[0],FOV,AS[0],AS[1],FS[0],FS[1],))
(r1,r2) = path.marginalRays(y=0)
c1=path.chiefRay(y=FOV/2)
print("Theta: Marginal=%.4f ChiefRay=%.4f" % (r1.theta,c1.theta))

#M1 = Space(d=10)
#M2 = Lens(f=5)
#M3 = M2*M1
#print(M3.forwardConjugate())
#print(M3.backwardConjugate())
