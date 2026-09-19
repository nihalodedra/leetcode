import math
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1>xCenter:
            nx=x1
        elif x2<xCenter:
            nx=x2
        else:
            nx=xCenter
        if y1>yCenter:
            ny=y1
        elif y2<yCenter:
            ny=y2
        else:
            ny=yCenter
        d=math.sqrt(((nx-xCenter)**2)+((ny-yCenter)**2))
        if d<=radius:
            return True
        else:
            return False