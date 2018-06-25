from matplotlib import pyplot as pt
x=[1,2,3]
y=[4,5,6]
x1=[10,11,12]
y1=[12,13,14]
pt.plot(x,y,'b',label="l1",linewidth=2)
pt.plot(x,y,'g',label="l2",linewidth=3)
pt.grid(False,color="yellow")
pt.show()


