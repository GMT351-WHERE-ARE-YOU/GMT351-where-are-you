"""
Function use the 3 GSM tower coordinates and ranges and
return position coordinates according to these towers.
"""

def trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*y2 - 2*y1
  B = 2*x2 - 2*x1
  C = r1**2 - r2**2 - y1**2 + y2**2 - x1**2 + x2**2
  D = 2*y3 - 2*y2
  E = 2*x3 - 2*x2
  F = r2**2 - r3**2 - y2**2 + y3**2 - x2**2 + x3**2
  x = (C*E - F*B) / (E*A - B*D)
  y = (C*D - A*F) / (B*D - A*E)
  return x,y

