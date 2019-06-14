# A script that will rotate a bunch of parts

import pcbnew

board = pcbnew.GetBoard()

part_names=['R%d' % (num+1,) for num in range(26)]

for pn in part_names:
    part=board.FindModuleByReference(pn)
    part.SetOrientationDegrees(90)
