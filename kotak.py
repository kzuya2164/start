from turtle import *
bgcolor('black')
pencolor('red')
speed(10)     
#kotak tanpa ujung
for i in range(150):
    forward(20 + i * 3)
    right(110)
    left(-110)
    right(5)
done()
