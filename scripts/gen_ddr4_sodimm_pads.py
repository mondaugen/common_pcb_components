
x_start=[1.675,1.425]
x_gap=2
pitch=0.5
front=1
layers=['B.Cu B.Mask','F.Cu F.Mask']
n_pins=260

lw=0.001 # line width

clip_notch=dict(
centre_y=-22,
height_y=4,
width_x=2,
corner_r=1)

card_corner_r=0.25

card_width=69.6
part_centre_x=card_width*0.5

conn_notch_x=part_centre_x+3.5
conn_notch_width_x=1
conn_notch_height_y=4
conn_notch_top_r=conn_notch_width_x*0.5

pad_w_x=0.35 
pad_h_y=2.3
pad_centre_y=-1.4

def mirror_x_center(x):
    return 2*part_centre_x - x

def draw_clip_notch():
    print("""
(fp_line (start 0 {top_y}) (end {w_r} {top_y}) (layer Edge.Cuts) (width {lw}))
(fp_line (start 0 {bottom_y}) (end {w_r} {bottom_y}) (layer Edge.Cuts) (width {lw}))
(fp_line (start {width_x} {bottom_y_r}) (end {width_x} {top_y_r}) (layer Edge.Cuts) (width {lw}))
(fp_arc (start {w_r} {top_y_r}) (end {width_x} {top_y_r}) (angle -90) (layer Edge.Cuts) (width {lw}))
(fp_arc (start {w_r} {bottom_y_r}) (end {width_x} {bottom_y_r}) (angle 90) (layer Edge.Cuts) (width {lw}))
""".format(
top_y=clip_notch['centre_y']-clip_notch['height_y']*0.5,
w_r=clip_notch['width_x']-clip_notch['corner_r'],
lw=lw,
bottom_y=clip_notch['centre_y']+clip_notch['height_y']*0.5,
width_x=clip_notch['width_x'],
bottom_y_r=clip_notch['centre_y']+clip_notch['height_y']*0.5-clip_notch['corner_r'],
top_y_r=clip_notch['centre_y']-clip_notch['height_y']*0.5+clip_notch['corner_r']))


    print("""
(fp_line (start {far_edge} {top_y}) (end {w_r} {top_y}) (layer Edge.Cuts) (width {lw}))
(fp_line (start {far_edge} {bottom_y}) (end {w_r} {bottom_y}) (layer Edge.Cuts) (width {lw}))
(fp_line (start {width_x} {bottom_y_r}) (end {width_x} {top_y_r}) (layer Edge.Cuts) (width {lw}))
(fp_arc (start {w_r} {top_y_r}) (end {width_x} {top_y_r}) (angle 90) (layer Edge.Cuts) (width {lw}))
(fp_arc (start {w_r} {bottom_y_r}) (end {width_x} {bottom_y_r}) (angle -90) (layer Edge.Cuts) (width {lw}))
""".format(
far_edge=mirror_x_center(0),
top_y=clip_notch['centre_y']-clip_notch['height_y']*0.5,
w_r=mirror_x_center(clip_notch['width_x']-clip_notch['corner_r']),
lw=lw,
bottom_y=clip_notch['centre_y']+clip_notch['height_y']*0.5,
width_x=mirror_x_center(clip_notch['width_x']),
bottom_y_r=clip_notch['centre_y']+clip_notch['height_y']*0.5-clip_notch['corner_r'],
top_y_r=clip_notch['centre_y']-clip_notch['height_y']*0.5+clip_notch['corner_r']))

def draw_card_edges():

    print("""
(fp_line (start {notch_bottom_x} {notch_bottom_y}) 
(end {card_sw_r_x} {card_sw_r_y}) (layer Edge.Cuts) (width {lw}))
(fp_arc (start {card_corner_r} {card_sw_r_y}) (end {card_sw_r_x} {card_sw_r_y}) 
(angle -90) (layer Edge.Cuts) (width {lw}))
""".format(
    notch_bottom_x=0,
    notch_bottom_y=clip_notch['centre_y']+clip_notch['height_y']*0.5,
    card_sw_r_x=0,
    card_sw_r_y=-card_corner_r,
    card_corner_r=card_corner_r,
    lw=lw))

    print("""
(fp_line (start {notch_bottom_x} {notch_bottom_y}) 
(end {card_sw_r_x} {card_sw_r_y}) (layer Edge.Cuts) (width {lw}))
(fp_arc (start {card_corner_r} {card_sw_r_y}) (end {card_sw_r_x} {card_sw_r_y}) 
(angle 90) (layer Edge.Cuts) (width {lw}))
""".format(
    notch_bottom_x=mirror_x_center(0),
    notch_bottom_y=clip_notch['centre_y']+clip_notch['height_y']*0.5,
    card_sw_r_x=mirror_x_center(0),
    card_sw_r_y=-card_corner_r,
    card_corner_r=mirror_x_center(card_corner_r),
    lw=lw))
    
def draw_card_bottom():
    print("""
(fp_line (start {card_sw_x} {card_s_y}) 
(end {notch_sw_x} {card_s_y}) (layer Edge.Cuts) (width {lw}))
(fp_line (start {notch_se_x} {card_s_y}) 
(end {card_se_x} {card_s_y}) (layer Edge.Cuts) (width {lw}))
(fp_line (start {notch_sw_x} {card_s_y}) 
(end {notch_sw_x} {notch_n_y}) (layer Edge.Cuts) (width {lw}))
(fp_line (start {notch_se_x} {card_s_y}) 
(end {notch_se_x} {notch_n_y}) (layer Edge.Cuts) (width {lw}))
(fp_arc (start {notch_c_x} {notch_n_y})
(end {notch_se_x} {notch_n_y}) 
(angle -180) (layer Edge.Cuts) (width {lw}))
""".format(
    card_sw_x=card_corner_r,
    card_s_y=0,
    notch_sw_x=conn_notch_x-conn_notch_width_x*0.5,
    notch_se_x=conn_notch_x+conn_notch_width_x*0.5,
    card_se_x=card_width-card_corner_r,
    notch_n_y=-(conn_notch_height_y-conn_notch_top_r),
    notch_c_x=conn_notch_x,
    lw=lw))

def draw_solder_mask():
    """
    It seems memory connectors remove the solder mask at the end of the part.
    """
    for l in ['B.Mask','F.Mask']:
        print("""
(fp_poly (pts 
(xy {pads_w_nw_x} {pads_w_nw_y}) 
(xy {pads_w_ne_x} {pads_w_ne_y})
(xy {pads_w_se_x} {pads_w_se_y})
(xy {pads_w_sw_x} {pads_w_sw_y})
) (layer {layer}) (width {lw}))
""".format(
        pads_w_nw_x=0,
        pads_w_nw_y=pad_centre_y-pad_h_y*0.5,
        pads_w_ne_x=conn_notch_x-conn_notch_width_x*0.5,
        pads_w_ne_y=pad_centre_y-pad_h_y*0.5,
        pads_w_se_x=conn_notch_x-conn_notch_width_x*0.5,
        pads_w_se_y=0,
        pads_w_sw_x=0,
        pads_w_sw_y=0,
        layer=l,
        lw=lw))

        print("""
(fp_poly (pts 
(xy {pads_e_nw_x} {pads_e_nw_y}) 
(xy {pads_e_ne_x} {pads_e_ne_y})
(xy {pads_e_se_x} {pads_e_se_y})
(xy {pads_e_sw_x} {pads_e_sw_y})
) (layer {layer}) (width {lw}))
""".format(
        pads_e_nw_x=conn_notch_x+conn_notch_width_x*0.5,
        pads_e_nw_y=pad_centre_y-pad_h_y*0.5,
        pads_e_ne_x=card_width,
        pads_e_ne_y=pad_centre_y-pad_h_y*0.5,
        pads_e_se_x=card_width,
        pads_e_se_y=0,
        pads_e_sw_x=conn_notch_x+conn_notch_width_x*0.5,
        pads_e_sw_y=0,
        layer=l,
        lw=lw))

header="""
(module DDR4_SODIMM_MALE (layer F.Cu) (tedit 5D03CED4)
  (fp_text reference REF** (at 0 0.5) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value DDR4_SODIMM_MALE (at 0 -0.5) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
"""

footer="""
)
"""

print(header)

draw_clip_notch()
draw_card_edges()
draw_card_bottom()
draw_solder_mask()

for n in range(n_pins):
    xs=x_start[front]+x_gap*float((n+1)>144)
    l=layers[front]
    print("(pad %d connect rect (at %f %f) (size %f %f) (layers %s))"
        % (n+1,xs+pitch*(n//2),pad_centre_y,pad_w_x,pad_h_y,l))
    front = 1 - front

print(footer)
