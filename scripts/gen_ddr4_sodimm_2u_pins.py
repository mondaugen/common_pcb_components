start_x=-3250
x_diff=100
top_y=[-400,400]
top_let=['U','D']
n_pins=260
top=0
for n in range(n_pins//2):
    print("X ~ %d %d %d 150 %s 50 50 1 1 P" %
        (n+1,start_x+x_diff*(n//2),top_y[top],top_let[top]))
    print("X ~ %d %d %d 150 %s 50 50 2 1 P" %
        (n+1+n_pins//2,start_x+x_diff*(n//2),top_y[top],top_let[top]))
    top = 1 - top

print("S %d 250 %d -250 0 1 0 f" % (start_x-x_diff//2,start_x+n_pins//4*x_diff-x_diff//2))
print("S %d 250 %d -250 0 2 0 f" % (start_x-x_diff//2,start_x+n_pins//4*x_diff-x_diff//2))
