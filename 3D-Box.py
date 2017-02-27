from visual import *

print("""
Right button drag or Ctrl-drag to rotate "camera" to view scene.
Middle button or Alt-drag to drag up or down to zoom in or out.
  On a two-button mouse, middle is left + right.
""")

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk
wallR = box (pos=( side, 0, 0), size=(thk, s2, s3),  color = (1,0,0), material=materials.emissive)
wallL = box (pos=(-side, 0, 0), size=(thk, s2, s3),  color = (1,0.5,0), material=materials.emissive)
wallB = box (pos=(0, -side, 0), size=(s3, thk, s3),  color = (0,1,0), material=materials.emissive)
wallT = box (pos=(0, side, 0), size=(s3, thk, s3),  color = (0,0,1), materisal=materials.emissive)
wallBK = box(pos=(0, 0, -side), size=(s2, s2, thk), color = (1,1,0), material=materials.emissive)
wallFT = box(pos=(0, 0, side), size=(s2, s2, thk), color = (1,1,1), material=materials.emissive)
