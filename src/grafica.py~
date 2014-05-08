#encoding: UTF-8
#!/usr/bin/python

import pylab as pl

x=[0.0001,0.0002,0.0003,0.0004,0.0005]
y1=[20,90,100,100,100]
y2=[0,10,50,100,100]
y3=[0,0,20,90,100]
y4=[0,0,10,60,100]


pl.subplot(211)
pl.ylim(-1,110)
pl.plot(x,y1,label='10',marker='*')
pl.plot(x,y2,label='50',marker='*')
pl.plot(x,y3,label='100',marker='*')
pl.plot(x,y4,label='150',marker='*')


pl.legend()


pl.subplot(212)
x=[10,50,100,150,500]
y1=[0.000256,0.000126,0.000120,0.000119,0.000117]

pl.plot(x,y1,marker='*')





pl.show()