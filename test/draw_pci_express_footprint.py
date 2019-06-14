from dxfwrite import DXFEngine as dxf

# all units in mm

OUTFILE='/tmp/pci_express_male.dxf'

UPPER_CONN_CUT_Y=3.2
UPPER_CONN_CUT_R=0.8
CONN_WIDTH_X=25.7
CARD_WIDTH_X=30
CONN_CL_X=CARD_WIDTH_X*0.5
UPPER_CONN_CUT_X=(CARD_WIDTH_X-CONN_WIDTH_X)*0.5-UPPER_CONN_CUT_R
CUTOUT_R=.75
CUTOUT_CENTRE_X=CONN_CL_X-3.85
PAD_WIDTH_X=0.6
PAD_HEIGHT_Y=2.3
PAD_CENTER_Y=0.25+PAD_HEIGHT_Y*0.5
PAD_START_RIGHT_X=CUTOUT_CENTRE_X+1.65
PAD_START_LEFT_X=PAD_START_RIGHT_X-4
PAD_PITCH_X=0.8
N_PADS_RIGHT=18
N_PADS_LEFT=8

def draw_pad(d,center=(0,0),front=True):
    layer='B.Mask'
    color=2
    if front:
        layer='F.Mask'
        color=3
    x,y=center
    w=0.5*PAD_WIDTH_X
    h=0.5*PAD_HEIGHT_Y
    points=[
    (x-w,y-h),
    (x-w,y+h),
    (x+w,y+h),
    (x+w,y-h)
    ]
    solid = dxf.solid(
    points,
    layer=layer,
    color=color)
    d.add(solid)

def draw_pads(d):
    for n in range(N_PADS_RIGHT):
        c=(PAD_START_RIGHT_X+PAD_PITCH_X*n,PAD_CENTER_Y)
        draw_pad(d,center=c)
    for n in range(N_PADS_LEFT):
        c=(PAD_START_LEFT_X-PAD_PITCH_X*n,PAD_CENTER_Y)
        draw_pad(d,center=c)
    for n in range(N_PADS_RIGHT):
        c=(PAD_START_RIGHT_X+PAD_PITCH_X*n,PAD_CENTER_Y)
        draw_pad(d,center=c,front=False)
    for n in range(N_PADS_LEFT):
        c=(PAD_START_LEFT_X-PAD_PITCH_X*n,PAD_CENTER_Y)
        draw_pad(d,center=c,front=False)
    
drawing = dxf.drawing(OUTFILE)
drawing.add_layer('Edge.Cuts')

drawing.add(dxf.line(
(0,UPPER_CONN_CUT_Y),
(UPPER_CONN_CUT_X,UPPER_CONN_CUT_Y),
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.line(
(UPPER_CONN_CUT_X+UPPER_CONN_CUT_R,UPPER_CONN_CUT_Y-UPPER_CONN_CUT_R),
(UPPER_CONN_CUT_X+UPPER_CONN_CUT_R,0),
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.arc(
radius=UPPER_CONN_CUT_R,
center=(UPPER_CONN_CUT_X,UPPER_CONN_CUT_Y-UPPER_CONN_CUT_R),
startangle=0,
endangle=90,
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.line(
(UPPER_CONN_CUT_X+UPPER_CONN_CUT_R,0),
(CUTOUT_CENTRE_X-CUTOUT_R,0),
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.line(
(CUTOUT_CENTRE_X-CUTOUT_R,0),
(CUTOUT_CENTRE_X-CUTOUT_R,UPPER_CONN_CUT_Y),
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.arc(
radius=CUTOUT_R,
center=(CUTOUT_CENTRE_X,UPPER_CONN_CUT_Y),
startangle=0,
endangle=180,
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.line(
(CUTOUT_CENTRE_X+CUTOUT_R,0),
(CUTOUT_CENTRE_X+CUTOUT_R,UPPER_CONN_CUT_Y),
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.line(
(CUTOUT_CENTRE_X+CUTOUT_R,0),
(CARD_WIDTH_X-(UPPER_CONN_CUT_X+UPPER_CONN_CUT_R),0),
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.line(
(CARD_WIDTH_X-(UPPER_CONN_CUT_X+UPPER_CONN_CUT_R),0),
(CARD_WIDTH_X-(UPPER_CONN_CUT_X+UPPER_CONN_CUT_R),UPPER_CONN_CUT_Y-UPPER_CONN_CUT_R),
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.arc(
radius=UPPER_CONN_CUT_R,
center=(CARD_WIDTH_X-UPPER_CONN_CUT_X,UPPER_CONN_CUT_Y-UPPER_CONN_CUT_R),
startangle=90,
endangle=180,
color=7,
layer='Edge.Cuts'))

drawing.add(dxf.line(
(CARD_WIDTH_X-UPPER_CONN_CUT_X,UPPER_CONN_CUT_Y),
(CARD_WIDTH_X,UPPER_CONN_CUT_Y),
color=7,
layer='Edge.Cuts'))

draw_pads(drawing)

drawing.save()
